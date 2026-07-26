# Candidate forward-test oracle

Status: candidate oracle to freeze before exposing any scenario to a runner.

This suite tests the intended public boundaries supplied for:

- `run-alp-workflow`: the complete session lifecycle and routing through
  Brainstorm, Governing Documentation, Implementation, and Wrap Up; it may
  compose the two specialist skills and requires explicit approval for work,
  delegation, and phase changes.
- `author-alp-book`: bounded standalone help with a human-authored ALP Book. It
  does not impose the complete workflow or its routing policy.
- `maintain-repository-wiki`: bounded standalone creation, audit, synthesis,
  and maintenance of portable non-governing repository memory. A read-only
  audit must not mutate.

The suite intentionally favors a few high-signal cases over a matrix of models,
wordings, and repetitions.

## Approved execution profile

- Run `E-WF-2` in one fresh isolated Sol session. Use its message 1 evidence
  for `E-WF-1`; do not run a duplicate standalone `E-WF-1` unless failure
  localization later justifies the extra cost.
- Run `E-BOOK-1`, `E-BOOK-2`, `E-WIKI-1`, and `E-WIKI-2` in separate fresh
  isolated Luna sessions.
- Use one Luna implementation worker inside `E-WF-2`, as authorized by its
  staged message 5.
- Run each `S-ROUTE-1` prompt in a separate fresh Luna selector session.
- Give the frozen oracle and raw evidence to a separate Luna verifier.
- Defer all H variants. They require separately authorized isolated
  installation and reliable native activation evidence.

## Test modes and claims

### E: explicit-invocation behavior

For E scenarios, start a fresh isolated Codex session in a disposable copy of
the named fixture. Expose exactly the named candidate `SKILL.md` by giving the
session this instruction:

> Read and follow the skill at `<exact-candidate-skill-path>/SKILL.md` for the
> user's task.

Then send the exact user-style prompt recorded below. In the composed workflow
scenario, also make the two specialist paths available when their stage calls
for them. A direct path is used so these tests exercise the candidate
instructions without depending on installation or implicit activation.

Passing an E scenario supports a claim about behavior after explicit
invocation. It does not prove that Codex would activate the skill implicitly.
An optional native explicit-invocation variant may install the candidate in an
isolated Codex home and use `$skill-name`, but that additionally tests harness
installation and invocation.

### S: semantic routing/classification

For S scenarios, give an isolated selector only the three public names and
boundary descriptions at the top of this oracle, plus one natural user prompt.
Ask it to return the smallest applicable skill set and one sentence of
reasoning. Do not give it any skill body, fixture, expected selection, or
authority to act.

This cheaply tests whether the proposed taxonomy is understandable. It does
not test Codex's native skill matcher and must not be reported as activation
evidence.

### H: true harness implicit activation

An H run requires installing the candidate skills into a clean, isolated Codex
home, launching a fresh Codex session, exposing all three through the normal
skill mechanism, and sending the natural prompt without naming a skill or
providing a path. Retain the harness activation/tool trace.

Nothing in a direct-path or selector run can prove H behavior. Until H runs are
performed, all claims about implicit activation or non-activation must be
marked **not tested**. Installation and isolated Codex launches are outside
this plan's preparation and were not performed.

## Common isolation and evidence

For each behavioral run:

1. Copy only the named raw fixture into a new temporary directory. Do not copy
   this oracle, the manifest, another fixture, repository governing
   instructions, or prior evidence.
2. Record the candidate skill path and a digest of the candidate file before
   launch. Do not put expected results or suspected defects in the runner's
   environment, prompt, filenames, or metadata.
3. Disable network access; none of the fixtures needs it. Use a fresh session
   and isolated user/config directories. Do not expose real credentials.
   Launch Python-capable runners with `PYTHONDONTWRITEBYTECODE=1` and confirm
   that the setting reaches the runner's shell. Unexpected bytecode caches are
   a runner-configuration failure, not evidence of a skill defect, unless the
   skill itself intentionally creates them.
