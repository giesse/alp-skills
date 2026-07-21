# Legacy Reconciliation

Use this method when implementation predates the Book, the Book and code
disagree, or intent must be reconstructed from mixed evidence.

## Separate Evidence from Intent

Inspect only task-relevant:

- existing Book chapters and durable design records;
- code and configuration;
- focused tests and fixtures;
- operator documentation and runbooks;
- runtime observations, telemetry, and production constraints; and
- user decisions or historical evidence with known provenance.

Code proves that a mechanism exists, not why it exists or whether every detail
is intentional. Tests prove only the semantics they actually observe. Runtime
evidence may expose compatibility or operational truth without explaining
rationale.

## Classify Material Observations

Classify each observation that affects the forward design:

- **Intended:** Supported by approved decisions, the governing Book, explicit
  user decisions, or established operational requirements. Tests may
  corroborate observed behavior but do not establish intent by themselves.
- **Compatibility constraint:** Required to remain stable even if it is not the
  preferred new design.
- **Incidental:** An implementation detail that does not need to become
  governing behavior.
- **Contradictory:** Conflicts with approved intent or another authoritative
  source.
- **Unresolved:** Material behavior whose intended status cannot be
  established.

Do not resolve contradictory or unresolved material behavior by majority vote
among artifacts. Return it to the root orchestrator.

## Reconstruct Current Behavior

Explain the current behavior in reader order:

1. State the responsibility and observed outcome.
2. Identify ownership, persisted state, and external boundaries.
3. Describe material normal and failure paths.
4. Name compatibility and operational constraints.
5. Cite the evidence type behind important claims.
6. Mark unknown rationale as unknown.

Avoid a file-by-file tour. Teach the behavior that the files collectively
produce.

## Define the Forward Design

For each material current behavior, state whether the approved design:

- preserves it unchanged;
- preserves only its externally visible compatibility;
- replaces it and why;
- migrates it through an explicit transition;
- leaves it deliberately outside scope; or
- blocks pending a decision.

Keep reconstructed current behavior and forward intent distinguishable. A
tangler must be able to tell which mechanics are evidence and which semantics
are prescriptive.

## Handle Tests and Oracles Honestly

Use the repository's real validation surface. A legacy system may rely on deep
static review, bounded inspection, runtime observation, operator evidence, or a
rollback trigger rather than an executable unit test.

Do not invent a harness, browser check, database query, or production operation
only to satisfy generic test language. When a practical executable oracle
exists, define its semantics precisely enough for independent preparation
before delegated implementation.

## Reconciliation Output

Include:

- an evidence summary with inspected and uninspected scope;
- the observation classification;
- current behavior and forward design;
- explicit unchanged compatibility;
- contradictions and unresolved decisions;
- real acceptance oracles and limitations; and
- any deferred repository cleanup that should not broaden the current task.

Return `BLOCKED BY DESIGN GAP` when a contradictory or unresolved observation
would force the author or tangler to choose material behavior.
