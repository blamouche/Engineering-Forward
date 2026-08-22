# How Airtable Built the Search Layer Behind Their AI Features
**Source**: https://blog.bytebytego.com/p/how-airtable-built-the-search-layer
**Date**: 2026-05-27
**Author**: ByteByteGo
**Keywords**: airtable, vector-search, semantic-search, milvus, hnsw, embeddings, multi-tenancy, partitioning, cold-offloading, disaster-recovery

## Elevator pitch
Airtable's semantic search architecture was driven not by algorithm choice but by one peculiar property of their data — 75% of customer bases sit idle any given week — which forced a chain of engineering decisions from per-base partitioning through HNSW indexes to cold-offloading and re-embed-on-recovery.

## Takeaways
- Airtable chose one-partition-per-base (over shared partitions) for strong physical isolation, trivial deletion, and no post-query filtering latency — but hit a cliff at ~100,000 partitions per Milvus collection
- The fix was hierarchical capping: 400 collections per cluster, 1,000 partitions per collection, provisioning new clusters as the customer base grows
- HNSW was chosen over IVF-SQ8 and DiskANN because the 500ms p99 latency target and high recall requirements outweighed memory cost — the right index depends on your specific constraints, not universal superiority
- 75% of bases are idle any given week; Milvus partition offloading keeps only hot partitions in memory, making HNSW economically viable — this only works because access patterns are bursty and bimodal, not uniform
- Disaster recovery re-embeds from source data rather than restoring snapshots — the existing async embedding pipeline just runs against an empty cluster, handling corruption, model migrations, and data residency changes with one procedure
- The transferable principle: let your data's actual properties drive architecture, not the other way around — the technologies (Milvus, HNSW) are interchangeable, the reasoning is not

## Synthesis
ByteByteGo's deep dive into Airtable's vector infrastructure reveals how a single upstream property — customers running small, isolated, mostly-cold bases — cascaded through every architectural decision in their semantic search system. The article is a case study in data-driven architecture, showing how each choice only makes sense in light of the one before it.

The partitioning strategy came first. Airtable chose one partition per base over shared partitions with customer ID filtering, prioritizing physical isolation, trivial deletion, and avoiding query-time filter overhead. This hit a wall at ~100,000 partitions per Milvus collection, where partition creation latency jumped from 20ms to 250ms and loading took over 30 seconds. The solution was hierarchical capping — 400 collections per cluster, 1,000 partitions each — trading operational complexity for predictable performance at every layer. This pattern of introducing a new grouping level above a flat namespace that hit a wall is recognizable across distributed systems, from sharded databases to message broker topics.

Index selection followed. Airtable benchmarked HNSW, IVF-SQ8, and DiskANN against the classic memory-latency-recall triangle. HNSW won because their 500ms p99 latency target ruled out DiskANN's disk-touching queries, and high recall requirements (directly affecting how good the Omni AI feature feels) ruled out IVF-SQ8's compression artifacts. The memory cost was real but addressed separately. The article emphasizes that no index is universally better — the right choice depends on your specific priorities and constraints.

The memory problem was solved by measurement, not guessing. Analysis showed only 25% of bases were read from or written to in any given week — a bimodal, bursty access pattern. Milvus's partition offloading let Airtable keep only hot partitions in memory and push cold ones to storage, reloading within seconds when accessed. This only works because the access pattern is bursty; if usage were uniform, cold offloading would save nothing. The HNSW choice became economically viable only because of this measurement.

Recovery was the most elegant decision. Instead of backup-and-restore, Airtable spins up a fresh Milvus cluster and re-embeds from source data using the existing async embedding pipeline — the same pipeline that normally generates embeddings on data changes. Most-used bases are re-embedded first for quick user-visible recovery; the rest rebuild lazily. This handles corruption, model migrations, and data residency changes with one simple procedure, because recovery is not a separate system but the existing pipeline running against an empty cluster.

The article's core lesson: technologies are interchangeable, but the discipline of letting data properties drive architecture is harder to replicate. Change any upstream property — if all bases were always hot, if strict consistency were required, if per-customer datasets were tiny — and the design would fall apart.