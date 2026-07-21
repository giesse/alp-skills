#!/usr/bin/env python3
"""Dispatch one bounded capability worker through Codex App Server stdio."""
from __future__ import annotations

import json
import os
import queue
import subprocess
import sys
import threading
import time
import tomllib
from pathlib import Path
from typing import Any

EXIT_CODES = {
    "completed": 0, "blocked": 20, "interrupted": 21,
    "routing_failure": 22, "turn_failure": 23,
    "transport_failure": 24, "invalid_result": 25,
}
ROLES = {"explorer", "verifier", "tangler", "implementer", "reviewer", "escalation_reviewer"}
PACKET_KEYS = {"schema_version", "role", "task", "cwd", "sandbox", "timeout_seconds",
               "response_contract", "stop_conditions", "paths", "evidence"}
REQUIRED_PACKET_KEYS = PACKET_KEYS - {"paths", "evidence"}
SANDBOX_RANK = {"read-only": 0, "workspace-write": 1}
RESULT_KEYS = {"classification", "sections"}
MANDATORY_SECTIONS = {"Conclusion", "Evidence", "Uncertainty", "Inspected scope", "Uninspected scope"}
GOVERNED_EVENTS = {"turn/started", "item/completed", "turn/completed", "model/rerouted"}

progress_sequence = 1
start_time = 0.0
last_gov_event = None
log_file = None
log_truncated = False
bytes_written = 0
log_lock = threading.Lock()


def reset_globals(keep_start_time=False):
    global progress_sequence, start_time, last_gov_event, log_file, log_truncated, bytes_written
    progress_sequence = 1
    if not keep_start_time:
        start_time = 0.0
    last_gov_event = None
    log_file = None
    log_truncated = False
    bytes_written = 0


def log_diagnostic(data_type: str, data: Any):
    global log_truncated, bytes_written, log_file
    if not log_file or log_truncated:
        return
    try:
        record = {
            "type": data_type,
            "timestamp": time.time(),
        }
        if isinstance(data, str):
            record["content"] = data
        else:
            record["message"] = data
            
        line = json.dumps(record, separators=(",", ":")) + "\n"
        line_bytes = line.encode("utf-8")
        
        with log_lock:
            if log_truncated:
                return
            if bytes_written + len(line_bytes) <= 8 * 1024 * 1024:
                log_file.write(line_bytes)
                log_file.flush()
                bytes_written += len(line_bytes)
            else:
                allowed = 8 * 1024 * 1024 - bytes_written
                if allowed > 0:
                    log_file.write(line_bytes[:allowed])
                    log_file.flush()
                    bytes_written += allowed
                log_truncated = True
    except Exception:
        pass


class DispatchError(Exception):
    def __init__(self, status: str, code: str = "dispatch_failure") -> None:
        super().__init__(code)
        self.status, self.code = status, code


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _string_list(value: Any, required: bool = True) -> bool:
    return (isinstance(value, list) and (not required or bool(value))
            and all(_nonempty_string(x) for x in value)
            and len(value) == len(set(value)))


def validate_packet(packet: Any) -> dict[str, Any]:
    if not isinstance(packet, dict) or set(packet) - PACKET_KEYS or REQUIRED_PACKET_KEYS - set(packet):
        raise DispatchError("blocked", "invalid_packet")
    if packet.get("schema_version") != 1 or not isinstance(packet.get("schema_version"), int) or isinstance(packet.get("schema_version"), bool):
        raise DispatchError("blocked", "invalid_packet")
    if not _nonempty_string(packet["role"]) or packet["role"] not in ROLES or not _nonempty_string(packet["task"]):
        raise DispatchError("blocked", "invalid_packet")
    if not _nonempty_string(packet["cwd"]):
        raise DispatchError("blocked", "invalid_cwd")
    cwd = Path(packet["cwd"])
    if not cwd.is_absolute() or not cwd.is_dir():
        raise DispatchError("blocked", "invalid_cwd")
    if not _nonempty_string(packet["sandbox"]) or packet["sandbox"] not in SANDBOX_RANK:
        raise DispatchError("blocked", "invalid_sandbox")
    if not isinstance(packet["timeout_seconds"], int) or isinstance(packet["timeout_seconds"], bool) or packet["timeout_seconds"] <= 0:
        raise DispatchError("blocked", "invalid_timeout")
    if not _string_list(packet["stop_conditions"]):
        raise DispatchError("blocked", "invalid_stop_conditions")
    for field in ("paths", "evidence"):
        if field in packet and not _string_list(packet[field], required=False):
            raise DispatchError("blocked", "invalid_packet")
    contract = packet["response_contract"]
    if not isinstance(contract, dict) or set(contract) != {"classifications", "required_sections"}:
        raise DispatchError("blocked", "invalid_response_contract")
    if not _string_list(contract["classifications"]) or "blocked" not in contract["classifications"]:
        raise DispatchError("blocked", "invalid_response_contract")
    if len(set(contract["classifications"])) != len(contract["classifications"]):
        raise DispatchError("blocked", "invalid_response_contract")
    if not _string_list(contract["required_sections"]) or len(set(contract["required_sections"])) != len(contract["required_sections"]):
        raise DispatchError("blocked", "invalid_response_contract")
    if not MANDATORY_SECTIONS.issubset(contract["required_sections"]):
        raise DispatchError("blocked", "invalid_response_contract")
    for path in packet.get("paths", []):
        candidate = Path(path)
        if not candidate.is_absolute():
            resolved = (cwd / candidate).resolve(strict=False)
            if resolved != cwd.resolve() and cwd.resolve() not in resolved.parents:
                raise DispatchError("blocked", "path_outside_cwd")
        elif packet["sandbox"] not in SANDBOX_RANK:
            raise DispatchError("blocked", "path_outside_cwd")
    return packet


