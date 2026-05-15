# High Performance Rate Limiting at Databricks
**Source**: https://blog.bytebytego.com/p/high-performance-rate-limiting-at
**Date**: 2026-05-13
**Author**: ByteByteGo
**Keywords**: rate limiting, Databricks, token bucket, Dicer, batch-reporting, optimistic rate limiting, in-memory counters, distributed systems, Redis

## Elevator pitch
Databricks redesigned its rate limiter from a synchronous Redis-backed architecture to an optimistic, in-memory, token-bucket system with asynchronous batch-reporting, trading strict accuracy for 10x lower tail latency and horizontal scalability.

## Takeaways
- The old architecture used Envoy → Ratelimit Service → Redis, creating two network hops on the critical path, with P99 latency of 10-20ms from cloud provider networking alone.
- Moving counters in-memory via Dicer (a routing layer for sharded ownership) eliminated the Redis hop and single point of failure.
- Batch-reporting inverts the model: instead of asking permission per-request, clients report counts every ~100ms and the server tells them what to reject, reducing tail latency by ~10x.
- Token bucket algorithm (now viable in-memory) prevents fixed-window "crossover" bursts and approximates a sliding window without extra burst capacity.
- The three decisions—algorithm (token bucket), state location (sharded in-memory), and sync model (async batch-reporting)—are coupled and had to be rolled out in dependency order.

## Synthesis
In early 2023, Databricks ran its rate limiter on a straightforward stack: an Envoy ingress gateway, a Ratelimit Service, and a single Redis instance for counters. This worked until real-time model serving launched, generating orders of magnitude more traffic and exposing three cracks: rising tail latency from two network hops, diminishing returns from adding machines and caches, and a single point of failure in the Redis instance.

The team's first move was to ask a deeper question: does rate limiting actually need durable storage? A per-second count is transient by nature—when that second rolls over, the old value is irrelevant. This insight led them to move counters entirely in-memory using a routing layer called Dicer. Dicer partitions keys across servers, gives each server authoritative ownership of its slice, and lets any client find the right owner. The Redis hop vanished, tail latency dropped sharply, and horizontal scaling became additive again.

But making the server fast only shifted the bottleneck: clients still made synchronous calls for every single request. The most consequential decision was to invert the model entirely. Instead of clients asking "may I proceed?" before every request, they now proceed optimistically and report their counts asynchronously every ~100ms. The server responds with rejection instructions—which keys to block, until when, at what rate. This "batch-reporting" approach turned spiky inbound traffic into constant outbound reports and made server-side load predictable.

The inversion introduces overshoot: requests can leak through between reports. To keep overshoot within roughly 5%, Databricks layered three fixes: a rejection rate computed server-side based on recent traffic patterns, a client-side local rate limiter for extreme spikes, and finally, a migration to token bucket algorithm. Token bucket continuously fills and drains, can go negative to remember past excess, and eliminates the fixed-window boundary problem where traffic can blast through at double the intended rate. Token bucket requires compare-and-set semantics on every increment—slow in Redis but nearly free in memory.

The entire rebuild follows a dependency chain: token bucket requires cheap compare-and-set, which rules out Redis at Databricks' QPS, forcing in-memory state; in-memory state across millions of counters forces sharding; sharding with authoritative per-key ownership enables batch-reporting. This explains the rollout order: sharded in-memory first, batch-reporting on top, token bucket last. The result: a rate limiter that is faster, more resilient, horizontally scalable, and explicitly designed around the tradeoff that strict accuracy is too expensive at scale.
