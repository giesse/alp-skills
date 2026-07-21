# TODO

Part of the [ALP Skills Book](README.md). Previous: [Legacy Reconciliation and LLM Wiki](book/legacy-reconciliation-and-llm-wiki.md).  Next: none — end of the appendices.

## Priority 1 — Tasks we are working on right now

- [x] Establish the ALP Skills repository foundation: governing Book, canonical source-layout design, navigation, and migration boundary from the old Antigravity repository. Canonical source import remains deferred.
- [ ] Resolve and codify the repository knowledge lifecycle before the first GitHub publication. Define portable repository knowledge, per-clone and user-local bindings, condition-bound advisories, precedence and retirement rules, lazy local onboarding, clean-checkout behavior, and treatment of existing external-path dependencies. Use the recorded [knowledge lifecycle brainstorm](wiki/sources/knowledge-lifecycle-brainstorm-2026-07-19.md) as deferred evidence, not current policy. This is a publication blocker.
- [ ] Reconcile and, if approved, codify delegation economics around preserving expensive root Codex context: use Luna freely for bounded exploration, multi-file discovery, command-heavy investigation, test/log output, and structured extraction; constrain the returned evidence packet rather than the exploration budget; and treat delegation as net-negative only when briefing, reconciliation, or judgment risk outweighs that benefit. Define the root's minimum reading boundary, a broad-enough Luna evidence boundary, outside-sandbox dispatcher preflight requirements for writable `~/.codex` state, and a separate diagnostic path for missing terminal worker output.
- [x] Initialize the LLM wiki with its index, log, provenance rules, and legacy source inventory; do not promote any old material to current knowledge.
- [ ] We need AI responses to contain the current phase. I often lose track of where we are in investigation-heavy tasks. This is a good candidate for a custom UI but that's out of the scope of this repository.
- [ ] Keep TDD as the preferred implementation approach when a meaningful executable oracle can be prepared. Do not make TDD universal: use the approved static, manual, runtime, telemetry, rollback, or other observable oracle where an executable test would be synthetic, unsafe, or impractical.
- [ ] Import and reconcile the selected old Antigravity wiki and seed material against current installed skills and TG ALP design documents before promoting any imported claim to current knowledge.
- [ ] Reconcile the existing ALP design chapters from the development workspace
  into this Book's reader order. Preserve their approved intent and evidence,
  but do not leave them as a parallel external source of truth.
- [ ] Design and validate a portable seed wiki and repository guide for new
  projects. It should provide durable ALP and memory foundations without
  copying legacy model names, commands, layout rules, or project-specific
  knowledge; adoption by an existing project must include local discovery and
  reconciliation.
- [x] Import the exact active installed-skill baseline into the canonical source tree: both Codex skills, active role profiles, dispatcher and EC-linter code with their tests, and the Antigravity companion. This baseline does not install or alter external artifacts.
- [ ] Create deterministic validation and drift-aware synchronization tooling for the canonical source tree, as described in [Canonical Sources and Installation](book/canonical-sources-and-installation.md).

- [ ] Evaluate GitHub Spec Kit and other relevant specification-driven
  practices against ALP. Consider artifact flow, project principles, reusable
  templates, and deterministic cross-artifact checks; adopt only ideas that
  improve clarity or portability without replacing the Book, phase ownership,
  or evidence model. Start from the recorded
  [Spec-driven development research](wiki/sources/spec-driven-development-research-2026-07-19.md).

## Priority 2 — Tasks we will work on next

- [ ] Write the **Installation** chapter. It must explain the supported installation and synchronization workflow from the canonical repository, distinguish it from this baseline import, and preserve the external-artifact authority boundary.
- [ ] Write the **Getting started** chapter. It must give a new project a small, safe first-use path through the Book, repository guide, TODO, wiki, and phase gates.
- [ ] Write the **Companion Antigravity skill** chapter. It must explain the companion's purpose, contract boundary, relationship to the Codex workflow, and the conditions for a safe handoff without treating its installed copy as governing source.

## Priority 3 — Tasks we will work on in the future

- [ ] Specify and validate a portable ALP pseudo-code dialect for Full ALP Books. Define its intended audience, exact and intentionally abstract forms, ambiguity boundaries, and representative tangle/reader validation before making it a governing requirement. The legacy Python-oriented bracket dialect is historical evidence, not the adopted dialect.

---

Part of the [ALP Skills Book](README.md). Previous: [Legacy Reconciliation and LLM Wiki](book/legacy-reconciliation-and-llm-wiki.md).  Next: none — end of the appendices.
