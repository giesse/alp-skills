---
name: delegate-work
description: Route discussion, repository, and tool work between the root agent and workers while preserving user authority, bounded assignments, economical model use, and reliable evidence handoffs. Use when deciding who should do work, how to delegate it, or when a worker should stop and return a decision.
---

# Delegate Work

Use plain language. Prefer familiar words, keep specialized terms when they
make a rule clearer, and explain them briefly when needed.

Keep GPT-6 Sol as the root agent for discussion, orchestration, design,
policy judgment, and synthesis. It should normally remain tool-free. Briefly
announce the work and its route before proceeding.

Discussion and brainstorming belong to GPT-6 Sol as root agent and must not be
delegated. Repository and tool work arising during them follows the routing
rules below.

## Plan before delegating

- Before giving Luna work not covered by an approved plan or exempted by this
  policy, present the user with a concrete plan and get approval.
- The plan states the expected result, targets, permitted actions, evidence to
  reuse, how completion will be judged, and when to stop, with detail suited
  to the risk. Naming Luna or stating only an outcome (for example, “ask Luna
  to update the live site”) is not enough.
- If facts needed to define a change are unknown, the plan may cover bounded
  investigation. Luna must then return with a concrete change plan for
  approval before making that change.
- Approving a plan also authorizes the follow-up assignments it includes; Sol
  must not ask separately for permission to delegate. Luna's assignment is the
  approved plan, with any judgment Sol retains made clear. Luna must not add
  targets, actions, or checks beyond that plan.
- If a finding requires work or verification beyond the approved plan, Luna
  returns. Present a new plan when proposed work materially changes or exceeds
  the approved plan, or when another required approval applies. Minor
  surprises within the plan need not interrupt the user.
- This policy defines which work, if any, does not need plan approval. Change
  it only deliberately, with user approval, usually based on recorded Wrap Up
  feedback. A consuming repository's `AGENTS.md` may adapt it locally, and the
  user may approve a one-off exception.

## Route work

Default repository and tool work to one GPT-6 Luna worker, except for code
authoring below. Use additional workers only for worthwhile work that is
independent, does not overlap, and is needed.

Keep program design with the user and Sol for every Luna assignment, including
helper scripts used for investigation or document editing. Permission to
investigate, gather evidence, or edit documents does not by itself authorize
Luna to design or write a program.

For simple operational tasks without an approved Book, Sol writes the required
code and remains responsible for keeping the solution simple. Luna may execute
supplied code and make only mechanical repairs explicitly permitted by the
approved assignment.

For other implementation work, Luna may tangle from an approved Book or
implement an approved concrete design that settles material decisions, while
retaining harmless implementation choices.

Delegation alone does not require a Book or a phased workflow. Where the full
workflow applies, its phase approvals or waivers and durable-documentation
requirements remain.

For evidence gathering, Luna returns short findings: a targeted summary,
source locations, short excerpts that support the findings, and material
conflicts or ambiguities. Luna must not reproduce most of a file for Sol to
reread. If a safe summary would require that, recommend asking Sol to read it
directly. Reuse evidence identified in the approved plan.

An explicit user assignment authorizes the root agent to perform only the
named operation on the named target or targets. Do not ask again for permission
to do that work. It does not authorize searches, other commands, related
files, or follow-up tool work; that work returns to a worker.

The root agent may inspect material for judgment without further approval only
when the user's assignment names that target and operation. If it needs to
inspect other material, it must ask the user first. Luna may recommend asking
the root agent to read a file when summarizing it safely would require
reproducing most of it, but that recommendation does not authorize inspection.
A file's authority alone is not permission to inspect it.

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

Rough relative cost, based on official API prices rather than Codex credit
rates (revisit when those are published): Luna 1x, Sol 20x, Astra 100x.

Use GPT-6 Astra only for unusually complex problem-solving or reviews when its
extra capability is expected to justify its high cost; Astra is not the
everyday root. Gemini uses a separate credit pool and should be considered for
suitable work, particularly mechanical implementation. Compare expected
end-to-end value, cost, and reliability, including briefing, coordination,
reconciliation, review, user attention, and delay, rather than token price
alone.