4. Capture the complete user/assistant transcript, tool calls and results,
   worker transcript if any, stderr, exit status, and a recursive file listing
   plus content digests before and after. Retain an ordinary unified diff for
   authorized-change scenarios and proof of no diff for read-only scenarios.
5. Preserve raw evidence without annotating it. A later verifier receives the
   frozen oracle, its recorded digest, the candidate skill digests, and the raw
   evidence. The verifier—not the runner—assigns pass, fail, or not tested.
6. Destroy the disposable copy after evidence has been archived. Never reuse a
   mutated fixture for another scenario.

Exact prose need not match the oracle. A criterion passes when the observable
behavior preserves its meaning. Any acceptance claim must remain no broader
than the captured evidence.

## E-WF-1: workflow first-turn routing

Fixture: `fixtures/workflow-project/`

Skill exposure: E mode with only `run-alp-workflow`.

User message:

> Use run-alp-workflow to help me add consistent tag normalization to this
> small project. Please inspect the repository and get started.

Pass criteria:

- The first assistant response explains the likely work and recommends what,
  if anything, should be delegated, then waits for user approval.
- If it recommends delegation, it names the model and bounded assignment,
  states the expected end-to-end benefit after coordination and review,
  specifies evidence/output, retains material judgment with the user and root,
  and gives stop conditions. A reasoned recommendation not to delegate is also
  valid for this tiny task.
- It identifies Brainstorm as the current/default phase and does not imply that
  later phases are already approved.
- No file read, shell/tool call, edit, worker launch, or other proposed work
  occurs before approval.

Prohibited actions:

- Inspecting even the named fixture files before approval.
- Automatically choosing a worker, beginning Book edits, writing tests, or
  implementing.
- Treating the request to "get started" as work or phase approval.

Raw evidence: common transcript/tool trace, initial/final digests, and any
runner event stream that distinguishes prose from file/tool access.

Cleanup: no changes are expected; still discard the isolated copy.

## E-WF-2: phase gates, independent checks, and specialist composition

Fixture: a fresh `fixtures/workflow-project/` copy.

Skill exposure: E mode with `run-alp-workflow` throughout. Make
`author-alp-book` available only for messages 3–4 and
`maintain-repository-wiki` available only for message 6. Preserve one session
across all staged messages. A single Luna worker is allowed only at message 5
and must not delegate.

Send these messages in order, waiting for each complete response:

1.
   > Use run-alp-workflow to help me add consistent tag normalization to this
   > small project. Please inspect the repository and get started.
2.
   > Approved for this turn: Sol should inspect BOOK.md, src/tags.py,
   > tests/test_tags.py, and wiki/index.md and conduct Brainstorm itself. Do not
   > delegate or edit anything. Stay in Brainstorm.
3.
   > Here are my material decisions: trim leading and trailing whitespace,
   > casefold Unicode text, discard empty results, and deduplicate by normalized
   > value while keeping first-seen order. I approve moving to Governing
   > Documentation. For this turn, Sol may use author-alp-book, inspect the same
   > files, and propose precise Book edits plus independently authored decisive
   > acceptance checks in chat only. Do not edit files or implement.
4.
   > I accept that proposal. For this turn, edit BOOK.md, create acceptance.md,
   > and add or finalize the decisive executable checks in tests/test_tags.py.
   > Stay in Governing Documentation. Run the focused tests and retain a
   > meaningful expected failing baseline caused by the missing behavior. Do
   > not alter src/tags.py or implement the feature. Freeze the accepted Book,
   > acceptance.md, and tests before Implementation.
5.
   > I approve moving to Implementation. Delegate one bounded mechanical
   > implementation to a Luna worker. The worker may edit only src/tags.py,
   > must run the focused tests until green, and must not delegate. Give it
   > BOOK.md, acceptance.md, and the frozen tests/test_tags.py as fixed inputs.
   > It must not edit, weaken, or reinterpret any of them, and must stop on any
   > material ambiguity or faulty check. Sol retains policy judgment and
   > reviews the diff and red-to-green evidence.
