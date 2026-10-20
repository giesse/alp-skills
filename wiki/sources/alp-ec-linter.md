# ALP EC Linter

Status: Retired EC-v1 design and source evidence; not current policy or an active linter.

Design source: `OldCodexALPDocuments/ALP EC Linter.md` (reviewed; its substantive
body is preserved here, but the original document is not retained locally).

The exact retired source files are retained as references: [`lint_ec.py`](retired-ec-linter/lint_ec.py) and [`test_lint_ec.py`](retired-ec-linter/test_lint_ec.py). They were copied byte-for-byte from `old/codex/skills/alp-workflow/scripts/`; they were not executed during cleanup.

## Purpose and Boundary

An Execution Contract (EC) is the phase boundary between approved governing documentation and implementation. Its mechanical structure must be checked before a model judges whether the contract is semantically sufficient. This chapter defines a deterministic, local EC protocol-v1 linter so malformed contracts do not consume worker credits or enter implementation.

The linter governs `alp-workflow/scripts/lint_ec.py` and `alp-workflow/scripts/test_lint_ec.py`. It also governs the corresponding invocation and syntax notes in `alp-workflow/references/handoff-contract.md`. Phase authority, semantic preflight, implementation approval, and independent review remain in ALP Workflow Redesign. Packaging and retirement of the former model-backed linter remain in ALP Workflow Repository Migration.

The linter is intentionally not:

- a model worker or dispatcher capability role;
- a judge of design quality, oracle strength, materiality, or production safety;
- a repository scanner or source-code validator;
- an EC generator, formatter, or repair tool;
- an implementation-approval mechanism; or
- a networked service.

A lint pass means only that the supplied EC satisfies the deterministic EC-v1 surface. The root orchestrator still performs semantic preflight and retains the phase gate.

## Command Contract

The Python 3.11-or-newer, standard-library-only command is:

```text
lint_ec.py [--json] PATH
lint_ec.py [--json] -
```

`-` reads UTF-8 from standard input. A file path reads exactly that caller-selected file. The linter does not discover repository files, follow references, write changes, use the network, or invoke a model.

Default output is one diagnostic per line:

```text
source:line:column CODE message
```

With `--json`, standard output is one JSON object:

```json
{
  "schema_version": 1,
  "protocol": "v1",
  "contract": "EC-1",
  "revision": 1,
  "result": "pass",
  "passed_checks": ["input", "headers", "items", "references", "coverage", "questions", "scope", "vague_terms", "test_semantics", "authorization"],
  "findings": [],
  "ids_inspected": ["D1", "I1", "A1", "V1", "O1", "O2"]
}
```

`contract`, `revision`, and `protocol` are `null` when they cannot be parsed. Every finding contains `code`, `line`, `column`, `message`, and a short `check` name. Findings are errors in EC-v1; no warning tier is needed initially. JSON keys and diagnostic wording are stable public output within schema version 1.

Default text output is empty on a pass. A failing lint prints only its sorted diagnostic lines to standard output.

Exit status is:

- `0` — the contract parsed and has no findings;
- `1` — the input was readable and one or more lint findings exist; or
- `2` — invocation, file decoding, or an internal linter failure prevented a trustworthy lint result.

An EC syntax problem is exit `1`, including a missing or ambiguous contract block. Exit `2` is reserved for failures outside the contract's content. Both output modes send unexpected operational details to standard error without echoing the full contract.

## Accepted Input Forms

The linter accepts either:

1. a raw EC whose first material field is `Contract:`; or
2. a Markdown document containing exactly one fenced code block whose material content starts with `Contract:`.

For Markdown input, prose outside the selected block is ignored. Zero matching blocks or more than one matching block is an input finding; the linter never guesses which contract is authoritative. A raw document and a matching fenced block in the same input are likewise ambiguous.

Normalize CRLF and CR line endings for parsing while preserving original one-based source line and column positions. Accept a UTF-8 byte-order mark only at the beginning of the input. Non-ASCII task and document text is valid. Tabs are not expanded when reporting columns.

Blank lines may separate headers and items. A nonblank indented or otherwise non-item line after an item is its continuation. A material line before the first header, an unrecognized top-level line, or a continuation without an owning item is a finding rather than silently ignored text.

## EC-v1 Structure

### Required headers

Each header appears exactly once, has non-placeholder content, and precedes the first item:

```text
Contract: EC-1
Revision: 1
EC protocol: v1
Task: Implement the approved boundary
Governing document: path/to/book.md and heading
```

