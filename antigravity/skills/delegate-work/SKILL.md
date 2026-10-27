---
name: delegate-work
description: Route discussion, repository, and tool work between the root agent and workers while preserving user authority, bounded assignments, economical model use, and reliable evidence handoffs. Use when deciding who should do work, how to delegate it, or when a worker should stop and return a decision.
---

# Delegate Work

Use plain language. Prefer familiar words, keep specialized terms when they
make a rule clearer, and explain them briefly when needed.

Keep Gemini 4 Argon as the root agent for discussion, orchestration, design,
policy judgment, and synthesis. It should normally remain tool-free. Briefly
announce the work and its route before proceeding.

Discussion and brainstorming belong to Gemini 4 Argon as root agent and must not
be delegated. Repository and tool work arising during them follows the routing
rules below.

## Read-only investigation without advance approval

A Gemini 3.8 Flash worker (`invoke_subagent` with `Model: 'flash'` and
`TypeName: 'research'`) may perform bounded, task-relevant, read-only
investigation of existing local files and local repository state without advance
plan approval. This includes initial repository investigation and directly
relevant files outside the checkout, such as the workflow feedback log
(`~/.gemini/config/workflow-feedback.md`).

Briefly announce the purpose and scope before assigning the investigation.
The Flash worker remains within that assignment and returns concise findings
with source locations.

This permission covers file and repository inspection only. It does not
authorize changes, helper-program creation, running project code, tests or
builds, or remote, network, application, or data-store access. Existing
approval requirements apply beyond this boundary.

## Plan before delegating

- Before giving a Flash worker work not covered by an approved plan or exempted
  by this policy, present the user with a concrete plan and get approval.
- The plan states the expected result, targets, permitted actions, evidence to
  reuse, how completion will be judged, and when to stop, with detail suited
  to the risk. Naming the worker or stating only an outcome (for example, “ask
  Flash to update the live site”) is not enough.
- If facts needed to define a change are unknown, the plan may cover bounded
  investigation. The Flash worker must then return with a concrete change plan
  for approval before making that change.
- Approving a plan also authorizes the follow-up assignments it includes; Argon
  must not ask separately for permission to delegate. The Flash worker's
  assignment is the approved plan, with any judgment Argon retains made clear.
  The worker must not add targets, actions, or checks beyond that plan.
- If a finding requires work or verification beyond the approved plan, the
  worker returns. Present a new plan when proposed work materially changes or
  exceeds the approved plan, or when another required approval applies. Minor
  surprises within the plan need not interrupt the user.
- This policy defines which work, if any, does not need plan approval. Change
  it only deliberately, with user approval, usually based on recorded Wrap Up
  feedback. A consuming repository's `AGENTS.md` may adapt it locally, and the
  user may approve a one-off exception.

## Route work

Default repository and tool work to one Gemini 3.8 Flash worker
(`invoke_subagent` with `Model: 'flash'`, using `TypeName: 'research'` for
read-only inspection and `TypeName: 'self'` for approved file or command work),
except for code authoring below. Use additional workers only for worthwhile
work that is independent, does not overlap, and is needed.

Keep program design with the user and Argon for every Flash worker assignment,
including helper scripts used for investigation or document editing. Permission
to investigate, gather evidence, or edit documents does not by itself authorize
a Flash worker to design or write a program, including helper scripts for those
tasks.

For simple operational tasks without an approved Book, Argon writes the required
code and remains responsible for keeping the solution simple. The Flash worker
may execute supplied code and make only mechanical repairs explicitly permitted
by the approved assignment.

For other implementation work, the Flash worker may tangle from an approved Book
or implement an approved concrete design that settles material decisions, while
retaining harmless implementation choices.

Delegation alone does not require a Book or a phased workflow. Where the full
workflow applies, its phase approvals or waivers and durable-documentation
requirements remain.

For evidence gathering, the Flash worker returns short findings: a targeted
summary, source locations, short excerpts that support the findings, and
material conflicts or ambiguities. The worker must not reproduce most of a file
for Argon to reread. If a safe summary would require that, recommend asking
Argon to read it directly. Reuse evidence identified in the approved plan.

An explicit user assignment authorizes the root agent to perform only the
named operation on the named target or targets. Do not ask again for permission
to do that work. It does not authorize searches, other commands, related
files, or follow-up tool work; that work returns to a worker.

The root agent may inspect material for judgment without further approval only
when the user's assignment names that target and operation. If it needs to
inspect other material, it must ask the user first. A Flash worker may recommend
asking the root agent to read a file when summarizing it safely would require
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
a deeper scope, the Flash worker checks for closer target-local `AGENTS.md` or
override instructions and surfaces any conflict.

## Choose models economically

Gemini 3.8 Flash (`Model: 'flash'`) is much cheaper to use than Gemini 4 Argon.
Offload routine repository and tool work and mechanical implementation to a
Gemini 3.8 Flash worker whenever practical so Gemini 4 Argon is reserved for
discussion, design, policy judgment, and synthesis. Compare expected end-to-end
value, cost, and reliability, including briefing, coordination, reconciliation,
review, user attention, and delay, rather than token price alone.
