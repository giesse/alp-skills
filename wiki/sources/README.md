# Wiki Source Handling

Part of the [ALP Skills Book](../../README.md). Source material is preserved
for provenance; it is not automatically current policy.

## Status labels

- **Current operational evidence:** installed behavior observed at an external
  native path. It must be reconciled with the Book before becoming canonical
  repository source.
- **Current design evidence:** a durable approved design chapter outside this
  repository. It can explain intent but may conflict with installed behavior.
- **Historical candidate:** useful prior reasoning that needs reconciliation.
- **Historical template:** old reusable material, preserved without adoption.
- **Superseded or deferred:** retained for history but not eligible for current
  policy without a new explicit decision.

## Promotion procedure

Import a selected source without rewriting it, record its original path and
SHA-256 digest, then compare its material claims with the Book, current
operational evidence, and explicit user decisions. Record the classification
and date in `wiki/log.md`. Only a claim classified current may be written into
a reconciled `wiki/` page and linked from `wiki/index.md`.

Stop for a governing decision when evidence is contradictory or unresolved and
the difference would change material workflow, tool, safety, or compatibility
behavior.
