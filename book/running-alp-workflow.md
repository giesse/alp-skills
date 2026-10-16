# Running an ALP Workflow

[Table of contents](../README.md) · Previous: [Choosing and Combining the Skills](choosing-and-combining-skills.md) · Next: [Authoring an ALP Book](authoring-alp-books.md)

## Start with one goal

Invoke `$run-alp-workflow` and tell the agent what you want to accomplish. The
workflow loads its required `$delegate-work` companion; you do not need to
invoke that separately. You can begin with a rough idea; clarifying it is part
of the work.

Keep the session focused on that goal. If something unrelated comes up, record
it for later rather than letting the session grow around it.

The normal phases are Brainstorm, Governing Documentation, Implementation, and
Wrap Up. The agent should state the current phase and obtain your approval
before moving to another. You may explicitly waive a phase when it does not fit
the work; explain the reason.

## Brainstorm

Brainstorm helps you work out what you mean to do. You might know the outcome
you want without knowing how to achieve it, or have a proposed solution without
being sure it addresses the real problem.

The AI asks questions, acts as a sounding board, and helps you identify
assumptions, ambiguity, constraints, and important cases you may have missed.
You remain responsible for deciding the goal and which approach to pursue.

For example, "add notifications" leaves many questions open: who should receive
them, which events matter, and what recipients should be able to control.
Brainstorm helps expose those questions before a plausible implementation
silently answers them for you.

You do not need a separate brainstorming document or a complete specification.
The result may remain in the conversation. You are ready to propose moving to
Governing Documentation when you have enough clarity to begin writing the
explanation that will govern implementation.

## Governing Documentation

This is where you develop the explanation that will govern implementation. For
ALP, that explanation belongs in the Book. Writing and approving it is the
central work of the session.

You remain the author and decision-maker. Normally, you write the first draft
or a significant part of it, but you do not have to work alone. A useful
approach is to ask the AI to pose focused questions, answer in your own words,
and have it propose passages that you then edit and refine. Your answers,
decisions, and revisions give the writing its substance.

The AI can also research the existing system, identify gaps, suggest
alternatives, and improve the wording. When an important decision remains
unresolved, it should bring the question back to you.

Develop the Book until a reader can understand the intended behavior and its
reasoning, and an implementation agent can proceed without inventing material
decisions. You do not need to prescribe every detail. You do need to settle
choices whose consequences matter.

### Define acceptance before implementation

Before implementation begins, decide what evidence will show that the result
satisfies the Book. Agree on the decisive tests or other checks, have them
designed independently of the implementation agent, and approve them alongside
the documentation.

This reduces how much you need to trust the implementer. The agent receives
both the explanation of what to build and independently established criteria
for judging the result. It can add useful checks, but it cannot change,
weaken, or reinterpret the approved critical checks to make its implementation
pass. This makes it more practical to assign implementation to a cheaper agent
once the important decisions are settled.

Defining checks also tests the clarity of the Book. Asking "how would we know
this is correct?" can expose vague promises, missing cases, and decisions we
have not actually made. Those discoveries belong in Governing Documentation,
while we can still clarify the intended behavior before code is written.

For example, "respect notification preferences" may sound clear until we try
to define a check. What should happen if someone changes their preferences
after a notification has been queued? Writing the check exposes a decision
that the Book needs to settle.

The checks need not all be automated tests. Use the evidence appropriate to
the work, and check that it covers the important promises and boundaries.
Make any remaining evidence limitations explicit.

If implementation later reveals a faulty critical check or an unresolved
material decision, return to Governing Documentation and correct it with the
human author.

When the documentation and acceptance checks are ready, explicitly approve the
transition to Implementation.

## Implementation

Implementation is where the explanation in the Book becomes working software.
The work done in the earlier phases should make this comparatively
straightforward: the important decisions are settled, and the implementer has
checks designed independently of the implementer and approved by the human.
These checks help establish whether it has understood those decisions. That
makes it practical to use a cheaper agent for much of this work.

There is still judgment involved. The Book leaves ordinary implementation
choices open, and translating an explanation into code can reveal something
we overlooked. A missing case or ambiguous promise is useful feedback about
the Book. Returning to Governing Documentation lets the human resolve it
deliberately, before an implementation choice becomes accidental policy.

Tests and other checks provide evidence about the result. Running suitable
tests before implementation can establish that they detect the missing
behavior; running them afterward helps show that the implementation supplies
it. Review can provide additional evidence where tests leave important
questions open. Each form of verification has limits, which should remain
visible when judging the result.

The phase should leave us with an accepted implementation whose material
behavior agrees with the Book. Keeping both aligned preserves the explanation
behind the software that was actually built and verified.

## Wrap Up

A completed change leaves more behind than code. We may have learned something
about the system, discovered a limitation, deferred useful work, or found a
better way to collaborate. Wrap Up gives those findings a durable home so that
future sessions can benefit from them.

It also provides a final opportunity to check that the Book and implementation
still tell the same story. Useful working knowledge belongs in the wiki;
decisions that govern the program belong in its governing documentation.

Just as importantly, Wrap Up is a conversation about how the work went. An
agent may have produced correct code while taking an unnecessarily complicated
route. A check may have exposed an important misunderstanding early. Discussing
these experiences helps us understand what to repeat and what to improve.

Meaningful feedback about agents and skills goes into the shared workflow
feedback log, where it can inform later improvements across projects. The
agent's observations and the human's assessment should remain distinguishable,
and proposed policy changes still need human approval.

The human's acceptance closes the work. Wrap Up should leave both a result the
human accepts and the knowledge needed to continue intelligently later.

---

[Table of contents](../README.md) · Previous: [Choosing and Combining the Skills](choosing-and-combining-skills.md) · Next: [Authoring an ALP Book](authoring-alp-books.md)
