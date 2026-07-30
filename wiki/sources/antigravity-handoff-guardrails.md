# Antigravity Handoff Guardrails

Status: Historical input; not adopted current policy.

Original source: `OldAntigravityALP/wiki/alp-guardrails-and-ownership.md`

Preservation: Portable guardrail lessons retained for a future handoff-design
session. Stale wiki framing and cross-links were normalized; examples naming
specific neighboring projects or local configuration were omitted.

## Core distinction

Spec-driven development writes desired behavior before implementation. ALP
additionally makes the durable human-facing Book the source of truth and keeps
implementation artifacts synchronized from it. The value is strongest when a
repository teaches agents intent, not only mechanics.

## Ownership model

The proposed model keeps ownership on the Book side. A chapter may declare the
implementation artifacts it governs, making ownership visible and toolable
without requiring every source file to carry process metadata. A canonical
chapter may own a module while later chapters explicitly extend it and point
back to the canonical explanation.

## Avoid premature bidirectionality

Implementation files need not carry mandatory links back to chapters. Such
comments can help generated or heavily governed files, but mandatory
bidirectional links create another graph that can drift. Add them only if
repeated evidence shows the Book and its navigation are insufficient.

## Guardrail and scaffolding lessons

Implementation workflow rules should apply to every implementation artifact,
not only a source directory. Scaffold commands should fail when a target exists
by default, require an explicit destructive mode for replacement, and offer a
narrow update mode for managed template files. A future ownership manifest may
make update scope machine-readable. Downstream projects should preserve enough
wiki context to understand their operating rules.
