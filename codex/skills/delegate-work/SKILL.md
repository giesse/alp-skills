---
name: delegate-work
description: Route discussion, repository, and tool work between the root agent and workers while preserving user authority, bounded assignments, economical model use, and reliable evidence handoffs. Use when deciding who should do work, how to delegate it, or when a worker should stop and return a decision.
---

# Delegate Work

Use plain language. Prefer familiar words, keep specialized terms when they
make a rule clearer, and explain them briefly when needed.

Keep GPT-6 Sol as the root agent for discussion, orchestration, design,
policy judgment, and synthesis. It should normally remain tool-free. Briefly
announce the work and its route before proceeding. Before giving Luna work not
covered by an approved plan or standing permission, present the user with a
concrete plan and get approval. The plan states the expected result, targets,
permitted actions, evidence to reuse, how completion will be judged, and when
to stop, with detail suited to the risk. Naming Luna or stating only an outcome
(for example, “ask Luna to update the live site”) is not enough. If facts
needed to define a change are unknown, the plan may cover bounded
investigation. Luna must then return with a concrete change plan for approval
before making that change. Approval covers the plan, including follow-up
assignments it covers; Sol must not ask separately for permission to delegate.
Luna's assignment is the approved plan, with any judgment Sol retains made
clear. Luna must not add targets, actions, or checks beyond that plan. Present
a new plan when proposed work materially changes or exceeds the approved plan,
or when another required approval applies. The user may approve standing
permission for a defined class of work; record its scope and limits durably.

Discussion and brainstorming belong to GPT-6 Sol as root agent and must not be
delegated. Repository and tool work arising during them follows the routing
rules below.

## Route work

Default repository and tool work to one GPT-6 Luna worker, even when it appears
small. Delegate only under an approved plan or standing permission. Prefer one
worker when practical; use additional workers only for independently worthwhile
assignments. Parallel tasks must be independent, non-overlapping, and all
needed.

Luna must return when a finding requires work or verification beyond the
approved plan. Minor surprises within the plan need not interrupt the user.

For evidence gathering, Luna returns short findings: a targeted summary,
source locations, short excerpts that support the findings, and material
conflicts or ambiguities. Luna must not reproduce most of a file for Sol to
reread. If a safe summary would require that, recommend asking Sol to read it
directly. Reuse evidence identified in the approved plan.

An explicit user assignment authorizes the root agent to perform only the
named operation on the named target or targets. Do not ask again for permission
to do that work, but do not treat it as permission for follow-up repository or
tool work.

The root agent may inspect material for judgment without further approval only
when the user's assignment names that target and operation. If it needs to
inspect other material, it must ask the user first. Luna may recommend asking
the root agent to read a file when summarizing it safely would require
reproducing most of it, but that recommendation does not authorize inspection.
A file's authority alone is not permission to inspect it. As above, an
assignment does not authorize searches, other commands, related files, or
follow-up tool work. Further repository or tool work returns to a worker.

## Keep authority with the user

User approval remains mandatory for phase transitions and waivers, material
scope changes, policy decisions, significant risk, and other consequential
choices. Approval of one plan or assignment does not authorize a later phase,
materially different work, or separate consequential choices.

A worker must stay within its bounded assignment, must not redelegate, and
must return material ambiguity instead of deciding policy, changing acceptance
criteria, or expanding scope. Agents need not reread applicable `AGENTS.md`
instructions already supplied by the harness. When repository work moves into
a deeper scope, Luna checks for closer target-local `AGENTS.md` or
override instructions and surfaces any conflict.

## Choose models economically

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
suitable work, particularly mechanical implementation. Compare expected
end-to-end value, cost, and reliability, including briefing, coordination,
reconciliation, review, user attention, and delay, rather than token price
alone.
