# MCP vs RAG vs AI Agents
**Source**: https://blog.bytebytego.com/p/ep224-mcp-vs-rag-vs-ai-agents
**Date**: 2026-09-05
**Author**: ByteByteGo
**Keywords**: MCP, RAG, AI agents, distributed systems, virtualization, containerization, HTTP, HTTPS, system design

## Elevator pitch
ByteByteGo's EP224 newsletter clarifies the differences between MCP (a standard protocol for connecting AI models to external tools), RAG (a pattern for pulling fresh information into model responses), and AI agents (autonomous systems that perform tasks and make decisions), alongside a system design refresher covering distributed systems patterns, virtualization vs. containerization, and HTTP vs. HTTPS.

## Takeaways
- MCP is an open standard protocol that connects AI models to external tools and data sources (APIs, databases, Gmail, Slack, GitHub) through a single standard interface, replacing per-application integration code
- RAG pulls fresh information from external data sources (docs, PDFs, databases) when a query comes in, so the model doesn't have to rely on stale training data or hallucinate
- AI agents are autonomous systems that perform tasks and make decisions, unlike chatbots which are simple request-response loops
- The newsletter also covers 9 distributed systems patterns: replication, sharding, consistent hashing, PubSub, circuit breaker, retry with backoff, leader election, quorum read/write, and saga
- Virtualization provides hardware-level isolation (each VM runs a full OS) while containerization provides OS-level isolation (shared kernel, isolated processes) — containers start in milliseconds vs. minutes for VMs

## Synthesis
ByteByteGo's EP224 newsletter provides a concise technical comparison of three concepts that are often conflated in the AI engineering space. MCP (Model Context Protocol) is positioned as an open standard that gives AI models a uniform way to connect to external systems — APIs, databases, and applications like Gmail, Slack, or GitHub — eliminating the need to write bespoke integrations for each service. RAG (Retrieval-Augmented Generation) is a complementary pattern where the model fetches fresh information from external sources at query time rather than relying on training data, reducing hallucination. AI agents represent a further abstraction: systems that perform tasks autonomously and make decisions, moving beyond the request-response chatbot paradigm.

The newsletter also includes a system design refresher covering nine distributed systems patterns. Replication copies data across servers for availability; sharding splits databases horizontally; consistent hashing distributes data via a virtual ring; PubSub decouples producers from consumers; circuit breaker prevents repeated failed calls; retry with backoff handles transient failures; leader election designates a master node; quorum read/write ensures consistency across replicas; and saga manages distributed transactions through compensating actions.

The virtualization vs. containerization comparison highlights the fundamental tradeoff: VMs provide strong isolation (full OS per instance) at the cost of heaviness and slow startup, while containers share the host kernel for lightweight, fast-starting processes but require kernel compatibility. The HTTP vs. HTTPS breakdown traces the TLS handshake step by step: TCP handshake, certificate check, asymmetric key exchange, and symmetric data transmission — emphasizing that HTTPS is not just "encrypted HTTP" but a multi-stage cryptographic protocol.