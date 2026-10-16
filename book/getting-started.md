# Getting Started

[Table of contents](../README.md) · Previous: [Goals and Non-Goals](../GOALS.md) · Next: [Choosing and Combining the Skills](choosing-and-combining-skills.md)

## How to use the skills in this repository

> [!WARNING]
>
> This section describes the repository's current experimental use. Installation, compatibility, and the set of available skills may change before publication.

At present, only Codex is supported. The skills may be adaptable to other agent harnesses, but this repository does not yet provide or maintain an adaptation procedure. If you want to experiment, you can ask your agent to attempt a port to your preferred harness in a fork of this repository.

If you are using Codex, ask it to install the skills from this repository. At present, this installs four skills. They can be combined, but they have different scopes. `$run-alp-workflow` requires `$delegate-work`, so install both together when using the complete workflow. You can also use `$delegate-work` on its own for delegation guidance.

- `$delegate-work` — routes discussion, repository, and tool work between the root agent and workers, with bounded assignments and user authority.
- `$run-alp-workflow` — coordinates a complete session across four phases, with a root orchestrator and delegation when worthwhile. It requires `$delegate-work` and pauses for your approval before each phase transition. See [Running an ALP Workflow](running-alp-workflow.md).
- `$author-alp-book` — supports bounded Book work without requiring the complete workflow. See [Authoring an ALP Book](authoring-alp-books.md).
- `$maintain-repository-wiki` — preserves non-governing repository memory and can be used with or without ALP. See [Maintaining Repository Memory](maintaining-repository-memory.md).

See [Choosing and Combining the Skills](choosing-and-combining-skills.md) for more details.

## How to start a new repository using ALP

My best advice, if you're starting a new project and want to use ALP, is to start from a `GOALS.md` file with your goals for the project. You can have the AI help you refine it, but this should be what **you** want and don't want, not the AI's possibly mistaken interpretation of something you said.

Once you have `GOALS.md`, I suggest asking the AI to help you craft an `AGENTS.md` file for the project and brainstorming an initial table of contents (`README.md`). This order is deliberate: `GOALS.md` records human intent, `AGENTS.md` turns the project's collaboration constraints into instructions that agents will encounter, and `README.md` establishes the Book's reading path.

From then on, how you proceed depends on your project. You can write one chapter at a time with `$author-alp-book`. If you are starting from a vaguer goal, use `$run-alp-workflow` to refine it in Brainstorm and, when you choose to continue, guide the work through the remaining phases. The details depend greatly on the project's goals, its programming language or languages, and its other constraints.

## How to start using ALP in an existing project

Adopting ALP in an existing project depends on both the project and the
developer. Start by making the project's goals explicit, just as you would for
a new project.

A useful scope for the first part of the Book is a reasonably self-contained
module or subsystem. Write a coherent set of chapters that explains its
purpose, behavior, important decisions, and constraints. Existing code and
tests provide evidence about the system, but you still need to decide which
behavior is intended and which decisions should govern future work.

The aim is a Book complete enough that, in principle, an AI could recreate the
module while preserving its intended behavior and material decisions. This
does not mean that you should regenerate working code: doing so could introduce
regressions and other problems. It is a way to judge whether the Book explains
the program sufficiently to guide implementation.

This requires an initial investment. If you only need to fix a bug, writing
chapters for the surrounding module may be much more work than the fix itself.
I have written chapters that describe only a fix, but in my experience the
value of ALP is minimal in that case. A collection of such chapters can become
scattered notes without ever becoming a coherent, tangle-ready Book.

When you are not ready to write the Book, preserve what you learn in the
repository wiki and defer the chapters until you can give the module or
subsystem proper treatment. Record the problem, the reasoning behind the fix,
and anything future work will need to know.

Practical compromises will be necessary. Preserve useful knowledge throughout,
but do not force it into a premature Book that you will have to scrap and
rewrite. The wiki can hold that knowledge until you are ready to develop the
human-readable explanation.

## How to use the workflow for spec-driven development or some other approach other than ALP

The workflow and the repository wiki can also be useful if you prefer spec-driven development or another approach instead of literate programming. In the Governing Documentation phase, the specification becomes the source of material intent instead of an ALP Book chapter. You retain the focused phases, approval boundaries, governing-document discipline, and repository memory; what you give up is the ALP Book's requirement to teach the system through a reader-first narrative.

If you take only one principle from this project, make the goals explicit before work: define project-wide goals in a `GOALS.md` file (or, when short, in a clearly identified section of `AGENTS.md`), and define each session's goal using Brainstorm to clarify a vague prompt.

---

[Table of contents](../README.md) · Previous: [Goals and Non-Goals](../GOALS.md) · Next: [Choosing and Combining the Skills](choosing-and-combining-skills.md)
