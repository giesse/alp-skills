# Knowledge Lifecycle Brainstorm — 2026-07-19

Part of the [ALP Skills Book](../../README.md). This is deferred design
evidence, not current repository policy.

**Status:** Superseded or deferred — unresolved brainstorm.

## Problem

The repository currently depends on three kinds of knowledge that are easy to
conflate:

- machine-local knowledge, such as paths to `../TG/`, `../Antigravity/`, or
  installed tool artifacts;
- transition knowledge that must survive several conversations but should stop
  guiding work when a migration, workaround, source dependency, or software
  version changes; and
- portable repository knowledge that must remain useful to another user and AI
  agent after cloning the repository.

The Book, current wiki, source layer, and TODO already distinguish governing
intent, reconciled knowledge, evidence, and future work. They do not yet define
how knowledge scope and lifetime interact, how local bindings are discovered,
or how condition-bound guidance is reviewed and retired.

This must be resolved before the repository's first publication to GitHub. No
policy or operational change was approved in this brainstorm.

## External patterns reviewed

- [`AGENTS.md`](https://github.com/agentsmd/agents.md) is an open repository
  format for durable agent instructions. Codex supports global, repository,
  nested, and override guidance, but an `AGENTS.override.md` at a directory
  takes the place of that directory's ordinary `AGENTS.md`; it is not a safe
  default store for additive local context.
- [Git configuration scopes](https://git-scm.com/docs/git-config#SCOPES)
  provide system, global, repository-local, and worktree-local values.
  Repository-local `.git/config` is a strong candidate for simple per-clone
  path bindings.
- The [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/)
  distinguishes user configuration, persistent but non-portable state,
  disposable cache data, and login-lifetime runtime data. This is relevant if
  ALP later gains tooling that stores user-local state outside a checkout.
- [Python PEPs](https://peps.python.org/pep-0001/),
  [Kubernetes KEPs](https://github.com/kubernetes/enhancements/blob/master/keps/sig-architecture/0000-kep-process/README.md),
  and [MADR](https://adr.github.io/madr/) use explicit lifecycle states and
  replacement or supersession links while retaining historical decisions.
  Their metadata conventions are useful, but adding a parallel ADR or proposal
  hierarchy would duplicate the ALP Book's authority.
- [IETF document states](https://datatracker.ietf.org/doc/html/rfc6174#section-3.1)
  distinguish active, expired, replaced, and withdrawn drafts. The useful
  lesson is explicit freshness and replacement state; age alone should not
  normally decide whether guidance is false.
- [Diataxis](https://diataxis.fr/) distinguishes tutorials, how-to guides,
  reference, and explanation. That content taxonomy is complementary but does
  not solve knowledge scope, authority, or retirement.

## Candidate model

Treat knowledge as having independent dimensions rather than placing it in one
of three competing buckets:

| Dimension | Candidate values |
| --- | --- |
| Reach | repository-portable, per-clone, or user-local |
| Lifetime | durable or condition-bound |
| Authority | governing, current guidance, evidence, or working material |

The candidate placement model is:

| Knowledge | Candidate home |
| --- | --- |
| Durable repository instructions | `AGENTS.md` |
| Governing repository knowledge | Book |
| Reconciled durable knowledge | current wiki |
| Immutable or historical evidence | `wiki/sources/` |
| Portable condition-bound guidance | a tracked active-advisory convention |
| Simple per-clone path bindings | namespaced `git config --local` keys |
| Future user-local configuration | `$XDG_CONFIG_HOME` |
| Future persistent non-portable state | `$XDG_STATE_HOME` |
| Disposable derived data | `$XDG_CACHE_HOME` |
| Unfinished work | TODO or issue, not a knowledge store |

An active advisory would likely need explicit status, scope, creation and
last-verification dates, a review trigger, an observable validity or retirement
condition, evidence, and replacement linkage. A review date should request
revalidation rather than silently expire otherwise-correct guidance.

When a condition-bound repository advisory is retired, the candidate approach
is to remove it from current navigation, record a material closure in the wiki
log, preserve it under `wiki/sources/` only when it has lasting evidentiary
value, and otherwise rely on Git history rather than accumulating an archive of
every workaround.

## Unresolved decisions

- Define the minimum lifecycle vocabulary and whether active advisories need a
  dedicated directory, page type, or index section.
- Decide whether Git local configuration is sufficient for all current local
  bindings and what, if anything, should hold richer local explanatory notes.
- Define lazy onboarding: a clean checkout must work without local sources, and
  an agent should ask for a missing binding only when the current task needs it.
- Define precedence between remembered agent claims, current repository
  guidance, active advisories, and freshly verified local evidence.
- Reconcile existing references to local external paths so that another clone
  does not require unavailable files to understand current policy.
- Decide what metadata can be checked deterministically without creating wiki
  bookkeeping merely to prove that work happened.
- Preserve cross-agent portability while documenting any Codex-specific
  behavior, especially `AGENTS.override.md` replacement semantics.

## Closure condition

Before the first GitHub publication, approve a governing knowledge-lifecycle
design, update the repository instructions and wiki model within that approved
boundary, resolve or explicitly classify existing local-path dependencies, and
validate that a clean checkout can distinguish current portable guidance from
local, transitional, historical, or superseded material.

