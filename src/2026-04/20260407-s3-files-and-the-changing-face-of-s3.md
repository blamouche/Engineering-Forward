# S3 Files and the changing face of S3

**Source**: https://www.allthingsdistributed.com/2026/04/s3-files-and-the-changing-face-of-s3.html
**Date**: April 7, 2026
**Author**: Andy Warfield
**Keywords**: Amazon S3, S3 Files, S3 Tables, S3 Vectors, agentic development, data infrastructure, storage

## Elevator pitch
Andy Warfield argues that as agentic development collapses the cost of building applications, storage systems need to become higher-level primitives; S3 Files is Amazon’s attempt to remove the object-vs-filesystem friction that still slows down data-heavy workflows.

## Takeaways
- The original motivation comes from genomics and other burst-parallel workloads where users kept copying data between filesystems and object storage just to satisfy tooling expectations.
- Warfield argues agents make this worse because more people can now assemble applications quickly, which increases the premium on durable, reusable data abstractions.
- Amazon’s recent S3 push reframes storage around native data types: objects, tables, vectors, and now files.
- S3 Tables and S3 Vectors are presented as earlier examples of the same strategy: raise the abstraction level while preserving S3 durability and scale.
- The deeper claim is that data should outlive rapidly changing applications, and storage products should reduce attachment costs as software gets more disposable.

## Synthesis
This piece is less a feature announcement than a storage thesis for the agent era. Warfield starts from a familiar pain point: real workloads rarely fail because the data does not exist, they fail because the data sits behind the wrong interface. In genomics, that meant Linux tools expecting a local filesystem while the cloud-native execution model wanted S3. The result was an expensive choreography of copying, syncing, and reconciling versions.

The interesting update is that Warfield sees agentic software development turning this from an annoyance into a strategic bottleneck. If application creation gets dramatically cheaper, more domain experts will build specialized tools. That makes the code layer more fluid and disposable, while the data layer becomes even more valuable. Storage systems therefore need to act less like passive buckets and more like durable, composable primitives that many transient applications can attach to.

That logic explains Amazon’s recent sequence of launches. S3 Tables addressed the gap between raw objects and the expectations of structured analytics. S3 Vectors addressed the gap between archival storage economics and the needs of semantic search. S3 Files extends the same idea to workloads that still assume POSIX-like file access. Rather than forcing every customer to maintain translation glue, S3 absorbs more of that adaptation into the platform.

The broader implication is that infrastructure vendors are repositioning around attachment friction. In an agent-heavy world, the winners may be the systems that make data easiest to discover, mount, mutate, and reuse across many short-lived applications. S3 Files matters not because files are new, but because it signals that even object storage now has to compete on ergonomics for rapidly iterated software ecosystems.
