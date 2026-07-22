# EC Linter

[ALP Skills Book](../README.md) · Previous:
[Execution Contracts and Evidence](execution-contracts-and-evidence.md) ·
Next: [Native Worker Delegation](worker-dispatch.md)

## A cheap check for handoff omissions

An Execution Contract is deliberately compact, which makes small omissions
easy to miss: an acceptance criterion without a validation, an unclear file
boundary, or a question with nobody responsible for resolving it. The EC linter
is a local, deterministic command that catches those mechanical mistakes before
a contract is handed to another agent.

It is not an AI reviewer and it is not a design authority. A passing result
means the contract is structurally complete; the workflow owner still decides
whether the design is sensible, the evidence is strong, and the task may enter
Implementation.

## What it accepts and checks

The linter accepts either a raw EC-v1 document or one fenced EC in Markdown.
It can read a file or standard input, and returns stable text diagnostics or a
stable JSON result. It performs no repository discovery, network access, model
call, command execution, or file edit.

Its checks include:

- required headers, a positive revision, and the supported protocol version;
- unique decision, invariant, acceptance, validation, scope, and optional
  question identifiers;
- a validation reference for every acceptance criterion;
- complete ownership and resolution metadata for every question;
- explicit out-of-scope and repository file-boundary entries;
- critical-test ownership and replacement-revision handling when tests are in
  scope; and
- wording that permits planning but prevents edits or implementation validation
  before approval.

## Why the boundary matters

The linter should never grow into a second orchestrator. It cannot know whether
a retry policy is safe, a manual oracle is credible, or an extra file is truly
necessary. Making it pretend otherwise would hide judgment behind a green
command. Its job is to make missing structure visible cheaply so a person or
reviewer can spend attention on the important questions.

## Evidence for the linter

Its standard-library test suite is the primary oracle. It covers valid raw and
fenced input, stable JSON, duplicate or missing fields, invalid references,
coverage gaps, question metadata, scope and authorization wording, vague terms,
and test-semantics rules. A successful lint is evidence of structural
completeness only.

---

[ALP Skills Book](../README.md) · Previous:
[Execution Contracts and Evidence](execution-contracts-and-evidence.md) ·
Next: [Native Worker Delegation](worker-dispatch.md)
