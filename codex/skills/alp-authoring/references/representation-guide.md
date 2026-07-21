# Representation Guide

Choose the least representation that removes material ambiguity and teaches the
concept at the reader's current point in the chapter.

## Start with the Reader's Question

| Reader question | Useful representation |
| --- | --- |
| Why does this exist? | Explanatory prose and a decision comparison |
| What owns what? | Responsibility table or component diagram |
| What happens in what order? | Event sequence, numbered algorithm, or pseudocode |
| How does state change? | State machine or transition table |
| What maps exactly to what? | Table, schema, or worked example |
| What may fail and then what? | Failure matrix plus pseudocode |
| What must callers provide or receive? | Contract, schema, and boundary examples |
| What proves acceptance? | Criterion-to-oracle table with limitations |

Do not add a diagram or pseudocode merely to make the chapter look substantial.
Change representation when prose forces the reader to hold too many
relationships or branches in working memory.

## Teach Before Encoding

Introduce the mental model and rationale before a dense representation. Define
terms and ownership so the reader knows what the table, diagram, or algorithm
means.

Order information for learning rather than compiler execution. A chapter may
teach a policy before showing the low-level calls that enforce it; the tangle
can restore implementation order later.

Hide or defer details that do not help the current explanation. This is not
permission to omit material behavior: place exact semantics where the reader
can understand why they matter.

## Prefer Semantic Exactness

Specify exact conditions, state changes, invariants, and observable outcomes
without prescribing incidental syntax.

For example:

- explain why and when a database record changes, which fields are preserved,
  and how concurrency is handled;
- omit the exact SDK call unless its expression syntax changes semantics;
- name the timeout, retry, and cleanup policy rather than copying a library
  invocation; and
- use literal protocol or query syntax when compatibility depends on it.

Unfamiliar implementation syntax can make a reviewer skim and miss subtly
wrong logic. Use literal code only when the code form itself is part of the
governing behavior.

Distinguish a mathematical definition from a prescribed evaluation algorithm
when resource behavior is material or an unbounded intermediate is visibly
dangerous. State a bounded algorithm when the evaluation strategy is part of
the approved behavior; otherwise preserve the exact result and leave safe,
equivalent expression choices to implementation and review.

## Select the Right Precision

Use prose for intent, rationale, tradeoffs, and unchanged behavior.

Use a diagram for three or more relationships, ownership boundaries, state,
event flow, or a sequence that prose makes difficult to follow.

Use a table for mappings, configuration variants, compatibility cases,
decisions, failure responses, or oracle coverage.

Use examples for boundary semantics and user-visible transformations. Include
normal, adversarial, and ambiguous cases when they reveal different behavior.

Use schemas or contracts for fields, types, preconditions, postconditions,
side effects, and failure categories.

Use pseudocode for branching, ordering, retry, timeout, cleanup, idempotency,
and partial failure. Keep it readable and semantic; do not imitate source syntax
unless necessary.

Use a literal algorithm or readable code when multiple valid implementations
would behave materially differently and prose or pseudocode cannot select the
approved one.

## Review the Representation

For each structured element, ask:

- What ambiguity does this remove?
- Has the chapter already taught the concepts it uses?
- Does it expose rationale or only mechanics?
- Is any visible precision incidental rather than material?
- Can a reviewer spot subtly wrong behavior without translating unfamiliar
  syntax?
- Could the tangler choose a materially different behavior while claiming
  conformance?

Remove or simplify a representation that adds cognitive load without closing a
material choice.

A dedicated ALP notation or language may eventually make some representations
more expressive. Do not invent one inside an ordinary chapter or make version 1
of the authoring skill depend on it.
