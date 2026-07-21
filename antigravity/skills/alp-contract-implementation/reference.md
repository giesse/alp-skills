# EC Protocol v1 Vocabulary Mirror

The supplied self-contained EC revision is authoritative. Accept `Governing document` as the canonical source header and legacy `ALP chapter` for compatibility.

- **Contract**: stable task contract ID
- **Revision**: complete approved revision number
- **EC protocol**: supported protocol version
- **D**: decision
- **I**: invariant
- **A**: acceptance criterion
- **V**: observable oracle covering named `A` items
- **O**: out of scope or file boundary
- **Q**: question or conflict requiring resolution

Omit `Q` when there are no unresolved questions.

## Plan Self-Check

- [ ] Decisions, invariants, acceptance/oracle semantics, boundaries, test semantics, and blocking questions are acknowledged.
- [ ] Every `A` has one or more `V` oracles.
- [ ] Planned repository edits stay inside the declared boundary.
- [ ] No blocking `Q` remains unresolved.
- [ ] Critical test semantics remain unchanged except for named authorized updates.
- [ ] Contradictory repository evidence is reported.
- [ ] The plan avoids material design decisions when tangling a Full ALP Book.

Use ID mapping where it improves clarity; do not annotate every plan or task item exhaustively.

## Evidence Packet

- [ ] Governing document and contract ID/revision named
- [ ] Changed files listed
- [ ] Validation evidence and limitations stated
- [ ] Acceptance coverage reported
- [ ] Deviations and unresolved concerns listed
- [ ] Repository discoveries and suggested durable learnings separated
- [ ] Concrete workflow friction reported when observed
