# Goals and Non-Goals

[Table of contents](README.md) · Previous: [AI-Assisted Literate Programming](ALP.md) · Next: [Getting Started](book/getting-started.md)

Every project using [AI-assisted Literate Programming](ALP.md) should have a chapter dedicated to establishing the project's goals and non-goals. Typically, this would be a root `GOALS.md` file; if the goals file is very small, it could make sense to include the goals and non-goals directly in `AGENTS.md`. I strongly suspect that any project using an AI coding agent such as Codex would benefit from the same practice, even when it does not otherwise adopt ALP.

## Role of this chapter

This chapter is the constitution of this project. It governs future workflow and design decisions; [RULES](RULES.md) translates it into operational policy and must remain consistent with it.

I have found that explicit goals help AI agents stay focused on what matters. Project-wide goals keep work aligned over time, while a clear goal — and often explicit non-goals — for each session reduces the odds of straying into directions that do not matter. Non-goals are equally important because they rule out tempting approaches that might appear useful while undermining the project's real purpose. I struggled with this repository for a while until I decided to start with `GOALS.md` and work outward from it. This has been very successful, so I recommend the practice for every new ALP project, and I expect it can help existing projects as well.

`GOALS.md` began primarily as guidance for AI agents, with a role similar to `AGENTS.md`, rather than as a chapter written to teach human readers. It still serves that original purpose. Including it in the Book also gives human readers useful context: what the project is trying to accomplish, which tradeoffs it prioritizes, and which approaches it deliberately excludes.

## Goals

1. **KEEP IT SIMPLE**. This should always take precedence. Complexity must be justified.

2. **Use plain language.** Write GOALS, RULES, project Books, and skills so their intended readers can understand them on the first read. Prefer familiar words. Keep specialized terms when they make the meaning clearer, and explain them briefly when needed.

3. **Support AI-assisted Literate Programming.** Apply [ALP](ALP.md) through modern coding harnesses, Codex in particular since that's what I'm using.

4. **Use clearly defined phases.** The phases are Brainstorm, Governing Documentation (which is the source of truth), Implementation, and Wrap Up.
   1. Brainstorm is necessary because I rarely start with a clearly defined plan. Sometimes I have an idea that does not account for important edge cases; sometimes I do not yet know how to solve a problem; and sometimes I am not even sure what the exact problem is. During Brainstorm, the AI asks questions, acts as a sounding board, and helps me identify gaps, ambiguity, assumptions, and edge cases so that I can clarify what I mean to do. Its result may resemble a plan or detailed specification, but it does not require a separate artifact. It may exist in the thread context or simply give me enough clarity to begin writing the governing documentation.
   2. Governing Documentation is the real work (writing the code follows from that and should be a mostly mechanical step). I think that one of the reasons for all the problems we've been having is that I should be the center of this phase. I must write the first draft, or at least a significant part of it, with AI assistance when needed. The AI can do research, give suggestions and recommendations, review and improve my writing, and handle tedious or evidence-based sections such as fixing links, summarizing research, reporting on existing code, or recording reverse-engineering results. But it must not replace me as the author of the documentation.
   3. Before implementation begins, any critical tests that the result must pass must be defined and approved during Governing Documentation. "Tests" includes automated tests and any other decisive acceptance checks appropriate to the work. They must be authored independently of the implementation agent and supplied alongside the governing documentation as input to the AI tangle. The implementer may add other tests, but must not change, weaken, or reinterpret the critical tests. If a critical test is wrong, insufficient, or ambiguous, stop implementation and return to Governing Documentation.
   4. If we did Brainstorm and Governing Documentation correctly, the implementation step becomes mostly mechanical and any modern LLM can do it - possibly even small local models; however in practice we can assume something like GPT-6 Luna or Gemini 3.7 Flash. An AI tangle is not completely deterministic, and implementation may expose missing cases or mistaken assumptions. When that happens, we stop implementation and return to Governing Documentation rather than letting the implementer silently invent policy.
   5. Wrap Up is important to cross every t and dot every i; preserve knowledge such as lessons learned during the session; make sure any necessary follow-up is recorded so we don't forget about it; and so on. Knowledge worth retaining, including unresolved follow-up work, must be recorded outside the transient chat in an appropriate durable project artifact so that future sessions can find and use it. The workflow determines the appropriate location and format. But Wrap Up is also an opportunity to look at the session and discuss how we did. Was the workflow useful? Can we improve it? Did the AI struggle? Did we make mistakes, and how do we avoid them in the future? And so on. This step is much more important than it may appear.
   6. Moving from one phase to the next always requires user approval. A phase may be waived with explicit user approval when the normal sequence does not fit the work, such as investigation or operational work, but the waiver must be justified. Any durable implementation change must be reflected in durable documentation before the change is considered complete.

5. **FOCUS**. I think another reason for our problems has been tackling too many things at once. One session - the chat thread in which the user and root agent collaborate - should be focused on one thing. Anything else that comes along should be deferred to another session. If it is blocking, preserve the context needed to resume the original work, for example in a document or TODO item. We may address the blocker in another session, or convert the current session to the blocker and resume the original work in a new session.

6. **Credit optimization.** This has been the major source of complexity and problems. I don't want to give up on it yet, because it's very important, but I'm willing to drop it completely if we cannot solve this satisfactorily.
   1. We have two fixed pools of credits - ChatGPT (for Codex) and Google (for Gemini in Antigravity). We want to make use of Gemini when we can in order to save ChatGPT credits for what's more important. For example, Gemini Flash can take care of the implementation phase most of the time. Update: the newest Gemini Flash is more capable and therefore even better suited to offload tasks to.
   2. The active Codex routing policy uses GPT-6 Luna, GPT-6 Sol, and GPT-6 Astra. The following planning multipliers are simplified approximations based on official standard API short-context input and output prices, not published Codex credit rates: Luna is the 1x baseline, Sol is 20x Luna, and Astra is 100x Luna. The goal is to offload as much work to Luna as possible while using Sol and Astra when their additional capability justifies the cost.
   3. I have learned through almost a couple months of practice that the best approach is:
      - GPT-6 Sol leads discussion, design, policy judgment, and synthesis. GPT-6 Luna handles repository and tool work by default, even when it appears small, because Sol can underestimate the cost of tool-call loops and Sol output. Reviewing a concrete plan before uncovered work begins lets me stop or simplify unnecessary work and checks. RULES explains how to route work and preserve my authority.
      - Keep a Codex-wide log of meaningful feedback on agent and skill use from Wrap Up, including my assessment when I provide one, to help refine the skills and identify classes of work that may not need plan approval. Log entries are evidence, not policy or authorization. Changes to skills, including which work needs plan approval, require my explicit approval.
      - GPT-6 Astra only when unusually complex problem-solving or review justifies its expense.

## Non-goals

1. Replacing the user as the author and decision-maker for the governing documentation.
2. Allowing the AI to move between phases, skip phases, or make undocumented policy decisions without user approval.
3. Expanding a session to absorb unrelated work instead of recording and deferring it.
4. Making implementation succeed at all costs when it reveals a problem in the documentation.
5. Optimizing credit use at the expense of simplicity, clarity, or the quality of the result.
6. Creating complicated agent swarms, elaborate agent protocols, ceremony, or paperwork that do not directly help us do the work. We want the most practical and SIMPLE solution that solves our problem.

---

[Table of contents](README.md) · Previous: [AI-Assisted Literate Programming](ALP.md) · Next: [Getting Started](book/getting-started.md)
