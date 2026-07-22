---
name: alp-workflow
description: Orchestrate phase-gated repository work through Brainstorm, Governing Documentation, Implementation, independent review, and Wrap Up using Full ALP, Spec-driven, or Mechanical strategies. Use for non-trivial tasks, vague requirements that need refinement, ALP Books and AI-assisted tangling, specifications, critical acceptance oracles, implementation or Antigravity handoffs, repository workflow alignment, independent review, and durable TODO/wiki wrap-up.
---

# ALP Delivery Workflow

Use the least process that gives adequate assurance. The governing Book or
approved specification is the source of intent; current code and legacy
artifacts are evidence, never an unstated specification.

## Strategies and phase gates

Brainstorm clarifies goal, non-goals, risks, compatibility, likely files,
strategy, and acceptance. Choose Full ALP for a readable, tangle-ready Book;
Spec-driven for an approved specification that leaves only ordinary
implementation discretion; Mechanical only for a small behaviorally obvious
change allowed by local guidance. Summarize each phase and obtain explicit
approval before continuing. A user may explicitly waive or batch named
non-code phase summaries, but Implementation still needs explicit
authorization. Apply [alp-authoring](../alp-authoring/SKILL.md) when authoring
a Book chapter.

Every material behavior traces to a decision or criterion and a visible
observable oracle. Prefer an independently owned executable oracle when it is
meaningful and practical; otherwise name the real static, manual, runtime,
telemetry, rollback, or other oracle and its limitations. Do not weaken or
redefine critical test semantics. A failed or weak oracle is reported with
residual risk; it never causes automatic escalation.

## Delegation and authority

Delegate only when the value gate predicts a concrete benefit (cheaper bounded
work, protected root context, noisy-output compression, independent judgment,
useful latency, or separate external capacity) that outweighs briefing,
reconciliation, drift, and repair cost. Sol and the user retain material
decisions, scope, phase gates, acceptance, reconciliation, and final synthesis;
Sol performs no repository work. Native packets and manual ECs are distinct
routes; route mechanics live in [native-worker-delegation](references/native-worker-delegation.md)
and [handoff-contract](references/handoff-contract.md). Workers are fresh,
narrow, non-recursive, and stop on design, scope, permission, or oracle gaps.

## Implementation, review, and wrap up

The user chooses the approved Implementation route: native worker delegation or manual/external EC handoff. For native Full ALP, use a fresh Luna tangler; for a manual/external route, use the complete revisioned EC and external implementer.
If a Luna tangler is chosen, it returns a design-gap packet rather than
inventing architecture, algorithms, compatibility behavior, or other material
decisions. Spec-driven workers use only the discretion explicitly left open by
the specification. Native or manual completion is evidence, not acceptance.

Every non-trivial change receives a fresh Terra review. Review input, session
goals, exact findings, non-acceptance, closure, deferability, deterministic
verifier exception, weak-oracle handling, and one reconciliation are governed
by [review-and-wrap-up](references/review-and-wrap-up.md). Sol and the user
alone may defer or accept findings. Wrap Up records only manifested durable
follow-ups and required TODO/wiki/index/log or governing-document reconciliation.

## Safety

Keep the approved file boundary closed. Do not access production or databases,
perform destructive or out-of-scope actions, install or synchronize external
artifacts, or create compatibility shims, fallback transports, or bespoke prose
oracles. If recovery changes design, scope, permissions, phase, or acceptance,
stop and return to the user.
