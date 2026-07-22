# Native Worker Delegation

[ALP Skills Book](../README.md) · Previous:
[EC Linter](ec-linter.md) ·
Next: [Repository Charter](repository-charter.md)

## Why delegation is native now

For the sake of saving token credits (or more direct costs if you are using the
API), our workflow makes use of workers that can inspect a broad repository,
implement an approved boundary, or independently challenge a result without
filling the root conversation with command output and local detail. The former
Python/App Server dispatcher was a workaround for a broken version of
`spawn_agent` in some versions of Codex. Native `spawn_agent` delegation has
now supplied the needed worker boundary directly, so we retire that workaround
rather than maintaining two internal delegation transports.

Native delegation is one of two common Implementation routes. It is the
internal route for bounded Codex work. A manual or external handoff to
Antigravity, or where appropriate Gemini Flash, instead uses the complete,
revisioned EC governed by [Execution Contracts and Evidence](execution-contracts-and-evidence.md).
Both routes implement the same approved intent, but they do not share a
transport or envelope.

The root uses native delegation to give a fresh worker a small, self-contained
packet and receives a compact evidence packet in return. This is a context and
assurance design, not a claim that a worker is infallible. Root-context
minimization is a primary constraint: broad repository discovery and noisy
evidence belong with the bounded worker, while the root receives only the
conclusion needed to make the next material decision.

```mermaid
flowchart LR
    U[User and Sol root] --> P[Approved, narrow task packet]
    P --> N[Native fresh worker]
    N --> E[Compact evidence packet]
    E --> S[Sol and user reconcile meaning]
    S --> G[Phase gate or next bounded task]
```

This chapter governs the native route's delegation policy and outcomes, not a
particular native-tool call form or the manual EC route. Platform invocation
details may evolve; an implementation must use the native surface so that the
worker receives no broader repository or conversation context than the
approved packet requires.
It must not recreate an App Server bridge, a Python dispatcher, a daemon, a
scheduler, a transcript store, or another orchestrator.

## The authority boundary

> [!note]
>
> Model names assume OpenAI and Codex, as of July 2026. We might reword this to be more generic in the future, or simply keep it up to date with current model names and roles.

**Sol is the default root orchestrator.** Sol and the user own the material
thinking: user dialogue, material decisions, scope, phase gates, delegation,
the meaning of acceptance, reconciliation of the compact worker reports, and
final synthesis. Selecting a worker does not transfer any of those powers.

Sol deliberately does no repository work. It must not read or summarize
repository or source material, edit files, implement, run tests or
deterministic verification, or perform review. The sole narrow exception is
checking an independently authored test specification or test file only to
confirm that it expresses user-approved requirements. That check does not
extend to judging implementation evidence or inspecting the implementation.

The **root Sol orchestrator** is not the separately spawned
`alp_escalation_reviewer` worker, even though both use Sol. The retained
profile is a fresh, read-only escalation-review worker. It may perform a full
repository review only when the user explicitly authorizes that particular Sol
review. Its profile text can never authorize the root Sol orchestrator to read
the repository or evidence. Terra remains the normal, default fresh reviewer
to conserve credits. The root may recommend a Sol escalation review when risk
or an oracle limitation warrants it, but neither risk nor a weak oracle starts
one automatically: explicit user approval is required.

Luna handles bounded discovery, summarization, documentation, implementation,
and deterministic verification. Terra handles repository work that needs
stronger judgment and every normal independent review. Existing native
capabilities or profiles may be chosen according to task risk, but they do not
alter this authority map and this chapter creates no new orchestrator profile.
The retained escalation-review profile already represents a separately spawned,
user-authorized Sol worker and remains unchanged by this revision.

