# Raw fixture manifest

This manifest is for the test coordinator and verifier. Do not mount it into a
runner session.

The fixtures are intentionally small and contain no instructions from the ALP
Skills repository. They contain no secrets and require no network access.

## `workflow-project`

Purpose: exercise a small lifecycle in which a human-authored Book leaves a
material feature term open, then the user supplies the decisions needed for
documentation, independently defined checks, mechanical implementation, and
optional durable working memory.

Initial files are `BOOK.md`, `src/tags.py`, `tests/test_tags.py`, and
`wiki/index.md`.

Permitted changes depend on the staged authorization:

- first-turn and Brainstorm stages: none;
- Book proposal stage: none;
- accepted Governing Documentation stage: `BOOK.md`, new `acceptance.md`, and
  `tests/test_tags.py`; `src/tags.py` must remain unchanged while the focused
  tests establish the expected failing baseline;
- Implementation stage: only `src/tags.py`; `BOOK.md`, `acceptance.md`, and
  `tests/test_tags.py` are frozen inputs;
- Wrap Up stage: at most `wiki/index.md`.

## `book-review`

Purpose: provide a short human-authored Book whose pricing and refund prose can
be reviewed without an implementation repository.

No file may change.

## `book-preparation`

Purpose: provide a short human-authored Book that is close to implementation
but still needs material author decisions and candidate acceptance semantics.

No file may change.

## `wiki-project`

Purpose: provide a compact repository-memory entry point plus nearby source and
README evidence for portability and freshness auditing.

- In the read-only scenario, no file may change.
- In the authorized-update scenario, only `wiki/index.md` may change.
