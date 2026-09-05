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

## Route work and require approval for consequential decisions

The root agent is GPT-5.6 Sol for discussion, orchestration, design,
brainstorming, policy judgment, and synthesis. Briefly announce the work and
its route before proceeding. Default repository and tool work to one GPT-5.6
Luna worker, even when it appears small; clear, bounded Luna delegation may
proceed after that announcement without advance approval. Prefer one Luna
worker when practical, and use additional workers only for independently
worthwhile assignments. Parallel tasks must be independent, non-overlapping,
and all needed.

Sol may work directly when the user explicitly assigns the work to Sol or when
Sol must inspect exact authoritative material to exercise its retained
judgment. If Sol wants another exception to the default Luna route, ask the
user rather than relying on its own cost estimate. An explicit user request
already authorizes that action and must not trigger redundant permission;
ordinary routing defaults apply unless the user assigns the route.

User approval remains mandatory for phase transitions and waivers, material
scope changes, policy decisions, significant risk, and other consequential
choices. A worker must stay bounded, must not redelegate, and must return
material ambiguity instead of deciding it.

Use these conservative, simplified upper-bound planning multipliers for
ChatGPT models: Luna 1x, Terra 10x, Sol 20x, and Astra 50x. These are planning
approximations, not exact billing ratios for every token class. Use GPT-6 Astra
only for unusually complex problem-solving or reviews when its extra capability
justifies its high cost; Astra is not the everyday root. Terra is very rare.
Gemini uses a separate credit pool and should be considered for suitable work,
particularly mechanical implementation.

## Keep work focused and phased

Keep one session focused on one goal. Record and defer unrelated work. Do not
silently expand scope.

Use the normal phases: Brainstorm, Governing Documentation, Implementation, and
Wrap Up. Obtain explicit user approval before moving to another phase. The user
may waive a phase when the normal sequence does not fit, but state the reason.
Do not treat approval of one phase as approval of another.

## Work from the repository's sources

Before substantive repository work, consult:

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
