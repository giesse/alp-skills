# Execution Contracts and Evidence

[ALP Skills Book](../README.md) · Previous:
[Authoring ALP Books](authoring-alp-books.md) · Next: [EC Linter](ec-linter.md)

## When a Book needs a compact travelling companion

The governing Book or specification remains the source of intent. An Execution
Contract (EC) is used only when an external or materially fresh implementer
needs a short, self-contained handoff. It prevents a handoff from depending on
an unavailable conversation while avoiding a second competing design document.

An EC names the governing document, approved decisions and invariants,
acceptance criteria, observable validation, out-of-scope work, file boundary,
and any question that must be resolved before the next phase. A changed
contract is a new revision, not a quiet patch to an already dispatched brief.

## What the contract protects

The contract asks an implementer to report a conflict instead of silently
expanding scope. An additional repository file, changed critical-test meaning,
or contradiction between the Book and task is therefore a stop condition, not
an invitation to improvise.

Critical test or fixture semantics belong to the workflow owner whenever that
independence is practical. An external implementer may add compatible coverage,
but may not weaken the agreed oracle merely to make a result pass.

## Mechanical checks and human judgment

The EC linter is a small deterministic check. Its detailed contract is in the
next chapter. It verifies structure; it does not decide whether a design is
wise, an oracle is strong, or a production action is safe.

That separation is intentional. Mechanical checks catch omissions cheaply and
consistently; the root workflow retains semantic preflight, phase approval, and
acceptance judgment.

## Evidence after implementation

A compact completion packet records changed files, validation, deviations,
unresolved concerns, acceptance coverage, discoveries, and durable lessons.
A fresh reviewer first compares the governing document, final diff, and
independent evidence before reading an implementation walkthrough. This makes
the review a check against intent, not a confirmation of the implementer's
story.

---

[ALP Skills Book](../README.md) · Previous:
[Authoring ALP Books](authoring-alp-books.md) · Next: [EC Linter](ec-linter.md)
