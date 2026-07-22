# Native Worker Delegation

Native delegation is the internal Implementation route. It uses a fresh, narrow context and a compact return; it is not a manual EC, transport protocol, dispatcher, or second design authority.

## Capability and weighted credit routing

Routing optimizes weighted credit consumption and protects expensive root context rather than raw token count. As of July 2026, relative GPT-5.6 credit rates give Sol:Terra:Luna = `5:2.5:1` across input, cached-input, and output tokens; consult the [official rate card](https://learn.chatgpt.com/docs/pricing#what-are-tokens-and-credits) and revalidate when models or pricing change. Before repository exploration or action, Sol states the selected route in one short line.

Luna handles broad or multi-file discovery, unknown answer locations, command-heavy investigation, noisy test or log output, large diffs or structured data, repeatable checks, routine documentation, implementation, and deterministic verification. Terra handles stronger-judgment tasks and default fresh independent review. The separately spawned `alp_escalation_reviewer` profile represents a fresh read-only Sol reviewer usable only after explicit user authorization for that review.

Direct Sol root work is limited to the economic safe harbor: reading one named artifact needed in full, one or two small known artifacts, reading verbatim supplied material, or making a localized edit needing no tests, broad follow-on inspection, iterative repair, or material design choice, with constant-cost localized diff confirmation. Sol retains ownership of authoring approved Full ALP governing documentation; Luna may gather evidence or run mechanical checks. If direct work exposes a need for search, additional artifacts, tests, verification, or iterative repair, Sol stops and delegates the remaining bounded work. Native work is sequential by default; there is no swarm target or preferred worker count.

## Fresh packet and closed boundary

Sol provides a self-contained packet containing:
- role or capability;
- bounded task and exact repository file boundary;
- relevant supplied evidence and paths;
- allowed permissions;
- stop conditions; and
- compact response requirements.

Every worker operates only inside the root packet's closed repository and action boundary. A necessary extra file, permission, scope expansion, changed oracle meaning, or material design choice is a blocked conflict returned to the root. Workers must not decide material design, expand scope, authorize phases, redefine acceptance or compatibility behavior, or recursively delegate except for the explicitly authorized controlled Terra-to-Luna evidence hop.

The packet may authorize broad inspection inside one bounded decision subtree to let the worker resolve questions without repeated root handoffs. Workers receive narrow context rather than the root transcript. One writer owns a shared checkout; parallel workers need independent files and quota headroom.

## Controlled Terra-to-Luna hop

Workers remain non-recursive by default. An authorized Terra worker may create exactly one fresh, sequential, read-only Luna child for bounded mechanical or noisy evidence gathering (such as focused search, structured extraction, approved deterministic checks, or log/test compression) only when explicitly authorized by the root packet.

Terra retains its assigned judgment and must personally inspect the governing source, relevant diff, and evidence necessary for semantic judgment without citing the Luna packet as a substitute. Terra must explicitly state that it used the Luna child and reconcile the child's compact evidence into Terra's own single return. The Luna child is read-only and must not edit, write, decide material meaning, expand scope, authorize phases, assess acceptance, retry, or delegate again. If the Luna child fails or reports a material gap, Terra returns a blocked result; it does not retry, use a fallback route, or spawn another child.

## Lifecycle, return, and timing

The native lifecycle is strictly bounded: one root packet, one worker attempt, one compact return, and one root reconciliation. The controlled Terra child operates inside Terra's single attempt and creates no second root reconciliation path.

Every return states:
- conclusion or current status;
- concrete evidence;
- uncertainty or precise blocked reason;
- inspected scope; and
- uninspected scope.

Implementation and review returns additionally state changed files or reviewed diff, oracle results, deviations, acceptance coverage, and residual risk. A conflict, missing authority, failed oracle, unavailable capability, or design gap is a blocked result—never a trigger for automatic retry, fallback, or dispatcher restoration. The root and user reconcile compact reports and make any new attempt a new decision.

Native spawning has no enforceable task timeout. A packet may include an advisory time budget or checkpoint request; it is advisory only and does not promise interruption, cancellation, or worker termination.
