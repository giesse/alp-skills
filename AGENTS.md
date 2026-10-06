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

The root agent is GPT-6 Sol for discussion, orchestration, design,
brainstorming, policy judgment, and synthesis; it should normally remain
tool-free. Briefly announce the work and its route before proceeding. Default
repository and tool work to one GPT-6 Luna worker, even when it appears
small. Before giving Luna any assignment not already covered by an approved
plan or standing permission, present the concrete bounded plan Luna will
execute and obtain user approval so the user can stop or simplify it before
execution. The plan must describe the expected result, affected targets,
permitted actions, evidence to reuse, decisive check, and stop condition, with
detail proportional to risk. Naming Luna or stating only an outcome (for
example, “ask Luna to update the live site”) is not a sufficient plan. If facts
needed to define a change are unknown, the plan may seek approval for bounded
investigation; Luna must then return with a concrete change plan for approval
before making that change. Approval authorizes Luna to execute the approved
plan, including follow-up assignments it covers, without a separate request for
permission to delegate. The worker assignment is that approved plan, with any
clarification of judgment Sol retains; it must not add targets, operations, or
checks beyond the plan. Present a new plan for approval when proposed work
materially changes or exceeds the approved plan, or when another consequential
approval gate applies. A user may explicitly approve standing permission for a
defined class of work; record its scope and limits durably. Prefer one Luna
worker when practical, and use additional workers only for independently
worthwhile assignments. Parallel tasks must be independent, non-overlapping,
and all needed.

Luna must return when a finding requires work or verification beyond the
approved plan. Minor surprises within the plan need not interrupt the user.

For evidence gathering, Luna returns a compressed packet: a targeted summary,
source locations, short decisive excerpts, and material conflicts or
ambiguities. Do not reproduce most of a file for Sol to reread; recommend a
direct-read handoff when safe compression would require that.

An explicit user assignment to Sol, including a request that directly asks Sol
to perform a narrow, named operation, authorizes direct work only on the named
targets and operations. The user may name multiple exact files. Do not request
redundant permission for that work, but do not carry its authorization into
follow-on repository or tool work.

Sol may directly inspect material for judgment only when the user's explicit
assignment authorizes that named target and operation. If Sol must inspect
material not covered by an explicit assignment, Sol must ask the user first.
Luna may recommend a direct-read handoff when safe compression would reproduce
most of a file, but that recommendation does not authorize Sol to inspect it.
An identified file's authority alone is insufficient. An explicit assignment
authorizes only the identified target and operation; it does not authorize
searches, running other commands, reading related files, or a follow-on tool
loop. Further repository or tool work returns to Luna.

User approval remains mandatory for phase transitions and waivers, material
scope changes, policy decisions, significant risk, and other consequential
choices. A worker must stay bounded, must not redelegate, and must return
material ambiguity instead of deciding it. Agents need not reread applicable
`AGENTS.md` instructions already supplied by the harness. When work moves into
a deeper scope, Luna checks for closer target-local `AGENTS.md` or override
instructions and surfaces conflicts.

Use these provisional, simplified planning multipliers for GPT-6 models, using
official standard API short-context input and output prices as a proxy rather
than published Codex credit rates:

- Luna: 1x planning multiplier
- Sol: 20x Luna's planning multiplier
- Astra: 100x Luna's planning multiplier

These are simplified planning multipliers, not exact billing ratios for every
token class or Codex product surface. Reassess them when official rates
materially change or published Codex credit rates become available for the
GPT-6 models.

Use GPT-6 Astra only for unusually complex problem-solving or reviews when its
extra capability is expected to justify its high cost; Astra is not the
everyday root. Gemini uses a separate credit pool and should be considered for
suitable work, particularly mechanical implementation.

## Keep work focused and phased

Keep one session focused on one goal. Record and defer unrelated work. Do not
silently expand scope.

Use the normal phases: Brainstorm, Governing Documentation, Implementation, and
Wrap Up. Obtain explicit user approval before moving to another phase. The user
may waive a phase when the normal sequence does not fit, but state the reason.
Do not treat approval of one phase as approval of another.

## Work from the repository's sources

For substantive repository investigation, the repository worker consults:

- `GOALS.md` and `RULES.md`;
- `ALP.md` when the artifact concerns ALP; and
- `wiki/index.md`, following only task-relevant links.

The worker returns targeted findings to Sol; Sol need not reread these sources.
A narrow direct read under the routing rules does not itself trigger wiki
preflight. If `wiki/index.md` is absent, the worker surfaces that workflow gap
rather than inventing its contents or silently ignoring the requirement.

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
