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

For the time being, use a deliberately strict approval process. It remains in
force until the user explicitly approves a revision to these governing rules.
This additional control is deliberate: earlier attempts at automatic
delegation caused repeated problems, and there is not yet enough evidence to
identify reliable automatic routes. The user decides when its cost is no
longer justified.

1. In response to a request, the root agent first explains the work it believes
   is needed and recommends which work, if any, should be delegated. A
   delegation recommendation must identify the proposed model, the bounded
   task, the expected end-to-end benefit, the evidence or output to return,
   the judgment retained by the user and root, and the conditions under which
   the worker must stop.
2. Before approval, the root agent must not read files, use tools, change
   artifacts, or perform the proposed work.
3. The user decides what the root agent should do and what should be delegated
   to a sub-agent.
4. Approval applies only to the work assigned for the root agent's next
   assistant turn. An approved worker may complete its bounded assignment
   without renewed approval. The process resets before the root begins work in
   a later turn or makes another routing decision.
5. A delegated agent must not delegate again unless the user explicitly
   approves that further delegation.
6. Delegation should be proposed only when its expected benefit outweighs the
   cost of briefing, coordination, review, and possible drift.
7. An approved assignment must remain within its stated goal and boundary. A
   worker must return material ambiguity instead of deciding policy, changing
   acceptance criteria, or expanding scope.
8. Propose parallel delegation only when the tasks are genuinely independent,
   every result is needed, and ownership does not overlap.
9. Discussion and Brainstorm from information already available in the
   conversation are the root agent's work, must not be delegated, and do not
   require approval under this section. Reading files, using tools, changing
   artifacts, or performing other proposed work during Brainstorm still
   requires approval.

These requirements improve the information available to the user; they do not
authorize automatic delegation or weaken the turn-by-turn approval requirement.

The current Codex cost structure is:

- Luna: 1x credit cost
- Terra: 2.5x Luna's credit cost
- Sol: 5x Luna's credit cost

The root agent is Sol. Recommend Luna or Terra when their lower cost and
capabilities fit the work, but let the user approve the route. Gemini uses a
separate credit pool and should be considered for suitable work, particularly
mechanical implementation. Compare expected end-to-end cost and reliability,
including briefing, coordination, reconciliation, review, user attention, and
delay, rather than token price alone. Model names and costs are intentionally
explicit for now and may be generalized later.

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
   result. This exception permits derivative restatement; it does not transfer
   authorship of intent or authorize the AI to add policy.
5. New policy, unresolved ambiguity, or a material design choice must be
   brought back to the user rather than invented during drafting.
6. Any durable implementation change must be reflected in durable
   documentation before the work is complete.
7. When ALP applies, the Book is the durable, reader-first explanation and
   source of material intent. Not every document or repository observation is
   automatically part of the Book.
8. Use the least precise representation that removes material ambiguity.
   Greater detail is useful only when it makes an important decision clearer
   or prevents a consequential misinterpretation.
9. Before implementation, the Book must be readable, tangle-ready, and
   reviewable: it must teach the intended mental model, constrain material
   implementation choices, and expose important decisions and risks for
   challenge.
10. In an existing system, distinguish evidence about present behavior from
    approved intent. Existing behavior may be intended,
    compatibility-constrained, incidental, contradictory, or unresolved. Do
    not silently turn an observation into governing policy; return unresolved
    material questions to the user.

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
6. Implementation is defined by its effect, not its file type or location.
   Scripts, migrations, configuration, infrastructure, generated artifacts,
   and similar changes are implementation when they create or alter executable
   or operational behavior.
7. When ALP applies, the accepted implementation and the Book must be
   semantically aligned on material behavior and decisions before the work is
   complete. Alignment does not require a one-to-one mapping between Book
   passages and implementation files.

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
6. Retained knowledge should be concise, searchable, linked from a likely
   entry point, and clear about whether it is governing policy, evidence,
   history, or unresolved follow-up.

## 6. Define acceptance before implementation

1. During Governing Documentation, identify and obtain user approval for the
   decisive acceptance checks that the result must pass.
2. A critical acceptance check may be an automated test or another decisive
   static, manual, or runtime check appropriate to the work.
3. Critical acceptance checks must be designed independently of the
   implementation agent and supplied to that agent with the governing
   documentation.
4. Before finalizing critical checks for implementation, perform a
   proportionate coverage pass. Confirm that each approved material criterion
   and important boundary has an observable check, or identify the remaining
   evidence limitation explicitly. Use the simplest representation that makes
   coverage clear; do not require a matrix, traceability document, or separate
   artifact unless it materially helps.
5. Prefer test-driven development (TDD) when decisive acceptance checks can be
   executable tests. When safe and meaningful, run new critical tests before
   implementation and confirm that they fail for the expected reason.
   Implement until they pass, then refactor without weakening them. Do not
   manufacture a failing baseline when the appropriate check is static or
   manual, when existing behavior already satisfies it, or when the failure
   would be unsafe or misleading.
6. The implementer may add useful tests or checks, but must not change, weaken,
   or reinterpret the approved critical checks.
7. If a critical check is wrong, insufficient, or ambiguous, stop and return
   to Governing Documentation.
8. Do not invent an artificial test harness when the nature of the work does
   not support one. If no suitable test can be created in advance, an
   independent static review may itself be defined and approved as the
   critical acceptance check. Its scope and criteria must be agreed before
   implementation, and the reviewer must be independent of the implementer.
