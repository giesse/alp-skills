# AI-Assisted Literate Programming

[Table of contents](README.md) · Previous: _to be assigned_ · Next: _to be
assigned_

AI-assisted Literate Programming (ALP) is a method in which a human authors a
reader-first **Book** that explains what a program should do, why it should do
it, and which decisions matter. An AI uses the Book to produce the
implementation through an **AI tangle**.

The Book states important decisions with the precision they need while leaving
genuinely mechanical details to the AI. The AI may exercise implementation
judgment, but it must not invent unstated policy. When implementation exposes
an ambiguity, missing case, or decision that matters, that decision returns to
the Book.

This chapter defines ALP itself. The phases, approval rules, tests, delegation,
and other practices used to deliver work are supporting workflow. They are
governed separately by [Goals and Non-Goals](GOALS.md) and the other workflow
documentation.

## The problem ALP is trying to solve

An AI can produce code very quickly. That is useful, but it also makes it easy
to lose the reason a system behaves as it does. A later human or agent may see
source files and tests but still have to guess which details are intentional,
which are accidents, and why one choice was made instead of another. The code
becomes the only story left.

ALP preserves a human-facing explanation of the program. The Book records the
outcome we want, the reasoning behind it, the constraints that shape it, and
the behavior that must not change. The implementation realizes that
explanation as working software.

This does not make code disposable or require the Book to imitate code. The
Book should make a careful reader understand the program substantially more
easily than reading its implementation alone. It should also be precise enough
to keep material decisions from being made silently during implementation.

## Its literate-programming heritage

Literate programming begins with the idea that a program should be written for
human understanding. Concepts should be introduced in the order that best
helps the reader build a correct mental model, rather than only in the order
required by a compiler or interpreter.

