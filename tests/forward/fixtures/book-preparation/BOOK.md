# Retry scheduling

The worker reschedules a job after a temporary failure so short outages do not
discard useful work.

The first retry waits five seconds. Each later failure doubles the previous
delay up to a reasonable maximum. The stored attempt count increases whenever
a failure is scheduled.

A job becomes eligible at or after its scheduled retry time. A worker must not
claim it until the current time is later than that time.

When a retry succeeds, the retry schedule and failure count are cleared. When
the system stops retrying, it records the outcome so operators can find the
job.

The scheduler uses a supplied clock so acceptance checks do not depend on wall
clock timing.