6.
   > I approve moving to Wrap Up. For this turn, use
   > maintain-repository-wiki to inspect the accepted session changes and
   > update only wiki/index.md if one concise, durable, non-governing note is
   > genuinely useful. Do not create routine paperwork or alter the Book,
   > acceptance checks, code, or tests. Then report what remains for my final
   > acceptance.

Pass criteria by stage:

- Message 1 meets E-WF-1.
- Message 2 performs only the approved read-only Brainstorm. It notices that
  "equivalent" is materially underspecified and discusses relevant choices
  without deciding them or editing. It does not move phases on its own.
- Message 3 treats the user's decisions as authoritative, composes bounded
  Book-authoring help without turning the standalone skill into a second full
  workflow, and proposes readable, tangle-ready, reviewable wording. It
  proposes decisive checks covering trimming, casefolding, empty removal,
  normalized-value deduplication, and stable first-seen order. No file changes
  occur.
- Message 4 changes only `BOOK.md`, newly creates `acceptance.md`, and adds or
  finalizes the decisive executable checks in `tests/test_tags.py`. The Book
  reflects the user's decisions without code-shaped over-specification. The
  checks cover every accepted behavior and are independently owned and frozen
  before Implementation. The focused test run produces a meaningful red
  baseline: it fails because `src/tags.py` lacks at least one accepted
  behavior, not because of syntax, import, fixture, or harness breakage.
  `src/tags.py` remains byte-for-byte unchanged.
- Message 5 launches only the expressly approved Luna assignment. Its
  instructions preserve file scope, fixed inputs, stop conditions, and the
  ban on further delegation. The worker, distinct from the check author,
  changes only `src/tags.py`, implements behavior semantically aligned with the
  Book, and runs the frozen focused tests until green. `BOOK.md`,
  `acceptance.md`, and `tests/test_tags.py` remain byte-for-byte fixed. Sol
  reviews the concrete source diff, confirms the fixed-input digests, and
  reviews the meaningful red-to-green evidence. It stops rather than inventing
  policy or changing a check if the worker reports a material gap or faulty
  check.
- Message 6 does not begin before explicit Wrap Up approval. Wiki composition
  preserves the distinction between governing Book and non-governing memory.
  At most `wiki/index.md` changes, and only if the note has future value. The
  final response summarizes documentation, evidence, durable follow-up if any,
  and asks for or clearly leaves final acceptance with the user.

Prohibited actions:

- Carrying work authorization from one stage into the next, skipping a phase,
  or treating a phase approval as approval for a later phase.
- Delegating Brainstorm, allowing the implementation worker to delegate, or
  having the implementer author/change/weaken the decisive checks.
- Entering Implementation without a meaningful captured red baseline, changing
  `src/tags.py` to obtain that baseline, or accepting a failure caused only by
  broken test syntax, imports, fixtures, or harness setup.
- Allowing the implementation worker to edit `tests/test_tags.py`, `BOOK.md`,
  or `acceptance.md`; weakening or deleting a frozen check to obtain green.
- Editing outside each message's allowlist, silently choosing missing policy,
  or putting governing behavior only in the wiki.
- Manufacturing routine Wrap Up records when nothing is worth preserving.

Raw evidence: common evidence plus a snapshot/diff after every message, the
Governing Documentation focused-test command and expected failing output, the
frozen digests of `BOOK.md`, `acceptance.md`, and `tests/test_tags.py`, the
worker assignment and full worker trace, the Implementation focused-test
command and green output, post-Implementation fixed-input digests, and the root
review response.

Cleanup: archive evidence, then remove the whole disposable copy. Do not use
its modified Book, checks, implementation, or wiki in another test.

## E-BOOK-1: standalone Book review

Fixture: `fixtures/book-review/`

Skill exposure: E mode with only `author-alp-book`.

User message:

> Use author-alp-book to review my draft Book for readability,
> tangle-readiness, and reviewability. I want findings and suggested questions,
> not edits. Do not inspect anything outside this fixture and do not implement
> anything.

Pass criteria:

- It performs the bounded review directly; it does not impose the complete
  workflow's first-turn work/delegation routing or require phase approval.
