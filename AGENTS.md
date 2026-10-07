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
tool-free. Briefly announce the work and its route before proceeding.

Default repository and tool work to one GPT-6 Luna worker, except for code
authoring below, even when it appears small. Use additional workers only for
worthwhile work that is independent, does not overlap, and is needed.

Keep program design with the user and Sol for every Luna assignment, whether
delegation is used alone or with the full workflow. Permission to investigate
or gather evidence does not include permission to design or write a program.
For simple operational tasks without an approved Book, Sol writes the required
code and remains responsible for keeping the solution simple. Luna may execute
supplied code and make only mechanical repairs explicitly permitted by the
approved assignment. For other implementation work, Luna may tangle from an
approved Book or implement an approved concrete design that settles material
decisions, while retaining harmless implementation choices.

- Before giving Luna any assignment not already covered by an approved plan or
  exempted by this policy, present the concrete bounded plan Luna will execute and
  obtain user approval.
- The plan describes the expected result, affected targets, permitted actions,
  evidence to reuse, how completion will be judged, and when to stop, with
  detail suited to the risk. Naming Luna or stating only an outcome (for
  example, “ask Luna to update the live site”) is not enough.
- If facts needed to define a change are unknown, the plan may seek approval
  for bounded investigation; Luna then returns with a concrete change plan for
  approval before making that change.
- Approving a plan also authorizes the follow-up assignments it includes; do
  not ask separately for permission to delegate. Luna's assignment is the
  approved plan, with any judgment Sol retains made clear. Luna must not add
  targets, actions, or checks beyond it.
- If a finding requires work or verification beyond the approved plan, Luna
  returns. Present a new plan when proposed work materially changes or exceeds
  the approved plan, or when another required approval applies. Minor
  surprises within the plan need not interrupt the user.
- This policy defines which work, if any, does not need plan approval. Change
  it only deliberately, with user approval, usually based on recorded Wrap Up
  feedback. A consuming repository's `AGENTS.md` may adapt it locally, and the
  user may approve a one-off exception.

For evidence gathering, Luna returns short findings: a targeted summary,
source locations, short excerpts that support the findings, and material
conflicts or ambiguities. Luna must not reproduce most of a file for Sol to
reread; if a safe summary would require that, recommend asking Sol to read it
directly. Reuse evidence identified in the approved plan.

A direct user assignment authorizes Sol to perform only the named operation on
the named target or targets, without asking again. It does not authorize
searches, other commands, related files, or follow-up tool work; that work
returns to Luna. Sol may inspect other material for judgment only after asking
the user. A Luna recommendation to read a file, or a file's authority, is not
permission to inspect it.

User approval remains mandatory for phase transitions and waivers, material
scope changes, policy decisions, significant risk, and other consequential
choices. A worker must stay bounded, must not redelegate, and must return
material ambiguity instead of deciding it. Agents need not reread applicable
`AGENTS.md` instructions already supplied by the harness. When work moves into
a deeper scope, Luna checks for closer target-local `AGENTS.md` or override
instructions and surfaces conflicts.

Rough relative cost, based on official API prices rather than Codex credit
rates (revisit when those are published): Luna 1x, Sol 20x, Astra 100x. Use
GPT-6 Astra only for unusually complex problem-solving or reviews when its
extra capability justifies the cost; Astra is not the everyday root. Gemini
uses a separate credit pool and should be considered for suitable work,
particularly mechanical implementation.

## Keep work focused and phased

Keep one session focused on one goal. Record and defer unrelated work. Do not
silently expand scope.

Use the normal phases: Brainstorm, Governing Documentation, Implementation, and
Wrap Up. Obtain explicit user approval before moving to another phase. The user
may waive a phase when the normal sequence does not fit, but state the reason.
A waiver does not waive documenting durable implementation changes. Do not
treat approval of one phase as approval of another.

State the current phase when starting or resuming a session and after an
approved transition. During a long discussion, give occasional brief reminders
when the phase may be unclear, especially around governing-document work. Use
judgment; there is no fixed reminder schedule. Naming a phase does not approve
a transition.

Use plain language in governing documents, project Books, and skills. Prefer
familiar words; keep specialized terms when they make meaning clearer, and
explain them briefly when needed.

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