def load_profile(role: str, profile_dir: Path | None = None) -> tuple[dict[str, Any], Path]:
    if role not in ROLES:
        raise DispatchError("blocked", "unknown_role")
    home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    path = (profile_dir or (home / "agents")) / f"alp_{role}.toml"
    try:
        with path.open("rb") as handle:
            profile = tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError):
        raise DispatchError("blocked", "invalid_profile") from None
    required = {"name", "description", "model", "model_reasoning_effort", "sandbox_mode", "developer_instructions"}
    if set(profile) != required or profile["name"] != f"alp_{role}" or not all(_nonempty_string(profile[k]) for k in required):
        raise DispatchError("blocked", "invalid_profile")
    if (profile["sandbox_mode"] not in SANDBOX_RANK
            or profile["model_reasoning_effort"] not in {"low", "medium", "high"}):
        raise DispatchError("blocked", "invalid_profile")
    return profile, path


def output_schema(contract: dict[str, Any]) -> dict[str, Any]:
    return {"type": "object", "additionalProperties": False,
            "required": ["classification", "sections"],
            "properties": {
                "classification": {"type": "string", "enum": contract["classifications"]},
                "sections": {"type": "object", "additionalProperties": False,
                             "required": contract["required_sections"],
                             "properties": {name: {"type": "string"} for name in contract["required_sections"]}},
            }}


