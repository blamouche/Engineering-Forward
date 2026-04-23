# B-Trees vs LSM Trees: Comparison and Trade-Offs

**Source**: https://blog.bytebytego.com/p/b-trees-vs-lsm-trees-comparison-and
**Date**: April 22, 2026
**Author**: ByteByteGo
**Keywords**: databases, B-Trees, LSM Trees, storage engines, compaction, indexing

## Elevator pitch
ByteByteGo compares B-Trees and LSM Trees as two different answers to the same storage-engine problem: whether you optimize for in-place reads and updates or for write-heavy sequential ingestion with deferred compaction.

## Takeaways
- B-Trees keep data ordered in-place and are strong for point reads and range scans.
- LSM Trees optimize heavy writes by turning random updates into sequential appends plus background compaction.
- The tradeoff is that LSMs often pay in read amplification, compaction cost, and operational complexity.
- Choice depends on workload shape more than on one structure being universally better.
- The article reinforces that database performance is driven by storage-engine economics, not just query syntax or feature lists.

## Synthesis
The ByteByteGo comparison is a useful refresher on a systems tradeoff that keeps resurfacing as workloads change. B-Trees and LSM Trees both solve the problem of organizing persistent data efficiently, but they optimize opposite pain points. B-Trees prioritize ordered access and in-place updates, which makes them good for balanced read-heavy workloads and range queries. LSM Trees treat writes as the primary bottleneck and therefore convert them into sequential appends and deferred compaction, which can dramatically improve ingestion throughput.

What makes the comparison relevant is that it is really about cost shifting. B-Trees pay more during writes and updates because maintaining order in-place is expensive. LSM Trees make writes cheaper up front but move the complexity into background compaction and read amplification. The system still pays, just in a different place. That framing is often more useful than trying to memorize which structure is “faster.”

The broader lesson is that storage-engine choice is inseparable from workload shape. If an application does frequent point lookups, range scans, and updates that need predictable latency, B-Trees often remain attractive. If it ingests huge write volumes and can tolerate compaction and some read overhead, LSM Trees can win. Many real-world systems then add caches, bloom filters, and tuning layers to compensate for the structure they chose.

That is why this topic remains so durable. It is not just academic database internals. It is a practical reminder that infrastructure design is always about moving tradeoffs around. As AI, analytics, and application backends create more varied data patterns, understanding the write-read-compaction balance behind these structures becomes more, not less, important.
