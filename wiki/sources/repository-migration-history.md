# Repository Migration History

Status: Historical synthesis; not current operational guidance.

Original source: `OldCodexALPDocuments/ALP Workflow Repository Migration.md` and
`old/wiki/repository-foundation.md`

Preservation: Concise dated synthesis of durable lessons. Current operational
claims, machine-local or per-clone values, temporary locations, secrets, and
unverified installation details were omitted. Earlier Codex/Antigravity
boundaries and staged EC/dispatcher work are historical context only.

## 2026 transition rationale

Earlier ALP workflow work was split across durable design notes and installed
tool copies. Directly editing installed copies made review, version history,
rollback, release identification, and cross-tool drift detection difficult.
The migration rationale was to make versioned repository sources canonical and
to treat installed artifacts as deployment outputs.

The boundary also separated Codex-owned workflow policy from contracted
implementation behavior in the companion tool, with an EC proposed as a
self-contained bridge when a handoff needed one. Staged work explored
model-neutral roles, deterministic EC checking, and a thin dispatcher before
any standalone repository decision.

## Durable lessons

- Keep governing intent beside distributable workflow sources.
- Keep installed copies identifiable and synchronizable from a reviewed source
  revision rather than treating them as independent policy.
- Keep secrets, per-machine state, session logs, and unrelated user
  configuration outside versioned sources.
- Preserve rollback and drift detection before overwriting deployment outputs.
- Do not infer a repository identity, host, packaging mechanism, or current
  runtime behavior from a historical migration proposal.

The legacy directories remain historical evidence and require broader audit
before any deletion decision.
