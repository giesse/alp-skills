#!/usr/bin/env python3
"""Lint the deterministic surface of an ALP Execution Contract (EC-v1)."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

CHECKS = (
    "input", "headers", "items", "references", "coverage", "questions",
    "scope", "vague_terms", "test_semantics", "authorization",
)
HEADER_NAMES = (
    "Contract", "Revision", "EC protocol", "Task", "Governing document",
    "ALP chapter",
)
ALLOWED_LABELS = {
    "D": {"Decision"},
    "I": {"Invariant", "Test semantics"},
    "A": {"Acceptance"},
    "V": {"Validation"},
    "O": {"Out of scope", "File boundary"},
    "Q": {"Question"},
}
PLACEHOLDER_RE = re.compile(r"(?:<[^>]*>|TBD|TODO|N/A|none)[.!?]?", re.I)
REFERENCE_RE = re.compile(r"(?<![A-Za-z0-9_])([DIAVOQ][0-9]+)(?![A-Za-z0-9_])")
ITEM_RE = re.compile(r"^([A-Za-z]+)([0-9]+)\s+([^:]+):\s*(.*)$")
VAGUE_PHRASES = ("agreed", "appropriate", "as needed", "when needed")


@dataclass(frozen=True)
class Finding:
    code: str
    line: int
    column: int
    message: str
    check: str


@dataclass
class Item:
    ident: str
    prefix: str
    label: str
    text: str
    line: int
    column: int
    coverage: str | None = None
    continuations: list[tuple[int, int, str]] = field(default_factory=list)

    @property
    def all_text(self) -> str:
        return "\n".join((self.text, *(entry[2] for entry in self.continuations)))


def add(findings: list[Finding], code: str, line: int, column: int,
        message: str, check: str) -> None:
    findings.append(Finding(code, line, column, message, check))


def is_placeholder(value: str) -> bool:
    value = value.strip()
    return not value or PLACEHOLDER_RE.fullmatch(value) is not None


def normalize(text: str) -> list[str]:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if text.startswith("\ufeff"):
        text = text[1:]
    return text.splitlines()


def matching_fenced_blocks(lines: list[str]) -> list[tuple[int, list[str]]]:
    blocks: list[tuple[int, list[str]]] = []
    fence: tuple[str, int, list[str]] | None = None
    for index, line in enumerate(lines):
        if fence is None:
            match = re.match(r"^\s*(`{3,})([^`]*)$", line)
            if match:
                fence = (match.group(1), index + 2, [])
            continue
        marker, start_line, body = fence
        if re.match(rf"^\s*{re.escape(marker)}\s*$", line):
            material = next((entry.strip() for entry in body if entry.strip()), None)
            if material is not None and material.startswith("Contract:"):
                blocks.append((start_line, body.copy()))
            fence = None
        else:
            body.append(line)
    return blocks


def select_ec(text: str) -> tuple[list[str], list[Finding]]:
    lines = normalize(text)
    first = next((i for i, line in enumerate(lines) if line.strip()), None)
    raw = first is not None and lines[first].strip().startswith("Contract:")
    blocks = matching_fenced_blocks(lines)
    if (raw and blocks) or (not raw and len(blocks) != 1):
        return [], [Finding("EC001", 1, 1,
                            "no unique raw or fenced EC could be selected", "input")]
    if raw:
        return lines, []
    start, body = blocks[0]
    return ([""] * (start - 1)) + body, []


def parse(lines: list[str]) -> tuple[dict[str, list[tuple[int, int, str]]],
                                     list[Item], list[Finding]]:
    headers: dict[str, list[tuple[int, int, str]]] = {}
    items: list[Item] = []
    findings: list[Finding] = []
    current: Item | None = None
    seen_item = False

    for line_no, raw in enumerate(lines, 1):
        stripped = raw.strip()
        if not stripped:
            continue
        column = len(raw) - len(raw.lstrip()) + 1

        header = next((name for name in HEADER_NAMES
                       if stripped.startswith(name + ":")), None)
        if header is not None and not raw[:1].isspace():
            value = stripped[len(header) + 1:].strip()
            if seen_item:
                add(findings, "EC100", line_no, column,
                    "header appears after the first item", "headers")
            else:
                headers.setdefault(header, []).append((line_no, column, value))
            continue

        if raw[:1].isspace():
            if current is None:
                add(findings, "EC200", line_no, column,
                    "continuation has no owning item", "items")
            else:
                current.continuations.append((line_no, column, stripped))
            continue

        match = ITEM_RE.fullmatch(stripped)
        if match is None:
            add(findings, "EC200", line_no, column,
                "unrecognized top-level line", "items")
            current = None
            continue

        prefix, number, raw_label, value = match.groups()
        label = raw_label.strip()
        coverage: str | None = None
        coverage_malformed = False
        if prefix == "V" and label.startswith("Validation"):
            suffix = label[len("Validation"):]
            coverage_match = re.fullmatch(r" \[covers ([^]]+)\]", suffix)
            label = "Validation"
            if coverage_match:
                coverage = coverage_match.group(1)
            else:
                coverage_malformed = True

        ident = prefix + number
        current = Item(ident, prefix, label, value.strip(), line_no, column,
                       coverage)
        items.append(current)
        seen_item = True

        valid_id = prefix in ALLOWED_LABELS and int(number) > 0
        valid_label = valid_id and label in ALLOWED_LABELS[prefix]
        if not valid_id or not valid_label:
            add(findings, "EC200", line_no, column,
                "invalid EC item prefix, number, or label", "items")
        if prefix == "V" and label == "Validation" and coverage_malformed:
            add(findings, "EC210", line_no, column,
                "validation must use exact [covers A...]: syntax", "coverage")
        if is_placeholder(value):
            add(findings, "EC200", line_no, column,
                "EC item has empty or placeholder text", "items")
    return headers, items, findings


def first_position(headers: dict[str, list[tuple[int, int, str]]],
                   name: str) -> tuple[int, int]:
    values = headers.get(name, [])
    return (values[0][0], values[0][1]) if values else (1, 1)


def lint(text: str) -> tuple[int, dict[str, object]]:
    lines, findings = select_ec(text)
    if findings:
        return 1, make_report(None, [], findings)

    headers, items, parse_findings = parse(lines)
    findings.extend(parse_findings)

    for name in ("Contract", "Revision", "EC protocol", "Task"):
        values = headers.get(name, [])
        if len(values) != 1:
            add(findings, "EC100", *first_position(headers, name),
                f"required header {name!r} is missing or duplicated", "headers")
        elif is_placeholder(values[0][2]):
            add(findings, "EC100", values[0][0], values[0][1],
                f"required header {name!r} is empty or placeholder", "headers")

    governing = headers.get("Governing document", [])
    legacy = headers.get("ALP chapter", [])
    if not governing and not legacy:
        add(findings, "EC100", 1, 1,
            "required governing-document header is missing", "headers")
    elif len(governing) + len(legacy) != 1:
        candidates = governing + legacy
        position = (candidates[1][0], candidates[1][1]) if len(candidates) > 1 else (1, 1)
        add(findings, "EC103", *position,
            "governing-document and legacy headers conflict", "headers")
    elif is_placeholder((governing or legacy)[0][2]):
        value = (governing or legacy)[0]
        add(findings, "EC100", value[0], value[1],
            "governing-document header is empty or placeholder", "headers")

    revisions = headers.get("Revision", [])
    if len(revisions) == 1 and re.fullmatch(r"[1-9][0-9]*", revisions[0][2]) is None:
        add(findings, "EC101", revisions[0][0], revisions[0][1],
            "revision must be a positive integer", "headers")
    protocols = headers.get("EC protocol", [])
    if len(protocols) == 1 and protocols[0][2] != "v1":
        add(findings, "EC102", protocols[0][0], protocols[0][1],
            "EC protocol must be exactly v1", "headers")

    declared: dict[str, Item] = {}
    declaration_order: list[str] = []
    for item in items:
        if item.prefix not in ALLOWED_LABELS or not item.ident[len(item.prefix):].isdigit() or int(item.ident[len(item.prefix):]) < 1:
            continue
        if item.ident in declared:
            add(findings, "EC201", item.line, item.column,
                f"duplicate item identifier {item.ident}", "items")
        else:
            declared[item.ident] = item
            declaration_order.append(item.ident)

    for item in items:
        reference_text = item.all_text
        if item.prefix == "V" and item.coverage is not None:
            reference_text = item.text + "\n" + "\n".join(
                entry[2] for entry in item.continuations)
        for match in REFERENCE_RE.finditer(reference_text):
            reference = match.group(1)
            if reference not in declared:
                add(findings, "EC202", item.line, item.column,
                    f"undefined item reference {reference}", "references")

    covered: set[str] = set()
    acceptances = {ident for ident, item in declared.items() if item.prefix == "A"}
    for item in items:
        if item.prefix != "V" or item.label != "Validation":
            continue
        if item.coverage is None:
            continue
        references = [part.strip() for part in item.coverage.split(",")]
        malformed = (not references or any(re.fullmatch(r"A[1-9][0-9]*", ref) is None
                                            for ref in references)
                     or len(references) != len(set(references)))
        if malformed:
            add(findings, "EC210", item.line, item.column,
                "validation coverage is malformed or duplicated", "coverage")
        for reference in dict.fromkeys(references):
            if re.fullmatch(r"A[1-9][0-9]*", reference) is None:
                continue
            if reference not in acceptances:
                add(findings, "EC211", item.line, item.column,
                    f"coverage names undeclared acceptance {reference}", "coverage")
            else:
                covered.add(reference)
    for ident in declaration_order:
        if ident in acceptances and ident not in covered:
            item = declared[ident]
            add(findings, "EC212", item.line, item.column,
                f"acceptance {ident} has no validation coverage", "coverage")

    for item in items:
        if item.prefix != "Q" or item.label != "Question":
            continue
        fields = {name: [] for name in ("Owner", "Evidence required", "Resolve before")}
        for line_no, column, line in item.continuations:
            for name in fields:
                if line.startswith(name + ":"):
                    fields[name].append((line_no, column, line[len(name) + 1:].strip()))
        for name, values in fields.items():
            if len(values) != 1 or is_placeholder(values[0][2]):
                add(findings, "EC220", item.line, item.column,
                    f"question metadata {name!r} is missing, duplicated, or placeholder",
                    "questions")

    out_of_scope = [item for item in items if item.prefix == "O" and item.label == "Out of scope"]
    boundaries = [item for item in items if item.prefix == "O" and item.label == "File boundary"]
    if not out_of_scope:
        add(findings, "EC230", 1, 1,
            "at least one Out of scope item is required", "scope")
    if not boundaries:
        add(findings, "EC230", 1, 1,
            "at least one File boundary item is required", "scope")
    elif not any(re.search(r"report\s+any\s+additional\s+file\s+before\s+editing",
                           item.all_text, re.I) for item in boundaries):
        add(findings, "EC230", boundaries[0].line, boundaries[0].column,
            "file boundary must require reporting additional files before editing",
            "scope")

    definitions: set[str] = set()
    definition_lines: set[tuple[int, int]] = set()
    for item in items:
        for line_no, column, line in item.continuations:
            if not line.lower().startswith("definition:"):
                continue
            definition_lines.add((line_no, column))
            body = line.split(":", 1)[1].strip()
            if "=" not in body:
                add(findings, "EC240", line_no, column,
                    "definition must name a governed phrase and use '='", "vague_terms")
                continue
            phrase, value = (part.strip() for part in body.split("=", 1))
            phrase_lower = phrase.lower()
            still_vague = any(re.search(rf"(?<!\w){re.escape(candidate)}(?!\w)", value, re.I)
                              for candidate in VAGUE_PHRASES)
            if phrase_lower not in VAGUE_PHRASES or is_placeholder(value) or still_vague:
                add(findings, "EC240", line_no, column,
                    "definition is malformed, placeholder, or still vague", "vague_terms")
            else:
                definitions.add(phrase_lower)
    for item in items:
        portions = [(item.line, item.column, item.text)] + list(item.continuations)
        for line_no, column, portion in portions:
            if (line_no, column) in definition_lines:
                continue
            for phrase in VAGUE_PHRASES:
                if phrase not in definitions and re.search(
                        rf"(?<!\w){re.escape(phrase)}(?!\w)", portion, re.I):
                    add(findings, "EC240", line_no, column,
                        f"undefined vague control term {phrase!r}", "vague_terms")

    test_items = [item for item in items
                  if item.prefix == "I" and item.label == "Test semantics"]
    if len(test_items) > 1:
        add(findings, "EC250", test_items[1].line, test_items[1].column,
            "duplicate Test semantics items", "test_semantics")
    explicit_no_test = any(
        re.search(r"\b(?:no executable product test applies|tests are not in scope)\b",
                  item.all_text, re.I)
        for item in test_items + out_of_scope
    )
    test_signal = False
    for item in items:
        if item.label in {"Validation", "Test semantics"}:
            continue
        if item.label == "Out of scope" and re.search(
                r"\b(?:no executable product test applies|tests are not in scope)\b",
                item.all_text, re.I):
            continue
        scrubbed = re.sub(r"\S+\.(?:md|rst|txt)\b", "", item.all_text, flags=re.I)
        if re.search(r"\b(?:executable\s+tests?|tests?|fixtures?|assertions?|snapshots?|test\s+files?)\b",
                     scrubbed, re.I):
            test_signal = True
            break
    if test_signal and len(test_items) != 1:
        add(findings, "EC250", 1, 1,
            "in-scope or ambiguous tests require exactly one Test semantics item",
            "test_semantics")
    if len(test_items) == 1 and (test_signal or not explicit_no_test):
        text_lower = test_items[0].all_text.lower()
        has_owner = re.search(r"\b(?:owner|owned|ownership)\b", text_lower) is not None
        has_disposition = re.search(
            r"\bexisting tests?\b[^\n;.]*(?:authorized|not authorized|forbidden|none)\b|"
            r"\b(?:authorized|not authorized|forbidden|none)\b[^\n;.]*\bexisting tests?\b",
            text_lower,
        ) is not None
        has_revision = (re.search(r"\breplacement\b", text_lower) is not None
                        and re.search(r"\brevision\b", text_lower) is not None)
        if not (has_owner and has_disposition and has_revision):
            add(findings, "EC250", test_items[0].line, test_items[0].column,
                "Test semantics must state owner, existing-test disposition, and replacement revision",
                "test_semantics")

    authorization = [False, False, False, False]
    for item in items:
        low = item.all_text.lower()
        if re.search(r"\bbefore\s+(?:phase\s+3\s+approval|implementation\s+approval)\b", low):
            authorization[0] = True
        if ("read-only" in low
                and re.search(r"\b(?:planning|inspection)\b", low)
                and re.search(r"\b(?:allowed|permitted)\b", low)):
            authorization[1] = True
        if (re.search(r"\b(?:edit|edits|write|writes)\b", low)
                and re.search(r"\b(?:forbidden|not\s+permitted|must\s+not)\b", low)):
            authorization[2] = True
        if (re.search(r"\bimplementation[\s-]+validation\b", low)
                and re.search(r"\b(?:forbidden|not\s+permitted|must\s+not)\b", low)):
            authorization[3] = True
        for clause in re.split(r";", low):
            controlled = re.search(r"\b(?:edit|edits|write|writes)\b|\bimplementation[\s-]+validation\b", clause)
            permitted = re.search(r"\b(?:allowed|permitted|authorized)\b", clause)
            negated = re.search(r"\b(?:forbidden|not\s+permitted|must\s+not|not\s+authorized)\b", clause)
            if controlled and permitted and not negated:
                add(findings, "EC260", item.line, item.column,
                    "authorization boundary contradicts forbidden edit or validation language",
                    "authorization")
    concepts = (
        "pre-approval boundary", "read-only planning or inspection",
        "forbidden edits or writes", "forbidden implementation validation",
    )
    for present, concept in zip(authorization, concepts):
        if not present:
            add(findings, "EC260", 1, 1,
                f"authorization boundary is missing {concept}", "authorization")

    return (1 if findings else 0), make_report(headers, declaration_order, findings)


def make_report(headers: dict[str, list[tuple[int, int, str]]] | None,
                ids: list[str], findings: list[Finding]) -> dict[str, object]:
    findings.sort(key=lambda entry: (entry.line, entry.column, entry.code))
    contract: str | None = None
    protocol: str | None = None
    revision: int | None = None
    if headers:
        if len(headers.get("Contract", [])) == 1:
            contract = headers["Contract"][0][2] or None
        if len(headers.get("EC protocol", [])) == 1:
            protocol = headers["EC protocol"][0][2] or None
        if len(headers.get("Revision", [])) == 1:
            raw_revision = headers["Revision"][0][2]
            if re.fullmatch(r"[1-9][0-9]*", raw_revision):
                revision = int(raw_revision)
    failed_checks = {entry.check for entry in findings}
    return {
        "schema_version": 1,
        "protocol": protocol,
        "contract": contract,
        "revision": revision,
        "result": "pass" if not findings else "findings",
        "passed_checks": [check for check in CHECKS if check not in failed_checks],
        "findings": [
            {
                "code": entry.code,
                "line": entry.line,
                "column": entry.column,
                "message": entry.message,
                "check": entry.check,
            }
            for entry in findings
        ],
        "ids_inspected": ids,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("path")
    args = parser.parse_args(argv)
    try:
        if args.path == "-":
            raw = sys.stdin.buffer.read()
            source = "<stdin>"
        else:
            raw = Path(args.path).read_bytes()
            source = args.path
        status, result = lint(raw.decode("utf-8"))
        if args.json:
            print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
        else:
            for entry in result["findings"]:
                print(f"{source}:{entry['line']}:{entry['column']} "
                      f"{entry['code']} {entry['message']}")
        return status
    except (OSError, UnicodeError) as exc:
        print(f"EC900 input failure: {exc.__class__.__name__}", file=sys.stderr)
        return 2
    except Exception:
        print("EC900 internal linter failure", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
