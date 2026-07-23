# Workflow Rules

This document translates the principles in [GOALS](GOALS.md) into operational rules.
It is meant to be detailed enough to derive concise [AGENTS](AGENTS.md) instructions
and task-specific skills, while remaining short and clear enough for effective
human review.

[GOALS](GOALS.md) is the constitution of the project and takes precedence over this
document. These rules must be corrected if they conflict with it.

## 1. Keep the workflow simple and clear

1. Use the simplest process that can produce a reliable result. Every added
   phase, artifact, role, handoff, or rule must provide a concrete benefit that
   justifies its cost.
2. Prefer plain language. Use specialized terms only when they make the rule
   more precise, and explain them where necessary.
3. Do not optimize model credits at the expense of simplicity, clarity, or
   result quality.
4. Rules should guide judgment rather than replace it with ceremony. Do not
   create paperwork merely to prove that the workflow was followed.

## 2. Keep one session focused on one thing

1. A session is the chat thread in which the user and root agent collaborate.
   It must remain focused on one goal.
2. Record and defer unrelated work instead of absorbing it into the current
   session.
3. If unrelated work blocks the current goal, preserve enough context to
   resume the original work. Address the blocker in another session, or
   explicitly convert the current session to the blocker and resume the
   original goal in a new session.
4. Do not silently expand the scope of a session or implementation.

## 3. Preserve user authority

1. The user owns the goal, scope, material decisions, governing
   documentation, phase transitions, exceptions, and final acceptance.
2. An agent must surface ambiguity, missing policy, conflicting requirements,
   and material tradeoffs instead of resolving them silently.
3. An explicit decision for one task or session does not automatically become
   permanent workflow policy. Recurring decisions should be incorporated into
   the appropriate durable document with user approval.

## 4. Require approval before work and delegation

For the time being, use a deliberately strict approval process. It may be
relaxed later after experience shows which delegation patterns are reliable.

1. In response to a request, the root agent first explains the work it believes
   is needed and recommends which work, if any, should be delegated.
2. Before approval, the root agent must not read files, use tools, change
   artifacts, or perform the proposed work.
3. The user decides what the root agent should do and what should be delegated
   to a sub-agent.
4. Approval applies only to the work assigned for the next assistant turn.
   After that turn, the approval process resets.
5. A delegated agent must not delegate again unless the user explicitly
   approves that further delegation.
6. Delegation should be proposed only when its expected benefit outweighs the
   cost of briefing, coordination, review, and possible drift.

The current Codex cost structure is:

- Luna: 1x credit cost
- Terra: 2.5x Luna's credit cost
- Sol: 5x Luna's credit cost

The root agent is Sol. Recommend Luna or Terra when their lower cost and
capabilities fit the work, but let the user approve the route. Gemini uses a
separate credit pool and should be considered for suitable work, particularly
mechanical implementation. Model names and costs are intentionally explicit
for now and may be generalized later.

## 5. Work through explicit phases

The normal phases are Brainstorm, Governing Documentation, Implementation, and
Wrap Up.

1. Moving from one phase to the next always requires explicit user approval.
2. The user may waive a phase when the normal sequence does not fit the work,
   such as an investigation or operational task. The reason for the waiver
   must be stated clearly.
3. An agent must not treat approval of one phase as approval of a later phase.

### Brainstorm

1. Use Brainstorm to clarify the problem, intent, scope, assumptions, gaps,
   edge cases, risks, and possible approaches.
2. The agent should ask useful questions, act as a sounding board, and help the
   user discover what they mean to do.
3. Brainstorm does not require a separate artifact. Its result may remain in
   the thread if that provides enough clarity to begin the governing
   documentation.
4. Do not turn Brainstorm into implementation or present an exploratory idea
   as an approved decision.

### Governing Documentation

1. The governing documentation is the source of truth for implementation.
   Writing and approving it is the central work, not a prelude to the real
   work.
2. The user must remain the author and decision-maker. Normally, the user
   writes the first draft or a significant part of it.
3. The AI may research, suggest, review, edit, clarify, and complete tedious or
   evidence-based portions without taking ownership of material policy.
4. The AI may draft most of a derivative governing document when the policy is
   already established in user-authored and approved sources, the user
   explicitly authorizes the drafting, and the user reviews and steers the
   result.
5. New policy, unresolved ambiguity, or a material design choice must be
   brought back to the user rather than invented during drafting.
6. Any durable implementation change must be reflected in durable
   documentation before the work is complete.

### Implementation

1. Implementation follows the approved governing documentation and critical
   acceptance checks. It must not quietly redefine either.
2. Implementation should be mostly mechanical. Prefer an economical model
   capable of carrying it out reliably.