Traditional systems such as WEB and CWEB combine prose with the complete source
of the program. They can then **weave** a human-readable document and
**tangle** compilable source code. These are mechanical transformations: the
source already exists in a precise form inside the literate program. Donald
Knuth's [overview of literate
programming](https://cs.stanford.edu/~knuth/lp.html) and the
[CWEB page](https://cs.stanford.edu/~knuth/cweb.html) describe this tradition.

ALP keeps the reader-first Book but changes the tangle. The Book does not need
to contain every line of source code. It can use whichever representation best
communicates each idea, and an AI can interpret that explanation in the
context of the repository to produce an implementation.

The result is not merely an unstructured prompt with more prose. The Book is a
durable work written to teach human readers and to preserve the decisions that
govern the program.

## The Book

The **Book** is a coherent, durable explanation intended for humans to read. It
need not be one physical file or a monolithic manual. It may be divided into
chapters, but it has an intentional reading path that builds the reader's
understanding of the program.

A good Book explains:

- what the program or feature is for;
- how a reader should think about it;
- the behavior it promises;
- why its important decisions were made;
- the constraints and compatibility requirements that shape it; and
- the boundaries where a seemingly harmless choice could be dangerous.

The Book is not required to contain every fact that might be useful when
working on the repository. Reference documentation can remain optimized for
lookup. API references can enumerate interfaces. Operational instructions can
explain how to perform a task. These artifacts may support or form part of the
Book when they help teach the system, but none automatically becomes literate
merely because it is documentation.

In this project, the Book is a collection of Markdown chapters.
[`README.md`](README.md) introduces the project and provides the table of
contents. Each chapter links back to the table of contents and to the previous
and next chapters so that the Book can be read in sequence.

The repository wiki has a different audience and purpose. The Book is written
for humans; the wiki is working memory for LLMs. Information found in the wiki
may help an agent research or maintain the Book, but the wiki does not replace
the Book and cannot silently override it.

## Human authorship and AI assistance

The human remains the author and decision-maker. This does not mean that the
human must type every word without help. It means that the human owns the
explanation, controls its material decisions, and decides what the Book is
trying to teach.

AI can assist the author by:

- asking questions and exposing assumptions;
- researching the existing system or the problem domain;
- suggesting alternatives and consequences;
- identifying ambiguity, contradictions, and missing cases;
- reviewing structure, clarity, and completeness;
- helping improve wording; and
- preparing evidence-based material for the author to evaluate.

The amount of assistance can vary. What must not change is the ownership of
intent. The AI does not become the author of product, design, compatibility, or
failure policy merely because it can produce plausible prose or code.

## Choosing the necessary precision

The central authoring principle is:

> Use the least precise representation that removes material ambiguity.

The Book may use a short intention, examples, prose, tables, diagrams,
flowcharts, pseudocode, a literal algorithm, or source code. Greater precision
is not automatically better. The author should choose the form that best
communicates the idea to a reader while constraining the decisions for which a
wrong choice would matter.

Material decisions often include:

- architecture and ownership boundaries;
- public behavior and interfaces;
- data meaning and compatibility requirements;
- trust, privacy, and security boundaries;
- failure, retry, and recovery policy;
- algorithms whose details affect observable results; and
- the semantics by which the result will be accepted.

Other choices may be harmless implementation details: a local variable name,
the placement of a private helper, or another choice that does not change a
contract, important quality, or future decision. These can usually remain open
to the tangle.

The distinction depends on consequences, not apparent level. A low-level detail
can encode important policy, while a large amount of code can be routine once
the governing decisions are clear.

Code-shaped pseudocode is not the goal. It can make a Book harder to read while
still hiding the reason the code takes that shape. Literal detail is useful
when the literal detail is itself the clearest expression of a material
algorithm or constraint, not merely because it makes implementation easier.

## The three tests of a good Book

A good Book is **readable**, **tangle-ready**, and **reviewable**. These are
separate tests.

### Readable

A human reader can build the intended mental model without reconstructing it
from the implementation. The Book introduces ideas in reader order, explains
why they matter, and distinguishes central concepts from supporting detail.

### Tangle-ready

An implementation agent can produce the program without inventing material
decisions. The Book need not prescribe every line, but it must remove ambiguity
where different interpretations would produce meaningfully different results.

### Reviewable

A reviewer can inspect the rationale, assumptions, constraints, and dangerous
boundaries directly. The Book makes important choices visible enough to
challenge without requiring the reviewer to reverse-engineer intent from code.

A document can succeed at one test and fail another. Pleasant explanatory prose
may be too ambiguous to tangle. A precise specification may enable code
generation without teaching the system. Detailed pseudocode may produce an
implementation while leaving the rationale and dangerous boundaries difficult
to review.

## The AI tangle

An **AI tangle** is the process by which an AI interprets the Book in the
context of the repository and produces or changes the implementation.

Unlike a traditional mechanical tangle, an AI tangle is contextual and
nondeterministic. It may consider existing code, tests, configuration,
interfaces, conventions, and tool output in addition to the Book. Different
tangles can produce different implementations that all satisfy the same
governing explanation.

This flexibility is useful, but it creates a boundary that must remain clear.
The AI may decide how to express a settled decision in code. It may choose
harmless details and adapt the implementation to the repository. It may not
decide what an ambiguous requirement ought to mean merely because stopping is
inconvenient.

Implementation is also a test of the Book. If the tangle cannot proceed without
choosing material behavior, this reveals that the Book is incomplete or
unclear. The answer is to return the decision to the human author and improve
the Book, then continue the tangle from the clarified explanation.

The output of a tangle is ordinary software. Its AI-assisted origin does not
make it correct. It must still fit the repository and be verified with the
appropriate tests, review, static analysis, runtime evidence, or other
acceptance checks. The workflow defines how that evidence is chosen and who
owns it.

## ALP in an existing system

In a new program, the Book can state intent before an implementation exists. In
an existing system, the repository contains evidence that must be understood
without automatically being treated as intent.

Code proves that a mechanism exists. Tests show behavior that someone chose to
assert. Runtime observations show what happened under particular conditions.
Comments and documentation record earlier explanations with varying degrees of
authority and freshness. All of these can be valuable evidence, but none proves
by itself that the current behavior is what the system should continue to do.

When reconciling an existing system with its Book, behavior may be:

- **intended:** it expresses a decision we want to preserve;
- **compatibility-constrained:** it may not be ideal, but changing it would
  break a promise or dependency;
- **incidental:** it is an implementation detail with no reason to govern
  future work;
- **contradictory:** it conflicts with the intended behavior; or
- **unresolved:** the evidence is insufficient and a human decision is still
  needed.

The Book must distinguish observations about the present from decisions about
the future. It should not canonize an accident merely because the code already
contains it. Conversely, it should not erase inconvenient behavior without
recognizing real compatibility commitments.

## Two durable representations

The Book and the implementation are two durable representations of the
program:

- The Book is the human-readable representation of its intent and design.
- The implementation is the executable realization accepted for the
  repository.

They should remain aligned, but alignment does not mean duplication. The Book
does not need to describe every file, function, or line. The implementation
does not need a one-to-one traceability link for every passage in the Book.
Such mappings can create another structure that must be maintained and can
drift.

Alignment is semantic: material behavior and decisions in the implementation
must agree with the Book. When a material change is accepted, both
representations must tell the same story before the work is complete.

The implementation remains durable even though it can be produced through an
AI tangle. A tangle depends on repository context, model behavior, tools, time,
and cost. It is not guaranteed to reproduce identical code later. Committing
the accepted implementation preserves the executable realization that was
actually reviewed and verified.

The Book remains durable because code alone cannot preserve the full reason for
that realization. A conflict between the two exposes work to reconcile them; it
does not give an AI authority to decide which intent is correct.

## What ALP is not

ALP is not merely:

- writing a long prompt and asking an AI to generate code;
- maintaining reference documentation;
- storing agent memory in a repository wiki;
- translating an existing program into prose line by line;
- prescribing a universal pseudocode language;
- treating generated code as a disposable byproduct; or
- running an AI generator as part of every ordinary software build.

Brainstorming, workflow phases, critical tests, review practices, delegation,
model routing, and durable agent memory can all support ALP. They help people
and agents apply the method carefully, but they are not what defines it.

The essential promise is simpler: a human writes a Book that teaches the
program and preserves its material decisions; an AI tangles that Book into
ordinary software without silently taking ownership of intent.

---

[Table of contents](README.md) · Previous: _to be assigned_ · Next: _to be
assigned_
