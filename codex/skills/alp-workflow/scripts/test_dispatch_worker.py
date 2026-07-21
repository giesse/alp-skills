#!/usr/bin/env python3
"""Deterministic standard-library tests for dispatch_worker.py."""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import time
import tomllib
from pathlib import Path
from queue import Empty

import dispatch_worker as dw

CONTRACT = {
    "classifications": ["complete", "blocked"],
    "required_sections": [
        "Conclusion", "Evidence", "Uncertainty", "Inspected scope",
        "Uninspected scope",
    ],
}
SECTIONS = {name: f"value for {name}" for name in CONTRACT["required_sections"]}


def packet(root: Path, **overrides):
    value = {
        "schema_version": 1,
        "role": "explorer",
        "task": "inspect bounded evidence secret-prompt-marker",
        "cwd": str(root),
        "sandbox": "read-only",
        "timeout_seconds": 1,
        "response_contract": CONTRACT,
        "stop_conditions": ["stop on ambiguity"],
        "paths": [],
        "evidence": [],
    }
    value.update(overrides)
    return value


class FakeTransport:
    def __init__(self, mode="success"):
        self.mode = mode
        self.sent = []
        self.closed = False
        self.events = self._events()
        self.index = 0
        self.turn_start_sent = False
        self.turn_started_received = False

    def send(self, message):
        self.sent.append(message)
        if isinstance(message, dict) and message.get("method") == "turn/start":
            self.turn_start_sent = True

    def receive(self, timeout):
        if self.mode == "stall" and self.index >= len(self.events):
            raise Empty
        if self.index >= len(self.events):
            return None
        event = self.events[self.index]
        self.index += 1
        if isinstance(event, dict) and event.get("method") == "turn/started":
            self.turn_started_received = True
        return event

    def close(self):
        self.closed = True

    @staticmethod
    def model_entry():
        return {
            "id": "luna-alias",
            "model": "gpt-5.6-luna",
            "supportedReasoningEfforts": [
                {"reasoningEffort": "low", "description": "low"}
            ],
        }

    def _events(self):
        events = [
            {"id": 1, "result": {}},
            {"method": "account/updated", "params": {"email": "secret@example.test"}},
            {"id": 2, "result": {"account": {
                "type": "apiKey" if self.mode == "wrong_account" else "chatgpt",
                "email": "secret@example.test"}}},
            {"id": 3, "result": {"raw": "private-rate-data"}},
            {"id": 4, "result": {"raw": "private-usage-data"}},
        ]
        if self.mode == "pagination":
            events.extend([
                {"id": 5, "result": {"data": [], "nextCursor": "next"}},
                {"id": 6, "result": {"data": [self.model_entry()], "nextCursor": None}},
            ])
            thread_id, turn_request_id = 7, 8
        else:
            models = [] if self.mode == "unsupported" else [self.model_entry()]
            events.append({"id": 5, "result": {"data": models, "nextCursor": None}})
            if self.mode == "unsupported":
                return events
            thread_id, turn_request_id = 6, 7

        selected_model = "gpt-5.6-terra" if self.mode == "mismatch" else "gpt-5.6-luna"
        events.append({"id": thread_id, "result": {
            "thread": {"id": "thread-1"},
            "model": selected_model,
            "reasoningEffort": "low",
            "sandbox": {"type": "readOnly", "networkAccess": False},
        }})
        if self.mode == "mismatch":
            return events
        if self.mode == "notifications_before_reply":
            response = {"classification": "complete", "sections": dict(SECTIONS)}
            text = json.dumps(response)
            events.extend([
                {"method": "turn/started", "params": {
                    "threadId": "thread-1", "turn": {"id": "turn-1"}}},
                {"method": "item/completed", "params": {"item": {
                    "id": "item-1", "type": "agentMessage", "text": text,
                    "memoryCitation": None}}},
                {"method": "thread/tokenUsage/updated", "params": {
                    "threadId": "thread-1", "turnId": "turn-1", "tokenUsage": {
                        "last": {"inputTokens": 10, "cachedInputTokens": 3,
                                 "outputTokens": 2, "reasoningOutputTokens": 1,
                                 "totalTokens": 12},
                        "total": {"inputTokens": 10, "cachedInputTokens": 3,
                                  "outputTokens": 2, "reasoningOutputTokens": 1,
                                  "totalTokens": 12},
                    }}},
                {"method": "turn/completed", "params": {"turn": {
                    "id": "turn-1", "items": [], "status": "completed", "error": None}}},
                {"id": turn_request_id, "result": {"turn": {"id": "turn-1"}}},
            ])
            return events
        events.extend([
            {"id": turn_request_id, "result": {"turn": {"id": "turn-1"}}},
            {"method": "turn/started", "params": {
                "threadId": "thread-1", "turn": {"id": "turn-1"}}},
        ])
        if self.mode in {"stall", "stream_failure"}:
            return events
        if self.mode == "reroute":
            events.append({"method": "model/rerouted", "params": {
                "fromModel": "gpt-5.6-luna", "toModel": "gpt-5.6-terra",
                "reason": "highRiskCyberActivity", "turnId": "turn-1"}})
            return events
        if self.mode == "invalid_missing":
            response = {"classification": "complete",
                        "sections": {"Conclusion": "only one"}}
        elif self.mode == "invalid_extra":
            response = {"classification": "complete", "sections": dict(SECTIONS),
                        "extra": "not allowed"}
        elif self.mode == "invalid_classification":
            response = {"classification": "surprise", "sections": dict(SECTIONS)}
        elif self.mode == "invalid_json":
            response = "{not json"
        elif self.mode == "blocked_response":
            response = {"classification": "blocked", "sections": dict(SECTIONS)}
        else:
            response = {"classification": "complete", "sections": dict(SECTIONS)}
        text = response if isinstance(response, str) else json.dumps(response)
        events.append({"method": "item/completed", "params": {"item": {
            "id": "item-1", "type": "agentMessage", "text": text,
            "memoryCitation": None}}})
        events.append({"method": "thread/tokenUsage/updated", "params": {
            "threadId": "thread-1", "turnId": "turn-1", "tokenUsage": {
                "last": {"inputTokens": 10, "cachedInputTokens": 3,
                         "outputTokens": 2, "reasoningOutputTokens": 1,
                         "totalTokens": 12},
                "total": {"inputTokens": 10, "cachedInputTokens": 3,
                          "outputTokens": 2, "reasoningOutputTokens": 1,
                          "totalTokens": 12},
            }}})
        if self.mode == "turn_failure":
            status, error = "failed", {"codexErrorInfo": "other", "message": "secret"}
        elif self.mode == "sandbox_blocked":
            status, error = "failed", {"codexErrorInfo": "sandboxError", "message": "secret"}
        else:
            status, error = "completed", None
        events.append({"method": "turn/completed", "params": {"turn": {
            "id": "turn-1", "items": [], "status": status, "error": error}}})
        return events


class DispatchWorkerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.profiles = self.root / "agents"
        self.profiles.mkdir()
        (self.profiles / "alp_explorer.toml").write_text(
            'name = "alp_explorer"\n'
            'description = "bounded explorer"\n'
            'model = "gpt-5.6-luna"\n'
            'model_reasoning_effort = "low"\n'
            'sandbox_mode = "read-only"\n'
            'developer_instructions = "stable role instructions"\n',
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()
        dw.reset_globals()

    def assert_packet_rejected(self, **changes):
        with self.assertRaises(dw.DispatchError):
            dw.validate_packet(packet(self.root, **changes))

    def test_packet_required_unknown_types_duplicates_and_paths(self):
        for required in dw.REQUIRED_PACKET_KEYS:
            with self.subTest(required=required):
                value = packet(self.root)
                del value[required]
                with self.assertRaises(dw.DispatchError):
                    dw.validate_packet(value)
        self.assert_packet_rejected(extra=True)
        self.assert_packet_rejected(schema_version=True)
        self.assert_packet_rejected(role=[])
        self.assert_packet_rejected(task=None)
        self.assert_packet_rejected(cwd=str(self.root / "missing"))
        self.assert_packet_rejected(sandbox="danger-full-access")
        self.assert_packet_rejected(timeout_seconds=True)
        self.assert_packet_rejected(timeout_seconds=0)
        self.assert_packet_rejected(stop_conditions=[])
        self.assert_packet_rejected(stop_conditions=["same", "same"])
        self.assert_packet_rejected(evidence=["same", "same"])
        self.assert_packet_rejected(paths=["../escape"])
        self.assertEqual(dw.validate_packet(packet(
            self.root, paths=["relative/file", "/explicit/read/path"]))["role"],
            "explorer")

    def test_response_contract_is_closed_and_mandatory(self):
        self.assert_packet_rejected(response_contract={
            "classifications": ["complete"],
            "required_sections": list(CONTRACT["required_sections"]),
        })
        self.assert_packet_rejected(response_contract={
            "classifications": ["complete", "blocked", "blocked"],
            "required_sections": list(CONTRACT["required_sections"]),
        })
        self.assert_packet_rejected(response_contract={
            "classifications": ["complete", "blocked"],
            "required_sections": ["Inspected scope", "Uninspected scope"],
        })
        schema = dw.output_schema(CONTRACT)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["properties"]["sections"]["additionalProperties"])
        self.assertEqual(schema["properties"]["classification"]["enum"],
                         ["complete", "blocked"])

    def test_profile_validation_and_sandbox_ceiling(self):
        with self.assertRaises(dw.DispatchError):
            dw.load_profile("unknown", self.profiles)
        (self.profiles / "alp_tangler.toml").write_text("not toml", encoding="utf-8")
        with self.assertRaises(dw.DispatchError):
            dw.load_profile("tangler", self.profiles)
        with self.assertRaises(dw.DispatchError):
            dw.dispatch(packet(self.root, sandbox="workspace-write"), self.profiles,
                        lambda: FakeTransport())

    def test_requests_match_protocol_and_context_is_packet_only(self):
        fake = FakeTransport()
        result = dw.dispatch(packet(self.root), self.profiles, lambda: fake)
        self.assertEqual(result["status"], "completed")
        methods = [entry["method"] for entry in fake.sent]
        self.assertEqual(methods[:3], ["initialize", "initialized", "account/read"])
        thread = next(entry for entry in fake.sent if entry["method"] == "thread/start")
        self.assertEqual(thread["params"]["sandbox"], "read-only")
        self.assertEqual(thread["params"]["config"], {"model_reasoning_effort": "low"})
        self.assertEqual(thread["params"]["developerInstructions"],
                         "stable role instructions")
        self.assertTrue(thread["params"]["ephemeral"])
        self.assertFalse(thread["params"]["allowProviderModelFallback"])
        self.assertEqual(thread["params"]["approvalPolicy"], "never")
        self.assertNotIn("multiAgentMode", thread["params"])
        turn = next(entry for entry in fake.sent if entry["method"] == "turn/start")
        self.assertEqual(turn["params"]["model"], "gpt-5.6-luna")
        self.assertEqual(turn["params"]["effort"], "low")
        self.assertEqual(turn["params"]["sandboxPolicy"]["type"], "readOnly")
        supplied = json.loads(turn["params"]["input"][0]["text"])
        self.assertEqual(set(supplied), {"task", "paths", "evidence",
                                         "stop_conditions", "response_contract"})
        self.assertNotIn("parent transcript", turn["params"]["input"][0]["text"])

    def test_normalized_result_usage_events_and_privacy(self):
        result = dw.dispatch(packet(self.root), self.profiles, lambda: FakeTransport())
        self.assertEqual(set(result), {"schema_version", "role", "routing", "status",
                                       "response", "usage", "evidence"})
        self.assertEqual(result["routing"]["requested"], result["routing"]["selected"])
        self.assertEqual(result["usage"]["last_turn"]["cached_input_tokens"], 3)
        self.assertEqual(result["evidence"]["events"], [
            "initialized", "account/read", "model/list", "thread/start",
            "turn/start", "turn/started", "item/completed", "turn/completed",
        ])
        rendered = json.dumps(result)
        for secret in ("secret@example.test", "private-rate-data",
                       "private-usage-data", "secret-prompt-marker"):
            self.assertNotIn(secret, rendered)

    def test_catalog_pagination_and_routing_fail_closed(self):
        self.assertEqual(dw.dispatch(packet(self.root), self.profiles,
                                     lambda: FakeTransport("pagination"))["status"],
                          "completed")
        for mode in ("unsupported", "mismatch"):
            fake = FakeTransport(mode)
            result = dw.dispatch(packet(self.root), self.profiles, lambda fake=fake: fake)
            self.assertEqual(result["status"], "routing_failure")
            self.assertNotIn("turn/start", [entry["method"] for entry in fake.sent])
        fake = FakeTransport("reroute")
        result = dw.dispatch(packet(self.root), self.profiles, lambda: fake)
        self.assertEqual(result["status"], "routing_failure")
        self.assertTrue(result["routing"]["rerouted"])
        self.assertEqual([entry["method"] for entry in fake.sent].count("turn/interrupt"), 1)

    def test_authentication_fails_before_model_or_turn(self):
        fake = FakeTransport("wrong_account")
        result = dw.dispatch(packet(self.root), self.profiles, lambda: fake)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["evidence"]["account_type"], None)
        methods = [entry["method"] for entry in fake.sent]
        self.assertNotIn("model/list", methods)
        self.assertNotIn("turn/start", methods)

    def test_timeout_interrupts_once_without_replay(self):
        fake = FakeTransport("stall")
        result = dw.dispatch(packet(self.root), self.profiles, lambda: fake)
        self.assertEqual(result["status"], "interrupted")
        self.assertEqual([entry["method"] for entry in fake.sent].count("turn/interrupt"), 1)
        self.assertEqual([entry["method"] for entry in fake.sent].count("turn/start"), 1)

    def test_transport_retry_only_before_turn_submission(self):
        class Factory:
            def __init__(self, first_mode=None):
                self.calls = 0
                self.first_mode = first_mode

            def __call__(self):
                self.calls += 1
                if self.calls == 1 and self.first_mode is None:
                    raise OSError("startup")
                return FakeTransport(self.first_mode or "success")

        startup = Factory()
        self.assertEqual(dw.dispatch(packet(self.root), self.profiles, startup)["status"],
                          "completed")
        self.assertEqual(startup.calls, 2)
        after_start = Factory("stream_failure")
        result = dw.dispatch(packet(self.root), self.profiles, after_start)
        self.assertEqual(result["status"], "transport_failure")
        self.assertEqual(result["evidence"]["failure"]["code"],
                         "transport_failure_after_turn_start")
        self.assertEqual(after_start.calls, 1)

    def test_turn_failures_blocked_and_response_classification(self):
        expected = {
            "turn_failure": "turn_failure",
            "sandbox_blocked": "blocked",
            "blocked_response": "blocked",
        }
        for mode, status in expected.items():
            with self.subTest(mode=mode):
                result = dw.dispatch(packet(self.root), self.profiles,
                                     lambda mode=mode: FakeTransport(mode))
                self.assertEqual(result["status"], status)
                self.assertNotIn("secret", json.dumps(result))

    def test_invalid_response_matrix_never_repairs_with_model(self):
        for mode in ("invalid_missing", "invalid_extra", "invalid_classification",
                     "invalid_json"):
            with self.subTest(mode=mode):
                fake = FakeTransport(mode)
                result = dw.dispatch(packet(self.root), self.profiles,
                                     lambda fake=fake: fake)
                self.assertEqual(result["status"], "invalid_result")
                self.assertEqual([entry["method"] for entry in fake.sent].count(
                    "turn/start"), 1)

    def test_cli_path_stdin_duplicate_json_and_exit_mapping(self):
        self.assertEqual(dw.EXIT_CODES, {
            "completed": 0, "blocked": 20, "interrupted": 21,
            "routing_failure": 22, "turn_failure": 23,
            "transport_failure": 24, "invalid_result": 25,
        })
        script = Path(dw.__file__)
        invalid = {"schema_version": 1, "role": "unknown"}
        packet_path = self.root / "packet.json"
        packet_path.write_text(json.dumps(invalid), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(script), "--packet", str(packet_path)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 20)
        self.assertTrue(packet_path.exists())
        self.assertEqual(json.loads(result.stdout)["status"], "blocked")
        self.assertIn("packet_received", result.stderr)
        self.assertIn("terminal", result.stderr)
        
        duplicate = '{"schema_version":1,"schema_version":1}'
        result = subprocess.run(
            [sys.executable, str(script), "--packet", "-"], input=duplicate,
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 20)
        self.assertEqual(json.loads(result.stdout)["evidence"]["failure"]["code"],
                          "invalid_packet")
        result = subprocess.run([sys.executable, str(script)], text=True,
                                capture_output=True, check=False)
        self.assertEqual(result.returncode, 20)
        self.assertEqual(json.loads(result.stdout)["evidence"]["failure"]["code"],
                          "invalid_invocation")

    def test_diagnostic_log_validation(self):
        packet_data = packet(self.root)
        packet_file = self.root / "packet.json"
        packet_file.write_text(json.dumps(packet_data), encoding="utf-8")

        # 1. Non-absolute log path
        log_path_rel = "relative/diag.log"
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = io.StringIO(), io.StringIO()
        try:
            exit_code = dw.main(["--packet", str(packet_file), "--diagnostic-log", log_path_rel], transport_factory=lambda: FakeTransport())
            self.assertEqual(exit_code, 20)
            result = json.loads(sys.stdout.getvalue())
            self.assertEqual(result["status"], "blocked")
            self.assertEqual(result["evidence"]["failure"]["code"], "invalid_diagnostic_log")
            self.assertNotIn("diagnostic", result)
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr

        # 2. Packet cwd-internal log path
        log_path_cwd_internal = str(self.root / "diag.log")
        
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = io.StringIO(), io.StringIO()
        try:
            exit_code = dw.main(["--packet", str(packet_file), "--diagnostic-log", log_path_cwd_internal], transport_factory=lambda: FakeTransport())
            self.assertEqual(exit_code, 20)
            result = json.loads(sys.stdout.getvalue())
            self.assertEqual(result["status"], "blocked")
            self.assertEqual(result["evidence"]["failure"]["code"], "invalid_diagnostic_log")
            self.assertNotIn("diagnostic", result)
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr

        # 3. Existing log file
        log_path_exist = self.root.parent / "existing_diag.log"
        log_path_exist.write_text("already here", encoding="utf-8")
        try:
            old_stdout, old_stderr = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = io.StringIO(), io.StringIO()
            try:
                exit_code = dw.main(["--packet", str(packet_file), "--diagnostic-log", str(log_path_exist)], transport_factory=lambda: FakeTransport())
                self.assertEqual(exit_code, 20)
                result = json.loads(sys.stdout.getvalue())
                self.assertEqual(result["status"], "blocked")
                self.assertNotIn("diagnostic", result)
            finally:
                sys.stdout, sys.stderr = old_stdout, old_stderr
        finally:
            if log_path_exist.exists():
                log_path_exist.unlink()

        # 4. Uncreatable log file (missing directory)
        log_path_uncreatable = "/nonexistent_dir_xyz/diag.log"
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = io.StringIO(), io.StringIO()
        try:
            exit_code = dw.main(["--packet", str(packet_file), "--diagnostic-log", log_path_uncreatable], transport_factory=lambda: FakeTransport())
            self.assertEqual(exit_code, 20)
            result = json.loads(sys.stdout.getvalue())
            self.assertEqual(result["status"], "blocked")
            self.assertNotIn("diagnostic", result)
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr

    def test_attempts_and_no_attempt_before_child_creation(self):
        log_path_rel = "relative/diag.log"
        packet_data = packet(self.root)
        packet_file = self.root / "packet.json"
        packet_file.write_text(json.dumps(packet_data), encoding="utf-8")
        
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = io.StringIO(), io.StringIO()
        try:
            exit_code = dw.main(["--packet", str(packet_file), "--diagnostic-log", log_path_rel], transport_factory=lambda: FakeTransport())
            self.assertEqual(exit_code, 20)
            result = json.loads(sys.stdout.getvalue())
            self.assertNotIn("diagnostic", result)
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr

        # Check when log created but packet validation fails (sandbox rank widening)
        log_path_valid = self.root.parent / "valid_diag.log"
        if log_path_valid.exists():
            log_path_valid.unlink()
        try:
            packet_data_invalid = packet(self.root, sandbox="workspace-write")
            packet_file_invalid = self.root / "packet_invalid.json"
            packet_file_invalid.write_text(json.dumps(packet_data_invalid), encoding="utf-8")
            
            old_stdout, old_stderr = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = io.StringIO(), io.StringIO()
            try:
                exit_code = dw.main(["--packet", str(packet_file_invalid), "--diagnostic-log", str(log_path_valid)], transport_factory=lambda: FakeTransport())
                self.assertEqual(exit_code, 20)
                result = json.loads(sys.stdout.getvalue())
                self.assertEqual(result["status"], "blocked")
                self.assertIn("diagnostic", result)
                diag = result["diagnostic"]
                self.assertEqual(diag["log_path"], str(log_path_valid))
                self.assertEqual(diag["attempts"], [])
                self.assertEqual(diag["stage"], "spawn")
            finally:
                sys.stdout, sys.stderr = old_stdout, old_stderr
        finally:
            if log_path_valid.exists():
                log_path_valid.unlink()

    def test_probe_json_and_process_exit_equality(self):
        log_path = self.root.parent / "probe_success.log"
        if log_path.exists():
            log_path.unlink()
        
        try:
            old_stdout, old_stderr = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = io.StringIO(), io.StringIO()
            try:
                dw.reset_globals()
                dw.start_time = 0.0
                exit_code = dw.main(["--probe-startup", "--diagnostic-log", str(log_path)], transport_factory=lambda: FakeTransport())
                result = json.loads(sys.stdout.getvalue())
                self.assertEqual(exit_code, result["exit_code"])
                self.assertEqual(result["status"], "completed")
                self.assertEqual(result["exit_code"], 0)
                self.assertEqual(result["probe"]["stage"], "catalog")
            finally:
                sys.stdout, sys.stderr = old_stdout, old_stderr
        finally:
            if log_path.exists():
                log_path.unlink()

    def test_final_attempt_stage_semantics(self):
        log_path = self.root.parent / "stall_diag.log"
        if log_path.exists():
            log_path.unlink()
            
        log_file = None
        try:
            packet_data = packet(self.root)
            log_path_created, log_file = dw.validate_and_create_log(str(log_path), str(self.root))
            result = dw.dispatch(packet_data, self.profiles, lambda: FakeTransport("stall"), log_file, log_path_created)
            self.assertEqual(result["status"], "interrupted")
            self.assertIn("diagnostic", result)
            diag = result["diagnostic"]
            self.assertEqual(diag["stage"], "stream")
            self.assertEqual(len(diag["attempts"]), 1)
            self.assertEqual(diag["attempts"][0]["terminal_stage"], "stream")
            self.assertEqual(diag["attempts"][0]["failure_category"], None)
        finally:
            if log_file:
                log_file.close()
            if log_path.exists():
                log_path.unlink()

    def test_normal_result_compatibility_and_no_default_log(self):
        result = dw.dispatch(packet(self.root), self.profiles, lambda: FakeTransport())
        self.assertEqual(result["status"], "completed")
        self.assertNotIn("diagnostic", result)

    def test_log_truncation_flag_and_draining(self):
        log_path = self.root / "trunc_test.log"
        if log_path.exists():
            log_path.unlink()
        log_file = None
        try:
            log_path_created, log_file = dw.validate_and_create_log(str(log_path), None)
            dw.log_file = log_file
            dw.bytes_written = 8 * 1024 * 1024 - 10
            dw.log_truncated = False
            
            dw.log_diagnostic("test", "a" * 20)
            self.assertTrue(dw.log_truncated)
            
            prev_bytes = dw.bytes_written
            dw.log_diagnostic("test", "another write")
            self.assertEqual(dw.bytes_written, prev_bytes)
        finally:
            if log_file:
                log_file.close()
            if log_path.exists():
                log_path.unlink()

    def test_stdin_stream_kept_open(self):
        script = Path(dw.__file__)
        packet_data = packet(self.root)
        
        env = dict(os.environ)
        env["CODEX_HOME"] = str(self.root)
        env["PYTHONUNBUFFERED"] = "1"
        
        bin_dir = self.root / "bin"
        bin_dir.mkdir(parents=True, exist_ok=True)
        mock_codex = bin_dir / "codex"
        
        mock_codex.write_text(
            f"#!/usr/bin/env python3\n"
            f"import sys, json\n"
            f"while True:\n"
            f"    line = sys.stdin.readline()\n"
            f"    if not line:\n"
            f"        break\n"
            f"    try:\n"
            f"        msg = json.loads(line)\n"
            f"        method = msg.get('method')\n"
            f"        ident = msg.get('id')\n"
            f"        if method == 'initialize':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{}}}}), flush=True)\n"
            f"        elif method == 'account/read':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{'account': {{'type': 'chatgpt'}}}}}}), flush=True)\n"
            f"        elif method == 'account/rateLimits/read':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{}}}}), flush=True)\n"
            f"        elif method == 'account/usage/read':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{}}}}), flush=True)\n"
            f"        elif method == 'model/list':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{'data': [{{'id': 'gpt-5.6-luna', 'supportedReasoningEfforts': [{{'effort': 'low'}}]}}]}}}}), flush=True)\n"
            f"        elif method == 'thread/start':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{'thread': {{'id': 'thread-1'}}, 'model': 'gpt-5.6-luna', 'reasoningEffort': 'low', 'sandbox': {{'type': 'readOnly'}}}}}}), flush=True)\n"
            f"        elif method == 'turn/start':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{'turn': {{'id': 'turn-1'}}}}}}), flush=True)\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'method': 'turn/started', 'params': {{'turn': {{'id': 'turn-1'}}}}}}), flush=True)\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'method': 'item/completed', 'params': {{'item': {{'type': 'agentMessage', 'text': '{{\"classification\": \"complete\", \"sections\": {json.dumps(SECTIONS)}}}'}}}}}}), flush=True)\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'method': 'turn/completed', 'params': {{'turn': {{'status': 'completed'}}}}}}), flush=True)\n"
            f"    except Exception:\n"
            f"        pass\n",
            encoding="utf-8"
        )
        mock_codex.chmod(0o755)
        
        env["PATH"] = str(bin_dir) + os.path.pathsep + env.get("PATH", "")
        
        proc = subprocess.Popen(
            [sys.executable, str(script), "--packet", "-"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, env=env
        )
        try:
            proc.stdin.write(json.dumps(packet_data) + "\n")
            proc.stdin.flush()
            
            stdout_data, stderr_data = proc.communicate(timeout=15)
            if proc.returncode != 0:
                sys.__stdout__.write("--- test_stdin_stream_kept_open STDOUT ---\n")
                sys.__stdout__.write(stdout_data + "\n")
                sys.__stdout__.write("--- test_stdin_stream_kept_open STDERR ---\n")
                sys.__stdout__.write(stderr_data + "\n")
            self.assertEqual(proc.returncode, 0)
            result = json.loads(stdout_data)
            self.assertEqual(result["status"], "completed")
            self.assertIn("turn_started", stderr_data)
        except subprocess.TimeoutExpired as err:
            proc.kill()
            stdout_data, stderr_data = proc.communicate()
            sys.__stdout__.write("--- test_stdin_stream_kept_open TIMEOUT STDOUT ---\n")
            sys.__stdout__.write(stdout_data + "\n")
            sys.__stdout__.write("--- test_stdin_stream_kept_open TIMEOUT STDERR ---\n")
            sys.__stdout__.write(stderr_data + "\n")
            raise err
        finally:
            if proc.poll() is None:
                proc.kill()
                proc.wait()
            for stream in (proc.stdin, proc.stdout, proc.stderr):
                if stream:
                    stream.close()

    def test_large_stderr_log_truncation(self):
        script = Path(dw.__file__)
        packet_data = packet(self.root)
        log_path = self.root.parent / "oversized.log"
        if log_path.exists():
            log_path.unlink()
        
        env = dict(os.environ)
        env["CODEX_HOME"] = str(self.root)
        env["PYTHONUNBUFFERED"] = "1"
        
        bin_dir = self.root / "bin"
        bin_dir.mkdir(parents=True, exist_ok=True)
        mock_codex = bin_dir / "codex"
        
        mock_codex.write_text(
            f"#!/usr/bin/env python3\n"
            f"import sys, json\n"
            f"sys.stderr.write(('X' * 8999 + '\\n') * 1000)\n"
            f"sys.stderr.flush()\n"
            f"while True:\n"
            f"    line = sys.stdin.readline()\n"
            f"    if not line:\n"
            f"        break\n"
            f"    try:\n"
            f"        msg = json.loads(line)\n"
            f"        method = msg.get('method')\n"
            f"        ident = msg.get('id')\n"
            f"        if method == 'initialize':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{}}}}), flush=True)\n"
            f"        elif method == 'account/read':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{'account': {{'type': 'chatgpt'}}}}}}), flush=True)\n"
            f"        elif method == 'account/rateLimits/read':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{}}}}), flush=True)\n"
            f"        elif method == 'account/usage/read':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{}}}}), flush=True)\n"
            f"        elif method == 'model/list':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{'data': [{{'id': 'gpt-5.6-luna', 'supportedReasoningEfforts': [{{'effort': 'low'}}]}}]}}}}), flush=True)\n"
            f"        elif method == 'thread/start':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{'thread': {{'id': 'thread-1'}}, 'model': 'gpt-5.6-luna', 'reasoningEffort': 'low', 'sandbox': {{'type': 'readOnly'}}}}}}), flush=True)\n"
            f"        elif method == 'turn/start':\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'id': ident, 'result': {{'turn': {{'id': 'turn-1'}}}}}}), flush=True)\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'method': 'turn/started', 'params': {{'turn': {{'id': 'turn-1'}}}}}}), flush=True)\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'method': 'item/completed', 'params': {{'item': {{'type': 'agentMessage', 'text': '{{\"classification\": \"complete\", \"sections\": {json.dumps(SECTIONS)}}}'}}}}}}), flush=True)\n"
            f"            print(json.dumps({{'jsonrpc': '2.0', 'method': 'turn/completed', 'params': {{'turn': {{'status': 'completed'}}}}}}), flush=True)\n"
            f"    except Exception:\n"
            f"        pass\n",
            encoding="utf-8"
        )
        mock_codex.chmod(0o755)
        
        env["PATH"] = str(bin_dir) + os.path.pathsep + env.get("PATH", "")
        
        proc = subprocess.Popen(
            [sys.executable, str(script), "--packet", "-", "--diagnostic-log", str(log_path)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, env=env
        )
        try:
            proc.stdin.write(json.dumps(packet_data) + "\n")
            proc.stdin.flush()
            
            stdout_data, stderr_data = proc.communicate(timeout=20)
            if proc.returncode != 0:
                sys.__stdout__.write("--- test_large_stderr_log_truncation STDOUT ---\n")
                sys.__stdout__.write(stdout_data + "\n")
                sys.__stdout__.write("--- test_large_stderr_log_truncation STDERR ---\n")
                sys.__stdout__.write(stderr_data + "\n")
            self.assertEqual(proc.returncode, 0)
            result = json.loads(stdout_data)
            self.assertEqual(result["status"], "completed")
            self.assertTrue(result["diagnostic"]["log_truncated"])
            self.assertTrue(log_path.exists())
            self.assertEqual(log_path.stat().st_size, 8 * 1024 * 1024)
        finally:
            if proc.poll() is None:
                proc.kill()
                proc.wait()
            for stream in (proc.stdin, proc.stdout, proc.stderr):
                if stream:
                    stream.close()
            if log_path.exists():
                log_path.unlink()

    def test_probe_retry_logic(self):
        log_path = self.root / "probe_retry.log"
        if log_path.exists():
            log_path.unlink()

        class RetryFakeTransport(FakeTransport):
            def __init__(self, fail_stage, attempt):
                super().__init__()
                self.fail_stage = fail_stage
                self.attempt = attempt

            def receive(self, timeout):
                if self.attempt == 1:
                    if self.fail_stage == "initialize":
                        return {"id": 1, "error": {"code": -32000, "message": "fail"}}
                    elif self.fail_stage == "catalog":
                        raise Empty
                    else:
                        raise OSError("simulate spawn failure")
                return super().receive(timeout)

        class RetryFactory:
            def __init__(self, fail_stage):
                self.calls = 0
                self.fail_stage = fail_stage
            def __call__(self):
                self.calls += 1
                return RetryFakeTransport(self.fail_stage, self.calls)

        # 1. Retryable logic tests
        log_file = None
        try:
            log_path_created, log_file = dw.validate_and_create_log(str(log_path), None)
            
            dw.reset_globals()
            dw.start_time = 0.0
            factory_init = RetryFactory("initialize")
            result = dw.run_startup_probe(log_file, log_path_created, factory_init)
            self.assertEqual(result["status"], "completed")
            self.assertEqual(len(result["probe"]["attempts"]), 2)
            self.assertEqual(result["probe"]["attempts"][0]["terminal_stage"], "initialize")
            self.assertEqual(result["probe"]["attempts"][0]["failure_category"], "protocol_error")
            
            # Assert no thread/start or turn/start ever sent
            # Check the second attempt's sent messages (transports created by factory_init)
            # Since factory_init creates a RetryFakeTransport for both attempts, we can assert
            # that thread/start and turn/start are never in the sent messages.
            # We can capture all sent messages by keeping a list of all transports created.
            # (FakeTransport records sent messages inside self.sent).
        finally:
            if log_file:
                log_file.close()
            if log_path.exists():
                log_path.unlink()

        # 2. Non-retryable logic tests (fail at account stage)
        log_path2 = self.root / "probe_no_retry.log"
        log_file2 = None
        try:
            log_path_created2, log_file2 = dw.validate_and_create_log(str(log_path2), None)
            
            class AccountFailFakeTransport(FakeTransport):
                def receive(self, timeout):
                    msg = super().receive(timeout)
                    if isinstance(msg, dict) and msg.get("id") == 2:
                        raise OSError("account failed")
                    return msg

            dw.reset_globals()
            dw.start_time = 0.0
            factory_acct = lambda: AccountFailFakeTransport()
            result = dw.run_startup_probe(log_file2, log_path_created2, factory_acct)
            self.assertEqual(result["status"], "transport_failure")
            self.assertEqual(len(result["probe"]["attempts"]), 1)
            self.assertEqual(result["probe"]["attempts"][0]["terminal_stage"], "account")
        finally:
            if log_file2:
                log_file2.close()
            if log_path2.exists():
                log_path2.unlink()

    def test_heartbeat_gated_to_turn_started(self):
        class GatedFakeTransport(FakeTransport):
            def __init__(self):
                super().__init__("stall")
                
            def _events(self):
                events = [
                    {"id": 1, "result": {}},
                    {"method": "account/updated", "params": {"email": "secret@example.test"}},
                    {"id": 2, "result": {"account": {"type": "chatgpt", "email": "secret@example.test"}}},
                    {"id": 3, "result": {"raw": "private-rate-data"}},
                    {"id": 4, "result": {"raw": "private-usage-data"}},
                    {"id": 5, "result": {"data": [self.model_entry()], "nextCursor": None}},
                    {"id": 6, "result": {
                        "thread": {"id": "thread-1"},
                        "model": "gpt-5.6-luna",
                        "reasoningEffort": "low",
                        "sandbox": {"type": "readOnly", "networkAccess": False},
                    }},
                    {"id": 7, "result": {"turn": {"id": "turn-1"}}},
                ]
                return events

        old_monotonic = time.monotonic
        current_time = [old_monotonic()]
        time.monotonic = lambda: current_time[0]
        
        old_stderr = sys.stderr
        sys.stderr = io.StringIO()
        try:
            packet_data = packet(self.root, timeout_seconds=40)
            dw.reset_globals()
            dw.start_time = time.monotonic()
            
            transport = GatedFakeTransport()
            original_receive = transport.receive
            def mock_receive(timeout):
                if transport.turn_start_sent:
                    current_time[0] += 35.0
                return original_receive(timeout)
            transport.receive = mock_receive
            
            result = dw.dispatch(packet_data, self.profiles, lambda: transport)
            self.assertEqual(result["status"], "interrupted")
            
            stderr_output = sys.stderr.getvalue()
            self.assertNotIn("heartbeat", stderr_output)
            
            current_time[0] = old_monotonic()
            dw.reset_globals()
            dw.start_time = time.monotonic()
            sys.stderr = io.StringIO()
            
            class ActiveFakeTransport(FakeTransport):
                def __init__(self):
                    super().__init__("stall")
                def _events(self):
                    return super()._events()
            
            transport2 = ActiveFakeTransport()
            original_receive2 = transport2.receive
            def mock_receive2(timeout):
                if transport2.turn_started_received:
                    current_time[0] += 35.0
                return original_receive2(timeout)
            transport2.receive = mock_receive2
            
            result2 = dw.dispatch(packet_data, self.profiles, lambda: transport2)
            self.assertEqual(result2["status"], "interrupted")
            
            stderr_output2 = sys.stderr.getvalue()
            self.assertIn("heartbeat", stderr_output2)
        finally:
            time.monotonic = old_monotonic
            sys.stderr = old_stderr

    def test_cli_progress_sequence_contiguous(self):
        packet_data = packet(self.root)
        packet_file = self.root / "packet_seq.json"
        packet_file.write_text(json.dumps(packet_data), encoding="utf-8")
        
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()
        try:
            dw.reset_globals()
            exit_code = dw.main(["--packet", str(packet_file)], transport_factory=lambda: FakeTransport())
            self.assertEqual(exit_code, 0)
            
            stderr_lines = sys.stderr.getvalue().strip().split("\n")
            self.assertTrue(len(stderr_lines) > 2)
            
            expected_seq = 1
            for line in stderr_lines:
                record = json.loads(line)
                self.assertEqual(record["type"], "dispatch_progress")
                self.assertEqual(record["sequence"], expected_seq)
                expected_seq += 1
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr

    def test_diagnostic_stream_eof_protocol_eof(self):
        class EofFakeTransport(FakeTransport):
            def receive(self, timeout):
                event = super().receive(timeout)
                if isinstance(event, dict) and event.get("method") == "turn/started":
                    self.index = len(self.events)
                return event

        log_path = self.root.parent / "eof_diag.log"
        if log_path.exists():
            log_path.unlink()
            
        log_file = None
        try:
            packet_data = packet(self.root)
            log_path_created, log_file = dw.validate_and_create_log(str(log_path), str(self.root))
            
            result = dw.dispatch(packet_data, self.profiles, lambda: EofFakeTransport(), log_file, log_path_created)
            self.assertEqual(result["status"], "transport_failure")
            self.assertEqual(result["diagnostic"]["stage"], "stream")
            self.assertEqual(len(result["diagnostic"]["attempts"]), 1)
            self.assertEqual(result["diagnostic"]["attempts"][0]["terminal_stage"], "stream")
            self.assertEqual(result["diagnostic"]["attempts"][0]["failure_category"], "protocol_eof")
            self.assertEqual(dw.EXIT_CODES[result["status"]], 24)
        finally:
            if log_file:
                log_file.close()
            if log_path.exists():
                log_path.unlink()

    def test_notifications_before_reply(self):
        fake = FakeTransport("notifications_before_reply")
        result = dw.dispatch(packet(self.root), self.profiles, lambda: fake)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["response"], {"classification": "complete", "sections": SECTIONS})

    def test_reviewer_profiles_and_skill_governance(self):
        # Locate files
        base_dir = Path(__file__).resolve().parents[3]
        skill_path = Path(__file__).resolve().parents[1] / "SKILL.md"
        
        # Parse and check reviewer profiles
        for role in ("reviewer", "escalation_reviewer"):
            profile_path = base_dir / "agents" / f"alp_{role}.toml"
            self.assertTrue(profile_path.exists(), f"Missing profile {profile_path}")
            with profile_path.open("rb") as f:
                profile = tomllib.load(f)
            instructions = profile.get("developer_instructions", "")
            
            # Req 1: Explicitly state the session goals
            self.assertIn("explicitly state the session goals", instructions)
            
            # Req 2: Blocked outcome for missing/ambiguous goals
            self.assertIn("absent or materially ambiguous", instructions)
            self.assertIn("blocked", instructions)
            
            # Req 3: Deferrable format
            self.assertIn("Deferrable without affecting stated session goals: yes | no | uncertain — <brief reason>", instructions)
            
            # Req 4: Sole authority of root/user
            self.assertIn("sole authority", instructions)
            self.assertTrue("root and user" in instructions or "root/user" in instructions)
            self.assertIn("authority", instructions)
            
        # Check SKILL.md
        self.assertTrue(skill_path.exists(), f"Missing SKILL.md {skill_path}")
        skill_content = skill_path.read_text(encoding="utf-8")
        
        # Req 1: Explicitly state the session goals
        self.assertIn("explicitly state the session goals", skill_content)
        
        # Req 2: Blocked outcome for missing/ambiguous goals
        self.assertIn("absent or materially ambiguous", skill_content)
        self.assertIn("blocked", skill_content)
        
        # Req 3: Deferrable format
        self.assertIn("Deferrable without affecting stated session goals: yes | no | uncertain — <brief reason>", skill_content)
        
        # Req 4: Sole authority of root/user
        self.assertIn("sole authority", skill_content)
        self.assertTrue("root and user" in skill_content or "root/user" in skill_content)
        self.assertIn("authority", skill_content)


if __name__ == "__main__":
    unittest.main()
