# Review and Wrap Up

## Fresh review contract

The reviewer receives the governing Book or specification, final diff,
independent evidence, and explicit session goals before any implementation
walkthrough. If session goals are absent or materially ambiguous, return
`blocked` rather than inventing a standard. Terra is the default fresh reviewer.
A fresh deterministic verifier may substitute only for read-only documentation
or data work with a fully deterministic oracle and no material interpretation,
policy choice, conflict resolution, or acceptance judgment. A separate Sol
escalation reviewer is eligible only after explicit user authorization.

Attempt to disprove acceptance and inspect unchanged invariants. Every finding
includes severity, exact evidence, affected criterion or invariant, why
acceptance is not justified, a closure condition, and the exact statement:
`Deferrable without affecting stated session goals: yes | no | uncertain — <reason>`.
Only Sol and the user may defer or accept a finding; classification does not
itself defer or close it.

## Oracle weakness and reconciliation

Label a weak, missing, or failed oracle and its residual risk. Never trigger
automatic Sol escalation. Sol and the user choose whether to reopen an earlier
phase, add an approved assurance measure, or accept the labelled limitation.
Reconcile implementation and review once. Permit one focused correction only
for a concrete blocker with evidence, non-acceptance reason, and closure
condition; reopen the appropriate phase if design or scope must change.

## Wrap Up

After acceptance, manifest only follow-ups created or fulfilled by the work:
update TODO, current wiki knowledge, required wiki index/log links, or the
governing document when the accepted design changed. Preserve historical
`wiki/sources/**` evidence and append corrections to history where appropriate.
Do not create bookkeeping merely to prove activity. State changed files,
validation, deviations, unresolved concerns, acceptance coverage,
discoveries, durable-learning suggestions, workflow friction, inspected scope,
and uninspected scope in the final packet.
