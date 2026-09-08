---
name: run-alp-workflow
description: Guide a complete AI-assisted Literate Programming session through Brainstorm, Governing Documentation, Implementation, and Wrap Up while preserving user authority, explicit phase approval, independent acceptance checks, economical delegation, and semantic alignment between the Book and implementation. Use for end-to-end ALP delivery, resuming or routing an ALP session, or phase-gated documentation intended to produce executable or operational change. Compose it with author-alp-book for detailed Book work and maintain-repository-wiki for worthwhile repository memory; use those skills alone when the full lifecycle is not wanted.
---

# Run an ALP Workflow

Keep the process simple, focused, and controlled by the user. Treat the
human-authored Book as the source of material intent and the implementation as
its executable realization.

## Preserve instruction authority

Follow the consuming repository's instructions. Surface a conflict between
those instructions and this skill instead of resolving it silently.

Treat use of this complete workflow as adoption of its repository-memory
requirement. For substantive repository investigation, the repository worker
consults `wiki/index.md`, follows only task-relevant links, and returns targeted
findings to Sol. Sol need not read the wiki, and a narrow direct read under the
routing rules does not itself trigger wiki preflight. If the index is absent,
the worker surfaces the gap and lets the user decide how to address it rather
than inventing its contents.

Keep one session focused on one goal. Record and defer unrelated work. If an
unrelated blocker must be addressed elsewhere, preserve enough context to
resume the original goal.

Let the user own the goal, scope, material decisions, governing documentation,
phase transitions, exceptions, and final acceptance. Surface ambiguity,
missing policy, conflicting requirements, and material tradeoffs.

Do not turn a decision for one task or session into permanent workflow policy.
When a decision recurs, propose recording it in the appropriate governing
document with user approval.

## Route work and require approval for consequential decisions

The root agent is GPT-5.6 Sol for discussion, orchestration, design,
brainstorming, policy judgment, and synthesis; it should normally remain
tool-free. Briefly announce the work and its route before proceeding. Default
repository and tool work to one GPT-5.6 Luna worker, even when it appears
small; clear, bounded Luna delegation may proceed after that announcement
without advance approval. Prefer one Luna worker when practical, and use
additional workers only for independently worthwhile assignments. Parallel
tasks must be independent, non-overlapping, and all needed.

For delegated evidence gathering, Luna returns a compressed packet: a targeted
summary, source locations, only short decisive excerpts, and material conflicts
or ambiguities. Luna must not reproduce most of a file for Sol to reread. If
safe compression would require that, recommend a direct-read handoff instead.

An explicit user assignment to Sol, including a request that directly asks Sol
to perform a narrow, named operation, authorizes direct Sol work only on the
named targets and operations. The user may name multiple exact files. This work
needs no redundant permission, but the authorization does not extend to
follow-on repository or tool work.

Without further approval, Sol may directly read one identified file only when
the file itself must be judged coherently within Sol's retained role, or Luna
reports that safe compression would reproduce most of it. A file's authority
alone is insufficient. This permits only the identified read operation, not
searches, other commands, related files, or a follow-on tool loop. Further work
returns to Luna. Sol asks the user before making any other exception to the
default route.

User approval remains mandatory for phase transitions and waivers, material
scope changes, policy decisions, significant risk, and other consequential
choices. A worker must stay bounded, must not redelegate, and must return
material ambiguity instead of deciding policy, altering acceptance criteria, or
expanding scope. Agents need not reread applicable `AGENTS.md` instructions
already supplied by the harness. When repository work moves into a deeper
scope, Luna checks for closer target-local `AGENTS.md` or override instructions
and surfaces conflicts.

Use these conservative, simplified upper-bound planning multipliers for
ChatGPT models: Luna 1x, Terra 10x, Sol 20x, and Astra 50x. These are planning
approximations, not exact billing ratios for every token class. Use GPT-6 Astra
only for unusually complex problem-solving or reviews when its extra capability
justifies its high cost; Astra is not the everyday root. Terra is very rare.
Gemini uses a separate credit pool and should be considered for suitable work,
particularly mechanical implementation. Compare expected end-to-end value,
cost, and reliability rather than token price alone.

## Control phase transitions

Use the normal sequence:

1. Brainstorm
2. Governing Documentation
3. Implementation
4. Wrap Up

Obtain explicit user approval before every transition. Do not treat approval
of one phase as approval of another. Let the user waive a phase when the
normal sequence does not fit, such as investigation or operational work, but
state the reason for the waiver.

### Brainstorm

