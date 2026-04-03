# How Datadog Redefined Data Replication
**Source**: https://blog.bytebytego.com/p/how-datadog-redefined-data-replication
**Date**: April 1, 2026
**Author**: ByteByteGo
**Keywords**: Datadog, CDC, change data capture, Postgres, Kafka, Debezium, Temporal, data replication, search

## Elevator pitch
Datadog solved a 7-second page load by recognizing the root cause: using a transactional database for search workloads — implementing CDC via Debezium + Kafka to replicate data to a specialized search platform, then automating the pipeline with Temporal.

## Takeaways
- Root cause was not query performance but architectural mismatch: Postgres (transactional) doing search workload
- CDC pipeline: Debezium reads Postgres WAL → Kafka as message broker → sink connectors to search platform
- Async replication chosen over sync to avoid coupling write performance to downstream latency (acceptable hundreds-of-ms lag)
- Schema evolution protected by automated migration validation and Confluent Schema Registry with backward compatibility
- Temporal (workflow orchestration) automated setup of 7+ component pipeline into repeatable platform

## Synthesis
Datadog's Metrics Summary page optimization is a textbook example of how performance problems that appear to be optimization problems are often architectural mismatches. The initial impulse when a page loads in 7 seconds is to optimize the query — add indexes, rewrite the join, tune the database. Datadog's engineers eventually diagnosed that no amount of query optimization would solve the problem because the problem was using a transactional database for a search workload.

Transactional databases like Postgres are optimized for writes that need ACID guarantees, point lookups, and row-level operations. They are poor choices for search workloads that require full-text search, faceted filtering, and ranked retrieval across large datasets. Joining 82,000 metrics with 817,000 configurations is not a query optimization problem — it is a data model problem that can only be solved by routing the search workload to infrastructure designed for it.

Change Data Capture is the standard approach for this architectural migration. Rather than requiring application code to write to two systems simultaneously (which creates consistency challenges and couples write performance to two databases), CDC taps into Postgres's Write-Ahead Log. Every write to Postgres automatically produces a CDC event that flows through Kafka to the search platform. The application writes to Postgres; the search system is eventually consistent.

The async replication decision reflects a deliberate tradeoff between consistency and performance. Synchronous replication — waiting for the search platform to confirm before acknowledging a write — would guarantee zero replication lag but would make every write as slow as the slowest system in the chain. For Datadog's use case, showing metrics configurations that are a few hundred milliseconds stale is acceptable; making all metric writes slower is not.

The Temporal automation addresses the operational overhead of CDC infrastructure. A Debezium source connector, a Kafka topic, a Confluent Schema Registry, a sink connector, and several supporting components must be configured correctly and kept in sync. Manual configuration doesn't scale when multiple teams need CDC pipelines. Temporal's workflow orchestration converts this into a reproducible, testable process that any team can invoke.
