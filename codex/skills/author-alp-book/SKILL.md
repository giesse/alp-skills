---
name: author-alp-book
description: Help a human author create, revise, structure, reconcile, or review an AI-assisted Literate Programming Book that is reader-first, tangle-ready, and reviewable without transferring ownership of intent to the AI. Use alone for bounded Book drafting, review, or reconciliation without imposing a full delivery workflow; use together with run-alp-workflow when authoring is part of phase-gated implementation work.
---

# Author an ALP Book

Help the human preserve the program's intent and reasoning in a coherent,
durable Book. Do not replace the human as author or decision-maker.

Write the Book in plain language. Prefer familiar words, keep specialized
terms when they make meaning clearer, and explain them briefly when needed.

## Respect the surrounding workflow

Follow the consuming repository's instructions. Surface conflicts instead of
resolving them silently.

Let separately applicable repository instructions or an invoked workflow
govern routing, delegation, authorization, and phase transitions. Do not
impose the complete ALP delivery workflow when this skill is used alone.

Do not treat invocation of this skill or approval of authoring work as
approval to implement.

## Keep the human at the center

Normally ask the human to write the first draft or a significant part of the
Book. Assist by:

- asking questions and exposing assumptions;
- researching the existing system or problem domain;
- suggesting alternatives and consequences;
- finding ambiguity, contradictions, and missing cases;
- reviewing structure, clarity, and completeness;
- improving wording; and
- preparing evidence-based material for the human to evaluate.

Draft most of a derivative governing document only when approved,
human-authored sources already settle the material policy, the user explicitly
authorizes the draft, and the user will review and steer it. Never turn
plausible prose into unapproved product, design, compatibility, security,
failure, or recovery policy.

Stop and return a material question to the user whenever the Book cannot be
completed without choosing intent.

## Inspect the local Book context

Before editing, perform only the preflight useful to the task:

- locate the Book's entry point and intended reading path;
- identify the chapter or document that already owns the subject;
- inspect relevant neighboring chapters, links, terminology, and repository
  evidence;
- distinguish what was inspected from what was not; and
- challenge applicable material boundaries such as failure and recovery,
  compatibility, concurrency or ordering, migration and rollback, data or
  security semantics, and acceptance limitations.

Do not force every topic into every Book. Use this preflight to find material
gaps and local integration constraints, not to manufacture checklist content.

## Identify the Book

Treat the Book as a durable, human-readable explanation of what the program
should do, why it should do it, and which decisions matter. It may span
multiple documents, but give it an intentional reading path that builds a
coherent mental model.

The AI tangle is the step in which an AI produces or changes the
implementation from the Book. A Book is tangle-ready when that step can
proceed without inventing material decisions.

Do not assume that every document belongs to the Book. Keep these distinctions:

- The Book teaches intent and design to human readers.
- Reference documentation optimizes facts for lookup.
- Operational instructions explain how to perform tasks.
- A repository wiki preserves working memory for agents.
- The implementation is the executable realization of the Book.

Supporting documents may form part of the Book when they help teach the
system, but names and file types do not make them literate.

## Structure for readers

Introduce concepts in the order that best helps a reader understand the
program, not merely in source-file or execution order.

Explain as applicable:

- the purpose and intended mental model;
- promised behavior and public interfaces;
- important decisions and their rationale;
- constraints and compatibility commitments;
- architecture, ownership, data, trust, privacy, and security boundaries;
- failure, retry, and recovery policy;
- algorithms whose details affect observable results; and
- boundaries where a seemingly harmless choice would be dangerous.

Prefer explanation over code-shaped pseudocode. Use code or literal algorithms
when they are the clearest representation of a material rule, not merely to
make implementation easier.

## Choose necessary precision

Use the least precise representation that removes material ambiguity.

Choose among intention, examples, prose, tables, diagrams, flowcharts,
pseudocode, literal algorithms, and source code according to what best teaches
the idea and constrains consequential choices.

Make a choice explicit when different interpretations could materially change
observable behavior, compatibility, architecture, data meaning, security,
recovery, acceptance semantics, or future decisions. Leave harmless choices
such as local names or private helper placement to the tangle.

Judge materiality by consequences, not by whether a detail appears high-level
or low-level.

## Work with an existing system

Treat repository evidence as evidence, not automatic governing intent:

- code shows that a mechanism exists;
- tests show behavior someone chose to assert;
- runtime observations show what happened in particular conditions; and
- comments and old documents provide explanations of uncertain authority and
  freshness.

Classify material behavior as:

- **intended**: preserve it as approved intent;
- **compatibility-constrained**: preserve or change it only with its real
  commitments understood;
- **incidental**: do not canonize it without a reason;
- **contradictory**: identify its conflict with approved intent; or
- **unresolved**: return the decision to the human.

Keep observations about the present distinct from decisions about the future.
Do not canonize an accident or erase a compatibility commitment silently.

## Apply the three Book tests

Evaluate each quality independently.

### Readable

Confirm that a human can build the intended mental model without
reverse-engineering the implementation. Introduce ideas in reader order,
explain why they matter, and distinguish central concepts from supporting
detail.

### Tangle-ready

Confirm that an implementation agent can proceed without inventing material
decisions. Do not require every line or low-level choice to be prescribed.

### Reviewable

Expose rationale, assumptions, constraints, compatibility commitments, and
dangerous boundaries so a reviewer can challenge them without reconstructing
intent from code.

Do not let success on one test stand in for the others.

## Integrate edits locally

When an approved edit adds, moves, removes, or materially repositions Book
content, update the applicable README, table of contents, index,
related-reading entry, or neighboring navigation. Inspect adjacent entries
afterward.

Do not broaden the task into a Book reorganization. Surface a larger navigation
problem as a separate repository concern.

## Prepare the implementation boundary

When implementation is contemplated, identify the decisive acceptance checks
that express what the result must prove. Keep their design independent of the
implementation agent and obtain user approval before implementation. Use
non-automated or static checks when they provide the right evidence; do not
invent a fake test harness.

Before finalizing the checks, perform a proportionate coverage pass. Confirm
that each approved material criterion and important boundary has an observable
check, or state the remaining evidence limitation. Use the simplest
representation that makes coverage clear; do not require a matrix,
traceability document, or separate artifact unless it materially helps.

Make clear which choices are settled policy and which ordinary implementation
choices remain open. If the tangle later exposes a material gap or faulty
critical check, return to the Book instead of letting the implementer decide.

When reconciling with an existing implementation or completing implementation
work, require semantic alignment on material behavior and decisions. Do not
require passage-to-line traceability.

End bounded authoring with the Book ready for user review. When an applicable
workflow governs phase transitions, do not move to implementation without its
required approval.
