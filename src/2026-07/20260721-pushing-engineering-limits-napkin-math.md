# Pushing Software Engineering Limits with "Napkin Math"
**Source**: https://newsletter.pragmaticengineer.com/p/pushing-software-engineering-limits
**Date**: 2026-07-21
**Author**: Gergely Orosz (The Pragmatic Engineer), interviewing Simon Eskildsen (turbopuffer)
**Keywords**: napkin math, first principles, turbopuffer, search infrastructure, Shopify, engineering practices, venture capital

## Elevator pitch
Simon Eskildsen's journey from Shopify infrastructure to founding turbopuffer shows how first-principles "napkin math" — quick calculations of theoretical performance limits — can reveal that existing systems are orders of magnitude more expensive than necessary, and how that insight became a search engine serving Cursor and others.

## Takeaways
- Napkin math is a table of ~50 key numbers (DRAM bandwidth, S3 costs per GB, round-trip latencies) maintained on GitHub with a script to regenerate them, used to challenge benchmark-driven decisions with theoretical limits
- At Shopify, napkin math revealed that a database benchmark claiming 10-second queries should theoretically take 10ms — exposing that the benchmark was measuring distributed queries across 100 nodes (p99) rather than single-node performance
- MySQL can handle 5x more transactions per second than the theoretical maximum of fsyncs per second — this "first-principle gap" led Simon to discover that MySQL groups transactions and does "group commits" to merge parallel fsync operations
- turbopuffer was born when LLM context windows were small (4-8KB in early 2023) and fast search was critical for AI applications, but existing search solutions cost $30K/month while infrastructure was only $5K/month
- The founding insight: store search data in S3 (cheap, reliable, high-latency), cluster and organize files, put an NGINX reverse proxy in front for caching — the simplest possible architecture that upheld its invariants (shut down all VMs, no data lost, all writes committed directly to blob storage)

## Synthesis
This deep-dive interview with Simon Eskildsen traces a career arc from competitive programming through eight years at Shopify infrastructure to founding turbopuffer, a search engine that reduced Cursor's search costs from $80K/month to $4K/month. The thread connecting all these phases is "napkin math" — a practice of doing quick, back-of-envelope calculations to estimate the theoretical limits of systems.

At Shopify, napkin math became a superpower for reviewing architectural decisions. When product teams presented benchmark results justifying database choices, Simon could show that the measured performance was orders of magnitude worse than theoretical limits — revealing that benchmarks measured the wrong things (distributed p99 instead of single-node latency, for instance). This practice of identifying "first-principle gaps" — where real performance diverges significantly from theoretical bounds — became both an auditing tool and a discovery mechanism.

The creation of turbopuffer illustrates this approach in startup form. When AI applications needed fast search to fill tiny LLM context windows, existing vector search solutions charged $30K/month for what should theoretically cost orders of magnitude less. Simon's napkin math showed that S3 storage ($0.02/GB) combined with intelligent clustering could deliver search at a fraction of the cost. The first version was deliberately minimal: no caching layer, just an NGINX reverse proxy in front of S3. Performance improvements came from caching S3 objects, not from adding complexity.

The article also offers a rare honest take on venture capital. Simon identifies six reasons founders raise VC — R&D, growth, ego, employee rewards, strategic partnerships, and M&A — and is candid about ego being a dangerous but common motivator. turbopuffer raised only $700K initially (after an $8M seed), keeping burn extremely low while proving the product worked. Cursor became customer #1 when Simon flew to San Francisco to help fix their existing database problems before selling them his own product — a case study in building trust before asking for a sale.