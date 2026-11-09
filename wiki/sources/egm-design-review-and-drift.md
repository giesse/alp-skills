# Elephant-Goldfish Model — Design Review and Drift Evidence

Status: Deferred external evidence; not an adopted process or tool.

Reviewed 2026-11-09 from the mutable upstream `main` documentation linked by
[egm.dev](https://egm.dev/), principally the [repository README](https://github.com/google/elephant-goldfish-model/blob/main/README.md),
[workflow guide](https://github.com/google/elephant-goldfish-model/blob/main/docs/getting_started.md),
[review skill](https://github.com/google/elephant-goldfish-model/blob/main/skills/egm-review/SKILL.md),
[resolution skill](https://github.com/google/elephant-goldfish-model/blob/main/skills/egm-resolve/SKILL.md),
and [drift-report skill](https://github.com/google/elephant-goldfish-model/blob/main/skills/egm-drift-report/SKILL.md).
The reviewed pages were not pinned to a commit; upstream content may change.

## What the documentation describes

EGM separates a context-rich drafting role (“Elephant”) from fresh-context
reviewers (“Goldfish”). Reviewers read the draft and selected source material,
without the earlier conversation. The README says this requires real fresh
subagents and does not replace tests or human judgment.

The design review skill describes five stages: a broad review, a comprehension
check that paraphrases the document, design critique, another broad review,
and an implementation-readiness check. It writes reports and provides
checkpoints. Its resolution skill sorts findings into contest, escalate,
propose-fix, or decline; a contest needs evidence the reviewer could inspect,
and proposed edits pass through a user decision. Its drift skill compares
design documents and referenced source with the current code and reports
divergences. The workflow guide leaves the choice to update the document or
code to a human.

## Questions for comparison with ALP

These are candidates for later evaluation, not recommendations:

- Would fresh-context comprehension and design review add useful evidence
  alongside ALP's independently authored acceptance checks? What should
  reviewers receive as context, and what can they reliably assess?
- Would evidence-backed finding disposition help resolve review comments
  without letting a reviewer redefine intent?
- Could drift reporting help keep an approved Book and implementation aligned,
  and what human decision should follow a reported divergence?
- What level of staged review, reports, and checkpoints is justified by the
  risk, given the repository's preference for simplicity?

No EGM workflow was run and no claim about effectiveness was independently
verified. These notes preserve what the upstream documentation says; they do
not establish that its process should be adopted or alter ALP policy.