| Actor | May do | Must not do |
| --- | --- | --- |
| User and Sol root | Set and revise approved intent; select bounded work; approve phases; reconcile compact reports; decide acceptance and final synthesis. | Read, summarize, edit, implement, test, verify, or review repository work; treat a worker report as self-proving. |
| Luna worker | Bounded discovery, extraction, documentation, implementation, and deterministic verification within an approved packet. | Decide material design, phase authority, scope expansion, acceptance, or recursive delegation. |
| Terra worker | Stronger-judgment repository work and the default fresh independent review. | Take the root's material-decision, phase, scope, acceptance, or recursive-delegation authority. |
| Separately spawned Sol escalation reviewer | A full, fresh, read-only repository review after explicit user authorization for that review. | Act as root Sol, start from risk or a weak oracle alone, edit, delegate, authorize a phase, or decide acceptance. |

Platform-mandated instruction reads are outside this repository-work policy;
this chapter does not try to govern them.

## A narrow packet, not a borrowed transcript

Before native delegation, Sol makes the delegation decision and prepares a
standalone packet. It contains only the approved task, role or capability,
exact repository boundary, supplied evidence or relevant paths, allowed
permissions, stop conditions, and the required compact response. A worker
starts with fresh, narrow context rather than the root transcript. It may read
and act only inside the packet boundary and reports a conflict rather than
silently widening it.

> [!important]
>
> Codex's `spawn_agent` tool may *require* not sharing the context with the root in order to allow specifying a different model and reasoning effort. Therefore the decision here is not only for isolation, but probably necessary for this to work at all.

Every response distinguishes at least:

- conclusion or current status;
- concrete evidence and commands or observations where applicable;
- uncertainty or a precise blocked reason;
- inspected scope; and
- uninspected scope.

Implementation and review packets additionally identify changed files or the
reviewed diff, oracle results, deviations, and residual risks. Raw command
logs, broad repository listings, and a worker's private reasoning are not a
root response format. Sol reconciles these compact reports with the user; it
does not rerun their checks or independently inspect their implementation
evidence.

Freshness and narrow packets protect correctness, independent judgment, and
root context. They are not a secrecy boundary and do not enlarge any native
permission ceiling.

Native `spawn_agent` does not provide an enforceable task timeout, so a timeout
is omitted by default and must not be presented as a control the workflow can
guarantee. A packet may include an advisory time budget or checkpoint
expectation when useful. It must be labelled advisory: reaching it requests a
status or root decision but does not prove interruption, cancellation, or
worker termination.

## Native delegation lifecycle

The normal lifecycle is deliberately short and has one owner at every point.

1. **Gate and packet.** Sol and the user retain the approved phase, scope,
   acceptance meaning, and stop conditions. Sol selects a suitable native
   worker and sends the narrow packet.
2. **Bounded work.** The worker performs only the packet's repository work.
   It may stop at a contradiction, missing authority, scope conflict,
   unavailable native capability, or failed approved oracle. It neither
   delegates again nor changes the task to work around the problem.
3. **Compact return.** The worker returns the required evidence packet. A
   blocked packet is useful evidence; it is not a result to hide with a
   transcript replay or an automatic fallback.
4. **Root decision.** Sol and the user reconcile the packet. They may clarify
   requirements, approve a new bounded attempt, return to the appropriate
   phase, or stop. A new attempt is a new root decision, not a worker retry
   loop.

If native delegation fails before useful work begins, the failure is reported
as such. It does not revive the retired dispatcher, grant Sol repository
access, authorize a worker to broaden scope, or make a failed task appear
complete. If recovery would change design, scope, phase, permissions, or
acceptance, the root returns to the user for that decision. Native delegation
has no separate diagnostic service, raw protocol log, persistent worker state,
or dispatcher-specific retry and timeout protocol to preserve.

## Independence before trust

Less-capable workers are useful but are not trusted merely because they say a
change succeeded. Before implementation, a separate fresh Luna or Terra worker
owns the approved test or oracle semantics whenever that independence is
practical. The implementer runs an executable oracle without weakening or
redefining it. When the behavior is English policy rather than executable
logic, the honest oracle is fresh Terra semantic review supported by cheap
deterministic link, navigation, and focused static checks.

