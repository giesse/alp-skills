# Canonical Handoff Contract

Create an EC only for an external or materially fresh implementation context that needs a concise, self-contained transfer artifact. The approved governing document remains the durable source of truth. The Phase 2 gate approves the document, critical-oracle semantics, implementation route, and EC revision before dispatch.

Copy the complete approved revision into the handoff. If contract content changes after approval, update the governing document when design changes, obtain approval, increment `Revision`, and issue a complete replacement. Never patch a dispatched revision silently.

```text
Contract: EC-1
Revision: 1
EC protocol: v1
Task: <short name>
Governing document: <path and heading>

D1 Decision: <settled behavior or design choice>
I1 Invariant: <must remain true>
I2 Test semantics: <independent owner when practical; name authorized existing-test updates and replacement-revision handling>
A1 Acceptance: <observable definition of done>
V1 Validation [covers A1]: <required command, check, observation, or other oracle>
O1 Out of scope: <explicit non-goal>
O2 File boundary: <expected repository files; report any additional file before editing>
Q1 Question: <unresolved point>
    Owner: <orchestrator, worker, user, or external implementer>
    Evidence required: <what resolves it>
    Resolve before: <task or phase>
```

Accept legacy `ALP chapter` in place of `Governing document` under EC protocol v1. Omit `Q` entirely when there are no unresolved questions.

## Deterministic mechanical lint

Run the local Python 3.11+ standard-library linter before semantic preflight or dispatch:

From the installed `alp-workflow` skill directory:

```text
python3 scripts/lint_ec.py path/to/contract.md
python3 scripts/lint_ec.py --json path/to/contract.md
python3 scripts/lint_ec.py - < path/to/contract.md
```

The command accepts a raw EC or exactly one matching fenced Markdown EC. `-` reads UTF-8 stdin. It performs no repository discovery, reference resolution, network access, model call, command execution, or file edit. Text output is empty on success or emits sorted `source:line:column CODE message` diagnostics. JSON output is one stable schema-version-1 object. Exit status `0` means the deterministic surface passes, `1` means EC findings exist, and `2` means input or internal failure. The check covers headers, item syntax and references, acceptance coverage, question metadata, scope boundaries, vague control terms, test semantics, and the pre-approval authorization boundary.

This is a mechanical surface check only. It does not judge design quality, semantic sufficiency, oracle strength, materiality, production safety, or phase approval. The root orchestrator retains semantic preflight and the phase gate. The implementation is [lint_ec.py](../scripts/lint_ec.py) and its standard-library oracle is [test_lint_ec.py](../scripts/test_lint_ec.py).

## External Handoff

- Perform semantic preflight across the governing document, contract, and critical oracles before dispatch.
- Mechanically lint the contract in the root thread when delegating that bounded check would cost more.
- Give every `A` item at least one observable `V` oracle and state limitations.
- Define the repository boundary; treat an extra required repository file as a scope conflict.
- Treat Antigravity planning artifacts as control-plane artifacts outside that boundary.
- Require the implementer to acknowledge decisions, invariants, acceptance/oracle semantics, boundaries, blocking questions, and test semantics and to report contradictions.
- Do not require exhaustive contract-ID annotation on every plan or task item.
- Bring the initial Antigravity plan to the Terra orchestrator for one conformance review.
- Correct only material blockers: wrong behavior, broken oracle, file-boundary violation, contradictory evidence, or unapproved critical-test change.
- After one focused correction, proceed unless a concrete blocker remains; return a remaining blocker to the user.
- Allow named existing-test updates and non-conflicting added coverage. Require a replacement revision before weakening or altering critical semantics beyond the approved intent.
- Require a compact evidence packet with contract revision, changed files, validation evidence, deviations, unresolved concerns, acceptance coverage, repository discoveries, durable-learning suggestions, and concrete workflow friction.

## Mechanical Lint Surface

Check structure only:

- required `Contract`, positive `Revision`, supported `EC protocol`, `Task`, and either `Governing document` or legacy `ALP chapter`;
- recognized, unique `D`, `I`, `A`, `V`, `O`, and optional `Q` IDs;
- valid `V [covers ...]` references and validation coverage for every `A`;
- complete metadata for each present `Q` and no placeholder `Q`;
- explicit out-of-scope and repository file-boundary entries;
- test-semantic ownership and replacement-revision handling when tests are in scope; and
- authorization wording that permits read-only planning but forbids edits and implementation validation before approval.

Leave behavioral sufficiency and oracle strength to semantic preflight.

## Review Sequence

1. Review the governing document or contract, diff, and independent evidence without the walkthrough.
2. Attempt to disprove acceptance, inspect unchanged invariants, detect unsupported behavior, and identify production failure modes.
3. Read the walkthrough and reconcile once.
4. Request another iteration only with a contract ID or diff evidence, a non-acceptance reason, and a closure condition.
