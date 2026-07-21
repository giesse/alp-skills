---
name: alp-authoring
description: Author and revise Full ALP Book chapters as readable, tangle-ready governing documents during alp-workflow Governing Documentation. Use when Full ALP has been selected and Codex must discover local Book conventions, encode approved intent, rationale, structured logic, compatibility, and acceptance oracles, reconcile legacy evidence, or preflight a chapter for Luna or Gemini Flash tangling. Do not use for Spec-driven or Mechanical work, delivery phase ownership, implementation, review, Wrap Up, or merely reading or tangling an already approved Book.
---

# ALP Book Authoring

Write a Book that teaches a human reader why the system behaves as it does and
lets a simple capable model regenerate the implementation without material
design judgment. Treat readability, reviewability, and tangle-readiness as
separate requirements that must all hold.

## Keep the Workflow Boundary

Use this skill only inside an approved Full ALP Governing Documentation phase,
or when the user directly supplies an explicitly approved Full ALP design
context.

Do not activate it merely because an Implementation task reads or tangles an
already approved Book. That work remains under `alp-workflow` and the selected
implementer.

Leave these responsibilities to `alp-workflow` and its root orchestrator:

- selecting Full ALP, Spec-driven, or Mechanical work;
- owning phases, user approvals, scope, and material decisions;
- choosing implementers or delegating work;
- defining whether evidence satisfies acceptance;
- creating EC contracts;
- implementing, independently reviewing, and wrapping up.

Expose missing decisions; never resolve them silently. Return to Brainstorm when
the missing choice affects intent, architecture, interfaces, data ownership,
compatibility, failure policy, rollout, or oracle semantics.

Do not apply this skill to generic documentation, concise specifications,
implementation prompts, ECs, code review, or routine Wrap Up reconciliation.
A material design change during Implementation or Wrap Up must reopen Governing
Documentation before this skill is applied again.

## Verify Authoring Authority

Require both complete material inputs and observable approval.

Accept approval when:

- the user approved the relevant Brainstorm result or entry into Governing
  Documentation in the current thread;
- the user supplies a complete brief and explicitly approves that revision for
  authoring; or
- an approved-status governing artifact identifies its revision and approval
  provenance, and the user directs Codex to use it.

If a complete brief lacks approval, return `MISSING DESIGN APPROVAL` without
editing. If material inputs are incomplete, return `BLOCKED BY DESIGN GAP`
with the exact missing choices and recommend `$alp-workflow` Brainstorm.
Direct invocation authorizes authoring activity, not unstated design
assumptions.

Require:

- goal, non-goals, constraints, and scope;
- intended and unchanged behavior;
- approved material decisions and unresolved questions;
- acceptance criteria or agreed oracle semantics; and
- a target Book location or enough repository evidence to identify it.

## Inspect Local Authority

At the start of authoring, inspect the relevant:

- `AGENTS.md`;
- `wiki/index.md` and `TODO.md` when present;
- Book README, table of contents, or navigation;
- related chapters and established terminology; and
- task-relevant code, tests, operational documentation, or runtime evidence.

Report useful institutional knowledge or state that none was found. Read only
the relevant Book neighborhood rather than the entire Book unless local rules
require more.

Use approved design intent for what should happen. Use code and tests as
evidence of current behavior, not as an unstated specification. Report stale or
contradictory local guidance instead of silently repairing unrelated material.
Do not import repository organization, commands, or validation rules from
another project.

For legacy or contradictory evidence, read
[references/legacy-reconciliation.md](references/legacy-reconciliation.md)
before drafting.

## Author the Chapter

### 1. Establish a coherent boundary

Locate the chapter that already owns the behavior. Revise or extend it when the
new material shares one coherent responsibility; add or split a chapter when a
human would otherwise need to learn unrelated concepts together.

Treat a boundary choice as a design gap when it changes architecture,
ownership, compatibility, or the approved implementation file boundary.

