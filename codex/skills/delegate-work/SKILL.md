---
name: delegate-work
description: Route discussion, repository, and tool work between the root agent and workers while preserving user authority, bounded assignments, economical model use, and reliable evidence handoffs. Use when deciding who should do work, how to delegate it, or when a worker should stop and return a decision.
---

# Delegate Work

Keep GPT-6 Sol as the root agent for discussion, orchestration, design,
policy judgment, and synthesis. It should normally remain tool-free. Briefly
announce the work and its route before proceeding. Before giving Luna any
assignment not already covered by an approved plan or standing permission,
present the concrete bounded plan Luna will execute and obtain user approval so
the user can stop or simplify it before execution. The
plan must describe the expected result, affected targets, permitted actions,
evidence to reuse, decisive check, and stop condition, with detail
proportional to risk. Naming Luna or stating only an outcome (for example,
“ask Luna to update the live site”) is not a sufficient plan. If facts needed
to define a change are unknown, the plan may seek approval for bounded
investigation; Luna must then return with a concrete change plan for approval
before making that change. Approval authorizes Luna to execute the approved
plan, including follow-up assignments it covers, without a separate request for
permission to delegate. The worker assignment is that approved plan, with any
clarification of judgment Sol retains; it must not add targets, operations, or
checks beyond the plan. Present a new plan for approval when proposed work
materially changes or exceeds the approved plan, or when another consequential
approval gate applies. A user may explicitly approve standing permission for a
defined class of work; record its scope and limits durably.

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

For delegated evidence gathering, Luna returns a compressed packet: a
targeted summary, source locations, only short decisive excerpts, and material
conflicts or ambiguities. Luna must not reproduce most of a file for the
root agent to reread. If safe compression would require that, recommend a
direct-read handoff instead.

An explicit user assignment to the root agent, including a request that
directly asks it to perform a narrow, named operation, authorizes direct work
only on the named targets and operations. The user may name multiple exact
files. This work needs no redundant permission, but the authorization does not
extend to follow-on repository or tool work.

The root agent may directly inspect material for judgment only when the user's
explicit assignment authorizes that named target and operation. If it must
inspect material not covered by an explicit assignment, it must ask the user
first. Luna may recommend a direct-read handoff when safe compression
would reproduce most of a file, but that recommendation does not authorize the
root agent to inspect it. A file's authority alone is insufficient. An
explicit assignment authorizes only the identified target and operation; it
does not authorize searches, running other commands, reading related files, or
a follow-on tool loop. Further repository or tool work returns to a worker.

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
