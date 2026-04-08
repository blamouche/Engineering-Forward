# Principles of Mechanical Sympathy

**Source**: https://martinfowler.com/articles/mechanical-sympathy-principles.html
**Date**: April 8, 2026
**Author**: Unknown
**Keywords**: mechanical sympathy, performance, CPU cache, false sharing, single writer principle, batching, observability

## Elevator pitch
This article updates Martin Thompson’s mechanical-sympathy tradition for modern software teams by showing how predictable memory access, avoiding false sharing, single-writer ownership, and natural batching can turn performance from an afterthought into an architectural property.

## Takeaways
- Mechanical sympathy starts with understanding memory hierarchy and favoring predictable, sequential access over scattered random access.
- False sharing remains a hidden latency trap when multiple threads write to different variables that occupy the same cache line.
- The single-writer principle is presented as the most practical way to avoid mutex contention and simplify access to shared writable resources.
- Natural batching improves throughput and latency by building batches greedily as soon as work appears instead of waiting on fixed timeouts.
- The article ends with an important guardrail: observability must come before optimization so teams know what to improve and when to stop.

## Synthesis
This is a useful bridge between low-level performance lore and modern application design. Mechanical sympathy can sound like a niche obsession for systems programmers, but the article reframes it as a general way to think about software architecture. The central idea is simple: hardware has strong preferences, and code that aligns with them often gets dramatically better latency and throughput without exotic tricks.

What makes the piece practical is its emphasis on a few reusable principles rather than a bag of micro-optimizations. Sequential access beats randomness because caches and prefetchers can help you. False sharing hurts because CPUs coordinate cache lines, not semantic variables. The single-writer principle reduces both contention and conceptual complexity by concentrating ownership of mutable resources. Natural batching exploits queue dynamics to improve utilization without the unnecessary waiting imposed by timer-based batching.

The AI inference example is especially timely. A lot of current software bottlenecks come from wrapping expensive models with naive concurrency patterns: many request threads, one mutex, accidental head-of-line blocking. Recasting the model runtime as an actor with explicit ownership and greedy batch formation is a good illustration of how systems thinking can outperform brute-force parallelism.

The closing reminder about observability is what keeps the article grounded. Mechanical sympathy is not an excuse for premature cleverness. It is a way to reason about where performance wins are likely when measurements show a real problem. In that sense, the article’s broader message is not “optimize everything,” but “design with enough sympathy for the machine that good performance becomes easier to achieve on purpose.”
