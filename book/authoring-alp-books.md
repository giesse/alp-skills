# Authoring an ALP Book

[Table of contents](../README.md) · Previous: [Running an ALP Workflow](running-alp-workflow.md) · Next: [Maintaining Repository Memory](maintaining-repository-memory.md)

## Finding the Book's structure

A skeleton can make a Book easier to start. A tentative table of contents gives
you places to develop ideas and helps you notice subjects that need attention.
I have often started this way, but the best approach depends on the project.

On a fresh project, it may be easier to begin explaining the central ideas and
let the structure emerge. As the purpose, behavior, and design become clearer,
you can arrange that material into chapters.

Either approach leaves room for revision. An early skeleton can change as you
understand the program better; an emerging explanation can gradually acquire a
deliberate reading path.

The eventual order should help a human understand the program. Think about what
the reader needs to know before each new idea makes sense. That may lead to a
different arrangement from the source files or the order in which the program
executes.

## Developing the chapters

I tend to develop one chapter at a time. Keeping one subject in focus helps me
work through its explanation, resolve important questions, and refine the
writing with AI assistance.

This is a preference, rather than a required sequence. Some projects may
benefit from a rough pass across several chapters while their relationships
become clearer. The approach depends on the project and how the author thinks.

A chapter will often expose something that belongs elsewhere in the Book. You
can record that connection or open question and return to it when developing
the relevant chapter. The reading path and the order in which you write do not
have to be identical.

## Working with AI as a writing partner

Human authorship does not mean writing alone or typing every word yourself. It
means owning what the Book says: its purpose, reasoning, and important
decisions. Normally, you write the first draft or a significant part of the
material, with whatever assistance helps you express it clearly.

You do not need to begin with finished prose. One useful approach is to have
the AI ask focused questions, answer in your own words, and then review
passages it proposes from those answers. You can correct the substance, change
the emphasis, and refine the wording together. Working on one manageable piece
at a time can make a difficult-looking chapter easier to approach.

This is how much of this Book has been developed. The questions help me
discover what I want to explain; the drafts give me something concrete to
respond to. Sometimes a draft reveals that I have not yet settled a decision,
which becomes the next subject of discussion.

AI can also research, suggest alternatives, and challenge the explanation.
Its findings help inform the writing, but a plausible suggestion still needs
the author's judgment. An unresolved decision should remain visible until the
human settles it.

`$author-alp-book` supports this collaboration, either independently or within
the Governing Documentation phase of `$run-alp-workflow`. Approval of writing
work does not itself authorize implementation.

## Choosing how much to specify

When I began experimenting with ALP, I needed to specify a great deal to get
reliable results from the agents I was using. The Book contained most of the
code, with omissions where the details were unimportant or where I felt
comfortable leaving them to the AI. In that respect, it was close to
traditional literate programming.

As agents have become more capable, I have been able to leave more of the
implementation open. The resulting Books can resemble detailed specifications
more closely. But I still prefer to settle important choices in the
documentation: I would rather review their explanation before implementation
than discover them in generated code afterward.

This affects how much detail I write. A broad statement of intent may be
sufficient for some parts of a program. Elsewhere, I may want an explicit
algorithm, examples, or source code so that I can understand and approve
exactly what is being proposed. Code belongs in the Book when it helps explain
and settle an important choice.

The appropriate level of detail depends on the program, the consequences of
getting something wrong, and how much judgment the author is comfortable
assigning to the AI. More capable agents may make higher-level descriptions
increasingly practical. For now, my preference is to keep more of the design
explicit.

Through these changes, the Book should continue to teach the program: its
purpose, reasoning, behavior, and constraints. Whatever form expresses a
decision, a human reader should be able to understand and challenge it. The
generated implementation still needs appropriate verification.

## Reviewing and revising the Book

Developing a chapter involves working closely with individual ideas. Reviewing
it means stepping back to see whether those ideas form an explanation a reader
can follow. A chapter can seem clear in isolation while depending on concepts
the Book has not introduced yet.

The three qualities described in [AI-Assisted Literate Programming](../ALP.md)
—readable, tangle-ready, and reviewable—give us different ways to examine the
writing.

For readability, consider what a human can understand from the explanation
itself. Does the reading order help them build a mental model? Can they
understand why the program takes this shape?

For tangle-readiness, consider which decisions an implementer would still have
to make. Concrete examples and acceptance checks can expose gaps that fluent
prose conceals. The Book needs to settle the material decisions within the
scope it covers; ordinary implementation choices can remain open.

For reviewability, consider whether someone can challenge the reasoning.
Important assumptions, constraints, and consequences need to be visible. A
precise description of what to build may still leave the reader unable to
judge why it should be built that way.

AI can help examine all three qualities, but its findings remain material for
the human author to evaluate. Success on one does not establish the others.

The Book will also change as the program develops. Implementation may expose a
missing decision, or later work may change an earlier one. Revising the
explanation preserves the reasoning behind the accepted software. Material
changes need to leave the Book and implementation aligned.

Changes to the chapter structure also affect the reader's path. Keeping the
table of contents, neighboring links, and related explanations consistent
helps the Book remain coherent as it grows.

---

[Table of contents](../README.md) · Previous: [Running an ALP Workflow](running-alp-workflow.md) · Next: [Maintaining Repository Memory](maintaining-repository-memory.md)
