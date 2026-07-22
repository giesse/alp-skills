---
name: alp-contract-implementation
description: Implement an explicitly supplied, approved EC-v1 handoff in Antigravity from a Full ALP Book or Spec-driven governing document using bounded planning, conflict reporting, scoped edits, acceptance-oracle validation, and a compact evidence packet.
---

# Antigravity EC Contract Implementation

Act only as the implementation-side companion for an explicitly supplied EC contract. Do not own Brainstorm, governing-document authoring, phase transitions, or canonical Wrap Up.

## 1. Read and Inspect

- Read the exact approved EC revision, its `Governing document` or legacy `ALP chapter`, `AGENTS.md`, and relevant repository guidance.
- Require a contract ID, positive revision, and `EC protocol: v1`.
- Require confirmation that Sol prepared the EC from the approved governing source and ran the repository-local deterministic EC linter directly before handoff; this mechanical gate does not require delegated semantic preflight.
- Perform read-only repository inspection during planning.
- Do not edit repository files or run implementation validation before explicit user authorization. Antigravity-native planning documents are the sole preauthorization artifact exception.

For Full ALP, Luna or Gemini Flash must be able to tangle the Book without material design decisions. If the Book requires invented architecture, a choice among materially different algorithms, inferred hidden compatibility behavior, or current code as an unstated specification, report the Book as incomplete and stop. Do not request a stronger implementation model.

## 2. Questions and Conflicts

- Stop on a `Q` whose `Resolve before` boundary affects the current task.
- Report missing decisions, contradictory repository evidence, required extra repository files, and unapproved critical-test changes.
- Do not silently repair or reinterpret the contract.

## 3. Plan and Acknowledge

Create Antigravity-native `implementation_plan.md` and `task.md` control-plane documents.

Give a concise acknowledgment covering:

- decisions and invariants;
- acceptance criteria and their `V` oracles;
- repository file boundary and out-of-scope work;
- critical-test semantics and authorized test updates;
- blocking questions and contradictory evidence.

Map IDs where useful for clarity, but do not annotate every plan or task item exhaustively. Self-check acceptance coverage, boundaries, questions, test semantics, and repository conflicts.

## 4. Initial Plan Gate

Return the initial plan and acknowledgment directly to Sol and the user for direct review and explicit authorization before repository implementation. No separate Terra plan review is required at this stage; fresh independent Terra review occurs post-implementation after evidence exists.

Accept one focused correction for a material blocker: wrong intended behavior, broken oracle, boundary violation, contradictory evidence, or unapproved critical-test change. After that correction, proceed unless a concrete blocker remains. Return any remaining blocker to the user rather than entering an open-ended refinement loop.

## 5. Implement and Validate

After authorization:

- keep edits inside the exact approved revision and file boundary;
- stop on contradictory evidence or a required contract change;
- require an approved complete replacement revision for changed contract content;
- execute or explicitly classify the oracle covering every acceptance criterion;
- state limitations for unavailable, non-executable, or production-only evidence;
- preserve critical test intent;
- apply only named existing-test updates authorized by the revision and non-conflicting added coverage.

Never weaken, delete, or alter critical assertions beyond approved intent to make tests pass.

## 6. Evidence Packet

Return:

- governing document and contract ID/revision;
- changed files;
- validation commands/results or other oracle evidence;
- deviations and unresolved concerns;
- acceptance coverage;
- repository discoveries and suggested durable learnings, separated from already recorded facts;
- concrete workflow friction or improvement opportunities.

Do not edit project `TODO.md`, wiki, governing documents, or other canonical Wrap Up artifacts unless the contract explicitly includes them. Codex owns normal Wrap Up.

Request another implementation or review iteration only with concrete contract/diff evidence, a non-acceptance reason, and a closure condition.
