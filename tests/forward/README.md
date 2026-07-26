# Forward tests

This directory contains a small forward-test suite for the three public ALP
skills. It is a verifier oracle and a set of raw fixtures, not an executable
test harness.

- `ORACLE.md` contains prompts, expected observations, and verification rules.
  It must never be mounted into a runner's session.
- `fixtures/` contains deliberately small raw repositories.
- `fixtures/MANIFEST.md` is coordinator documentation. It is not part of any
  runner fixture.
- `results/` contains concise durable conclusions from accepted runs.
- `evidence/` contains run-specific transcripts, diffs, snapshots, and frozen
  inputs. Git ignores it; retain it locally only while investigation or
  verification needs it.

Before a run, the coordinator freezes `ORACLE.md` (for example, by recording
its repository object ID or SHA-256 digest) and copies one named fixture into a
new temporary working directory. The runner receives only that raw fixture,
the exact user message for the current stage, and the exact candidate skill
path or installed skill exposure described by the scenario. Expected answers,
suspected defects, pass criteria, this README, and the fixture manifest remain
hidden.

No scenario should run in this repository checkout. Each authorized-change
scenario uses a disposable fixture copy. Read-only and authorized-change wiki
runs use separate fresh copies.

Launch Python-capable runners with `PYTHONDONTWRITEBYTECODE=1` so validation
does not create `__pycache__` files outside a scenario's mutation allowlist.
Confirm this setting reaches the runner's shell before relying on a strict
filesystem-scope result.

After verification, write one concise dated result under `results/`. Preserve
the frozen hashes, grades, material limitations, and conclusions worth
retaining. Do not commit raw evidence merely to preserve a transcript.
