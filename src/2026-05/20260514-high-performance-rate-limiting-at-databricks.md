# High Performance Rate Limiting at Databricks
**Source**: https://blog.bytebytego.com/p/high-performance-rate-limiting-at
**Date**: May 13, 2026
**Author**: ByteByteGo
**Keywords**: rate limiting, Databricks, Redis, in-memory counters, token bucket, optimistic rate limiting, batch-reporting, Dicer, tail latency, horizontal scaling

## Elevator pitch
Databricks redesigned their rate limiter by moving counters from Redis to sharded in-memory storage and inverting the sync model so clients report usage after the fact rather than checking before every request, cutting tail latency by 10x.

## Takeaways
- The old architecture's two network hops (Envoy → Rate Limit Service → Redis) dominated latency, with P99 network times of 10-20ms between cloud services
- Moving counts in-memory via Dicer (a routing layer for sharded state) eliminated the Redis hop and the single point of failure
- The most consequential change was batch-reporting: clients make no remote calls on the rate limit path, reporting usage every ~100ms and receiving rejection instructions for the future
- Token bucket replaced fixed window once in-memory storage made cheap compare-and-set viable, solving the window-boundary burst problem
- Databricks explicitly accepts that some requests will overshoot the limit between reports, betting that backends can tolerate ~5% overshoot for dramatically better performance

## Synthesis
This ByteByteGo article, published May 13, 2026, dissects Databricks' redesign of their rate limiting infrastructure following the launch of real-time model serving. The piece is a case study in how performance constraints at extreme scale force architectural decisions that initially seem counterintuitive.

The starting point is a familiar architecture: an Envoy ingress gateway calls a Ratelimit Service, which queries a single Redis instance for per-key counters. When real-time model serving launched, a single customer could generate orders of magnitude more traffic than the service was designed for. Three cracks appeared: climbing tail latency from two network hops (each with P99 of 10-20ms), diminishing returns from machine additions and caches, and the Redis singleton as an unacceptable single point of failure.

The redesign unfolded in three coupled decisions. First, algorithm choice: fixed window was replaced by token bucket, which continuously fills and drains rather than resetting at interval boundaries, preventing the classic window-boundary burst where a client sends double the intended rate. Token bucket requires cheap compare-and-set semantics on every increment, which was prohibitive in Redis but nearly free in-memory.

Second, storage location: the team built on Dicer, an internal routing layer that lets services keep state in memory while remaining horizontally scalable. Dicer partitions keys across servers and lets any client find the authoritative owner for a given key. This moved every counter in-memory, eliminated the Redis network hop, and made the Ratelimit Service horizontally scalable by adding replicas to Dicer's pool. Restarts and scale events redistributed ownership without external coordination.

Third, and most significant, the sync model was inverted. The team asked: does every request truly need to wait for a rate limit decision? The answer was no. In the batch-reporting model, clients make zero remote calls on the rate limit path. They count requests locally (allowed vs. rejected, grouped by key), and every ~100ms a background thread reports these counts to the Ratelimit Service. The server responds with instructions: which keys should be rejected, until when, and at what rejection rate. The client's default is to allow — rejection only happens when the client already has a reason from a previous report.

This inversion had substantial impact: tail latency fell by roughly 10x (calls became effectively free for clients), spiky inbound traffic turned into constant outbound reports, and server load became predictable. The explicit tradeoff is that some requests will overshoot the limit in the ~100ms window between reports. Three mechanisms bound this overshoot to roughly 5%: a rejection rate formula returned by the server, a client-side local rate limiter for defense in depth, and the token bucket algorithm itself which remembers overshoot across intervals.

The article's deeper insight is the dependency chain binding these decisions: token bucket needs cheap CAS → rules out Redis → forces in-memory state → forces sharding (one server can't hold all counters) → sharding with authoritative per-key ownership enables batch-reporting. The rollout order followed these constraints: sharded in-memory came first, batch-reporting on top, token bucket last. The Databricks story is ultimately about trading strict accuracy for speed, and being explicit about which tradeoffs your system can absorb.
