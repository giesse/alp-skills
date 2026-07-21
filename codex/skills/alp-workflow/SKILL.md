---
name: alp-workflow
description: Orchestrate phase-gated repository work through Brainstorm, Governing Documentation, Implementation, independent review, and Wrap Up using Full ALP, Spec-driven, or Mechanical strategies. Use for non-trivial tasks, vague requirements that need refinement, ALP Books and AI-assisted tangling, specifications, critical acceptance oracles, implementation or Antigravity handoffs, repository workflow alignment, independent review, and durable TODO/wiki wrap-up.
---

# ALP Delivery Workflow

Use the least process that gives adequate confidence. The root Codex session is the orchestrator and control plane: it owns the user conversation, scope, material decisions, phase gates, acceptance meaning, worker reconciliation, and final synthesis. Repository `AGENTS.md`, `wiki/index.md`, and `TODO.md` are checked at each relevant phase.

## Strategies and gates

Choose one strategy in Brainstorm:

- **Full ALP:** an approved readable Book explains intent, rationale, unchanged behavior, compatibility, structured logic, affected files, adversarial cases, and observable acceptance oracles. It must be complete enough for the bounded `tangler` to tangle without material design judgment. Apply `alp-authoring` while authoring the Book; reading or tangling the approved Book does not reactivate it.
- **Spec-driven:** an approved behavioral or technical specification may leave ordinary implementation choices open.
- **Mechanical:** explicitly skip new governing documentation only for small, behaviorally unambiguous work allowed by repository guidance.

Start non-trivial work in Brainstorm unless the user explicitly waives it. Summarize every completed phase and ask for approval before the next phase. A user may authorize a named maximum batch of non-code phases; the orchestrator still summarizes each boundary and stops at that maximum. Such a batch never includes Implementation unless the user separately and explicitly authorizes Implementation. Stop earlier on a material design gap, contradiction, or scope boundary.

The governing document remains the source of truth. Every material behavior traces to a decision or acceptance criterion, every criterion has an oracle, and conflicts are reported rather than silently redesigned. Critical executable test semantics are owned independently when practical; weak or unsafe systems use their real static, manual, runtime, telemetry, or rollback oracle and state its limitation.

## Capability roles and delegation

Workflow vocabulary names capabilities, not model families. The six dispatchable profiles are `explorer`, `verifier`, `tangler`, `implementer`, `reviewer`, and `escalation_reviewer`; `orchestrator` is the root-only role. Current dated mappings are held in `CODEX_HOME/agents/alp_<role>.toml`: Luna low for exploration and verification, Luna medium for tangling and bounded specification implementation, Terra high for normal review, and Sol high for authorized or weak-oracle escalation review. Mapping changes do not change role authority.

Delegate only when the value gate predicts a concrete benefit: lower total credits for substantial bounded work, preservation of Codex quota through Antigravity's separate credit pool, noisy-output compression, genuinely independent insight, or useful latency. Compare briefing and reconciliation cost, quota, drift risk, and repair cost. Before the root performs a plausible bounded read-only discovery or deterministic-verification task, record a `Delegation decision`: either `dispatch <role> — <concrete benefit>` or `skip — <concrete reason>`. Multi-file search, session-log search, noisy factual output, and structured or tabular extraction default to `explorer` or `verifier`. A skip is valid only when the necessary evidence is already in one or two directly named small artifacts, material judgment or a weak oracle is required, briefing and reconciliation demonstrably outweigh the bounded benefit, or the dispatcher runtime is unavailable. This is a brief pre-work decision, not a per-command ceremony. Use `explorer` by default for credit-positive bounded repository/document/data discovery and `verifier` for exact commands or deterministic CSV, JSON, schema, aggregation, and structural checks. Keep conflicting evidence, weak oracles, and material production judgment with the root or review roles. Parallelize only for independent work with isolated writes and useful quota headroom; use one writer per shared checkout.

Give a fresh worker only the role, bounded task, relevant paths or supplied evidence, permissions, explicit timeout, response contract, and stop conditions. Require conclusion, evidence, uncertainty, and inspected/uninspected scope. Workers do not delegate recursively or decide material design, phase transitions, scope expansion, acceptance, or the meaning of failed evidence.

For the observable runtime path, invoke the stdlib dispatcher from this skill directory:

```text
python3 scripts/dispatch_worker.py --packet PATH|-
python3 scripts/dispatch_worker.py --diagnostic-log LOG --packet PATH|-
python3 scripts/dispatch_worker.py --probe-startup
python3 scripts/dispatch_worker.py --probe-startup --diagnostic-log LOG
```

Use `-` for one UTF-8 JSON packet line terminated by a newline; the dispatcher acknowledges receipt without waiting for terminal EOF. Packet schema version 1 rejects unknown fields and requires role, task, absolute `cwd`, sandbox no broader than the profile, positive timeout, non-empty stop conditions, and a closed response contract containing `blocked` plus `Conclusion`, `Evidence`, `Uncertainty`, `Inspected scope`, and `Uninspected scope`. The dispatcher resolves `CODEX_HOME/agents/alp_<role>.toml`, starts `codex app-server --disable multi_agent --listen stdio://` directly, authenticates as ChatGPT/Codex, confirms catalog support and selected model/effort/sandbox, starts one ephemeral fresh turn with fallback disabled and non-interactive approval, and returns one sorted JSON result with stable exit mapping on stdout. Normal dispatch never inherits the parent transcript or persists a protocol log, but emits bounded structured lifecycle records on stderr for packet receipt, parse, stage changes, turn start, heartbeat, and terminal outcome; those records contain no packet or worker-output text. Root-authorized diagnostic use requires a caller-selected `LOG` outside the packet `cwd`, created only with the required host permission and reserved for manual user inspection. Raw App Server stderr and JSON-RPC trace go only to that mode-`0600`, non-overwritten, 8 MiB continuously drained log; the dispatcher result reports only its path, truncation flag, stages, and attempts. `--probe-startup` creates no thread or turn. Fresh context remains the default correctness, independence, and quota boundary rather than a secrecy boundary.

