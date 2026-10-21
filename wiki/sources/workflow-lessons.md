# Workflow lessons from earlier ALP work

Status: Historical synthesis; not current workflow guidance.

This page preserves useful rationale and reported experience from earlier ALP
work. The source compilation was dated 2026-07-23; this wiki reconciliation was
made on 2026-10-21. Current policy belongs to the linked governing documents.
The historical accounts below summarize what the source compilation recorded;
this reconciliation did not reread original files that are no longer retained
locally or independently verify the reported events. Their paths and titles are
provenance labels, not files available in this checkout.

## Simplicity and process cost

A retired Luna-owner/advisor experiment reportedly showed that a plausible
model hierarchy did not make the model seek advice at the right time or follow
control instructions reliably. A later delegation-economics effort reached a
technically acceptable result, but repeated contracts, plans, reviews,
revisions, and cross-document checks made the workflow costly and error-prone.
The account distinguished technical success from process success: extra
structure should address a specific risk or produce a concrete saving. This is
a historical synthesis, not a measured comparison of models or workflows.
Current simplicity guidance is in [GOALS](../../GOALS.md#goals) and
[RULES §1](../../RULES.md#1-keep-the-workflow-simple-and-clear).

## Cost, routing, and delegation

An earlier `Sol:Terra:Luna = 5:2.5:1` ratio served as a dated routing prior,
not a full cost model. The account noted briefing, root-context use,
reconciliation, repairs after drift, repeated review, user attention, and delay;
Antigravity also used a separate credit pool. The ratio is superseded and should
not be treated as a current estimate. Current routing and cost policy is in
[GOALS](../../GOALS.md#goals) and
[RULES §4](../../RULES.md#4-route-work-and-require-approval-for-consequential-decisions).

Two routing extremes reportedly failed: a soft delegation instruction let the
root announce a worker and then continue broad investigation itself, while an
absolute ban on root work forced relays for simple known reads and tiny edits.
A visible routing choice before discovery was proposed as a calibration lesson,
not a permanent boundary for every model or task. Delegation accounts also
favored bounded assignments with a goal, evidence request, response shape, and
stop condition; workers struggled when expected to settle policy, scope, or
acceptance. Parallel work was useful only when tasks were independent and each
result was needed. These are historical observations, not additional routing
rules; current authority and assignment policy is in
[RULES §4](../../RULES.md#4-route-work-and-require-approval-for-consequential-decisions)
and [AGENTS.md](../../AGENTS.md).

## Documentation, implementation, and review

Earlier implementation mistakes reportedly included defects that reviewers
thought could have reached production. More detailed plans reduced ambiguity but
did not remove it; pseudo-code that copied implementation syntax could make the
Book less useful by obscuring intent. The same account described independent
acceptance checks as a recurring safeguard and warned that a synthetic harness
can create confidence without testing the real risk. Fresh review of concrete
changes reportedly found defects, while reviewing a contract and then a
pre-implementation plan repeated judgment and still missed cross-artifact
problems. These are summarized historical experiences, not measured failure
rates. Current Book and acceptance guidance is in [ALP](../../ALP.md#the-book),
[RULES §5](../../RULES.md#5-work-through-explicit-phases),
[§6](../../RULES.md#6-define-acceptance-before-implementation), and
[§7](../../RULES.md#7-use-independent-review-where-it-adds-evidence).

One small-change account described requirements repeated across the Book,
execution and handoff contracts, skills, and operational references; information
was lost and the workflow acquired blockers. Earlier design work also rejected
mandatory links in both directions between Book chapters and implementation
files because that second link graph could drift. This is historical rationale,
not a ban on useful links. A related, separately preserved proposal appears in
[Antigravity handoff guardrails](antigravity-handoff-guardrails.md#avoid-premature-bidirectionality).

An early Docs-First guardrail reportedly applied only to `src/`, allowing a
swarm to create `bin/scaffold.sh` without a governing root specification while
appearing compliant. The general lesson is already reflected in current
action-scoped implementation rules. See [RULES §5](../../RULES.md#5-work-through-explicit-phases)
and the historical [handoff guardrails](antigravity-handoff-guardrails.md#guardrail-and-scaffolding-lessons).

Past wiki material reportedly called a deleted one-off integration test an
acceptance oracle; a separate entry distinguished an accepted delegation policy
from proven reliability or savings. The source compilation also summarized the
general limit of different evidence types: parsing, a focused test, a review,
and policy acceptance each establish different things. The original wiki
entries were reviewed but are not retained locally, so these details remain
qualified reported history. Current claim limits and source-status distinctions
are described in
[RULES §6](../../RULES.md#6-define-acceptance-before-implementation) and the
[knowledge lifecycle](../knowledge-lifecycle.md#knowledge-lifecycle).

## Keeping and changing workflow knowledge

Earlier work reported that the repository wiki did not consistently prevent
repeated trial and error because agents sometimes failed to consult it, while
Codex memory was said to work more consistently. This was not a measured
comparison, and the present wiki does not establish that one memory surface is
more effective. The account also noted that historical or duplicated documents
could look authoritative despite different evidence status. Current repository
memory guidance is in
[RULES §9](../../RULES.md#9-maintain-portable-repository-memory) and the
[wiki entry point](../index.md#alp-skills-repository-wiki).

Several proposed workflow designs reportedly failed through instruction drift,
hidden reconciliation cost, or weak enforcement. A lightweight trial across
roughly ten decisions was proposed: record the predicted route, reason, expected
saving, user verdict, and actual outcome before formalizing more policy. This
trial was a proposal, not an adopted requirement. Current policy remains in
GOALS and RULES; no trial requirement is implied here.

## Repository migration

Earlier migration notes described how direct edits to installed workflow files
made review, history, release identification, rollback, and cross-tool drift
detection harder. They motivated treating versioned repository sources as
canonical and installed copies as deployment outputs. The source inventory
records that the original migration notes were reviewed but are no longer kept
locally; the concise migration history is in
[Repository migration history](repository-migration-history.md#repository-migration-history).

The broader historical account also emphasized detecting drift before
overwriting an installed copy; checking that a replacement parses, its
invocation works, and rollback has been checked before retiring the old one; and
preserving downstream invocation and operational context for troubleshooting
and recovery. These are historical migration rationales, not a new installation
procedure. Current canonical-skill ownership is in
[RULES §8](../../RULES.md#8-derive-harness-instructions-from-these-rules) and
[AGENTS.md](../../AGENTS.md).

## Dated handoff observation

An Antigravity project log dated 2026-04-30 reports that role-specific
initialization immediately after a model switch felt like a stronger context
anchor than relying on passive constitutional text in `AGENTS.md`. This is one
dated, unverified observation, not a comparative test and not evidence that a
particular handoff workflow needs to change. Reconsider it only if practical
use reveals a concrete handoff problem. The user-identified source is the
[Antigravity project log at commit
`eaa968e599f0138614046e964f78888d726277dd`](https://github.com/giesse/antigravity-alp/blob/eaa968e599f0138614046e964f78888d726277dd/wiki/log.md#L28-L31);
remote availability was not independently verified. Related future-design
context is in [Antigravity handoff guardrails](antigravity-handoff-guardrails.md#antigravity-handoff-guardrails).

## Provenance and limits

The 2026-07-23 source compilation identified these reviewed but unretained
files: `OldCodexALPDocuments/ALP Workflow Notes.md`, `OldCodexALPDocuments/ALP
Workflow Redesign.md`, `OldCodexALPDocuments/ALP Workflow Repository
Migration.md`, `old/wiki/repository-foundation.md`, and `old/wiki/log.md`. The
current wiki inventory records their review and preservation disposition.

For the guardrail and scaffold account, the compilation cited the Antigravity
project log and [ALP guardrails and ownership at commit
`eaa968e599f0138614046e964f78888d726277dd`](https://github.com/giesse/antigravity-alp/blob/eaa968e599f0138614046e964f78888d726277dd/wiki/alp-guardrails-and-ownership.md).
For the pseudo-code and document/code drift account it cited [the Antigravity
ALP report at that commit](https://github.com/giesse/antigravity-alp/blob/eaa968e599f0138614046e964f78888d726277dd/wiki/sources/ALPReport.md),
especially its lines 42–70; the compilation itself described this as historical,
not independently verified measurement. The role-initialization observation
points to the project [log at that commit](https://github.com/giesse/antigravity-alp/blob/eaa968e599f0138614046e964f78888d726277dd/wiki/log.md#L28-L31).
The compilation also cited historical commits `fa9ab07` and `9be3f57` alongside
the unretained `old/wiki/log.md` for the acceptance-oracle correction and
delegation/review simplification. These are provenance references, not claims
that the deleted files have been rechecked here. Availability of external pages
was not verified during this wiki reconciliation.

The compilation cited Codex memory records by these identifiers:
`2026-07-22T12-04-03-v1gk-delegation_economics_workflow_postmortem.md` (thread
`019f89b6-26d0-7732-b565-fdea6f69e6e0`) and
`2026-07-18T13-44-53-I70g-alp_skills_foundation_book_wiki_baseline_import.md`
(thread `019f7579-04a2-7dc1-8466-b06b2ae6eecc`). These identify source
provenance only; they are not portable repository artifacts or local wiki links.
The reported routing, implementation, review, and retrieval experiences remain
qualified historical accounts, not present-day measurements or proof of
reliability. No private absolute paths or machine-specific values are included.