9. An acceptance claim must not exceed its evidence. A syntax check establishes
   syntax, a focused test establishes only the behavior it covers, and a review
   supports only its stated scope. Approval of a policy establishes that the
   decision was made, not that an implementation or workflow is proven
   reliable.

## 7. Use independent review where it adds evidence

1. For a non-trivial change, the root agent should consider whether independent
   post-implementation review is likely to add evidence worth its cost and
   recommend it when useful.
2. Prefer fresh review of the concrete implementation and its evidence over
   repeated semantic reviews of contracts, plans, or other proxies. Strong
   independently owned acceptance checks may reduce the value of another
   review.
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
2. Each operational rule must have one canonical owner. Derived artifacts may
   repeat a rule when self-contained use requires it, but the copy must
   preserve the canonical meaning and must not become independent policy.
3. The [AGENTS](AGENTS.md) file created for this repository applies only to this
   repository. It should contain the compact, always-loaded local instructions
   needed to develop and maintain this project's artifacts. It is not the
   mechanism by which other repositories adopt the workflow.
4. The skills produced by this project are the primary distributable
   artifacts. They are designed for global installation and reuse across many
   repositories.
5. Once invoked, a skill must contain all the rules and procedures needed for
   the behavior it governs. It must not assume that a consuming repository's
   `AGENTS.md` already mandates or explains this workflow, or that this
   repository and its documents are available.
6. A derived artifact that governs ALP work must carry the operational ALP
   requirements needed within its scope. A link to [ALP](ALP.md) is useful
   context in this repository, but is not a substitute for self-contained
   instructions.
7. A consuming repository's `AGENTS.md` may help invoke a skill, reinforce its
   essential rules, or adapt it to local requirements. The skill must remain
   usable without that optional integration.
8. Self-contained execution does not guarantee that a skill will be invoked.
   Activation may come from the user naming the skill, the harness matching
   its description, or an applicable global or repository instruction.
9. Skills produced by this project should not be tied to one repository.
   Keep repository-specific procedures in that repository's `AGENTS.md` or
   ordinary project documentation. Use a repository-local skill only when its
   activation, discovery, bundled resources, or other capabilities provide a
   concrete advantage over a referenced document.
10. Derived instructions may condense and specialize these rules, but must not
   contradict them, silently omit behavior required within their scope, or
   introduce new policy.
11. Avoid unnecessary duplication, but allow it when needed to make a skill
   self-contained or local integration reliable.
12. Canonical skills must be changed in their source repository. Installed
    copies are deployed outputs and must not become an independent source of
    policy. Detailed synchronization, drift detection, validation, and
    rollback procedures belong in the relevant installation or maintenance
    instructions.
13. The authority order in this document governs how this project creates its
    artifacts. It does not override the instructions of a repository that
    consumes them. Surface conflicts with a consuming repository's
    instructions to the user instead of resolving them silently.
14. Review each derived artifact against [GOALS](GOALS.md) and this document
    before accepting it. When the artifact governs ALP work, also verify that
    it preserves the applicable meaning of [ALP](ALP.md).
15. This document may be removed later only with explicit user approval, after
    deciding where its remaining authority and necessary rules will live.

## 9. Maintain portable repository memory

1. A repository that adopts our workflow must maintain a tracked, repository-local LLM
   Wiki. Its purpose is to preserve useful, non-governing knowledge for future
   humans and agents independently of any one machine, chat, model, or coding
   harness.
2. `wiki/index.md` is the mandatory, compact entry point to repository memory.
   The repository's `AGENTS.md` must point to it, and agents must consult it
   before substantive repository work. The index may route readers to useful
   durable documents outside `wiki/`; those documents need not be duplicated
   merely to place them under the wiki directory.
3. The wiki is working memory, not governing documentation. It must not
   replace, override, or silently reinterpret the Book or an explicit user
   decision. When wiki knowledge would change material intent, update and
   approve the governing documentation first.
4. The tracked wiki must remain portable with a clean clone. Machine-local,
   user-local, per-clone, secret, or otherwise non-portable values and notes
   must live outside it. Portable wiki pages may explain when such local
   knowledge is needed and how to discover it, but must not assume that a
   particular local value or artifact exists.
5. Use `wiki/sources/` for preserved external sources and historical evidence
   that inform the managed wiki. Sources are evidence, not automatically
   current knowledge, governing intent, or ground truth about what the project
   should do.
6. Wiki synthesis must preserve enough provenance and status to distinguish
   approved intent, current evidence, historical evidence, inference, and
   unresolved work. Reconcile material conflicts against current governing
   documentation, evidence, and user decisions before presenting a claim as
   current knowledge.
7. Keep wiki knowledge concise, searchable, interlinked, and reachable from `wiki/index.md`. Current navigation should not present superseded,
   historical, or unresolved material as current guidance.
8. Maintain the wiki only when doing so preserves knowledge worth retaining or
   improves its reliability and discoverability. Do not require a page update,
   index entry, source copy, or other bookkeeping merely to prove that a phase
   or Wrap Up occurred.
9. A chronological `wiki/log.md` is not required. Add one only when a concrete
   need for a wiki activity history justifies maintaining it; do not use it as
   a second record of governing decisions.

## 10. Handle conflicts and exceptions openly

1. When documents conflict, apply this order of authority:
   [GOALS](GOALS.md), then [RULES](RULES.md), then derived [AGENTS](AGENTS.md) and skills.
2. Stop and ask the user when applying a rule would require a material
   interpretation not already established by the governing documents.
3. The user may approve a justified exception without changing the permanent
   rule. If the exception reveals a recurring need, propose a durable revision
   in a later, explicitly approved documentation phase.
