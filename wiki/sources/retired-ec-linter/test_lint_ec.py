#!/usr/bin/env python3
"""Deterministic acceptance tests for lint_ec.py."""
from __future__ import annotations

import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent
LINTER = ROOT / "lint_ec.py"

CANONICAL = """Contract: EC-1
Revision: 1
EC protocol: v1
Task: Implement the deterministic città contract
Governing document: ALP EC Linter.md

D1 Decision: use a local command
I1 Invariant: preserve stable output
I2 Test semantics: owner is the root; existing tests are authorized; a behavior-changing correction requires a replacement EC revision before implementation continues
A1 Acceptance: the command checks EC-v1 structure
V1 Validation [covers A1]: run the standard-library suite
O1 Out of scope: network calls and model dispatch
O2 File boundary: scripts/lint_ec.py and scripts/test_lint_ec.py; Report any additional file before editing
    Before Phase 3 approval; read-only planning is allowed; edits and writes are forbidden; implementation validation is forbidden.
"""


class LintTests(unittest.TestCase):
    def run_lint(self, content: str, *options: str, stdin: bool = False,
                 path_spelling: str | None = None) -> subprocess.CompletedProcess[str]:
        if stdin:
            command = [sys.executable, str(LINTER), *options, "-"]
            return subprocess.run(command, input=content, text=True,
                                  capture_output=True, check=False)
        handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="",
                                             delete=False)
        try:
            handle.write(content)
            handle.close()
            self.addCleanup(lambda: os.path.exists(handle.name) and os.unlink(handle.name))
            path = path_spelling or handle.name
            if path_spelling:
                Path(path_spelling).write_text(content, encoding="utf-8", newline="")
                self.addCleanup(lambda: os.path.exists(path_spelling) and os.unlink(path_spelling))
            return subprocess.run([sys.executable, str(LINTER), *options, path],
                                  text=True, capture_output=True, check=False)
        finally:
            if not handle.closed:
                handle.close()

    def assert_codes(self, content: str, *codes: str) -> subprocess.CompletedProcess[str]:
        result = self.run_lint(content)
        self.assertEqual(result.returncode, 1, result.stderr + result.stdout)
        for code in codes:
            self.assertIn(code, result.stdout)
        return result

    def test_canonical_text_and_json_are_stable(self):
        text_result = self.run_lint(CANONICAL)
        self.assertEqual((text_result.returncode, text_result.stdout, text_result.stderr),
                         (0, "", ""))
        first = self.run_lint(CANONICAL, "--json")
        second = self.run_lint(CANONICAL, "--json")
        self.assertEqual(first.stdout, second.stdout)
        payload = json.loads(first.stdout)
        self.assertEqual(payload, {
            "schema_version": 1,
            "protocol": "v1",
            "contract": "EC-1",
            "revision": 1,
            "result": "pass",
            "passed_checks": ["input", "headers", "items", "references",
                              "coverage", "questions", "scope", "vague_terms",
                              "test_semantics", "authorization"],
            "findings": [],
            "ids_inspected": ["D1", "I1", "I2", "A1", "V1", "O1", "O2"],
        })
        self.assertNotRegex(first.stdout, r"\d{4}-\d{2}-\d{2}|/tmp/")

    def test_raw_stdin_bom_crlf_and_non_ascii(self):
        content = "\ufeff" + CANONICAL.replace("\n", "\r\n")
        result = self.run_lint(content, stdin=True)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)

    def test_fenced_markdown_preserves_source_line(self):
        content = "intro\n\n```text\n" + CANONICAL.replace(
            "Revision: 1", "Revision: zero") + "```\nfooter\n"
        result = self.assert_codes(content, "EC101")
        self.assertIn(":5:1 EC101", result.stdout)

    def test_input_selection_zero_multiple_and_raw_plus_fence(self):
        for content in ("prose only\n", "```text\nnot an EC\n```\n",
                        f"```text\n{CANONICAL}```\n```text\n{CANONICAL}```\n",
                        CANONICAL + "```text\n" + CANONICAL + "```\n"):
            with self.subTest(prefix=content[:20]):
                result = self.assert_codes(content, "EC001")
                self.assertEqual(result.stdout.count("EC001"), 1)

    def test_legacy_header_passes_but_both_conflict(self):
        legacy = CANONICAL.replace("Governing document", "ALP chapter")
        self.assertEqual(self.run_lint(legacy).returncode, 0)
        both = CANONICAL.replace("Governing document: ALP EC Linter.md",
                                 "Governing document: ALP EC Linter.md\nALP chapter: old.md")
        self.assert_codes(both, "EC103")

    def test_headers_missing_duplicate_misplaced_and_placeholder(self):
        cases = {
            "missing": CANONICAL.replace("Task: Implement the deterministic città contract\n", ""),
            "duplicate": CANONICAL.replace("Task:", "Task: first\nTask:", 1),
            "misplaced": CANONICAL + "Task: late\n",
            "placeholder": CANONICAL.replace("Task: Implement the deterministic città contract", "Task: TODO"),
            "wrong_case": CANONICAL.replace("Task:", "task:", 1),
        }
        for name, content in cases.items():
            with self.subTest(name=name):
                self.assert_codes(content, "EC100")

    def test_revision_protocol_and_governing_placeholder(self):
        self.assert_codes(CANONICAL.replace("Revision: 1", "Revision: 0"), "EC101")
        self.assert_codes(CANONICAL.replace("EC protocol: v1", "EC protocol: v2"), "EC102")
        self.assert_codes(CANONICAL.replace("Governing document: ALP EC Linter.md",
                                            "Governing document: <path>"), "EC100")

    def test_every_allowed_label_and_complete_question_pass(self):
        extra = CANONICAL.replace(
            "A1 Acceptance:",
            "D2 Decision: keep compatibility\nI3 Invariant: retain evidence\n"
            "A2 Acceptance: the second behavior is visible\nA1 Acceptance:",
        ).replace(
            "V1 Validation [covers A1]:",
            "V1 Validation [covers A1, A2]:",
        ).replace(
            "O1 Out of scope:",
            "Q1 Question: Which source settles compatibility?\n"
            "    Owner: root orchestrator\n"
            "    Evidence required: approved convention\n"
            "    Resolve before: implementation approval\n"
            "O1 Out of scope:",
        )
        self.assertEqual(self.run_lint(extra).returncode, 0)

    def test_item_syntax_continuation_duplicate_and_undefined_reference(self):
        invalid_cases = {
            "prefix": CANONICAL.replace("D1 Decision", "X1 Decision"),
            "zero": CANONICAL.replace("D1 Decision", "D0 Decision"),
            "label": CANONICAL.replace("D1 Decision", "D1 Choice"),
            "top_level": CANONICAL.replace("D1 Decision", "unrecognized\nD1 Decision"),
            "orphan": CANONICAL.replace("\nD1 Decision", "\n    orphan\nD1 Decision"),
            "duplicate": CANONICAL.replace("I1 Invariant", "D1 Decision: duplicate\nI1 Invariant"),
            "undefined": CANONICAL.replace("use a local command", "use D9 with a local command"),
        }
        expected = {"duplicate": "EC201", "undefined": "EC202"}
        for name, content in invalid_cases.items():
            with self.subTest(name=name):
                self.assert_codes(content, expected.get(name, "EC200"))
        self.assertEqual(self.run_lint(CANONICAL.replace(
            "use a local command", "use SHA1 and ROAD1 with a local command")).returncode, 0)

    def test_coverage_graph_shapes(self):
        many_to_one = CANONICAL.replace(
            "A1 Acceptance:", "A2 Acceptance: another result\nA1 Acceptance:").replace(
            "covers A1", "covers A1, A2")
        self.assertEqual(self.run_lint(many_to_one).returncode, 0)
        one_to_many = CANONICAL.replace(
            "V1 Validation [covers A1]: run the standard-library suite",
            "V1 Validation [covers A1]: run the standard-library suite\n"
            "V2 Validation [covers A1]: inspect the stable JSON")
        self.assertEqual(self.run_lint(one_to_many).returncode, 0)
        cases = {
            "brackets": CANONICAL.replace("Validation [covers A1]", "Validation covers A1"),
            "duplicate": CANONICAL.replace("covers A1", "covers A1, A1"),
            "wrong_type": CANONICAL.replace("covers A1", "covers D1"),
            "unknown": CANONICAL.replace("covers A1", "covers A9"),
            "uncovered": CANONICAL.replace("V1 Validation [covers A1]: run the standard-library suite\n", ""),
        }
        expected = {"brackets": "EC210", "duplicate": "EC210",
                    "wrong_type": "EC210", "unknown": "EC211", "uncovered": "EC212"}
        for name, content in cases.items():
            with self.subTest(name=name):
                self.assert_codes(content, expected[name])

    def test_question_metadata_matrix_and_synthetic_none(self):
        complete = "Q1 Question: Which source is authoritative?\n" \
                   "    Owner: root\n" \
                   "    Evidence required: approved source\n" \
                   "    Resolve before: Phase 3 approval\n"
        base = CANONICAL.replace("O1 Out of scope", complete + "O1 Out of scope")
        self.assertEqual(self.run_lint(base).returncode, 0)
        cases = (
            base.replace("    Owner: root\n", ""),
            base.replace("    Owner: root", "    Owner: root\n    Owner: user"),
            base.replace("    Evidence required: approved source", "    Evidence required:"),
            base.replace("    Resolve before: Phase 3 approval", "    Resolve before: TODO"),
            CANONICAL.replace("O1 Out of scope", "Q1 Question: none\nO1 Out of scope"),
        )
        for content in cases:
            with self.subTest(fragment=content[content.find("Q1"):content.find("Q1") + 50]):
                self.assert_codes(content, "EC220")

    def test_scope_boundaries_matrix(self):
        self.assert_codes(CANONICAL.replace(
            "O1 Out of scope: network calls and model dispatch\n", ""), "EC230")
        self.assert_codes(CANONICAL.replace(
            "O2 File boundary: scripts/lint_ec.py and scripts/test_lint_ec.py; Report any additional file before editing\n", ""), "EC230")
        self.assert_codes(CANONICAL.replace(
            "Report any additional file before editing", "additional files may be edited"), "EC230")
        self.assert_codes(CANONICAL.replace(
            "O1 Out of scope: network calls and model dispatch", "O1 Out of scope: none"), "EC200")

    def test_vague_terms_and_definitions(self):
        for phrase in ("agreed", "APPROPRIATE", "as needed", "When Needed"):
            with self.subTest(phrase=phrase):
                self.assert_codes(CANONICAL.replace("use a local command", f"use it {phrase}"),
                                  "EC240")
        self.assertEqual(self.run_lint(CANONICAL.replace(
            "use a local command", "use an appropriately named command")).returncode, 0)
        defined = CANONICAL.replace(
            "use a local command",
            "use the appropriate command\n    Definition: appropriate = satisfies A1 using V1")
        self.assertEqual(self.run_lint(defined).returncode, 0)
        self.assert_codes(defined.replace(" = satisfies A1 using V1", ": value"), "EC240")
        self.assert_codes(defined.replace("satisfies A1 using V1", "appropriate for the task"), "EC240")

    def test_test_semantics_complete_and_each_missing_concept(self):
        for old, new in (("owner", "custodian"),
                         ("existing tests are authorized", "test changes are discussed"),
                         ("replacement EC revision", "new EC approval")):
            with self.subTest(missing=old):
                self.assert_codes(CANONICAL.replace(old, new), "EC250")
        duplicate = CANONICAL.replace(
            "A1 Acceptance:",
            "I3 Test semantics: owner is root; existing tests are forbidden; replacement revision is required\n"
            "A1 Acceptance:")
        self.assert_codes(duplicate, "EC250")

    def test_test_semantics_exemptions_and_signals(self):
        without_item = CANONICAL.replace(
            "I2 Test semantics: owner is the root; existing tests are authorized; a behavior-changing correction requires a replacement EC revision before implementation continues\n", "")
        no_mention = without_item.replace("scripts/test_lint_ec.py", "scripts/lint_oracle.py")
        self.assertEqual(self.run_lint(no_mention).returncode, 0)
        validation_only = no_mention.replace("run the standard-library suite",
                                             "run python -m unittest tests")
        self.assertEqual(self.run_lint(validation_only).returncode, 0)
        doc_filename = no_mention.replace("use a local command", "follow testing-guide.md")
        self.assertEqual(self.run_lint(doc_filename).returncode, 0)
        explicit_item = CANONICAL.replace(
            "I2 Test semantics: owner is the root; existing tests are authorized; a behavior-changing correction requires a replacement EC revision before implementation continues",
            "I2 Test semantics: No executable product test applies")
        self.assertEqual(self.run_lint(explicit_item).returncode, 0)
        out_scope = no_mention.replace("network calls and model dispatch",
                                       "network calls; Tests are not in scope")
        self.assertEqual(self.run_lint(out_scope).returncode, 0)
        for signal in ("fixtures are added", "assertions may change", "snapshots are updated",
                       "tests may be needed"):
            with self.subTest(signal=signal):
                self.assert_codes(no_mention.replace("use a local command", signal), "EC250")

    def test_authorization_phrase_groups_and_each_missing_concept(self):
        variant = CANONICAL.replace(
            "Before Phase 3 approval; read-only planning is allowed; edits and writes are forbidden; implementation validation is forbidden.",
            "Before implementation approval; read-only inspection is permitted; write actions must not occur; implementation-validation is not permitted.")
        self.assertEqual(self.run_lint(variant).returncode, 0)
        boundary = "Before Phase 3 approval; read-only planning is allowed; edits and writes are forbidden; implementation validation is forbidden."
        replacements = (
            "After approval; read-only planning is allowed; edits and writes are forbidden; implementation validation is forbidden.",
            "Before Phase 3 approval; planning occurs; edits and writes are forbidden; implementation validation is forbidden.",
            "Before Phase 3 approval; read-only planning is allowed; implementation validation is forbidden.",
            "Before Phase 3 approval; read-only planning is allowed; edits and writes are forbidden.",
        )
        for replacement in replacements:
            with self.subTest(replacement=replacement):
                self.assert_codes(CANONICAL.replace(boundary, replacement), "EC260")
        contradiction = CANONICAL.replace(
            "edits and writes are forbidden",
            "edits are allowed; writes are forbidden")
        self.assert_codes(contradiction, "EC260")

    def test_findings_sort_and_passed_checks(self):
        bad = CANONICAL.replace("Revision: 1", "Revision: zero").replace(
            "use a local command", "use D9 as needed")
        first = self.run_lint(bad, "--json")
        second = self.run_lint(bad, "--json")
        self.assertEqual(first.stdout, second.stdout)
        payload = json.loads(first.stdout)
        self.assertEqual(payload["result"], "findings")
        ordering = [(item["line"], item["column"], item["code"])
                    for item in payload["findings"]]
        self.assertEqual(ordering, sorted(ordering))
        self.assertNotIn("headers", payload["passed_checks"])
        self.assertNotIn("references", payload["passed_checks"])
        self.assertNotIn("vague_terms", payload["passed_checks"])

    def test_caller_spelled_path_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "./contract.ec"
            path.write_text(CANONICAL.replace("Revision: 1", "Revision: zero"),
                            encoding="utf-8")
            spelling = str(Path(directory)) + "/./contract.ec"
            result = subprocess.run([sys.executable, str(LINTER), spelling], text=True,
                                    capture_output=True, check=False)
            self.assertTrue(result.stdout.startswith(spelling + ":2:1 EC101"), result.stdout)

    def test_operational_failures_are_concise_exit_two(self):
        missing = self.run_lint(CANONICAL)
        self.assertEqual(missing.returncode, 0)
        result = subprocess.run([sys.executable, str(LINTER), "/definitely/not/here.ec"],
                                text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertRegex(result.stderr, r"^EC900 input failure: \w+\n$")
        with tempfile.NamedTemporaryFile(delete=False) as handle:
            handle.write(b"\xff")
            name = handle.name
        self.addCleanup(lambda: os.path.exists(name) and os.unlink(name))
        result = subprocess.run([sys.executable, str(LINTER), name], text=True,
                                capture_output=True, check=False)
        self.assertEqual(result.returncode, 2)
        self.assertRegex(result.stderr, r"^EC900 input failure: \w+\n$")

    def test_internal_failure_is_concise_exit_two(self):
        spec = importlib.util.spec_from_file_location("lint_ec_under_test", LINTER)
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        sys.modules[spec.name] = module
        self.addCleanup(lambda: sys.modules.pop(spec.name, None))
        spec.loader.exec_module(module)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8") as handle:
            handle.write(CANONICAL)
            handle.flush()
            stderr = io.StringIO()
            with mock.patch.object(module, "lint", side_effect=RuntimeError("secret")):
                with redirect_stderr(stderr):
                    status = module.main([handle.name])
        self.assertEqual(status, 2)
        self.assertEqual(stderr.getvalue(), "EC900 internal linter failure\n")


if __name__ == "__main__":
    unittest.main()
