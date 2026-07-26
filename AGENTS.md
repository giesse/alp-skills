# Working in this repository

## Authority

`GOALS.md` is the constitution of this project. `RULES.md` translates it into
operational policy. They take precedence over this file and the skills derived
from them. When developing an artifact that governs ALP, also preserve the
applicable meaning of `ALP.md`.

The user owns the goal, scope, material decisions, governing documentation,
phase transitions, exceptions, and final acceptance. Surface conflicts,
ambiguity, missing policy, and material tradeoffs instead of resolving them
silently.

## Obtain approval before work

The root agent is Sol. Current relative Codex credit costs are Luna 1x, Terra
2.5x, and Sol 5x.

At the start of each root-agent turn:

1. Respond to the request by explaining the work needed and recommending what,
   if anything, to delegate.
2. Do not read files, use tools, change artifacts, perform the proposed work,
   or delegate before the user approves the route.
3. Let the user decide what Sol should do and what a worker should do.
4. Treat approval as authorization only for the root agent's next assistant
   turn. Reset to this protocol on the following turn.

Discussion and Brainstorm are Sol's work and must not be delegated. Discuss
from available context without separate approval, but obtain approval before
using files or tools.

A delegation recommendation must state:

- the model and bounded assignment;
- the expected end-to-end benefit after briefing, coordination, review, user
  attention, and delay;
- the evidence or output the worker must return;
- the judgment retained by the user and Sol; and
- the conditions under which the worker must stop.

Do not delegate unless the expected benefit exceeds its total cost. A worker
must stay within its assignment, return material ambiguity, and not delegate
again unless the user explicitly approves further delegation. Propose parallel
work only for genuinely independent, non-overlapping tasks whose results are
all needed.

## Keep work focused and phased

Keep one session focused on one goal. Record and defer unrelated work. Do not
silently expand scope.

Use the normal phases: Brainstorm, Governing Documentation, Implementation, and
Wrap Up. Obtain explicit user approval before moving to another phase. The user
may waive a phase when the normal sequence does not fit, but state the reason.
Do not treat approval of one phase as approval of another.

## Work from the repository's sources

Once substantive repository work is approved, consult:

- `GOALS.md` and `RULES.md`;
- `ALP.md` when the artifact concerns ALP; and
- `wiki/index.md` for durable repository knowledge.

If `wiki/index.md` is absent, surface that workflow gap rather than inventing
its contents or silently ignoring the requirement.

Keep the user at the center of Governing Documentation. Normally the user
writes the first draft or a significant part. AI may research, suggest,
review, clarify, and draft derivative text from already approved policy when
explicitly authorized, but it must not invent intent.

Define and approve decisive acceptance checks before Implementation. Keep
their authorship independent of the implementer. Before finalizing them, make
a proportionate coverage pass against the approved material criteria and
important boundaries; identify any remaining evidence limitation without
requiring a separate artifact unless it materially helps. Prefer test-first
implementation when executable critical tests and a meaningful failing
baseline fit the work; do not manufacture one when they do not. If
implementation exposes a material ambiguity, missing case, mistaken
assumption, or faulty critical check, stop and return to Governing
Documentation.

## Maintain derived artifacts

This repository is the canonical source of the skills under `codex/skills/`.
Installed copies are deployment outputs, not independent policy sources.

Keep this `AGENTS.md` specific to developing this repository. Make distributable
skills portable and self-contained; do not assume a consuming repository has
these source documents or already enforces this workflow. A consuming
repository's instructions retain authority within that repository, so surface
conflicts to the user.

Derived artifacts may condense or specialize the governing rules, but must not
contradict them, omit behavior required within their scope, or add policy.
Prefer the smallest useful artifact set and avoid ceremony. Review every
derived artifact against `GOALS.md` and `RULES.md`, and also against `ALP.md`
when it governs ALP work.
