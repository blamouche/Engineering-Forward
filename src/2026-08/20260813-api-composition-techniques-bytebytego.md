# A Detailed Guide to API Composition Techniques
**Source**: https://blog.bytebytego.com/p/a-detailed-guide-to-api-composition
**Date**: August 13, 2026
**Author**: ByteByteGo
**Keywords**: APIs, microservices, aggregation, GraphQL, BFF

## Elevator pitch
API composition is the design choice of where to assemble data from several services, balancing latency, resilience, caching, and ownership.

## Takeaways
- Client-side fan-out makes mobile latency and error handling worse.
- Gateways and backends-for-frontends centralize composition close to services.
- GraphQL makes data selection explicit but adds operational complexity.
- Edge composition can improve latency for cacheable, geographically distributed reads.
- The ownership model should follow the product contract, not only the underlying services.

## Synthesis
The article starts with a familiar microservices problem: a product view needs profile, orders, delivery status, and recommendations, yet those records live behind different services. The composition layer collects and shapes those responses into the representation needed by the caller. It can run in the client, a gateway, a dedicated backend-for-frontend, at the edge, or occasionally in a service itself. That location is not merely an implementation detail; it determines latency, caching, failure behaviour, and the team responsible for the user-facing contract.

Client-side composition avoids an extra server component, but it asks a device on a weak connection to make several expensive round trips and to handle partial failure. A server-side layer often turns that into one external call and several cheap internal calls. It can also supply sensible defaults, timeouts, fallback behaviour, and a cache tailored to the screen. The tradeoff is a new layer that must be owned and evolved rather than becoming an ungoverned aggregation service.

The practical lesson is to choose composition based on the workload. A BFF works well where distinct web and mobile products need distinct response shapes. GraphQL gives consumers selection power but requires schema governance and guardrails against costly queries. Edge composition benefits globally distributed, mostly-read traffic but is a poor fit for orchestration that needs private services or complex consistency. The composition boundary should make the interface simpler for callers without hiding operational responsibilities.
