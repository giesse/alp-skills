# Execution Contracts and Evidence

[ALP Skills Book](../README.md) · Previous:
[Authoring ALP Books](authoring-alp-books.md) · Next: [EC Linter](ec-linter.md)

## When implementation leaves the native conversation

The governing Book or specification remains the source of intent. A complete,
revisioned Execution Contract (EC) is the travelling companion for a manual or
external handoff to Antigravity using Gemini Flash. The
external implementer cannot be assumed to know the Codex conversation, local
phase history, or unstated test meaning. The EC makes that context portable
without becoming a second design authority.

Native Codex workers use the smaller packet governed by
[Native Worker Delegation](worker-dispatch.md). An EC is not a universal worker
envelope, and a native packet is not sufficient for the external route. Both
routes still obey the same approved governing source, closed file and task
boundary, oracle integrity, conflict-stop rule, evidence obligation, and
root/user acceptance authority.

## A complete revision

An EC carries a unique contract identity, a positive revision, its supported
protocol version, task, and governing document. Under EC protocol v1, the
legacy header `ALP chapter` remains accepted in place of `Governing document`
where existing governed material uses it.

The body contains:

| Item | Meaning |
| --- | --- |
| Decision | Approved behavior the implementer must not reopen. |
| Invariant | Behavior or compatibility that must remain true, including independently owned test semantics when practical. |
| Acceptance and validation | Observable completion criteria and the named oracle or check covering each one. |
| Out of scope | Explicit non-goals and a closed repository file boundary. |
| Question | An unresolved point with owner, required evidence, and a resolve-before boundary. |

Items use unique `D`, `I`, `A`, `V`, `O`, and optional `Q` identifiers.
Validation items explicitly name the acceptance items they cover. Every
revision includes both an out-of-scope statement and the repository file
boundary; test semantics are explicit whenever tests are in scope.

Questions are optional as a section: omit them entirely when the revision has
none. When present, every question is complete and must be resolved by its
named boundary. A change to any approved contract content produces a complete,
incremented replacement revision. Neither the root, worker, nor external tool
quietly patches a dispatched revision.

## What the contract protects

The contract asks an implementer to report a conflict instead of silently
expanding scope. An additional repository file, changed critical-test meaning,
or contradiction between the Book and task is therefore a stop condition, not
an invitation to improvise.

Critical test or fixture semantics belong to the workflow owner whenever that
independence is practical. An external implementer may add compatible coverage,
and may make a named existing-test update only when the approved EC authorizes
it. Weakening expected behavior, altering independently owned semantics, or
changing a critical oracle requires a replacement revision and approval before
implementation continues.

Antigravity plans, task lists, and similar planning artifacts are control-plane
artifacts, not repository edits, so they do not consume the repository file
boundary. That exception does not authorize an extra source file, test change,
generated repository artifact, or broader implementation action.

## From handoff to authorization

The manual route follows a visible sequence:

1. A bounded worker prepares the complete EC from the approved governing
   source. Deterministic EC lint and semantic preflight both pass before handoff.
2. The external implementer may inspect and return a read-only plan before
   implementation authorization. It must not edit files or run implementation
   validation during that planning step.
3. The implementer explicitly acknowledges the decisions, invariants,
   acceptance and oracle semantics, file boundary, test-update limits, and any
   blocking questions. A contradiction, missing authority, extra required file,
   or changed oracle meaning is reported and stops the handoff.
4. For Antigravity, the initial plan goes to one separate Terra worker for a
   conformance review against the EC. At most one focused correction follows
   unless a concrete blocker remains; the Terra worker is a reviewer and has
   no phase authority.
5. Only after the user authorizes implementation does the external implementer
   edit the approved boundary and run the approved validation.

This is a manual transfer: ALP does not pretend that Codex controls another
tool's transport, context, or process. The revisioned artifact and explicit
user authorization are the control boundary.

## Mechanical checks and human judgment

The EC linter is a small deterministic check. Its detailed contract is in the
next chapter. It verifies structure; it does not decide whether a design is
wise, an oracle is strong, or a production action is safe.

That separation is intentional. Mechanical checks catch omissions cheaply and
consistently. Semantic preflight is delegated to a suitable fresh worker; Sol
and the user retain phase approval and acceptance judgment through compact
reports without doing repository work themselves.

## Evidence after implementation

A compact completion packet records the EC identity and revision, changed
files, validation evidence, deviations, unresolved concerns, acceptance
coverage, repository discoveries, durable-learning suggestions, and concrete
workflow friction. It distinguishes inspected and uninspected scope and never
treats successful command execution alone as acceptance.

A fresh reviewer first compares the governing document or EC, final diff, and
independent evidence before reading an implementation walkthrough. This makes
the review a check against intent, not a confirmation of the implementer's
story. Sol and the user reconcile that compact review and retain the final
authority to defer a finding or accept the result.

---

[ALP Skills Book](../README.md) · Previous:
[Authoring ALP Books](authoring-alp-books.md) · Next: [EC Linter](ec-linter.md)