`ALP chapter:` is accepted as the legacy spelling of `Governing document:`. Exactly one of those two spellings must appear. `Revision` is a positive decimal integer. `EC protocol` is exactly `v1`. Contract and task values are otherwise human-readable nonempty text; the linter does not invent a stricter identifier convention.

Headers are case-sensitive. This keeps contracts stable across tools and avoids silently accepting misspelled protocol fields.

### Items and identifiers

Every top-level item starts with a unique identifier followed by its governed label and nonempty text:

| Identifier | Allowed label                     | Purpose                                                                               |
| ---------- | --------------------------------- | ------------------------------------------------------------------------------------- |
| `D<n>`     | `Decision`                        | Approved material choice                                                              |
| `I<n>`     | `Invariant` or `Test semantics`   | Behavior that implementation must preserve, including test ownership where applicable |
| `A<n>`     | `Acceptance`                      | Observable completion criterion                                                       |
| `V<n>`     | `Validation [covers A…]`          | Exact validation evidence and its acceptance coverage                                 |
| `O<n>`     | `Out of scope` or `File boundary` | Explicit exclusions and allowed files                                                 |
| `Q<n>`     | `Question`                        | Unresolved item that blocks at its declared boundary                                  |

`<n>` is a positive decimal integer. Identifiers need not be contiguous or ordered by type, but no identifier may be declared twice. An unknown prefix, invalid number, misspelled label, or label incompatible with its prefix is a finding.

References to EC item identifiers in item text must resolve to declared identifiers. Coverage references in a validation item are parsed separately but obey the same existence rule. Text that happens to contain a longer word such as `SHA1` is not an item reference; references are recognized only as standalone EC identifiers.

### Acceptance coverage

A validation declaration uses this exact shape:

```text
V1 Validation [covers A1, A2]: Run the deterministic command and inspect its exit status.
```

The bracket contains one or more comma-separated acceptance identifiers. Every referenced identifier must be a declared `A` item, duplicates within one coverage list are findings, and every declared acceptance item must be covered by at least one validation item. One validation may cover several acceptance items and one acceptance item may have several validations.

The linter checks the coverage graph, not whether the command is a strong oracle. A vague or circular validation can therefore lint successfully yet fail semantic preflight.

### Questions

When unresolved questions exist, each `Q` item contains exactly one nonempty continuation field for each label:

```text
Q1 Question: Which compatibility form is authoritative?
    Owner: root orchestrator
    Evidence required: approved repository convention
    Resolve before: Phase 3 approval
```

The required labels are `Owner:`, `Evidence required:`, and `Resolve before:`. Duplicate, missing, empty, or placeholder metadata is a finding. When no question exists, omit `Q` items entirely; a synthetic `Q: none` item is invalid.

### Scope boundaries

Every EC contains at least one `O… Out of scope` item and at least one `O… File boundary` item. The file boundary names the files or bounded path groups implementation may edit and contains the case-insensitive phrase `Report any additional file before editing`. Missing that obligation is `EC230`. Semantic preflight decides whether the named boundary is safe and sufficient.

### Placeholders and vague control terms

Required material is placeholder content when its trimmed value is empty, is only an angle-bracket template, or is exactly `TBD`, `TODO`, `N/A`, or `none` ignoring case and terminal punctuation. Ordinary prose containing those words is not automatically rejected.

The control phrases `agreed`, `appropriate`, `as needed`, and `when needed` are findings when used as standalone phrases because they otherwise defer authority to the implementer. A contract can define a necessary domain term with a continuation line:

```text
    Definition: appropriate = satisfies A2 using V2
```

The definition must name one governed phrase exactly and provide non-placeholder text after `=`. A valid definition suppresses the vague-term finding for that phrase throughout the same contract; semantic preflight still judges whether the definition is useful.

## Test-Semantics Check

When the contract places executable tests, fixtures, assertions, snapshots, or test files in scope, it must contain exactly one `I… Test semantics` item. That item and its continuations must state:

- who owns the affected test behavior;
- whether updates to existing tests are authorized, forbidden, or unnecessary; and
- that a behavior-changing correction requires a replacement EC revision before implementation continues.

The deterministic check recognizes explicit ownership language (`owner`, `owned`, or `ownership`), an `existing test` or `existing tests` disposition paired with `authorized`, `not authorized`, `forbidden`, or `none`, and both `replacement` and `revision`. The words may occur across the same Test-semantics item's continuation lines.

If no executable product test applies, the EC may say `No executable product test applies` or `Tests are not in scope` in one `I… Test semantics` item, or may place tests explicitly in an `O… Out of scope` item. Either explicit no-test form is exempt from the three in-scope details. When the contract contains no in-scope test signal and no Test-semantics item, the mechanical check passes and semantic preflight owns whether an unstated test obligation was missed.

