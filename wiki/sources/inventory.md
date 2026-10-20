# Source Inventory

Status: Current non-governing inventory.

The entries below record preserved material and source disposition.
Repository-relative paths may identify originals no longer retained locally;
they are provenance labels, not current authority.

## Preserved

| Original source | Status | Preservation treatment | Intended future use |
| --- | --- | --- | --- |
| `old/wiki/sources/knowledge-lifecycle-brainstorm-2026-07-19.md` | Deferred research | Portable research retained; local and checkout-specific examples sanitized and treatment disclosed. | Later lifecycle design study. |
| `old/wiki/sources/spec-driven-development-research-2026-07-19.md` | Deferred research | Portable Spec Kit research retained; relocation-framing links normalized and treatment disclosed. | Later comparison against ALP. |
| `OldCodexALPDocuments/ALP EC Linter.md` | Retired historical design evidence; original document not retained | Substantive design preserved in [the EC-linter note](alp-ec-linter.md); exact linter and test files retained as retired references at [`lint_ec.py`](retired-ec-linter/lint_ec.py) and [`test_lint_ec.py`](retired-ec-linter/test_lint_ec.py). | Historical validation and compatibility study. |
| [Antigravity handoff guardrails](https://github.com/giesse/antigravity-alp/blob/eaa968e599f0138614046e964f78888d726277dd/wiki/alp-guardrails-and-ownership.md) | Historical input | Portable guardrail lessons retained; stale wiki framing/cross-links normalized. User confirmed the Git subrepository is on GitHub; the remote was not independently checked. | Future handoff-design session. |
| `OldCodexALPDocuments/ALP Workflow Repository Migration.md` and `old/wiki/repository-foundation.md` | Historical synthesis | Durable migration lessons condensed; current operational claims and local values omitted. | Historical context for source and installation decisions. |
| `tests/forward/results/2026-07-26.md` | Historical evidence and retirement decision; original suite not retained | Substantive findings and retirement rationale preserved in [the forward-test retirement note](forward-test-suite-retirement.md); original suite retained in Git history. | Historical context for testing and acceptance decisions. |

## Reviewed but not retained

- `old/wiki/index.md`, `old/wiki/log.md`, and `old/wiki/repository-foundation.md`
  as standalone pages were not retained as current pages: the new entry point
  is intentionally compact, and logs/foundation claims require reconciliation.
- `OldCodexALPDocuments/ALP Workflow Redesign.md` was reviewed but not
  imported: it is governing-design history, not portable current wiki memory;
  only the migration lessons needed here were synthesized.
- `OldAntigravityALP/wiki/llm-memory-pattern.md` was reviewed but not retained:
  it asserts adoption of a memory architecture that is not approved here.

## Review disposition — 2026-10-20

The prose and ordinary files in all three legacy directories were reviewed at
the level of preservation, supersession, or retention need (93 files, excluding
Git metadata and generated Python bytecode). This review did not execute
historical programs or tests, verify external claims, or inspect Git object
contents.

- `old/` (39 files): its Book, skills, agents, and wiki mostly describe retired
  workflows or ideas now covered by `GOALS.md`, `RULES.md`, `ALP.md`, current
  skills, and `LESSONS.md`. The two research pages above are already preserved.
  The exact EC-v1 linter and test originals are retained at
  [`lint_ec.py`](retired-ec-linter/lint_ec.py) and
  [`test_lint_ec.py`](retired-ec-linter/test_lint_ec.py); byte-for-byte copies
  were checked before removing their source directory. Their design and test
  scope are described in [the preserved design](alp-ec-linter.md).
- `OldCodexALPDocuments/` (8 files): workflow redesign and role/dispatch
  documents are dated design history, not current guidance. Migration lessons
  and EC-linter design are preserved above; the remaining authoring and
  workflow rationale is substantially covered by current skills and
  `LESSONS.md`.
- `OldAntigravityALP/` (46 files, including placeholders): guardrail and
  scaffold rationale is preserved in
  [the handoff guardrails source](antigravity-handoff-guardrails.md) and
  `LESSONS.md`. The 2026-04-30 observation about role-specific model
  initialization is recorded as a dated, unverified anecdote in `LESSONS.md`.
  The model/pricing/research surveys contain dated, unverified claims and
  speculative designs; they were not adopted as current knowledge. The user
  confirmed that the entire `OldAntigravityALP/` Git subrepository is on GitHub
  and need not be preserved locally; the remote was not independently checked.
  It includes a voiced ALP presentation the user tried to create, got reasonably
  far with, and found frustrating. Its manifest says the 18 audio files exist,
  but only placeholders are present in the local media directories.

The three legacy directories (`old/`, `OldCodexALPDocuments/`, and
`OldAntigravityALP/`) have been removed locally after their live references
were updated in `TODO.md`, `LESSONS.md`, this inventory, and the three source
notes `alp-ec-linter.md`, `antigravity-handoff-guardrails.md`, and
`repository-migration-history.md`. Remaining mentions of removed originals are
plainly labeled provenance, not local links. The Antigravity sources are linked
to commit `eaa968e599f0138614046e964f78888d726277dd` in the user-identified
GitHub repository; remote availability was not independently verified.

No historical code or tests were run and no external claims were verified.
The legacy directories were untracked by the parent repository, so their
removal cannot be undone through its history. The exact EC-v1 linter and test
files are the only code retained from them, as retired references.
