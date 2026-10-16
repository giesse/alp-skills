# Choosing and Combining the Skills

[Table of contents](../README.md) · Previous: [Getting Started](getting-started.md) · Next: [Running an ALP Workflow](running-alp-workflow.md)

## Choose according to the session's goal

If your goal includes producing or changing code, use `$run-alp-workflow`. It
guides the session through Brainstorm, Governing Documentation, Implementation,
and Wrap Up, with your approval before each transition. It requires
`$delegate-work`, which handles how work is assigned between the root agent and
workers.

Within Governing Documentation, use `$author-alp-book` for help developing the
Book. The workflow guides the session; the author skill helps with the writing
itself. I expect this to be the most common way to use the author skill.

## Use the author skill independently for writing

A session focused on writing may not need the complete workflow. For example,
you might be improving the wording of an existing chapter without expecting
code changes, or developing the Book for a new project before you are ready
for an AI tangle.

In those cases, `$author-alp-book` can help you ask the right questions, develop
drafts, and refine the explanation independently. Applicable repository
instructions still govern the work. Using the author skill does not itself
authorize implementation.

## Use the wiki skill to preserve useful knowledge

`$maintain-repository-wiki` will most often be useful during Wrap Up, when you
preserve lessons, findings, and unresolved follow-up for future sessions.

It can also be used independently. You might have a session devoted to
restructuring the wiki, reconciling accumulated notes, or researching a topic
and preserving the findings. Combine it with `$delegate-work` when you want
workers to help with that work.

The wiki preserves working knowledge. It does not replace the Book or become a
source of governing decisions.

## Use delegation with or without the full workflow

`$delegate-work` governs how the root agent and workers share work. It keeps
discussion, design, and material decisions with the human and root agent, while
workers carry out bounded assignments.

The full workflow requires this skill, but delegation can also support a
research, writing, or maintenance session independently. Using `$delegate-work`
alone does not require a Book or adoption of the four phases.

## Typical combinations

- **Develop or change a program:** `$run-alp-workflow` with its required
  `$delegate-work` companion; use `$author-alp-book` during Governing
  Documentation and `$maintain-repository-wiki` when preserving useful
  knowledge.
- **Write or refine Book chapters:** `$author-alp-book`, with `$delegate-work`
  when worker assistance is useful.
- **Research and preserve findings, or maintain the wiki:**
  `$maintain-repository-wiki`, with `$delegate-work` when worker assistance is
  useful.

Choose the combination that fits the session's goal. The individual skills
remain useful outside the full workflow, while applicable repository
instructions continue to govern the work.

---

[Table of contents](../README.md) · Previous: [Getting Started](getting-started.md) · Next: [Running an ALP Workflow](running-alp-workflow.md)