def validate_response(response: Any, contract: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(response, dict) or set(response) != RESULT_KEYS:
        raise DispatchError("invalid_result", "invalid_response")
    if response["classification"] not in contract["classifications"]:
        raise DispatchError("invalid_result", "invalid_response")
    sections = response["sections"]
    if not isinstance(sections, dict) or set(sections) != set(contract["required_sections"]):
        raise DispatchError("invalid_result", "invalid_response")
    if not all(_nonempty_string(value) for value in sections.values()):
        raise DispatchError("invalid_result", "invalid_response")
    return response


def _redacted_failure(code: str) -> dict[str, str]:
    return {"code": code, "message": "dispatch failed; see status and stable failure code"}


def _blank_result(packet: dict[str, Any], profile_path: str | None = None) -> dict[str, Any]:
    role = packet.get("role")
    if not isinstance(role, str) or role not in ROLES:
        role = None
    return {"schema_version": 1, "role": role,
            "routing": {"profile": profile_path, "requested": None, "selected": None,
                         "rerouted": False, "reroute_events": []},
            "status": "blocked", "response": None, "usage": None,
            "evidence": {"account_type": None, "inspected_scope": None,
                          "uninspected_scope": None, "events": [], "failure": None}}


class JsonlTransport:
    def __init__(self, process: subprocess.Popen[str], log_fn=None) -> None:
        self.process = process
        self.log_fn = log_fn
        self.events: queue.Queue[dict[str, Any] | Exception | None] = queue.Queue()
        self.thread = threading.Thread(target=self._read, daemon=True)
        self.thread.start()
        self.stderr_thread = threading.Thread(target=self._read_stderr, daemon=True)
        self.stderr_thread.start()

    def _read(self) -> None:
        try:
            for line in self.process.stdout or ():
                if line.strip():
                    if self.log_fn:
                        self.log_fn("stdout_raw", line)
                    try:
                        parsed = json.loads(line)
                        if self.log_fn:
                            self.log_fn("received", parsed)
                        self.events.put(parsed)
                    except Exception as err:
                        self.events.put(err)
        except Exception as exc:  # pragma: no cover - OS-dependent
            self.events.put(exc)
        finally:
            self.events.put(None)

    def _read_stderr(self) -> None:
        try:
            if self.process.stderr:
                for line in self.process.stderr:
                    if self.log_fn:
                        self.log_fn("stderr_raw", line)
        except Exception:
            pass

    def send(self, message: dict[str, Any]) -> None:
        if self.process.stdin is None:
            raise OSError("stdin unavailable")
        if self.log_fn:
            self.log_fn("sent", message)
        self.process.stdin.write(json.dumps(message, separators=(",", ":")) + "\n")
        self.process.stdin.flush()

    def receive(self, timeout: float) -> dict[str, Any] | None:
        event = self.events.get(timeout=timeout)
        if isinstance(event, Exception):
            raise event
        return event

    def close(self) -> None:
        try:
            self.process.kill()
            self.process.wait(timeout=2)
        except Exception:
            pass
        try:
            self.thread.join(timeout=5)
        except Exception:
            pass
        try:
            self.stderr_thread.join(timeout=5)
        except Exception:
            pass
        for stream in (self.process.stdin, self.process.stdout, self.process.stderr):
            if stream:
                try:
                    stream.close()
                except Exception:
                    pass


def _request(transport: Any, method: str, params: dict[str, Any], counter: list[int], timeout: float) -> dict[str, Any]:
    counter[0] += 1
    ident = counter[0]
    transport.send({"jsonrpc": "2.0", "id": ident, "method": method, "params": params})
    deadline = time.monotonic() + timeout
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise queue.Empty
        message = transport.receive(remaining)
        if message is None:
            raise OSError("protocol closed")
        if message.get("id") == ident:
            if "error" in message:
                raise DispatchError("transport_failure", "protocol_error")
            return message.get("result", {})


def _first(mapping: Any, *keys: str) -> Any:
    if not isinstance(mapping, dict):
        return None
    for key in keys:
        if key in mapping:
            return mapping[key]
    return None


def _sandbox_policy(name: str, cwd: str) -> dict[str, Any]:
    if name == "read-only":
        return {"type": "readOnly", "networkAccess": False}
    return {"type": "workspaceWrite", "networkAccess": False,
            "writableRoots": [cwd]}


def _sandbox_name(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return {"readOnly": "read-only", "workspaceWrite": "workspace-write"}.get(value.get("type"))
    return None


def _model_entries(result: Any) -> list[dict[str, Any]]:
    data = _first(result, "data", "models")
    return data if isinstance(data, list) else []


def _model_supported(entry: dict[str, Any], model: str, effort: str) -> bool:
    if model not in {_first(entry, "id"), _first(entry, "model")}:
        return False
    efforts = _first(entry, "supportedReasoningEfforts", "supported_reasoning_efforts", "reasoningEfforts") or []
    values = [x.get("reasoningEffort", x.get("effort")) if isinstance(x, dict) else x for x in efforts]
    return effort in values


def _usage(value: Any) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        return None
    result: dict[str, Any] = {}
    for source, target in (("inputTokens", "input_tokens"), ("cachedInputTokens", "cached_input_tokens"),
                           ("outputTokens", "output_tokens"), ("reasoningOutputTokens", "reasoning_output_tokens"),
                           ("totalTokens", "total_tokens")):
        item = value.get(source, value.get(target))
        result[target] = item if isinstance(item, int) and not isinstance(item, bool) and item >= 0 else None
    return result


def _response_from_item(item: Any) -> Any:
    if not isinstance(item, dict):
        return None
    if item.get("type") in {"agentMessage", "assistantMessage"}:
        return item.get("text") or item.get("message")
    return None


def _protocol_string(value: Any) -> str:
    return value if isinstance(value, str) else "unknown"


def _interrupt(transport: Any, counter: list[int], thread_id: str,
               turn_id: str, events: list[str] | None = None) -> None:
    counter[0] += 1
    transport.send({"jsonrpc": "2.0", "id": counter[0],
                    "method": "turn/interrupt",
                    "params": {"threadId": thread_id, "turnId": turn_id}})
    record_governed_event("turn/interrupt", events)
    emit_progress("interrupt", "stream")
    deadline = time.monotonic() + 0.5
    while True:
        try:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                return
            message = transport.receive(remaining)
        except queue.Empty:
            return
        if message is None or message.get("id") == counter[0]:
            return
        if (message.get("method") == "turn/completed"
                and _first(message.get("params", {}), "threadId") == thread_id):
            return


def emit_progress(event: str, stage: str | None, status: str | None = None):
    global progress_sequence, start_time, last_gov_event
    elapsed_ms = max(0, int((time.monotonic() - start_time) * 1000))
    record = {
        "schema_version": 1,
        "type": "dispatch_progress",
        "sequence": progress_sequence,
        "event": event,
        "stage": stage,
        "elapsed_ms": elapsed_ms,
        "last_governed_event": last_gov_event,
        "status": status
    }
    progress_sequence += 1
    sys.stderr.write(json.dumps(record, separators=(",", ":")) + "\n")
    sys.stderr.flush()


def record_governed_event(event_name: str, events_list: list[str] | None = None):
    global last_gov_event
    last_gov_event = event_name
    if events_list is not None:
        events_list.append(event_name)


class InvalidLogException(Exception):
    pass


def validate_and_create_log(log_arg: str, cwd_arg: str | None) -> tuple[Path, Any]:
    log_path = Path(log_arg)
    if not log_path.is_absolute():
        raise InvalidLogException()
    if cwd_arg is not None:
        try:
            resolved_log = log_path.resolve(strict=False)
            resolved_cwd = Path(cwd_arg).resolve(strict=False)
            if resolved_log == resolved_cwd or resolved_cwd in resolved_log.parents:
                raise InvalidLogException()
        except Exception:
            raise InvalidLogException()
    try:
        fd = os.open(log_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        log_file = os.fdopen(fd, 'wb')
        return log_path, log_file
    except Exception:
        raise InvalidLogException()


def run_startup_probe(log_file: Any, log_path: Path | None, transport_factory: Any = None) -> dict[str, Any]:
    global log_truncated
    attempts = []
    
    status = "transport_failure"
    exit_code = 24
    account_type = None
    
    for attempt_idx in range(2):
        attempt_num = attempt_idx + 1
        current_attempt = {
            "number": attempt_num,
            "terminal_stage": "spawn",
            "failure_category": None,
            "child_exit_status": None
        }
        attempts.append(current_attempt)
        
        process = None
        transport = None
        try:
            if transport_factory is None:
                process = subprocess.Popen(["codex", "app-server", "--disable", "multi_agent", "--listen", "stdio://"],
                                           stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE if log_file else subprocess.DEVNULL,
                                           text=True)
                def tee_log(direction: str, data: Any):
                    log_diagnostic(direction, data)
                transport = JsonlTransport(process, log_fn=tee_log)
            else:
                transport = transport_factory()
                
            current_attempt["terminal_stage"] = "initialize"
            counter = [0]
            _request(transport, "initialize",
                     {"clientInfo": {"name": "alp-workflow", "version": "1"},
                      "capabilities": {"experimentalApi": True}}, counter, 10)
            transport.send({"jsonrpc": "2.0", "method": "initialized", "params": {}})
            record_governed_event("initialized", None)
            
            current_attempt["terminal_stage"] = "account"
            account = _request(transport, "account/read", {}, counter, 10)
            record_governed_event("account/read", None)
            
            account_obj = _first(account, "account") or account
            account_type = _first(account_obj, "type", "accountType", "account_type")
            if account_type not in {"chatgpt", "codex"}:
                status = "blocked"
                exit_code = 20
                current_attempt["failure_category"] = None
                break
                
            current_attempt["terminal_stage"] = "catalog"
            for method in ("account/rateLimits/read", "account/usage/read"):
                try:
                    _request(transport, method, {}, counter, 5)
                except Exception:
                    pass
                    
            cursor = None
            while True:
                models = _request(transport, "model/list",
                                  {"cursor": cursor} if cursor else {}, counter, 10)
                record_governed_event("model/list", None)
                cursor = models.get("nextCursor") if isinstance(models, dict) else None
                if not isinstance(cursor, str) or not cursor:
                    break
                    
            status = "completed"
            exit_code = 0
            current_attempt["failure_category"] = None
            break
            
        except Exception as exc:
            category = "unknown"
            if isinstance(exc, (FileNotFoundError, OSError)) and getattr(exc, "filename", None) is None:
                if current_attempt["terminal_stage"] == "spawn":
                    category = "spawn_os_error"
                else:
                    category = "protocol_eof"
            elif isinstance(exc, json.JSONDecodeError):
                category = "protocol_decode_error"
            elif isinstance(exc, queue.Empty):
                category = "request_timeout"
            elif isinstance(exc, DispatchError):
                if exc.code == "protocol_error":
                    category = "protocol_error"
                else:
                    category = "unknown"
            current_attempt["failure_category"] = category
            
        finally:
            if process:
                try:
                    transport.close()
                except Exception:
                    pass
                exit_status = process.poll()
                if exit_status is not None:
                    current_attempt["child_exit_status"] = exit_status
                    
        # Check retryability: only spawn, initialize, catalog failures are retryable.
        # Account failure must not retry.
        retryable = (
            status == "transport_failure"
            and current_attempt["terminal_stage"] in {"spawn", "initialize", "catalog"}
        )
        if not retryable or attempt_num == 2:
            break
            
    return {
        "schema_version": 1,
        "mode": "startup_probe",
        "status": status,
        "exit_code": exit_code,
        "probe": {
            "log_path": str(log_path) if log_path else None,
            "log_truncated": log_truncated,
            "stage": current_attempt["terminal_stage"],
            "attempts": attempts,
            "account_type": account_type if account_type in {"chatgpt", "codex"} else None
        }
    }


def _run_once(packet: dict[str, Any], profile: dict[str, Any],
              profile_path: Path, transport_factory: Any,
              log_file: Any, log_path: Path | None,
              current_attempt: dict[str, Any], thread_id_box: list[str | None]) -> dict[str, Any]:
    requested = {"model": profile["model"],
                 "effort": profile["model_reasoning_effort"],
                 "sandbox": packet["sandbox"]}
    result = _blank_result(packet, str(profile_path))
    result["routing"]["requested"] = requested
    events: list[str] = result["evidence"]["events"]
    counter = [0]
    process = None
    transport = None
    turn_submitted = False
    thread_id: str | None = None
    turn_id: str | None = None
    turn_started_event_received = False
    
    try:
        emit_progress("stage", "spawn")
        if transport_factory is None:
            process = subprocess.Popen(["codex", "app-server", "--disable", "multi_agent", "--listen", "stdio://"],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE if log_file else subprocess.DEVNULL,
                                       text=True)
            def tee_log(direction: str, data: Any):
                log_diagnostic(direction, data)
            transport = JsonlTransport(process, log_fn=tee_log)
        else:
            transport = transport_factory()
            
        current_attempt["terminal_stage"] = "initialize"
        emit_progress("stage", "initialize")
        _request(transport, "initialize",
                 {"clientInfo": {"name": "alp-workflow", "version": "1"},
                  "capabilities": {"experimentalApi": True}}, counter, 10)
        transport.send({"jsonrpc": "2.0", "method": "initialized", "params": {}})
        record_governed_event("initialized", events)
        
        current_attempt["terminal_stage"] = "account"
        emit_progress("stage", "account")
        account = _request(transport, "account/read", {}, counter, 10)
        record_governed_event("account/read", events)
        
        account_obj = _first(account, "account") or account
        account_type = _first(account_obj, "type", "accountType", "account_type")
        result["evidence"]["account_type"] = (
            account_type if account_type in {"chatgpt", "codex"} else None)
        if account_type not in {"chatgpt", "codex"}:
            raise DispatchError("blocked", "authentication_required")
            
        for method in ("account/rateLimits/read", "account/usage/read"):
            try:
                _request(transport, method, {}, counter, 5)
            except Exception:
                pass
                
        current_attempt["terminal_stage"] = "catalog"
        emit_progress("stage", "catalog")
        model_entries: list[dict[str, Any]] = []
        cursor: str | None = None
        while True:
            models = _request(transport, "model/list",
                              {"cursor": cursor} if cursor else {}, counter, 10)
            record_governed_event("model/list", events)
            model_entries.extend(_model_entries(models))
            cursor = models.get("nextCursor") if isinstance(models, dict) else None
            if not isinstance(cursor, str) or not cursor:
                break
        if not any(_model_supported(entry, requested["model"], requested["effort"])
                   for entry in model_entries):
            raise DispatchError("routing_failure", "model_unavailable")
            
        current_attempt["terminal_stage"] = "thread"
        emit_progress("stage", "thread")
        thread_result = _request(transport, "thread/start", {
            "model": requested["model"],
            "config": {"model_reasoning_effort": requested["effort"]},
            "cwd": packet["cwd"],
            "sandbox": requested["sandbox"],
            "developerInstructions": profile["developer_instructions"],
            "ephemeral": True,
            "allowProviderModelFallback": False,
            "approvalPolicy": "never",
        }, counter, 10)
        record_governed_event("thread/start", events)
        
        thread = _first(thread_result, "thread") or {}
        thread_id = _first(thread, "id", "threadId")
        selected = {
            "model": _first(thread_result, "model", "modelId"),
            "effort": _first(thread_result, "reasoningEffort", "effort"),
            "sandbox": _sandbox_name(_first(thread_result, "sandbox", "sandboxMode")),
        }
        if not isinstance(thread_id, str) or selected != requested:
            raise DispatchError("routing_failure", "thread_runtime_mismatch")
        result["routing"]["selected"] = selected
        thread_id_box[0] = thread_id
        
        current_attempt["terminal_stage"] = "turn"
        emit_progress("stage", "turn")
        task_text = json.dumps({
            "task": packet["task"],
            "paths": packet.get("paths", []),
            "evidence": packet.get("evidence", []),
            "stop_conditions": packet["stop_conditions"],
            "response_contract": packet["response_contract"],
        }, ensure_ascii=False, sort_keys=True)
        
        counter[0] += 1
        turn_request_id = counter[0]
        transport.send({"jsonrpc": "2.0", "id": turn_request_id,
                        "method": "turn/start", "params": {
            "threadId": thread_id,
            "input": [{"type": "text", "text": task_text}],
            "model": requested["model"],
            "effort": requested["effort"],
            "outputSchema": output_schema(packet["response_contract"]),
            "approvalPolicy": "never",
            "cwd": packet["cwd"],
            "sandboxPolicy": _sandbox_policy(requested["sandbox"], packet["cwd"]),
        }})
        turn_submitted = True
        
        current_attempt["terminal_stage"] = "stream"
        emit_progress("stage", "stream")
        response_obj: Any = None
        deadline = start_time + packet["timeout_seconds"]
        
        last_heartbeat_time = time.monotonic()
        
        while True:
            now = time.monotonic()
            remaining_dispatch = deadline - now
            if remaining_dispatch <= 0:
                raise queue.Empty
                
            if turn_started_event_received:
                next_heartbeat = last_heartbeat_time + 30.0
                remaining_heartbeat = next_heartbeat - now
                wait_timeout = min(remaining_dispatch, remaining_heartbeat)
            else:
                wait_timeout = remaining_dispatch
                
            if wait_timeout <= 0:
                if turn_started_event_received and now >= next_heartbeat:
                    emit_progress("heartbeat", "stream")
                    last_heartbeat_time = time.monotonic()
                    continue
                else:
                    raise queue.Empty
                    
            try:
                message = transport.receive(wait_timeout)
            except queue.Empty:
                now = time.monotonic()
                if turn_started_event_received and now >= last_heartbeat_time + 30.0:
                    emit_progress("heartbeat", "stream")
                    last_heartbeat_time = time.monotonic()
                    continue
                raise queue.Empty
                
            if message is None:
                raise DispatchError("transport_failure", "protocol_closed")
            method = message.get("method")
            if method in GOVERNED_EVENTS:
                record_governed_event(method, events)
            params = message.get("params", {})
            
            if message.get("id") == turn_request_id:
                if "error" in message:
                    raise DispatchError("turn_failure", "turn_start_error")
                record_governed_event("turn/start", events)
                turn_result = message.get("result", {})
                turn_id = _first(_first(turn_result, "turn") or turn_result,
                                 "id", "turnId") or turn_id
                continue
                
            if method == "model/rerouted":
                rerouted_turn = _first(params, "turnId")
                result["routing"]["rerouted"] = True
                result["routing"]["reroute_events"] = [{
                    "from_model": _protocol_string(_first(params, "fromModel")),
                    "to_model": _protocol_string(_first(params, "toModel")),
                    "reason": _protocol_string(_first(params, "reason")),
                }]
                exact_turn = rerouted_turn if isinstance(rerouted_turn, str) else turn_id
                if exact_turn is not None:
                    _interrupt(transport, counter, thread_id, exact_turn, events)
                raise DispatchError("routing_failure", "model_rerouted")
                
            if method == "turn/started":
                turn_started_event_received = True
                started_id = _first(params.get("turn", {}), "id", "turnId")
                if isinstance(started_id, str):
                    turn_id = started_id
                emit_progress("turn_started", "stream")
            elif method == "item/completed":
                candidate = _response_from_item(params.get("item"))
                if candidate is not None:
                    response_obj = candidate
            elif method == "thread/tokenUsage/updated":
                usage = params.get("tokenUsage", {})
                result["usage"] = {
                    "last_turn": _usage(usage.get("last")),
                    "thread_total": _usage(usage.get("total")),
                }
            elif method == "turn/completed":
                turn = params.get("turn", {})
                status = _first(turn, "status")
                if status != "completed":
                    error_info = _first(_first(turn, "error") or {}, "codexErrorInfo")
                    if error_info == "sandboxError":
                        raise DispatchError("blocked", "sandbox_blocked")
                    raise DispatchError("turn_failure", "turn_failed")
                break
                
        current_attempt["terminal_stage"] = "response"
        emit_progress("stage", "response")
        if isinstance(response_obj, str):
            try:
                response_obj = json.loads(response_obj)
            except json.JSONDecodeError:
                raise DispatchError("invalid_result", "invalid_response") from None
        response = validate_response(response_obj, packet["response_contract"])
        result["response"] = response
        result["status"] = ("blocked" if response["classification"] == "blocked"
                            else "completed")
        result["evidence"]["inspected_scope"] = response["sections"]["Inspected scope"]
        result["evidence"]["uninspected_scope"] = response["sections"]["Uninspected scope"]
        current_attempt["failure_category"] = None
        return result
        
    except queue.Empty:
        if turn_id is not None and transport is not None and thread_id is not None:
            try:
                _interrupt(transport, counter, thread_id, turn_id, events)
            except Exception:
                pass
            result["status"] = "interrupted"
            code = "turn_timeout"
            current_attempt["failure_category"] = None
        else:
            result["status"] = "transport_failure"
            code = ("transport_failure_after_turn_start" if turn_submitted
                    else "transport_failure_before_turn")
            current_attempt["failure_category"] = "request_timeout"
        result["evidence"]["failure"] = _redacted_failure(code)
        return result
        
    except DispatchError as exc:
        category = "unknown"
        if exc.code in {"protocol_error", "turn_start_error", "turn_failed", "sandbox_blocked"}:
            category = exc.code
        elif exc.code == "protocol_closed":
            category = "protocol_eof"
        else:
            category = None
        current_attempt["failure_category"] = category
        code = exc.code
        if exc.status == "transport_failure":
            code = ("transport_failure_after_turn_start" if turn_submitted
                    else "transport_failure_before_turn")
        result["status"] = exc.status
        result["evidence"]["failure"] = _redacted_failure(code)
        return result
        
    except Exception as exc:
        category = "unknown"
        if isinstance(exc, (FileNotFoundError, OSError)) and getattr(exc, "filename", None) is None:
            if current_attempt["terminal_stage"] == "spawn":
                category = "spawn_os_error"
            else:
                category = "protocol_eof"
        elif isinstance(exc, json.JSONDecodeError):
            category = "protocol_decode_error"
            
        current_attempt["failure_category"] = category
        result["status"] = "transport_failure"
        code = ("transport_failure_after_turn_start" if turn_submitted
                else "transport_failure_before_turn")
        result["evidence"]["failure"] = _redacted_failure(code)
        return result
        
    finally:
        if process:
            try:
                transport.close()
            except Exception:
                pass
            exit_status = process.poll()
            if exit_status is not None:
                current_attempt["child_exit_status"] = exit_status


def dispatch(packet: dict[str, Any], profile_dir: Path | None = None, transport_factory: Any = None, log_file_param: Any = None, log_path: Path | None = None) -> dict[str, Any]:
    global log_truncated, bytes_written, log_file, start_time, last_gov_event
    log_file = log_file_param
    log_truncated = False
    bytes_written = 0
    last_gov_event = None
    if start_time == 0.0:
        start_time = time.monotonic()
    
    packet = validate_packet(packet)
    profile, profile_path = load_profile(packet["role"], profile_dir)
    if SANDBOX_RANK[packet["sandbox"]] > SANDBOX_RANK[profile["sandbox_mode"]]:
        raise DispatchError("blocked", "sandbox_widening")

    attempts = []
    thread_id_box = [None]
    
    for attempt_idx in range(2):
        attempt_num = attempt_idx + 1
        current_attempt = {
            "number": attempt_num,
            "terminal_stage": "spawn",
            "failure_category": None,
            "child_exit_status": None
        }
        attempts.append(current_attempt)
        
        result = _run_once(packet, profile, profile_path, transport_factory, log_file, log_path, current_attempt, thread_id_box)
        
        failure = result["evidence"]["failure"]
        retryable = (
            result["status"] == "transport_failure"
            and isinstance(failure, dict)
            and failure.get("code") == "transport_failure_before_turn"
            and current_attempt["terminal_stage"] in {"spawn", "initialize", "catalog"}
        )
        if not retryable or attempt_idx == 1:
            break

    if log_path is not None:
        result["diagnostic"] = {
            "log_path": str(log_path),
            "log_truncated": log_truncated,
            "stage": current_attempt["terminal_stage"],
            "attempts": attempts,
            "thread_id": thread_id_box[0]
        }
    emit_progress("terminal", current_attempt["terminal_stage"], result["status"])
    return result


def main(argv: list[str] | None = None, transport_factory: Any = None) -> int:
    global start_time, log_file, log_truncated, bytes_written
    reset_globals()
    
    arguments = sys.argv[1:] if argv is None else argv
    
    packet_path = None
    diagnostic_log = None
    probe_startup = False

    i = 0
    while i < len(arguments):
        arg = arguments[i]
        if arg == "--packet":
            if i + 1 >= len(arguments):
                return handle_invalid_invocation()
            packet_path = arguments[i+1]
            i += 2
        elif arg == "--diagnostic-log":
            if i + 1 >= len(arguments):
                return handle_invalid_invocation()
            diagnostic_log = arguments[i+1]
            i += 2
        elif arg == "--probe-startup":
            probe_startup = True
            i += 1
        else:
            return handle_invalid_invocation()
            
    if (packet_path is not None) == probe_startup:
        return handle_invalid_invocation()
    if packet_path is not None and not packet_path:
        return handle_invalid_invocation()
    if diagnostic_log is not None and not diagnostic_log:
        return handle_invalid_invocation()
        
    if probe_startup:
        log_file = None
        log_path = None
        if diagnostic_log is not None:
            try:
                log_path, log_file = validate_and_create_log(diagnostic_log, None)
            except InvalidLogException:
                result = {
                    "schema_version": 1,
                    "mode": "startup_probe",
                    "status": "blocked",
                    "exit_code": 20,
                    "probe": {
                        "log_path": None,
                        "log_truncated": False,
                        "stage": "spawn",
                        "attempts": [],
                        "account_type": None
                    }
                }
                sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
                return 20
        try:
            result = run_startup_probe(log_file, log_path, transport_factory)
            sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
            return result["exit_code"]
        finally:
            if log_file is not None:
                try:
                    log_file.close()
                except Exception:
                    pass

    packet_hint: dict[str, Any] = {}
    log_path = None
    log_file = None
    try:
        if packet_path == "-":
            raw = sys.stdin.buffer.readline()
        else:
            raw = Path(packet_path).read_bytes()
            
        start_time = time.monotonic()
        emit_progress("packet_received", None)
        
        def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
            value: dict[str, Any] = {}
            for key, item in pairs:
                if key in value:
                    raise ValueError("duplicate JSON key")
                value[key] = item
            return value

        decoded = json.loads(raw.decode("utf-8"),
                             object_pairs_hook=reject_duplicates)
        packet_hint = decoded if isinstance(decoded, dict) else {}
        emit_progress("packet_parsed", None)
        
        if diagnostic_log is not None:
            cwd = packet_hint.get("cwd")
            log_path, log_file = validate_and_create_log(diagnostic_log, cwd)
            
        result = dispatch(decoded, transport_factory=transport_factory, log_file_param=log_file, log_path=log_path)
        sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
        return EXIT_CODES[result["status"]]
        
    except InvalidLogException:
        result = _blank_result(packet_hint)
        result["status"] = "blocked"
        result["evidence"]["failure"] = _redacted_failure("invalid_diagnostic_log")
        emit_progress("terminal", "spawn", "blocked")
        sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
        return EXIT_CODES["blocked"]
        
    except (json.JSONDecodeError, UnicodeError, ValueError, DispatchError, OSError, TypeError):
        result = _blank_result(packet_hint)
        if isinstance(sys.exc_info()[1], DispatchError):
            result["status"] = sys.exc_info()[1].status
            result["evidence"]["failure"] = _redacted_failure(sys.exc_info()[1].code)
        else:
            result["status"] = "blocked"
            result["evidence"]["failure"] = _redacted_failure("invalid_packet")
            
        if log_path is not None:
            result["diagnostic"] = {
                "log_path": str(log_path),
                "log_truncated": log_truncated,
                "stage": "spawn",
                "attempts": [],
                "thread_id": None
            }
        emit_progress("terminal", "spawn", "blocked")
        sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
        return EXIT_CODES[result["status"]]
        
    except Exception as exc:
        result = _blank_result(packet_hint)
        result["status"] = "transport_failure"
        result["evidence"]["failure"] = _redacted_failure("dispatcher_internal_failure")
        emit_progress("terminal", "spawn", "transport_failure")
        sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
        return EXIT_CODES["transport_failure"]
    finally:
        if log_file:
            try:
                log_file.close()
            except Exception:
                pass


def handle_invalid_invocation() -> int:
    result = _blank_result({})
    result["evidence"]["failure"] = _redacted_failure("invalid_invocation")
    sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
    return EXIT_CODES["blocked"]


if __name__ == "__main__":
    raise SystemExit(main())
