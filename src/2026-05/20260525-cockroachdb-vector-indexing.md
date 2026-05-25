# How CockroachDB Built Vector Indexing at Scale
**Source**: https://blog.bytebytego.com/p/how-cockroachdb-built-vector-indexing
**Date**: May 25, 2026
**Author**: ByteByteGo
**Keywords**: CockroachDB, vector indexing, C-SPANN, distributed database, ANN, embeddings, search, K-means tree

## Elevator pitch
CockroachDB built C-SPANN, a custom vector index that treats index data as ordinary SQL table rows, leveraging the database's existing sharding, replication, and caching infrastructure rather than bolting on a separate vector system — satisfying six architectural requirements that ruled out HNSW, IVF, and dedicated vector databases.

## Takeaways
- C-SPANN combines ideas from Microsoft's SPANN paper (tree partitioning), SPFresh (incremental updates), and Google's ScaNN (quantization) into a new index tailored for distributed SQL.
- Six architectural requirements ruled out existing solutions: no central coordinator, no large in-memory caches, minimal network hops, sharding-compatible, no hot spots, real-time incremental updates.
- The index uses a hierarchical K-means tree stored as key-value rows in CockroachDB ranges, inheriting automatic splitting, rebalancing, and block caching.
- A 1M-vector index needs only 3 tree levels with a fanout of ~100; a 10B-vector index needs 5, enabling parallel search with low, predictable latency.
- The approach eliminates "dual-system" complexity: vectors and transactional data live in the same database with the same consistency guarantees.

## Synthesis
The CockroachDB engineering team faced a classic infrastructure challenge: add vector search to a distributed SQL database without compromising the properties that make the database worth using. The popular options — HNSW (requires in-memory graph, resists sharding), IVF (single-node assumptions, struggles with dynamic updates), and dedicated vector databases (separate system, separate consistency model) — each failed at least one of six hard architectural constraints.

Their solution, C-SPANN, is architecturally clever in its restraint. The core is a hierarchical K-means tree that organizes vectors into partitions based on similarity, with centroids representing each partition's center of mass. The tree is wide and shallow: a fanout of approximately 100 means one million vectors need only three levels, and ten billion need five. Search traverses the tree from root to leaves, comparing query vectors to centroids at each level in parallel, then scanning candidate vectors at the leaves using SIMD CPU instructions.

What makes C-SPANN different is not the algorithm itself but how it's stored. Each partition is stored as self-contained key-value rows inside CockroachDB ranges — the same storage units that hold every other table. This means the vector index inherits CockroachDB's entire operational infrastructure for free: automatic range splitting when partitions grow, transparent rebalancing across nodes, block caching of frequently accessed rows, and immediate availability after node restarts because data lives on disk, not in memory.

This "index as table data" approach eliminates the dual-system complexity that plagues most vector search architectures. There's no need to keep vectors in one database and transactional data in another, no separate scaling story for search vs. storage, and no consistency gap between the two. When a node joins or fails, the vector index behaves exactly like any other table — the same replication, the same failover, the same recovery.

The background maintenance machinery (repartitioning, centroid recalculation, quantization for compression) operates within the same SQL framework, using existing CockroachDB job scheduling rather than a separate maintenance process. This design philosophy — solving new problems by mapping them onto existing, battle-tested infrastructure rather than building parallel systems — is a pattern worth studying for any team adding AI capabilities to existing data platforms. It trades some raw benchmark performance for operational simplicity and consistency guarantees, a tradeoff that makes increasing sense as AI features move from experimental to production-critical.