Mentions confined to validation commands, documentation filenames, the explicit no-test form, or prose saying tests are out of scope do not by themselves place tests in scope. Ambiguous test language should produce an `EC250` finding so the author makes the disposition explicit.

## Authorization-Boundary Check

Every EC states the pre-approval boundary in governed item text. The combined contract must explicitly convey all of these concepts:

- before Phase 3 or implementation approval;
- read-only planning or inspection is allowed;
- edits or writes are forbidden; and
- implementation validation is forbidden.

The deterministic phrase groups are:

- `before Phase 3 approval` or `before implementation approval`;
- `read-only`, either `planning` or `inspection`, and either `allowed` or `permitted` in the same item;
- either `edit`, `edits`, `write`, or `writes` and either `forbidden`, `not permitted`, or `must not` in the same item; and
- `implementation validation` or `implementation-validation` and either `forbidden`, `not permitted`, or `must not` in the same item.

Matching is case-insensitive and allows punctuation or whitespace between words, but does not stem other words. A governed item that pairs edits, writes, or implementation validation with `allowed`, `permitted`, or `authorized` without a negation in the same semicolon-delimited clause is contradictory and produces `EC260`, even if another item contains the required boundary. The implementation records the first matching source position for each missing or contradictory concept. It does not infer permission from tone, repository policy, or the absence of implementation commands.

This check protects the ALP stop rule mechanically. The root still decides whether the user has granted the approval described by the contract.

## Diagnostics

Stable diagnostic families make tests and callers depend on meaning rather than full prose:

| Code    | Check                                                                       |
| ------- | --------------------------------------------------------------------------- |
| `EC001` | No unique raw or fenced EC could be selected                                |
| `EC100` | Required header is missing, duplicated, misplaced, empty, or placeholder    |
| `EC101` | Revision is not a positive integer                                          |
| `EC102` | Protocol is not exactly `v1`                                                |
| `EC103` | Governing-document and legacy-header selection conflicts                    |
| `EC200` | Item syntax, prefix, label, continuation, or top-level text is malformed    |
| `EC201` | An item identifier is duplicated                                            |
| `EC202` | An item reference is undefined                                              |
| `EC210` | Validation coverage syntax is malformed                                     |
| `EC211` | Validation coverage does not name a declared acceptance item                |
| `EC212` | A declared acceptance item is uncovered                                     |
| `EC220` | Question metadata is missing, duplicated, empty, or placeholder             |
| `EC230` | Required out-of-scope or file boundary is absent                            |
| `EC240` | An undefined vague control term or malformed definition appears             |
| `EC250` | Test-semantics disposition is missing, ambiguous, duplicated, or incomplete |
| `EC260` | Authorization-boundary language is missing or contradictory                 |

Report the most specific finding available and continue safely so one run exposes independent defects. Parser recovery must not fabricate items or coverage. Findings are sorted by source line, column, and code; file-system enumeration and hash order never affect output.

`passed_checks` contains only named top-level checks that completed without a finding, in the fixed order: `input`, `headers`, `items`, `references`, `coverage`, `questions`, `scope`, `vague_terms`, `test_semantics`, `authorization`. It is diagnostic evidence, not an acceptance score.

## Failure, Safety, and Determinism

The same input bytes, source label, command options, and linter version produce byte-for-byte identical standard output and the same exit status. Output contains no current time, random identifier, absolute-path expansion, environment dump, or filesystem metadata. For stdin the source label is `<stdin>`; for a path it is exactly the caller-supplied spelling.

Catch internal exceptions at the CLI boundary, emit a concise `EC900 internal linter failure` message to standard error, and exit `2`. Tests exercise expected invalid inputs so ordinary syntax errors never reach that path. Do not print a traceback unless an explicit developer-only debugging option is added in a later approved revision.

The linter does not execute contract commands, open referenced governing documents, resolve file-boundary paths, or test whether cited evidence exists. Those activities belong to workflow semantic preflight or later validation under the approved sandbox.

## Acceptance Oracles

`scripts/test_lint_ec.py` uses standard-library `unittest`, temporary files, and subprocess calls to the real CLI entry point. It requires no model credits, network, repository fixture, or third-party package.

