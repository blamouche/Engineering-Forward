# Figma's next-generation data caching platform
**Source**: https://www.figma.com/blog/figmas-next-generation-data-caching-platform/
**Date**: March 27, 2026
**Author**: Kevin (Figma)
**Keywords**: Redis, caching, infrastructure, observability, scalability

## Elevator pitch
Figma rebuilt its Redis caching stack into FigCache—a stateless proxy plus first‑party clients—to isolate connection spikes, improve reliability, and add end‑to‑end observability across its ephemeral data platform.

## Takeaways
- Redis evolved into a critical dependency, exposing scalability and reliability risks.
- FigCache introduces a proxy data plane and standardized client libraries.
- The system decouples client connection churn from Redis clusters to prevent thundering herds.
- Configuration‑driven routing enables multi‑cluster traffic management and extensibility.
- The rollout delivered six‑nines caching uptime and major observability improvements.

## Synthesis
Figma’s infrastructure team describes the rearchitecture of its caching layer, moving from a direct‑to‑Redis model to a new platform called FigCache. As Figma’s user base grew, Redis shifted from a non‑critical component to a key dependency for site availability. That scale exposed issues: hard connection limits, thundering herds during traffic spikes, inconsistent observability across client libraries, and limited protection against misrouted or corrupting traffic. Earlier mitigations—like removing Redis dependencies in some subsystems or building localized pooling—helped, but they were not a durable solution.

The team set out to design a long‑term platform with clear objectives: isolate Redis from client volatility, provide consistent observability, simplify horizontal scalability, centralize routing across clusters, and enable future storage backends. To reach those goals, they built FigCache, a stateless proxy service that speaks the Redis protocol (RESP) and sits between services and Redis clusters. FigCache is paired with first‑party client libraries in Go, Ruby, and TypeScript, which wrap existing open‑source clients to standardize configuration and instrumentation without forcing major application rewrites.

A core technical decision was to build rather than buy. Off‑the‑shelf proxies didn’t expose enough command semantics to implement guardrails or protocol extensions, and forking open‑source solutions would have been brittle. FigCache’s proxy layer allowed Figma to add features like distributed locking, graceful connection draining, and a cluster‑aware shim while preserving compatibility with existing clients. Internally, the system separates a frontend RPC layer from a backend execution layer, with a configuration‑driven engine tree (expressed in Starlark) that can route, filter, or fan out commands based on keys or command types.

The migration strategy focused on minimizing risk: migrate clients to the new wrappers first, then roll out the proxy, and finally shift workloads incrementally with reversible feature flags. Performance risks were addressed with synthetic load testing, zonal traffic colocation to reduce latency, and continuous profiling in CI. This cautious rollout culminated in moving Figma’s main API service to FigCache in 2025.

The reported impact is significant. Connection counts on Redis clusters dropped by an order of magnitude, reducing volatility and helping scale the API fleet without stressing Redis. Reliability improved through connection pooling and centralized handling of failovers, while observability expanded to include end‑to‑end metrics, traces, and workload attribution. Operational burdens like cluster maintenance and shard failovers became routine, zero‑downtime events. Overall, FigCache represents Figma’s shift to a platform model for ephemeral data—one that treats caching as critical infrastructure with the same rigor as durable storage.
