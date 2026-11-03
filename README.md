# ALP Skills Book

This repository provides skills that help coding agents support AI-Assisted
Literate Programming (ALP): authoring program Books, guiding development
sessions, and maintaining repository knowledge.

This repository is licensed under the [MIT License](LICENSE).

This Book explains the approach, the goals behind these skills, and how to use
them.

**Start with [AI-Assisted Literate Programming](ALP.md)**, the first chapter. It
introduces ALP and the role of the human author, the Book, and the AI. Follow the
chapters in order, or use the table of contents to revisit a topic.

## Quick start

Both Codex and Antigravity are supported. The complete workflow,
`run-alp-workflow`, requires its companion, `delegate-work`.

### Codex

Ask Codex to install the four skills from this repository for your user account,
so they are available across projects:

```text
Use $skill-installer to install these skills from
https://github.com/giesse/alp-skills for my user account, so they are
available across projects:

- codex/skills/delegate-work
- codex/skills/run-alp-workflow
- codex/skills/author-alp-book
- codex/skills/maintain-repository-wiki

Use the installation location supported by this Codex setup. If any are
already installed, report their locations before replacing anything.
```

After installation, check that all four skills appear in Codex’s skills list.
If they do not, restart Codex and check again.

### Antigravity

Ask Antigravity to install the four skills from this repository for your user
account, so they are available across projects:

```text
Install these skills from https://github.com/giesse/alp-skills into
~/.gemini/config/skills for my user account, so they are available
across projects:

- antigravity/skills/delegate-work
- antigravity/skills/run-alp-workflow
- antigravity/skills/author-alp-book
- antigravity/skills/maintain-repository-wiki

If any are already installed in ~/.gemini/config/skills or the current
workspace, report their locations before replacing anything.
```

After installation, check that all four skills appear in Antigravity’s skills
list or `/` command menu. If they do not, start a new conversation or reload
Antigravity and check again.

See [Installation, Updating, and Validation](book/installation-updating-and-validation.md)
for updates and rollback.

## Table of contents

1. Introduction
   1. [AI-Assisted Literate Programming](ALP.md)
   2. [Goals and Non-Goals](GOALS.md)
   3. [Getting Started](book/getting-started.md)
2. The Skills
   1. [Choosing and Combining the Skills](book/choosing-and-combining-skills.md)
   2. [Running an ALP Workflow](book/running-alp-workflow.md)
   3. [Authoring an ALP Book](book/authoring-alp-books.md)
   4. [Maintaining Repository Memory](book/maintaining-repository-memory.md)
3. Maintaining This Repository
   1. [Canonical Sources and Derived Artifacts](book/canonical-sources-and-derived-artifacts.md)
   2. [Installation, Updating, and Validation](book/installation-updating-and-validation.md)
4. Appendices
   1. [Workflow Rules](RULES.md)
   2. [Project TODO](TODO.md)

## Repository resources

- [Repository instructions](AGENTS.md)
- [Repository wiki](wiki/index.md)