```mermaid
flowchart LR
    R[Detailed approved requirements] --> O[Independent oracle semantics]
    O --> I[Implementation and reported evidence]
    I --> V[Fresh Terra semantic review]
    V --> S[Sol and user decide acceptance]
```

This workflow does not commit a bespoke Python test that pretends to prove the
meaning of prose. One-off verifier commands may provide repeatable evidence
about links, headings, file presence, or forbidden terms; Terra still judges
whether the governing policy and implementation agree. Sol reconciles Terra's
compact review report with the user but does not rerun checks or inspect the
diff and raw evidence personally. A weak, missing, or failed oracle is a reason
to withhold acceptance or return to the appropriate phase.

## What native delegation does not change

Native spawning changes the transport only. The ALP phase gates and all three
delivery strategies remain in force:

| Invariant | Required behavior |
| --- | --- |
| Strategy | Brainstorm still selects Full ALP, Spec-driven, or Mechanical work; native delegation does not select a strategy. |
| Governing intent | A Book or specification remains the source of approved design. A worker stops at a material gap rather than deciding it. |
| Phase authority | Only Sol and the user move work between Brainstorm, Governing Documentation, Implementation, review, and Wrap Up. |
| Scope | A packet's file and action boundary is closed. A necessary extra file, permission, or changed oracle meaning is a reported conflict. |
| Acceptance | Native or external implementation completion is evidence, not acceptance. Sol and the user retain the acceptance decision after the required independent review. |
| Delegation | A worker cannot recursively delegate, appoint an orchestrator, or use native spawning to avoid its stop conditions. |
| External route | A manual EC handoff may be selected without changing approved intent; its revision, planning, and acknowledgment mechanics remain governed by the EC chapter. |

The user-provided successful native-spawn observation is valuable runtime
evidence that this replacement route exists. It is not a repository oracle and
does not remove independent oracle ownership or fresh-review requirements.

## Implementation boundary for the two-route workflow

The later Implementation keeps the always-loaded workflow core concise while
moving route-specific mechanics into focused references. Its closed boundary
is:

- `codex/skills/alp-workflow/SKILL.md`: retain the essential three-strategy
  phase gates, `alp-authoring` route,
  behavior-to-criterion-to-oracle traceability, delegation value gate, Full ALP
  versus Spec-driven authority, independent oracle integrity, weak-oracle
  disposition, reviewer session-goal and deferability contract, and short Wrap
  Up and safety rules prohibiting
  unapproved production, database, destructive, out-of-scope, installation, or
  synchronization actions. It selects native or manual Implementation without
  embedding either route's full mechanics.
- `codex/skills/alp-workflow/references/handoff-contract.md`: restore the
  manual/external, revisioned EC contract governed by the preceding chapter.
- `codex/skills/alp-workflow/references/native-worker-delegation.md`: add the
  native packet, capability routing, fresh-context, failure, compact-response,
  and advisory time-budget mechanics governed here.
- `codex/skills/alp-workflow/references/review-and-wrap-up.md`: add reviewer
  findings and deferability, the narrow deterministic-verifier exception,
  reconciliation, and durable Wrap Up mechanics.
- `antigravity/skills/alp-contract-implementation/SKILL.md`: preserve the
  external implementation companion and change its initial-plan gate to one
  separate Terra worker conformance review with no phase authority.
- `TODO.md` during Implementation or Wrap Up: remove the fulfilled reminder to
  mention Antigravity or Gemini in the workflow. Preserve the separate TODO for
  the user's deeper later manual review of this chapter.
- `wiki/repository-foundation.md` and `wiki/log.md` during Wrap Up: record the
  accepted two-route workflow and remove any current claim that a bespoke
  native-delegation test is the continuing acceptance oracle. Historical
  entries and `wiki/sources/**` remain historical evidence.

### Non-operative deletion targets

The closed boundary also contains these exact deletion targets:

