# NikolayS/pgque: PgQue – Zero-bloat Postgres queue. One SQL file to install, pg_cron to tick.

**Source**: https://github.com/NikolayS/pgque
**Date**: Unknown
**Author**: NikolayS
**Keywords**: Postgres, queueing, pg_cron, event streaming, infrastructure

## Elevator pitch
PgQue revives the old PgQ design for modern managed Postgres, offering a SQL-first event queue that trades ultra-low latency for stable throughput, zero-bloat hot paths, and Kafka-like fan-out semantics inside the database.

## Takeaways
- PgQue is positioned as an event log and consumer-cursor system inside Postgres rather than a conventional task queue built around row locking and deletes.
- Its core claim is that snapshot batching plus table rotation avoids the dead tuples, vacuum pressure, and performance decay common in SKIP LOCKED queue designs.
- Because it is implemented in SQL and PL/pgSQL, the project targets managed Postgres environments that cannot run custom extensions or sidecar daemons.
- The latency trade-off is explicit: the tool is built for durability and sustained load, not single-digit millisecond dispatch.
- The repo is a good example of teams trying to simplify infrastructure by reusing the operational guarantees of Postgres instead of adding another distributed system.

## Synthesis
PgQue is interesting because it is not trying to be another general-purpose background job framework. It is trying to reclaim an older, battle-tested idea from the Postgres ecosystem, PgQ, and modernize it for environments where teams want durable event processing without standing up Kafka, Redis, or a custom worker platform. The project’s core proposition is simple: if your system already runs on Postgres, maybe the right queue is the one you can install with SQL and operate with the durability model you already trust.

What differentiates PgQue from many Postgres queue implementations is its critique of the standard SKIP LOCKED pattern. Many in-database job systems claim success at small scale, then accumulate dead tuples, VACUUM pressure, and performance drift under sustained load because rows are continually updated and deleted. PgQue argues that the fix is architectural rather than operational. By using snapshot-based batching and TRUNCATE-driven rotation, it aims to remove bloat from the hot path entirely. That is a meaningful design choice because it targets one of the most painful long-run failure modes in database-backed queues.

The project is also explicit about where it fits. It is closer to a Kafka-like shared event log with independent consumer cursors than to a task queue where one worker claims one job. That enables fan-out without duplicating data per subscriber, which is attractive for systems that want multiple consumers observing the same event stream. At the same time, the author is honest about the trade-off. Delivery latency is typically on the order of one or two seconds because the system depends on ticking and batch formation. If ultra-low-latency dispatch is the requirement, this is not the right tool.

The managed Postgres angle matters a lot. PgQ’s original design relied on a C extension and an external daemon, which made it awkward or impossible to deploy on many hosted platforms. PgQue rebuilds the pattern in PL/pgSQL so it can run on RDS, Aurora, Cloud SQL, Supabase, Neon, and similar providers. That broadens the potential audience from Postgres specialists to any team that wants a queue without adding another infrastructure product.

More broadly, PgQue fits a wider engineering trend toward infrastructure consolidation. Teams are increasingly skeptical of introducing a separate distributed system unless the operational payoff is overwhelming. If a workload’s scale and latency requirements can be handled inside an existing durable store, the appeal of “one fewer thing to run” is real. PgQue is part of that movement, but with a more historically informed design than many newer queue libraries.

Overall, the repository is useful not only as a specific tool but as a design statement. It argues that in the AI and event-driven era, reliability under sustained load is often more valuable than benchmark-friendly low latency, and that thoughtful reuse of mature database primitives can still beat fashionable infrastructure sprawl.