Clarify the problem, intent, scope, assumptions, gaps, edge cases, risks, and
possible approaches. Ask useful questions and act as a sounding board.

Do not require a separate artifact. Keep exploratory ideas distinct from
approved decisions. Do not drift into documentation work or implementation.

### Governing Documentation

Treat writing and approving the governing documentation as the central work.
Keep the user as author and decision-maker. Normally require the user to write
the first draft or a significant part.

When `$author-alp-book` is available, use it for detailed Book work within the
approved Governing Documentation phase. Its use does not authorize a phase
transition. If it is unavailable, apply the self-contained requirements below.

Assist by researching, suggesting, reviewing, editing, clarifying, and
preparing evidence-based material. Draft most of a derivative governing
document only when approved user-authored sources already establish the
policy, the user explicitly authorizes drafting, and the user reviews the
result. Do not invent intent.

When ALP applies, require the Book to:

- teach a reader the intended mental model;
- state material intent, rationale, constraints, compatibility commitments,
  and dangerous boundaries;
- remove ambiguity where different interpretations would materially matter;
  and
- remain readable, tangle-ready, and reviewable.

In an existing system, treat code, tests, runtime observations, comments, and
old documents as evidence rather than automatic intent. Distinguish intended,
compatibility-constrained, incidental, contradictory, and unresolved
behavior. Return unresolved material questions to the user.

Use the least precise representation that removes material ambiguity. Leave
ordinary low-level implementation choices open.

Before Implementation, identify the decisive acceptance checks and obtain user
approval for them. Use automated tests or other decisive static, manual, or
runtime checks appropriate to the work. Keep critical-check authorship
independent of the implementer. Do not invent an artificial harness when an
approved independent static review is the better critical check.

Before finalizing the checks, perform a proportionate coverage pass. Confirm
that each approved material criterion and important boundary has an observable
check, or state the remaining evidence limitation. Use the simplest
representation that makes coverage clear; do not require a matrix,
traceability document, or separate artifact unless it materially helps.

Prefer test-first implementation when the decisive checks can be executable
tests. When safe and meaningful, run new critical tests before implementation
and confirm that they fail for the expected reason. Do not manufacture a red
baseline for static or manual checks, already-satisfied behavior, or unsafe or
misleading failures.

### Implementation

Give the implementer the approved governing documentation and critical
acceptance checks. Prefer an economical model capable of performing the work
reliably.

Allow ordinary low-level choices left open by the documentation. Do not allow
the implementer to invent policy or change, weaken, or reinterpret critical
checks. Let the implementer add useful supplementary checks when they do not
alter the approved acceptance contract.

Implement until the approved checks pass, then refactor while keeping them
passing. Do not weaken the checks to obtain green results.

Treat scripts, migrations, configuration, infrastructure, and generated or
operational artifacts as implementation when they alter executable or
operational behavior.

If implementation reveals a missing case, mistaken assumption, material
ambiguity, or incorrect critical check, stop and return to Governing
Documentation. Do not force success through undocumented behavior.

Verify in proportion to the claim. A syntax check proves syntax; a focused
test proves only its covered behavior; a review supports only its stated
scope.

Before completion, align the Book and accepted implementation on material
behavior and decisions. Do not demand one-to-one traceability.

### Independent review

For non-trivial changes, consider fresh post-implementation review when it is
likely to add evidence worth its cost. Prefer review of the concrete
implementation and evidence over repeated review of proxy plans or contracts.

Let the user decide whether optional review is worthwhile. When independent
review was approved as a critical acceptance check, treat it as mandatory and
keep the reviewer independent of the implementer.

Do not let review change policy, scope, or acceptance criteria.

### Wrap Up

Confirm that the documentation and accepted implementation remain aligned.
Record decisions, lessons, unresolved follow-up, and other knowledge worth
retaining in an appropriate durable artifact.

When `$maintain-repository-wiki` is available, use it for worthwhile portable,
non-governing repository knowledge. Its use is conditional: do not update the
wiki merely to prove that Wrap Up occurred. If the skill is unavailable,
preserve the same distinction between repository memory and governing
documentation.

Keep retained knowledge concise, searchable, reachable from a likely entry
point, and explicit about whether it is policy, evidence, history, inference,
or unresolved work. Do not create paperwork merely to prove that Wrap Up
occurred.

Discuss how the session and workflow performed: what helped, what failed, what
was unnecessarily difficult, and what may merit improvement. Obtain user
acceptance rather than declaring the work accepted on the user's behalf.