- `codex/skills/alp-workflow/scripts/dispatch_worker.py`
- `codex/skills/alp-workflow/scripts/test_dispatch_worker.py`

Both files are deleted without an archive, fallback, compatibility shim, or
replacement policy or prose oracle. These literal paths identify removal only;
they are not active commands, transports, or compatibility entry points.

The separately user-approved deletion of the untracked
`test_native_worker_delegation.py` also remains in force. That one-off file
stays absent and is not a governed artifact to recreate, replace, or maintain.

The former dispatcher remains retired and absent; this revision must not
restore its code, tests, transport, fallback, or protocol.
Existing worker profiles are unchanged by this revision. Installed and
external artifacts are outside scope; no installation or synchronization is
authorized.

There is no rollback that silently restores the dispatcher or collapses both
routes into one envelope. If native delegation or external handoff proves
insufficient, Sol and the user reopen Brainstorm and approve a new design.

## Acceptance for the two-route workflow

English-policy acceptance uses a fresh delegated Terra semantic review plus
cheap deterministic link, navigation, and focused static checks. One-off
verifier commands may support the evidence packet, but they do not decide
policy meaning.

| Criterion | Acceptance evidence | Limitation |
| --- | --- | --- |
| Both Implementation routes are usable and share the right invariants. | Terra compares the Book, final diff, concise core, all three operational references, and the Antigravity companion; a link check proves every referenced file is present and reachable. | Link existence cannot prove correct route semantics. |
| Native packets stay small and truthful to `spawn_agent`. | Terra checks the required packet fields, fresh context, blocked/failure behavior, and advisory-only time budget; a focused static check rejects a mandatory or enforceable native timeout. | This does not execute a live native worker. |
| Manual EC handoff is restored without becoming a native envelope. | Terra checks revisioning, compatibility, optional questions, lint/preflight, planning gate, acknowledgement, Antigravity plan review, test-update limits, and completion evidence against the EC chapter. | The EC linter proves mechanical structure of individual contracts, not the policy's semantic quality. |
| Contextual detail moved without weakening the core. | Terra traces every required core invariant into `SKILL.md` and each route/review behavior into exactly one referenced document; static checks resolve links and detect duplicated dispatcher or mandatory-timeout guidance. | Concision and adequate emphasis remain judgment calls. |
| Retired mechanisms and fulfilled follow-up stay retired. | A focused repository scan confirms no active dispatcher route or bespoke native-delegation Python policy test; TODO inspection confirms the fulfilled Antigravity/Gemini reminder is gone and the deeper manual-review TODO remains. | Static absence cannot prove an external installation or runtime state. |

Book and active-guidance link checks cover README, all Book chapters, the
workflow skill, and its references. Focused terminology checks cover the same
active surfaces plus worker profiles, TODO, and current wiki pages. Historical
dispatcher evidence remains allowed only in `wiki/log.md`, `wiki/sources/**`,
and the explicitly labelled section below; an allowance must never hide an
active command, transport, fallback, or authority rule. Normative prohibitions
outside those historical regions may name the retired mechanism only to forbid
its restoration; they are not historical allowances or active routes.

## Reconciled legacy evidence

The imported canonical baseline contained a Python `dispatch_worker.py`, its
dedicated deterministic tests, and `alp-workflow` text that invoked an App
Server. That is observed legacy implementation evidence, not continuing
forward intent. Earlier Book and source text described packet validation,
routing, diagnostics, retries, and terminal envelopes for that adapter. The
approved design replaces all of those dispatcher-specific mechanics with the
native lifecycle above; they are neither compatibility requirements nor a
fallback contract.

This chapter therefore preserves the history only to explain removal. It does
not erase evidence by pretending the adapter never existed, and it does not
make its old protocol a requirement for native workers.

---

[ALP Skills Book](../README.md) · Previous:
[EC Linter](ec-linter.md) ·
Next: [Repository Charter](repository-charter.md)
