# Manual and External Handoff Contract

Use this revisioned Execution Contract (EC) for a manual handoff to
Antigravity (Gemini Flash). The approved Book or specification remains the
source of intent. Native workers use the separate [native worker delegation](native-worker-delegation.md)
packet, not this envelope.

## EC protocol v1

Each complete revision has a stable `Contract`, positive `Revision`, `EC
protocol: v1`, `Task`, and `Governing document`. Existing material may use the
legacy header `ALP chapter`; it remains accepted for compatibility. The body
contains unique `D`, `I`, `A`, `V`, `O`, and optional `Q` items:

```text
Contract: EC-1
Revision: 1
EC protocol: v1
Task: <short name>
Governing document: <path and heading>

D1 Decision: <settled behavior>
I1 Invariant: <behavior or compatibility that remains true>
I2 Test semantics: <independent owner; named authorized updates only>
A1 Acceptance: <observable completion criterion>
V1 Validation [covers A1]: <command, check, observation, or other oracle>
O1 Out of scope: <explicit non-goal>
O2 File boundary: <exact repository files>
Q1 Question: <unresolved point>
    Owner: <named owner>
    Evidence required: <what resolves it>
    Resolve before: <task or phase>
```

Omit the `Q` section when no unresolved question exists. Every `A` needs one
or more `V` references. Any approved-content change requires a complete,
incremented replacement revision; never patch a dispatched revision silently.

## Deterministic lint before handoff

After the complete EC revision is prepared, Sol runs the repository-local deterministic linter directly in the root context before manual handoff. From the repository root use:

```text
python3 codex/skills/alp-workflow/scripts/lint_ec.py path/to/contract.md
python3 codex/skills/alp-workflow/scripts/lint_ec.py --json path/to/contract.md
```

From the `codex/skills/alp-workflow` directory, the equivalent file and stdin forms are:

```text
python3 scripts/lint_ec.py path/to/contract.md
python3 scripts/lint_ec.py - < path/to/contract.md
```

The command accepts a raw EC or one fenced Markdown EC. Exit `0` means no structural findings, `1` means deterministic EC findings were reported, and `2` means input or internal failure; normal text output is empty on success and lists deterministic diagnostics otherwise (the `--json` form emits the stable machine-readable report). The check covers structure only; it cannot establish semantic sufficiency, oracle strength, design quality, safety, or phase approval. Creating and mechanically checking this control artifact stays in the root context; it does not require a delegated EC semantic preflight. Sol and the user assess the plan directly against the approved EC before authorization, and fresh independent semantic review occurs post-implementation after evidence exists.

## Read-only planning and authorization

Before implementation, the external implementer may inspect the repository and return a read-only plan. It must not edit repository files or run implementation validation during planning. The implementer then acknowledges decisions, invariants, acceptance and oracle semantics, file boundary, out-of-scope work, test-update limits, and blocking questions. Contradictory evidence, a required extra file or permission, a changed critical-test meaning, or a material Full ALP design gap is reported and stops the handoff.

Antigravity-native plans and task lists are control-plane artifacts outside the repository boundary. That exception authorizes no repository source, test, or generated artifact. Named existing-test updates or compatible added coverage are allowed only when the approved EC says so; weakening or changing critical semantics requires a replacement revision.

Sol and the user review the initial read-only plan directly against the EC and decide whether to authorize implementation. A separate Terra plan review is not added here: reviewing both the EC and that plan independently before a diff exists would duplicate pre-implementation judgment. Exactly one fresh independent Terra review remains required after implementation evidence and the final diff exist. Explicit user authorization is required before repository implementation and approved validation.

## Completion evidence

The external implementer returns a compact packet naming contract and revision,
changed files, exact validation/oracle evidence and limitations, deviations,
unresolved concerns, acceptance coverage, repository discoveries, suggested
durable learnings, concrete workflow friction, and inspected/uninspected scope.
Successful commands alone are not acceptance; Sol and the user retain final
acceptance authority. Preserve the approved static, manual, runtime,
telemetry, rollback, or other observable oracle when an executable test would
be synthetic, unsafe, or impractical.
