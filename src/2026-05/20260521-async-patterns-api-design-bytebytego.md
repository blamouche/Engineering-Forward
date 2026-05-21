# A Guide to Async Patterns in API Design
**Source**: https://blog.bytebytego.com/p/a-guide-to-async-patterns-in-api
**Date**: 2026-05-21
**Author**: ByteByteGo (Alex Xu)
**Keywords**: async patterns, API design, polling, WebSockets, SSE, webhooks, message queues, GraphQL subscriptions

## Elevator pitch
ByteByteGo's comprehensive guide walks through the full spectrum of asynchronous API patterns — from short/long polling to WebSockets, server-sent events, webhooks, async APIs with status polling, message queues, and GraphQL subscriptions — explaining when request-response breaks down and which pattern fits each use case.

## Takeaways
- Request-response handles the majority of web applications but fails for long-running work, server-initiated events, continuous interactions, and messages that outlive the connection
- The eight patterns covered: short polling, long polling, server-sent events (SSE), WebSockets, webhooks, async APIs with status polling, message queues, and GraphQL subscriptions
- Each pattern has distinct trade-offs in complexity, latency, scalability, and client/server coupling
- The guide starts from where request-response stops fitting and progressively introduces more sophisticated patterns
- Published as a paid Substack post but available through Alex Xu's free post claim system

## Synthesis
ByteByteGo's latest deep-dive tackles a topic that every backend engineer eventually confronts: request-response only gets you so far. The guide systematically covers the eight major async API patterns that have emerged to handle the cases where a single synchronous HTTP exchange isn't sufficient — long-running operations, server-pushed events, continuous data streams, and durable messaging.

The progression is pedagogical: starting with the simplest extensions of HTTP (short polling, then long polling), moving through push-based alternatives (SSE for server-to-client streaming, WebSockets for bidirectional communication), and culminating in fully decoupled patterns (webhooks, message queues, async APIs with status endpoints). GraphQL subscriptions are included as the GraphQL ecosystem's answer to real-time data.

The practical value is in the decision framework. Each pattern comes with its preferred use case, latency characteristics, scalability profile, and implementation complexity. The guide helps engineers avoid the common mistake of reaching for WebSockets when SSE would suffice, or building a custom polling system when a message queue already solves the problem.

For the broader engineering community, this kind of systematic pattern catalog is increasingly important as AI-powered applications introduce new async requirements — long-running agent tasks, streaming model outputs, and event-driven agent architectures all depend on getting these patterns right. The article doesn't explicitly connect to AI, but the timing makes it practically relevant to the agent infrastructure discussions happening across the industry.