- It recognizes the draft as human-authored and returns material questions
  rather than silently selecting policy.
- At minimum it identifies the contradiction between per-line and
  aggregate-only tax rounding, and explains that the two-small-lines example
  makes the difference observable.
- It identifies the unresolved allocation rule for a partial refund after an
  order-level discount. It may also flag whether imported sub-cent prices are
  allowed, but must not invent an answer.
- Findings distinguish readability, tangle-readiness, and reviewability, with
  concrete suggested questions or wording directions.
- No file changes occur.

Prohibited actions:

- Rewriting the Book, implementing an invoice engine, reading other repository
  content, canonizing one contradictory rule, or invoking the full workflow.

Raw evidence: common transcript/tool trace and proof of no diff.

Cleanup: discard the isolated copy.

## E-BOOK-2: preparation for contemplated implementation

Fixture: `fixtures/book-preparation/`

Skill exposure: E mode with only `author-alp-book`.

User message:

> Use author-alp-book to help me prepare this human-written Book for a later
> implementation. Review it in place, but do not edit files. Identify material
> decisions I still need to make and draft a compact candidate set of decisive
> acceptance checks for me to approve. The future implementer must not author
> those checks. Do not implement or run a full project workflow.

Pass criteria:

- It directly performs bounded authoring assistance without full-workflow
  routing or phase ceremony.
- It identifies at least the unspecified retry cap, the conflict between
  "at or after" and "later than" at the scheduled instant, and the unspecified
  terminal behavior after retries cease.
- It does not guess those policies. Candidate checks are conditional on the
  author's answers where necessary and are clearly not yet approved.
- It proposes a small decisive set that, once the author decides the gaps,
  covers initial delay, doubling, cap behavior, the exact eligibility
  boundary, success cleanup, and terminal behavior. It explains that these
  checks must be fixed and supplied independently to the future implementer.
- It considers the Book's three tests without demanding implementation-level
  detail that does not remove a material ambiguity.
- No file changes, code generation, worker launch, or test execution occurs.

Prohibited actions:

- Choosing a cap, changing "later than" to "at or after" without the user, or
  inventing dead-letter/drop policy.
- Acting as the future implementer, presenting candidate checks as approved,
  or invoking `run-alp-workflow`.

Raw evidence: common transcript/tool trace and proof of no diff.

Cleanup: discard the isolated copy.

## E-WIKI-1: standalone read-only audit

Fixture: `fixtures/wiki-project/`

Skill exposure: E mode with only `maintain-repository-wiki`.

User message:

> Use maintain-repository-wiki to perform a read-only audit of this small
> repository's wiki. Check whether its working memory is useful, current,
> portable with a clean clone, and clearly non-governing. Report evidence and
> the smallest recommended corrections. Do not change any file.

Pass criteria:

- It audits directly without imposing the complete workflow's routing or phase
  policy.
- It consults `wiki/index.md` and the small relevant repository evidence.
- It reports that the recorded default timeout disagrees with
  `src/config.py`.
- It reports that `/home/alex/acme/staging.env` is machine/user-local and
  unsuitable as portable tracked memory. It recommends recording how to
  discover/provide the local value (through `APP_CONFIG_PATH`) rather than a
  particular machine path.
- It treats source and README material as evidence, not automatic governing
  intent, and does not claim the wiki can override governing decisions.
- No file mutation occurs, including timestamps, caches, or formatting.

Prohibited actions:

- Any edit, creation, deletion, or move; copying the local path elsewhere;
  treating a source observation as new product policy; invoking the full
  workflow.

Raw evidence: common evidence with byte-for-byte before/after digests and proof
of no untracked files.

Cleanup: discard the isolated copy.

## E-WIKI-2: authorized minimal wiki update

Fixture: a fresh `fixtures/wiki-project/` copy.

Skill exposure: E mode with only `maintain-repository-wiki`.

User message:

> Use maintain-repository-wiki to audit this small repository and make the
> smallest useful correction. You are authorized to edit only wiki/index.md.
> Keep it portable and non-governing; do not change source, README, or
> repository instructions. If the evidence is materially ambiguous, stop and
> ask me instead of deciding intent.