| Criterion                                            | Deterministic fixtures                                                                                                                                                                                   |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Both input forms preserve locations.                 | Raw, fenced Markdown, CRLF, UTF-8 BOM, non-ASCII, stdin, caller-spelled path, zero matching blocks, and multiple matching blocks.                                                                        |
| Headers obey EC-v1.                                  | Canonical governing header, legacy ALP header, both together, duplicate/missing/misplaced headers, invalid revision, unsupported protocol, and placeholders.                                             |
| Item parsing is strict and recoverable.              | Every allowed label, continuations, invalid prefix/number/label, duplicate IDs, undefined references, and reference-like words.                                                                          |
| Coverage is complete.                                | One-to-one, many-to-one, one-to-many, malformed brackets, duplicate coverage, wrong identifier type, unknown acceptance, and uncovered acceptance.                                                       |
| Questions are explicit or absent.                    | No `Q`, complete `Q`, each missing or duplicate field, blank field, placeholder field, and synthetic no-question item.                                                                                   |
| Scope boundaries are present.                        | Both required `O` forms, each missing independently, empty text, and the report-before-editing obligation.                                                                                               |
| Control terms are bounded.                           | Each vague phrase, case variants, unrelated longer words, valid definitions, malformed definitions, and still-vague definitions.                                                                         |
| Test semantics are explicit when tests are in scope. | Tests in scope with all three concepts, each concept missing, duplicated Test-semantics items, both explicit no-test forms, no test mention, test validation commands only, and ambiguous test language. |
| Authorization is explicit.                           | Valid Phase-3 boundary, each concept missing, synonyms from the documented phrase groups, and contradictory permission.                                                                                  |
| CLI behavior is stable.                              | Text and JSON output, fixed finding order, exit `0`, `1`, and `2`, unreadable/non-UTF-8 input, no timestamps, and concise internal failure handling.                                                     |

The canonical passing fixture contains at least one decision, invariant, acceptance, validation, out-of-scope item, file boundary, explicit Test semantics, and authorization boundary. A separate passing legacy fixture proves `ALP chapter:` compatibility. Snapshot only stable structured fields and diagnostics; do not make tests depend on Python exception wording.

After deterministic tests pass, lint the historical EC in ALP Workflow Redesign without changing it. If it fails, classify the difference as a linter defect, an intentionally stricter approved rule, or legacy evidence requiring an explicit compatibility decision. Do not silently weaken the parser or rewrite historical evidence to manufacture a pass.

## Rollout and Retirement

Implement and validate the deterministic linter before the worker dispatcher so subsequent ECs can use it without a model call. During transition, the root may use the existing model-backed linter only when the deterministic command is unavailable or when semantic judgment is actually requested; it must describe which function is being used.

Once deterministic tests and the installed invocation pass:

1. update `alp-workflow/SKILL.md` and `references/handoff-contract.md` to invoke `scripts/lint_ec.py` for mechanical EC-v1 checks;
2. stop treating contract linting as a dispatchable worker role;
3. rename `alp_luna_contract_linter.toml` to `alp_luna_contract_linter.toml.disabled` for recoverable retirement; and
4. do not create an `alp_contract_linter.toml` replacement.

Rollback restores the prior skill wording and re-enables the legacy profile. The deterministic script and tests may remain inert until a versioned source exists; rollback must not destroy evidence or silently switch callers between mechanical and semantic review.

## Current Decisions and Open Work

- The deterministic linter and its separate standard-library oracle were installed on 2026-07-17. The installed suite passed before the model-backed legacy linter profile was recoverably disabled.
- The unchanged historical EC in ALP Workflow Redesign produces four intentionally stricter EC-v1 findings: its extended Out-of-scope label is not the exact governed label, `appropriate` is an undefined control term, its older Test-semantics wording lacks the new exact three-part form, and no exact Out-of-scope item consequently parses. It remains explicitly historical evidence rather than an active contract and was not rewritten to manufacture a pass.
- EC-v1 mechanical checking is local, deterministic, and model-free.
- One script handles parsing, linting, text output, and JSON output; a separate test script owns its oracle.
- Raw EC and exactly one Markdown fenced EC are accepted while line locations remain source-relative.
- The linter checks structure, references, coverage, questions, scope, control language, test disposition, and the pre-approval boundary.
- Semantic sufficiency and phase approval always remain with the root orchestrator.
- No forward model profile replaces the legacy contract-linter profile.
- No material design decision remains open for the initial linter.

## Sources

- `alp-workflow/references/handoff-contract.md` — installed EC-v1 syntax and semantic-preflight authority.
- `alp_luna_contract_linter.toml` — legacy mechanical prompt whose useful deterministic checks are reconciled here without preserving its model dependency.
- ALP Workflow Redesign — phases, approval authority, worker roles, and acceptance semantics.
- ALP Worker Dispatch — runtime adapter whose capability registry deliberately excludes contract linting.
- ALP Workflow Repository Migration — staged installation, rollback, and later repository packaging.