Read [references/chapter-archetypes.md](references/chapter-archetypes.md) when
chapter shape is unclear. Treat archetypes as question sets, never mandatory
templates.

### 2. Build an authoring map

Map the approved material before drafting:

- purpose, rationale, and current context;
- intended and explicitly unchanged behavior;
- ownership, interfaces, data shapes, configuration, and affected artifacts;
- normal structured logic and boundary behavior;
- errors, retries, timeouts, cleanup, and partial failure;
- compatibility, migration, rollout, and rollback constraints;
- adversarial cases;
- observable acceptance oracles and their limitations; and
- unresolved questions.

Use this as a coverage map, not a required heading list.

### 3. Teach in reader order

Organize the chapter as a good teacher would build the reader's mental model,
not in compiler, source-file, or implementation order. Explain why before
mechanics. Reveal concepts only when the reader has enough context and defer
compiler-relevant detail that would distract at that point.

Make reviewability a safety property. A reviewer should be able to explain the
mental model, important decisions and rationale, dangerous boundaries, and why
the acceptance evidence is credible without reconstructing intent from code.

Avoid requirement dumps, code-shaped prose, large incidental code excerpts,
and workflow bookkeeping. A chapter that only lets an implementer emit code is
not sufficient Full ALP.

### 4. Add semantic precision

Choose prose, diagrams, tables, examples, schemas, contracts, pseudocode, state
machines, or literal algorithms according to the ambiguity they remove. Read
[references/representation-guide.md](references/representation-guide.md) when
structured behavior is hard to express or the draft becomes code-shaped.

Increase exactness wherever implementation freedom becomes material. Stop
before prescribing harmless idiomatic choices. Prefer exact semantics over
incidental or unfamiliar syntax unless the syntax or protocol is itself
material behavior.

### 5. Make material behavior traceable

Trace each material behavior to an approved decision, constraint, or
compatibility requirement and to an observable acceptance criterion or named
limited oracle. State unchanged behavior explicitly.

Use a compact decision summary when several material choices exist. Do not
annotate every paragraph with identifiers. Do not import EC protocol, contract
vocabulary, or handoff bookkeeping into the Book.

Encode critical test or fixture semantics in the Book, but do not create
executable tests or fixtures through this skill. `alp-workflow` decides at the
start of Implementation whether independent oracle preparation is practical
before delegated coding.

### 6. Integrate the chapter locally

Apply the repository's current discoverability rules: update the appropriate
README, table of contents, index, related-reading entry, or neighboring
navigation. Inspect adjacent entries after insertion.

Do not treat accidental omissions as preferred conventions, and do not broaden
the task into a Book reorganization. Report a larger navigation problem as a
separate repository concern.

## Preflight the Book

Before returning, read
[references/authoring-preflight.md](references/authoring-preflight.md) and run
the complete semantic preflight. Treat its good-teacher and simple-tangler
tests, finding classifications, outcome precedence, and evidence packet as the
authoritative return contract.

Repair an authoring gap when the approved decision already exists. Repair a
local integration gap within the documentation boundary. Return
`BLOCKED BY DESIGN GAP` only when completion needs an unapproved material
choice or resolution of contradictory authority.

If either mandatory test fails, improve the Book or report the blocking design
gap. Do not compensate with a stronger implementation model.

## Limit Writes and Return Evidence

Write only:

- the new or revised governing Book chapter;
- required Book integration documents such as a README, index, table of
  contents, or neighboring navigation; and
- documentation-only diagrams or examples embedded there.

Do not write production code, executable tests or fixtures, deployment files,
agent definitions, ECs, implementation plans, or routine wiki bookkeeping.

Return exactly one status using the precedence in the preflight reference:
`MISSING DESIGN APPROVAL`, `BLOCKED BY DESIGN GAP`, or
`READY FOR WORKFLOW PREFLIGHT`. Include the reference's compact evidence
packet. Readiness for workflow preflight is not Implementation approval.