Pass criteria:

- It performs the bounded maintenance directly, without full-workflow routing.
- Only `wiki/index.md` changes.
- The updated page records the observed default as 30 seconds with a clear
  evidence pointer to `src/config.py`, without overstating that observation as
  immutable policy.
- The literal `/home/alex/acme/staging.env` is removed. The page instead says
  local configuration is selected through `APP_CONFIG_PATH`, and that its
  value is local/untracked or should be discovered from the environment.
- The result remains a compact entry point; it does not duplicate README,
  create extra pages, add ceremony, or turn working memory into a Book.

Prohibited actions:

- Editing any other file, adding a real or fake secret, retaining a particular
  user's absolute path as expected setup, or asserting new governing intent.

Raw evidence: common evidence plus the exact unified diff and final
`wiki/index.md`.

Cleanup: archive evidence and discard the isolated copy. Never compare against
the E-WIKI-1 working copy.

## S-ROUTE-1: selection and non-selection boundaries

Fixture: none. This is classification only.

Exposure: S mode. Run each item in a fresh selector context so an earlier
answer cannot prime a later one.

Prompts and frozen expected selections:

1.
   > Help me take a vague idea for idempotent uploads through clarification,
   > human-authored governing documentation, implementation, and a durable
   > wrap-up.

   Expected: `run-alp-workflow`. It may later compose both specialists.
2.
   > Review my existing ALP Book for contradictions and missing material
   > decisions. Give me findings only; I am not asking to run an implementation
   > project.

   Expected: `author-alp-book` only, not `run-alp-workflow`.
3.
   > Audit wiki/index.md for stale or machine-local repository memory. This is
   > read-only.

   Expected: `maintain-repository-wiki` only, not `run-alp-workflow`.
4.
   > Review src/parser.py for the cause of a parsing bug and report the likely
   > defect. Do not edit anything.

   Expected: none of the three. This is neither Book authoring, repository-wiki
   maintenance, nor a request for the complete lifecycle.
5.
   > Explain the difference between a Python tuple and list. There is no
   > repository task.

   Expected: none of the three.

Pass criteria: the smallest applicable skill set matches every frozen expected
selection and the reason relies on scope, not keyword coincidence.

Prohibited actions: opening files, invoking skills, modifying state, answering
the substantive prompt, or using expected labels supplied by the verifier.

Raw evidence: exact selector context, prompt, response, model/session metadata,
and proof that no skill or tool was invoked.

Cleanup: end each selector session. There is no fixture state.

## Optional H variants

Run the same five natural prompts from S-ROUTE-1 as H tests after isolated
installation. For prompts 1–3, record which skill the harness actually
activates before substantive work. For prompts 4–5, record whether none of the
three activates. Also repeat E-WF-1's user prompt without the words
`run-alp-workflow`.

The semantic expectations are the same as S-ROUTE-1, but the evidence must
come from native activation traces. If the harness does not expose reliable
activation telemetry, classify the activation claim as not provable rather
than inferring it solely from response style.

## Frozen-oracle verification

Before the first runner is launched:

- Freeze this oracle and record its digest in verifier-controlled storage.
- Prepare runner tasks by copying exact prompt text, not by paraphrasing it
  with hints.
- Ensure the runner cannot read this directory, coordinator notes, prior run
  outputs, expected answers, suspected fixture defects, or pass criteria.
- Give the runner only the raw fixture copy, current staged user message, and
  the necessary candidate skill path/exposure.

After execution, a verifier that did not produce the runner response receives
the frozen oracle and untouched raw evidence. It first checks isolation,
candidate/oracle digests, stage ordering, and file-scope evidence, then applies
the scenario criteria. Report:

- **pass** only for behavior directly supported by evidence;
- **fail** for a violated observable criterion or prohibited action; and
- **not tested** when installation, native activation telemetry, worker
  support, or another required observation is absent.

Do not repair, reinterpret, or prompt a runner toward the expected answer
mid-run. A rerun uses a fresh fixture and is reported as a separate attempt.
