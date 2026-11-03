# Installation, Updating, and Validation

[Table of contents](../README.md) · Previous: [Canonical Sources and Derived Artifacts](canonical-sources-and-derived-artifacts.md) · Next: [Workflow Rules](../RULES.md)

The skill folders in this repository (`codex/skills/` for Codex and `antigravity/skills/` for Antigravity) are the maintained source. Installing them gives your coding harness local copies it can use across your projects. Changes pushed to GitHub do not automatically update those installed copies.

These instructions cover both Codex and Antigravity. The complete workflow, `run-alp-workflow`, requires its companion, `delegate-work`. Installing all four also makes the Book-authoring and repository-wiki skills available.

In Codex, the installation directory depends on your Codex setup, so let its installer choose the supported user-level location.

In Antigravity, user-level skills are installed in `~/.gemini/config/skills/<skill-name>/` so they are available across workspaces (while `.agents/skills/<skill-name>/` is used for workspace-specific skills).

## Install the skills

### Codex

Ask Codex:

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

After installation, check that the four skills appear in Codex’s skills list. If they do not appear, restart Codex and check again. This confirms that Codex can discover them; it does not exercise the workflows themselves. For more Codex skill guidance, see [Build skills](https://learn.chatgpt.com/docs/build-skills).

### Antigravity

Ask Antigravity:

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

After installation, check that the four skill folders (`delegate-work`, `run-alp-workflow`, `author-alp-book`, and `maintain-repository-wiki`, each containing `SKILL.md`) are present in `~/.gemini/config/skills` and appear in Antigravity’s skills list or `/` command menu. If they do not appear, start a new conversation or reload Antigravity and check again. This confirms that Antigravity can discover them; it does not exercise the workflows themselves.

## Update or roll back

Installed skills do not update automatically. You can optionally use [GitHub Watch settings](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications) to follow repository activity. Starring the repository bookmarks it; it does not subscribe you to notifications. Notifications and repository changes do not update installed skills.

### Codex

When you want to update your Codex skills, ask Codex:

```text
Update my installed ALP skills from the codex/skills directory in
https://github.com/giesse/alp-skills. Locate the existing copies and check
for local customizations. Ask me about any changes that need my decision
before replacing them. Preserve backups outside the skill discovery
directories, install the replacements in the existing locations, and verify
the installation. If the update fails, restore the previous copies. Report
what changed and where you saved the backups.
```

### Antigravity

When you want to update your Antigravity skills, ask Antigravity:

```text
Update my installed ALP skills in ~/.gemini/config/skills from the
antigravity/skills directory in https://github.com/giesse/alp-skills.
Locate the existing copies and check for local customizations. Ask me
about any changes that need my decision before replacing them. Preserve
backups outside ~/.gemini/config/skills and any workspace skill discovery
directories, install the replacements in the existing locations, and verify
the installation. If the update fails, restore the previous copies. Report
what changed and where you saved the backups.
```

Keep the backups until you are satisfied with the updated skills. To roll back, ask your agent to restore those saved copies.