Routing conflicts fail closed. A `model/rerouted` event interrupts the exact active turn once. A timeout interrupts once and ends that turn; never continue or replay it. Only a transport failure before `turn/start` may receive one local App Server restart. Any further replacement is a fresh, root-owned dispatch decision and the root may make at most one only when the packet can be tightened or a transient cause is known and delegation remains worthwhile.

The fixed worker envelope is locally validated: exactly `classification` and `sections`, allowed classification, exactly the required string sections, and no extra keys. `blocked` becomes dispatch status `blocked`; other valid classifications become `completed`. Stable statuses and exits are: completed/0, blocked/20, interrupted/21, routing_failure/22, turn_failure/23, transport_failure/24, invalid_result/25. A normalized failure is returned whenever initialization progressed far enough.

Do not create or invoke a model-backed contract-linter profile. EC-v1 mechanical checks use the deterministic `scripts/lint_ec.py`; semantic sufficiency, oracle strength, and phase approval remain root-owned. The linter's deterministic tests are separate from dispatcher tests.

## Phases

### 1. Brainstorm

Clarify goal, non-goals, constraints, risks, compatibility, likely files, task profile, strategy, and acceptance boundary from repository evidence. Resolve material choices and stop for approval to enter Governing Documentation or the explicitly authorized next phase.

### 2. Governing Documentation

Do not edit production code. Author or update the selected Book/specification and critical oracle semantics. For an external or materially fresh implementation, create a complete approved EC revision with explicit decisions, invariants, acceptance/validation coverage, out-of-scope, file boundary, test semantics, and questions. Run `python3 scripts/lint_ec.py` for mechanical EC checks, then perform semantic preflight. Stop on unresolved design or oracle gaps and ask for approval of the governing document, route constraints, and EC revision.

### 3. Implementation

Implement only the approved document and boundary. Select the actual route within the Phase 2 constraints; stop for approval rather than broadening them. For Full ALP, use `tangler` regardless of size; if tangling needs material judgment, return to Governing Documentation and repair the Book. For Spec-driven work, use `implementer` only when its bounded implementation discretion is sufficient; retain judgment in the root or seek a newly approved route otherwise. Small Mechanical work may remain in the root.

Before a materially fresh handoff, prepare and conformance-check any practical approved critical oracle independently when that buys confidence. Use red-before-green only when meaningful; preserve approved static, manual, runtime, telemetry, or rollback evidence when executable coverage would be synthetic or unsafe. Never silently patch an approved EC; issue a complete replacement revision after updating approved intent. Do not authorize production, database, destructive, or out-of-scope actions.

For an external handoff, supply the complete governing document or EC, exact file boundary, test semantics, and stop conditions. Require acknowledgment and conflict reporting. Treat an extra required file or changed critical-test semantics as a scope conflict. For Antigravity, bring the initial plan to the root for one conformance review and permit at most one focused correction unless a concrete blocker remains; do not require exhaustive contract-ID annotation. Require a compact evidence packet covering changed files, validation, deviations, unresolved concerns, acceptance coverage, repository discoveries, durable-learning suggestions, and workflow friction.

### 4. Independent Review and Wrap Up

Every non-trivial implementation gets a fresh read-only `reviewer`. Use `escalation_reviewer` for user-authorized Sol review or the weak-oracle production gate; approval to enter Implementation authorizes that gate unless explicitly waived. If that runtime is unavailable, stop before production-affecting completion and ask whether to wait, substitute another assurance measure, or accept the labeled review gap. A fresh `verifier` may independently review documentation/data-only work only when scope has no production-code behavior or operation, the oracle is deterministic, the packet is read-only and fresh, no walkthrough or inherited task conversation is supplied, and no material interpretation, conflict resolution, policy choice, or acceptance judgment is needed. Otherwise use `reviewer`; the root always decides whether the evidence satisfies acceptance.

Review the governing document, final diff, and independent evidence before any walkthrough. Every reviewer packet must explicitly state the session goals used for deferability assessment. If session goals are absent or materially ambiguous, the reviewer returns `blocked` rather than inventing an assessment. Findings require exact evidence, affected criterion/invariant, non-acceptance reason, closure condition, and a clear statement: `Deferrable without affecting stated session goals: yes | no | uncertain — <brief reason>`. The root/user retains sole authority to decide whether any deferrable finding is actually deferred; a deferrable classification does not defer, downgrade, or accept the finding. Reconcile once; do not invent improvements when no finding exists. After acceptance, update manifested follow-ups and durable TODO/wiki knowledge only when it changed, including required indexes/logs; update the governing document if accepted implementation changed the design. Return one compact packet with changed files, validation, review, deviations, residual risks, and classification. A successful Wrap Up ends the workflow without an acceptance-only turn; a correction reopens the appropriate phase.
