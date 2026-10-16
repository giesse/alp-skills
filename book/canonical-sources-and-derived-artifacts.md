# Canonical Sources and Derived Artifacts

[Table of contents](../README.md) · Previous: [Maintaining Repository Memory](maintaining-repository-memory.md) · Next: [Installation, Updating, and Validation](installation-updating-and-validation.md)

## Why this repository looks different

In a typical ALP project, the Book explains the program and governs the source
code produced from it. ALP does not prescribe a particular hierarchy of files
or require a separate `RULES.md`.

This repository has an unusual purpose: it develops instructions and reusable
skills for agents. Here, `GOALS.md` establishes intent and priorities,
`RULES.md` translates them into operational policy, and `AGENTS.md` and the
skills carry that policy into agent instructions. `ALP.md` defines the method
those instructions must preserve.

Most of the remaining Book explains the approach, its reasoning, and how to
use the skills. These chapters help human readers understand the project,
while the detailed governing policy is concentrated in `GOALS.md` and
`RULES.md`.

This arrangement serves this repository's needs. It is not a template that
every ALP project should reproduce. In another project, the relevant behavior,
design, constraints, and reasoning would normally be developed throughout the
Book's chapters and realized in source code.

I do recommend starting by making goals and non-goals explicit. A `GOALS.md`
file is a useful way to do that, even when the rest of the Book takes a very
different shape.

## What canonical and derived mean

A **derived artifact** adapts established guidance for a particular purpose.
It may condense or specialize that guidance, while preserving its meaning.
Rewording a rule for a skill must not silently change the policy.

A **canonical source** is the maintained source of an artifact. For the skills,
that source lives under `codex/skills/`. Installed copies are deployment
outputs.

These terms describe different relationships. A skill file can be the
canonical source for the installed skill while its policy is derived from the
governing documents. Maintaining the source file does not give it authority
to override those documents.

This separation helps us review changes where their meaning is established,
then carry that meaning consistently into the instructions agents actually
use.

## Keeping the guidance consistent

A policy change begins in the governing documentation, with human approval.
The affected agent instructions can then be revised to express that decision
within their own scope.

A wording improvement may need no policy change. The important question is
whether the meaning stays the same. A shorter instruction can accidentally
remove a required boundary; a more detailed instruction can introduce a rule
nobody approved. Reviewing derived instructions against `GOALS.md`,
`RULES.md`, and, where applicable, `ALP.md` helps expose those differences.

Changes to skills belong in their canonical sources under `codex/skills/`.
Editing an installed copy alone would leave the repository's maintained source
unchanged and create competing versions. Installation carries the reviewed
source into the environment where it will be used.

## Making skills usable elsewhere

Someone using these skills in another repository may never read this Book or
have access to our governing documents. The skills therefore need to carry
the instructions required for their work.

A skill can share responsibility with a named required companion. It must
explain that the companion needs to be loaded and what happens if it is
missing. Optional companions need guidance for proceeding without them.
Together, a skill and its required companions must provide enough instruction
to perform the work without relying on this repository being present.

This repository's `AGENTS.md` serves a different purpose: it governs developing
and maintaining this project. It is not the mechanism by which other
repositories adopt the skills.

A consuming repository retains authority over its own work. Its instructions
may adapt how the skills are used, and material conflicts need to be surfaced
to the human. Making a skill portable includes respecting that local
authority.

---

[Table of contents](../README.md) · Previous: [Maintaining Repository Memory](maintaining-repository-memory.md) · Next: [Installation, Updating, and Validation](installation-updating-and-validation.md)
