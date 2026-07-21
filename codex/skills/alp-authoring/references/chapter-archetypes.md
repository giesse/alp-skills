# Chapter Archetypes

Use these archetypes to discover the questions a chapter must answer. Combine
them when the behavior genuinely spans concerns. Do not copy their headings or
turn them into a universal repository layout.

## Contents

- [Architecture or System Narrative](#architecture-or-system-narrative)
- [Module or Function Contract](#module-or-function-contract)
- [Cross-component Feature](#cross-component-feature)
- [Legacy Reconstruction and Forward Design](#legacy-reconstruction-and-forward-design)
- [Operational or Production Behavior](#operational-or-production-behavior)

## Architecture or System Narrative

Use for a system boundary, major component relationship, or design direction.

Ask:

- What problem and constraints shape the architecture?
- Which components own which responsibilities and data?
- How do events, state, and failures move through the system?
- Why was this boundary selected over plausible alternatives?
- Which compatibility and operational properties must remain stable?

Prefer a relationship or event-flow diagram, a responsibility table, and prose
that teaches the mental model. Add pseudocode only for material orchestration or
state behavior.

Common omissions: hidden ownership, unexplained boundaries, failure propagation,
and a diagram that shows topology without rationale.

## Module or Function Contract

Use for cohesive behavior centered on a module, class, function, tool, or
protocol endpoint.

Ask:

- What responsibility does it own, and what remains outside it?
- What are the inputs, outputs, preconditions, side effects, and failures?
- Which ordering, retry, timeout, cleanup, or idempotency behavior is material?
- Which callers or persisted formats constrain compatibility?
- What evidence distinguishes correct from subtly wrong logic?

Prefer contracts, small examples, and pseudocode or a state machine. Explain why
each non-obvious branch exists rather than mirroring source layout.

Common omissions: exceptional paths, partial failure, cleanup, unchanged caller
behavior, and exact semantics hidden behind library syntax.

## Cross-component Feature

Use when one user-visible or operational behavior crosses several ownership
boundaries.

Ask:

- What is the end-to-end outcome?
- Where does responsibility transfer?
- Which data or invariants cross each boundary?
- How are partial success, retries, duplicate events, and rollback handled?
- Which components change, and which remain compatible?

Prefer an event sequence, ownership table, interface contracts, and boundary
examples. Keep the narrative centered on the feature rather than presenting a
file-by-file tour.

Common omissions: handoff failure, inconsistent state, ownership ambiguity, and
acceptance evidence that checks components without checking the whole behavior.

## Legacy Reconstruction and Forward Design

Use when code predates the Book or current intent must be recovered from mixed
evidence.

Ask:

- What is observed today, and what evidence supports it?
- Which behavior is intended, compatibility-required, incidental,
  contradictory, or unresolved?
- What rationale can be established, and what must remain explicitly unknown?
- What does the approved forward design preserve, replace, or leave alone?
- Which real oracle is trustworthy in this legacy environment?

Read [legacy-reconciliation.md](legacy-reconciliation.md). Prefer separate
current-behavior and forward-design explanations, followed by a compatibility
mapping.

Common omissions: canonizing every quirk, inventing rationale, hiding
contradictions, and manufacturing a test harness that does not reflect the real
system.

## Operational or Production Behavior

Use for deployment, migration, repair, monitoring, credentials, or other
operator-visible behavior.

Ask:

- What preconditions and safety boundaries apply?
- What is the blast radius and observable progress?
- How do retries, checkpoints, cancellation, and partial completion work?
- Which rollout, rollback, alarm, and stop conditions protect production?
- What evidence is available before, during, and after the operation?

Prefer a state or timeline diagram, configuration table, bounded algorithm, and
explicit operator evidence. Separate explanatory design from a command
runbook when the repository does so.

Common omissions: rollback reality, production-only failure modes, ambiguous
ownership, secret or state lifecycle, and nominal tests substituted for runtime
evidence.
