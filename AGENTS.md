# ALP Skills Repository Guide

Start with the [Book table of contents](README.md), then read the relevant Book chapter, [TODO](TODO.md), and [wiki index](wiki/index.md). The Book is the governing source for this repository's design; this guide explains how to keep that design, its operational artifacts, and durable knowledge aligned.

## Scope and authority

- Work only inside the approved file boundary for the current task.
- Treat installed Codex and Antigravity artifacts as external evidence unless the user explicitly authorizes an installation or synchronization operation.
- Do not promote material from `wiki/sources/` to current guidance without a recorded reconciliation against the Book, current operational evidence, and explicit user decisions.

## Governing documentation and implementation

For non-trivial work, use the ALP delivery workflow: brainstorm, approve the appropriate governing document, implement only the approved boundary, then review and wrap up. Full ALP Books must remain readable and tangle-ready; do not let code, tests, or legacy source material silently choose design intent. Use the ALP authoring skill when working on book chapters in this repository.

Use TDD when a meaningful executable oracle is practical. When it is not, state and preserve the approved static, manual, runtime, telemetry, rollback, or other observable oracle instead of manufacturing a synthetic test.

## Wiki and wrap up

The wiki has three layers: immutable evidence under `wiki/sources/`, reconciled current knowledge under `wiki/`, and navigation/history in `wiki/index.md` and `wiki/log.md`. A lasting lesson, source reconciliation, or accepted operational decision belongs in a current wiki page, linked from the index and recorded in the log. Do not create wiki bookkeeping merely to prove that work happened.

Every Book chapter and appendix links to the README and to its reader-order neighbors at both top and bottom. Preserve that navigation when adding or moving chapters.
