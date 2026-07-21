# Authoring ALP Books

[ALP Skills Book](../README.md) · Previous:
[Delivery Workflow](delivery-workflow.md) · Next:
[Execution Contracts and Evidence](execution-contracts-and-evidence.md)

## The author is teaching, not filling out a form

A Full ALP Book should let a human reader understand why the system behaves as
it does and let a bounded tangler implement it without inventing material
design. Those are separate tests. A detailed checklist can still fail both if
it follows source-file order, hides its rationale, or leaves crucial choices to
the implementer.

The Book-authoring companion is used only during an approved Full ALP
Governing Documentation phase. It does not own workflow phases, implementation,
review, or wrap-up, and it is not activated merely because a tangler reads an
already approved Book.

## Build the chapter in reader order

1. **Find the boundary.** Reuse the chapter that already owns the behavior, or
   add one coherent chapter when a reader would otherwise mix unrelated ideas.
2. **Make an authoring map.** Identify purpose, rationale, unchanged behavior,
   ownership, interfaces, failures, compatibility, adversarial cases, and
   acceptance evidence.
3. **Teach before encoding.** Introduce the mental model before diagrams,
   tables, pseudocode, or literal algorithms that depend on it.
4. **Choose the least precise representation that removes material ambiguity.**
   Use prose for rationale, a diagram for relationships, a table for mappings,
   pseudocode for ordering and failures, and literal code only when its exact
   form is itself part of the behavior.
5. **Make the important behavior observable.** State what remains unchanged
   and name a credible acceptance oracle, including its limitation.

## What a tangler may and may not choose

A good Book leaves harmless choices open: local names, helper decomposition,
formatting, and equivalent library calls. It does not leave architecture,
ownership, interface behavior, persistence, compatibility, failure policy, a
material algorithm, or an acceptance oracle to guesswork.

If a tangler needs one of those decisions, the right response is not a stronger
model. Return to Governing Documentation and improve the Book.

## Preflight

Before a Book is handed to the workflow, check both perspectives:

| Reader question | Preflight question |
| --- | --- |
| Can I explain why this exists? | Does the chapter teach rationale and boundaries before mechanics? |
| Can I spot a risky interpretation? | Are normal, failure, compatibility, and adversarial paths explicit? |
| Can I trust the evidence? | Does every material behavior have an observable, honest oracle? |
| Can a tangler proceed without invention? | Are all material choices settled or visibly blocked? |

The authoring result is readiness for workflow preflight, not permission to
implement. A material change discovered later reopens Governing Documentation.

---

[ALP Skills Book](../README.md) · Previous:
[Delivery Workflow](delivery-workflow.md) · Next:
[Execution Contracts and Evidence](execution-contracts-and-evidence.md)
