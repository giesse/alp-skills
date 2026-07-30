# Knowledge Lifecycle Brainstorm — 2026-07-19

Status: Deferred research evidence; not current policy.

Original source: `old/wiki/sources/knowledge-lifecycle-brainstorm-2026-07-19.md`

Preservation: Portable substance retained. Neighboring-checkout, per-clone,
installed-artifact, user-local, and machine-specific path examples were
removed or generalized; stale framing links were normalized after relocation.
Historical claims were not silently updated.

## Problem

Knowledge can be confused across three scopes: machine-local bindings,
transition knowledge that expires after a migration or workaround, and
portable repository knowledge that should survive a fresh copy. Existing Book,
wiki, source, and TODO distinctions did not yet define how scope and lifetime
interact, how local bindings are discovered, or how condition-bound guidance is
reviewed and retired. No policy or operational change was approved in this
brainstorm.

## External patterns reviewed

- [AGENTS.md](https://github.com/agentsmd/agents.md) shows a repository format
  for durable agent instructions; override files replace ordinary guidance
  rather than safely adding local context.
- [Git configuration scopes](https://git-scm.com/docs/git-config#SCOPES)
  distinguish system, global, repository-local, and worktree-local values.
- The [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/)
  separates user configuration, persistent state, cache, and runtime data.
- [Python PEPs](https://peps.python.org/pep-0001/), [Kubernetes KEPs](https://github.com/kubernetes/enhancements/blob/master/keps/sig-architecture/0000-kep-process/README.md),
  and [MADR](https://adr.github.io/madr/) use explicit lifecycle states and
  replacement links while retaining historical decisions.
- [IETF document states](https://datatracker.ietf.org/doc/html/rfc6174#section-3.1)
  distinguish active, expired, replaced, and withdrawn drafts.
- [Diataxis](https://diataxis.fr/) supplies a content taxonomy but does not
  solve scope, authority, or retirement.

## Candidate model

Treat reach (portable, per-clone, user-local), lifetime (durable or
condition-bound), and authority/status (governing, current guidance, evidence,
or working material) as independent dimensions. Candidate homes were:

- durable instructions in repository instruction files;
- governing knowledge in the Book;
- reconciled durable knowledge in the current wiki;
- immutable or historical evidence in `wiki/sources/`;
- simple per-clone bindings in local configuration;
- user-local configuration/state/cache in their respective user facilities;
- unfinished work in TODOs or issues.

Condition-bound guidance would need explicit status, scope, verification or
retirement trigger, evidence, and replacement linkage. Retirement removes it
from current navigation and preserves it only when evidentiary value remains.

## Unresolved decisions

Define lifecycle vocabulary; decide how local bindings and explanatory notes
are represented; ensure a clean copy works without optional local sources;
define precedence between remembered claims, current guidance, advisories, and
fresh evidence; reconcile local-path dependencies; choose metadata checks that
do not create bookkeeping; and preserve portability across agent tools.

## Closure condition

Before broad publication, approve a governing lifecycle design, classify local
dependencies, and validate that a clean copy distinguishes current portable,
transitional, historical, superseded, and unresolved material.
