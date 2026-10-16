# Maintaining Repository Memory

[Table of contents](../README.md) · Previous: [Authoring an ALP Book](authoring-alp-books.md) · Next: [Canonical Sources and Derived Artifacts](canonical-sources-and-derived-artifacts.md)

## Why repository memory

My use of repository memory predates ALP. With early coding agents such as
Cline and Roo Code, I found myself explaining the same things repeatedly. I
began building a knowledge base for the agent, initially as a knowledge graph:
a `root.md` file linked to other knowledge nodes, which could link to further
material.

When I encountered Andrej Karpathy's LLM Wiki idea, it seemed a natural fit for
what I was already doing. A repository wiki could preserve knowledge about the
project, research findings, and other useful context that would otherwise
disappear into conversations.

This helped establish the separation between the Book and the wiki. The Book
teaches human readers about the program and provides the governing explanation
for the AI tangle. The wiki preserves other useful knowledge for future agents
working on the repository.

That knowledge might include findings from an investigation, lessons from an
unsuccessful approach, or research that may inform later decisions. Preserving
it saves the human from repeating explanations and the agent from
rediscovering what previous sessions already established.

A tracked repository wiki remains useful even when an agent has built-in
memory. Its knowledge travels with a clone of the repository and is available
to other contributors and agents, independently of the original conversation
or coding harness.

## What belongs in the wiki

The wiki preserves knowledge that will help future work: findings that took
effort to establish, useful explanations of repository details, research,
unresolved questions, and lessons worth remembering. A concise account with
links to supporting evidence is usually more useful than making another agent
reconstruct the findings from a long conversation.

The status of that knowledge matters. Something directly observed, an
inference, an old finding, and an unresolved possibility have different
meanings. Keeping those distinctions visible helps future agents decide what
they can reuse and what needs checking again.

The wiki does not establish what the program should do. For example, an
investigation might discover that the existing notification code retries
indefinitely. That is useful knowledge about the implementation, but it does
not establish that unlimited retries are intended. Deciding the retry policy
belongs with the human author and the governing documentation.

Research preserved in the wiki may inform such a decision. When it would
change material intent, the governing documentation needs to be updated and
approved before that interpretation becomes guidance for implementation.

The wiki can also point to approved decisions and explain where to find them.
Linking to their governing source keeps that authority clear and reduces the
chance that a remembered summary becomes a competing rule.

## Keeping knowledge findable and portable

Preserved knowledge is useful when a future agent can find the relevant part
without reading everything. The workflow uses `wiki/index.md` as a compact
entry point, and the repository's `AGENTS.md` points to it. Before substantive
repository investigation, the worker consults that index and follows the links
relevant to its task.

The index can also point to useful documents elsewhere in the repository.
Moving or duplicating them merely to put everything under `wiki/` would create
more maintenance work without necessarily improving discovery.

Supporting research and historical material can be preserved under
`wiki/sources/`. The maintained wiki explains what we learned from those
sources and links back to the evidence. Keeping that relationship visible
helps future agents understand where a claim came from and whether it still
applies.

Portability matters because the wiki travels with the repository. Its
explanations should remain useful in a clean clone, independently of the
original author's machine or account. Machine-specific paths, personal
settings, secrets, and other local knowledge belong outside the tracked wiki.
Where local information is needed, a portable page can explain how to discover
it.

This structure gives future sessions a starting point and supporting evidence
while allowing the wiki to grow around the project's actual needs.

## Maintaining the wiki during normal work

Wrap Up is a natural time to preserve knowledge. The session is still fresh,
and we can identify what another human or agent would benefit from knowing
later. A useful update might record a difficult finding, explain why an
approach failed, or preserve an unresolved question with enough context to
continue investigating it.

`$maintain-repository-wiki` helps turn that material into concise, connected
repository knowledge. It can also support a dedicated research or
wiki-maintenance session, although most updates will arise from ordinary
project work.

Maintenance includes revisiting existing knowledge. When new work changes an
earlier understanding, updating the relevant explanation helps prevent the
next agent from following obsolete guidance. Links to supporting evidence and
clear wording about what remains uncertain make that work easier.

The amount of maintenance should reflect its value. A session that teaches us
nothing worth retaining does not need a wiki update merely because it reached
Wrap Up. Equally, preserving a useful finding may require only a small
correction or a link from an existing page.

The aim is a wiki that reduces repeated work and helps future sessions make
better-informed decisions. Keeping it concise, findable, and trustworthy
matters more than recording every activity.

---

[Table of contents](../README.md) · Previous: [Authoring an ALP Book](authoring-alp-books.md) · Next: [Canonical Sources and Derived Artifacts](canonical-sources-and-derived-artifacts.md)