3. The implementer may make ordinary low-level choices left open by the
   governing documentation, but must not invent policy or resolve a material
   design gap.
4. If implementation exposes a missing case, mistaken assumption, ambiguity,
   or incorrect critical check, stop implementation and return to Governing
   Documentation.
5. Do not make implementation succeed at all costs by adding undocumented
   behavior or weakening acceptance.

### Wrap Up

1. Wrap Up completes the work and preserves knowledge that should survive the
   transient chat.
2. Record lessons, decisions, unresolved follow-up, and other necessary context
   in the appropriate durable project artifact.
3. Confirm that required documentation and follow-up records are complete.
4. Discuss how the session and workflow performed: what helped, what failed,
   what was unnecessarily difficult, and what may merit improvement.
5. Record only knowledge worth retaining. Wrap Up must not become routine
   paperwork with no future value.

## 6. Define acceptance before implementation

1. During Governing Documentation, identify and obtain user approval for the
   decisive acceptance checks that the result must pass.
2. A critical acceptance check may be an automated test or another decisive
   static, manual, or runtime check appropriate to the work.
3. Critical acceptance checks must be designed independently of the
   implementation agent and supplied to that agent with the governing
   documentation.
4. The implementer may add useful tests or checks, but must not change, weaken,
   or reinterpret the approved critical checks.
5. If a critical check is wrong, insufficient, or ambiguous, stop and return
   to Governing Documentation.
6. Do not invent an artificial test harness when the nature of the work does
   not support one. If no suitable test can be created in advance, an
   independent static review may itself be defined and approved as the
   critical acceptance check. Its scope and criteria must be agreed before
   implementation, and the reviewer must be independent of the implementer.

## 7. Treat post-implementation review as a strong default

1. The root agent should normally recommend independent post-implementation
   review for non-trivial changes.
2. The recommendation should reflect the risk of the change and the likely
   value of another review, not a rigid requirement to add process.
3. The user decides whether an optional review is worthwhile. Skipping it does
   not require ceremonial justification.
4. When an independent static review was approved as a critical acceptance
   check under Section 6, it is not optional: in that case the review is the
   test the implementation must pass.
5. Review does not authorize the reviewer to change approved policy, scope, or
   acceptance criteria.

## 8. Derive harness instructions from these rules

1. While this document exists, it is the authoritative operational source for
   the [AGENTS](AGENTS.md) and `SKILL.md` instructions produced by this project.
   [GOALS](GOALS.md) remains superior to it.
2. The [AGENTS](AGENTS.md) file created for this repository applies only to this
   repository. It should contain the compact, always-loaded local instructions
   needed to develop and maintain this project's artifacts. It is not the
   mechanism by which other repositories adopt the workflow.
3. The skills produced by this project are the primary distributable
   artifacts. They are designed for global installation and reuse across many
   repositories.
4. Once invoked, a skill must contain all the rules and procedures needed for
   the behavior it governs. It must not assume that a consuming repository's
   `AGENTS.md` already mandates or explains this workflow.
5. A consuming repository's `AGENTS.md` may help invoke a skill, reinforce its
   essential rules, or adapt it to local requirements. The skill must remain
   usable without that optional integration.
6. Self-contained execution does not guarantee that a skill will be invoked.
   Activation may come from the user naming the skill, the harness matching
   its description, or an applicable global or repository instruction.
7. Skills produced by this project should not be tied to one repository.
   Keep repository-specific procedures in that repository's `AGENTS.md` or
   ordinary project documentation. Use a repository-local skill only when its
   activation, discovery, bundled resources, or other capabilities provide a
   concrete advantage over a referenced document.
8. Derived instructions may condense and specialize these rules, but must not
   contradict them, silently omit behavior required within their scope, or
   introduce new policy.
9. Avoid unnecessary duplication, but allow it when needed to make a skill
   self-contained or local integration reliable.
10. The authority order in this document governs how this project creates its
    artifacts. It does not override the instructions of a repository that
    consumes them. Surface conflicts with a consuming repository's
    instructions to the user instead of resolving them silently.
11. Review each derived artifact against [GOALS](GOALS.md) and this document
    before accepting it.
12. This document may be removed later only with explicit user approval, after
    deciding where its remaining authority and necessary rules will live.

## 9. Handle conflicts and exceptions openly

1. When documents conflict, apply this order of authority:
   [GOALS](GOALS.md), then [RULES](RULES.md), then derived [AGENTS](AGENTS.md) and skills.
2. Stop and ask the user when applying a rule would require a material
   interpretation not already established by the governing documents.
3. The user may approve a justified exception without changing the permanent
   rule. If the exception reveals a recurring need, propose a durable revision
   in a later, explicitly approved documentation phase.
