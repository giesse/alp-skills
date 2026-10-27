---
name: maintain-repository-wiki
description: Create, audit, organize, synthesize, or update a tracked repository-local LLM wiki that preserves portable, non-governing knowledge for future humans and agents. Use when initializing wiki/index.md, recording durable session knowledge, importing or reconciling evidence, improving wiki navigation and provenance, or checking repository memory for staleness, conflicts, secrets, or non-portable content.
---

# Maintain a Repository Wiki

Preserve useful working knowledge independently of any machine, chat, model,
or coding harness. Keep the wiki concise and trustworthy without turning it
into governing documentation or compulsory paperwork.

Write wiki guidance in plain language. Prefer familiar words, keep specialized
terms when they make meaning clearer, and explain them briefly when needed.

## Respect the surrounding workflow

Follow the consuming repository's instructions and governing documentation.
Surface conflicts instead of resolving them silently.

Let separately applicable repository instructions or an invoked workflow
govern routing, delegation, authorization, and phase transitions. Do not
impose the complete ALP delivery workflow when this skill is used alone.

Do not treat wiki work as permission to implement unrelated changes or move
between workflow phases.

## Preserve the wiki's role

Use the tracked repository-local wiki as working memory for future humans and
agents. Do not let it replace, override, or silently reinterpret the Book,
other governing documentation, or an explicit user decision.

When a proposed wiki claim would change material intent, stop. Update and
approve the governing documentation first.

Keep the repository portable from a clean clone. Exclude secrets and
machine-local, user-local, per-clone, or otherwise non-portable values and
notes. A portable page may explain that local knowledge is needed and how to
discover it without assuming a particular local value or artifact exists.

## Maintain the entry point

Maintain `wiki/index.md` as the mandatory compact entry point. Ensure the
repository's `AGENTS.md` points to it as the entry point for substantive
repository investigation.

Use the index to route readers to current knowledge in the wiki and to useful
durable documents elsewhere in the repository. Link rather than duplicate a
document merely to place it under `wiki/`.

Keep knowledge concise, searchable, interlinked, and reachable from the index.
Do not present superseded, historical, inferred, or unresolved material as
current guidance.

## Preserve evidence and status

Use `wiki/sources/` for external sources and historical evidence worth
preserving. Treat sources as evidence, not automatically as current knowledge,
governing intent, or ground truth about what the project should do.

Preserve enough provenance and status to distinguish:

- approved intent;
- current evidence;
- historical or superseded evidence;
- inference;
- unresolved work; and
- history retained only for context.

Use the lightest notation that keeps these distinctions clear. Do not add
labels or metadata merely for ceremony.

Reconcile a material conflict against current governing documentation,
evidence, and user decisions before presenting a claim as current. If
authority or intent remains unclear, record the uncertainty or return it to the
user.

## Perform wiki work

First distinguish the requested mode:

- For a read-only audit, inspect and report without changing the wiki,
  navigation, sources, or governing documentation.
- For approved maintenance, initialization, or repair, make only the changes
  within the authorized scope.

For either mode:

1. Read `wiki/index.md` when it exists, applicable governing documentation,
   and only the existing pages or sources needed for the task. When
   initialization is authorized and the index is absent, establish its
   minimal required role without inventing unsupported knowledge.
2. Identify the knowledge worth preserving and its status.
3. Check portability, provenance, freshness, conflicts, and governing
   boundaries.
4. Report the evidence, conclusions, inspected scope, uninspected scope, and
   unresolved questions.

For an approved change:

1. Update the smallest useful set of pages and index links.
2. Remove or clearly demote stale navigation when it misrepresents current
   knowledge.
3. Verify links, discoverability from `wiki/index.md`, and the absence of
   secrets or non-portable assumptions.
4. Report what changed and the evidence supporting it.

When initializing a wiki, create only the entry point and pages justified by
real knowledge. Do not manufacture empty sections or speculative structure.

Maintain the wiki during Wrap Up only when doing so preserves knowledge worth
retaining or improves reliability and discoverability. Do not require an
update merely to prove that Wrap Up occurred.

Do not create `wiki/log.md` by default. Add chronological activity history
only when a concrete need justifies maintaining it, and never use it as a
second record of governing decisions.
