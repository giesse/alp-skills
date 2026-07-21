# Authoring Preflight

Run this preflight before returning the Book to `alp-workflow`.

## Contents

- [Classify Findings](#classify-findings)
- [Good-teacher Test](#good-teacher-test)
- [Intent and Boundaries](#intent-and-boundaries)
- [Structured Behavior](#structured-behavior)
- [Compatibility and Evidence](#compatibility-and-evidence)
- [Traceability and Oracles](#traceability-and-oracles)
- [Tangle-readiness Test](#tangle-readiness-test)
- [Local Integration](#local-integration)
- [Return Contract](#return-contract)

## Classify Findings

Use one of these classifications:

- **Design gap:** Completing the Book requires an unapproved material decision
  or resolution of contradictory authority. Stop and return to Brainstorm.
- **Authoring gap:** The approved decision exists but the Book omits, obscures,
  or contradicts it. Repair the Book within Governing Documentation.
- **Local integration gap:** Placement, navigation, or terminology conflicts
  with current repository convention. Repair it within the documentation
  boundary.
- **Not applicable:** The topic genuinely does not apply. Record this only when
  silence would otherwise look accidental.

Do not call missing prose a design gap before checking the approved inputs.

## Good-teacher Test

Confirm that a human reader can explain:

- the problem and why the chapter exists;
- the mental model and terminology;
- the material decisions and their rationale;
- what changes and what explicitly remains unchanged;
- the dangerous boundaries and failure modes;
- how the design fits its neighboring concepts; and
- why the named acceptance evidence is credible.

Confirm that the chapter:

- follows learning order rather than source-file or compiler order;
- introduces concepts before using them in dense representations;
- defers distracting details without hiding material behavior;
- avoids requirement dumps and code-shaped narration; and
- lowers the cognitive load of reviewing subtle or production-risk behavior.

A chapter that enables implementation but does not teach the design fails this
test.

## Intent and Boundaries

Check:

- purpose and non-goals are explicit;
- ownership and system boundaries are unambiguous;
- intended and unchanged behavior are both stated;
- affected artifacts and interfaces are named where material;
- responsibilities excluded from the chapter are clear;
- unresolved questions are visible; and
- no material decision was silently introduced during authoring.

Challenge a chapter boundary that exists only because files happen to be
organized that way.

## Structured Behavior

Check the normal path and all material:

- branching and ordering;
- state transitions;
- errors and user-visible failures;
- retry, timeout, idempotency, and concurrency;
- cleanup and rollback;
- partial failure and restart;
- boundary and adversarial inputs; and
- configuration or environment variants.

Confirm that each behavior uses an appropriate representation and that exactness
stops before incidental implementation syntax.

## Compatibility and Evidence

Check:

- persisted data, public interfaces, callers, and operational behavior that
  must remain compatible;
- migration and rollback constraints;
- production-only limitations or evidence;
- claims about current behavior against code, tests, operations, or runtime
  observations; and
- contradictions between the Book and repository evidence.

Do not treat current code as authoritative intent. For legacy evidence, apply
`legacy-reconciliation.md`.

## Traceability and Oracles

For every material behavior, identify:

- the approved decision, constraint, or compatibility requirement; and
- an observable acceptance criterion or explicitly limited oracle.

Confirm:

- a compact decision summary exists when it materially reduces review effort;
- the narrative, structured logic, and oracles do not contradict that summary;
- oracle limitations are honest;
- weakly testable behavior uses real static, manual, runtime, telemetry, or
  rollback evidence rather than a nominal harness;
- critical executable test or fixture semantics are clear enough for
  independent preparation at the start of Implementation; and
- EC identifiers or handoff bookkeeping did not leak into the Book.

The authoring skill specifies oracle meaning but never decides that later
evidence passes or weakens an approved oracle.

## Tangle-readiness Test

Ask whether Luna or Gemini Flash would need to:

- invent architecture, ownership, or an interface;
- choose among materially different algorithm families;
- infer data shape, persistence, or compatibility;
- choose retry, timeout, cleanup, or failure semantics;
- use current code as the hidden specification;
- invent or weaken an oracle; or
- resolve an open question that changes material behavior.

If yes, repair an authoring gap or report a design gap. Do not assign a stronger
implementation model to compensate.

Allow harmless idiomatic choices such as local names, equivalent helper
decomposition, formatting, or library calls with identical approved semantics.

## Local Integration

Confirm:

- the chapter is placed beside the concepts it teaches;
- README, table-of-contents, index, or navigation changes follow the current
  repository convention;
- neighboring entries remain coherent;
- terminology matches the current Book;
- accidental omissions were not promoted into generic policy; and
- no unrelated Book or wiki reorganization occurred.

## Return Contract

Choose the outcome in this order:

1. Return `MISSING DESIGN APPROVAL` without editing when material inputs are
   complete but observable approval evidence is absent.
2. Return `BLOCKED BY DESIGN GAP` when approved authoring cannot be completed
   without an unapproved material choice or resolution of contradictory
   authority.
3. Return `READY FOR WORKFLOW PREFLIGHT` only when approval exists, all
   authoring and local integration gaps are repaired, and no design gap remains.

Report:

- governing document and changed documentation paths;
- decisions and unchanged behavior encoded;
- representations added and why;
- criterion-to-oracle coverage and limitations;
- local integration edits;
- contradictory or unresolved evidence; and
- inspected and uninspected scope.

Remember that readiness for workflow preflight is not Implementation approval.
