# The 2026-07-28 MCP Specification Release Candidate
**Source**: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
**Date**: May 21, 2026
**Author**: David Soria Parra, Den Delimarsky
**Keywords**: MCP, Model Context Protocol, specification, stateless, extensions, authorization, OAuth, HTTP, JSON-RPC

## Elevator pitch
The MCP 2026-07-28 release candidate delivers the largest protocol revision since launch, making the core stateless for commodity HTTP infrastructure, introducing first-class extensions including server-rendered UIs and Tasks, and hardening authorization for real-world OAuth deployments.

## Takeaways
- MCP is now stateless at the protocol layer: no more initialize/initialized handshake, no Mcp-Session-Id, and any request can land on any server instance.
- New routing headers (Mcp-Method, Mcp-Name) enable load balancers and gateways to route without inspecting request bodies; list responses now carry ttlMs for cache control.
- W3C Trace Context propagation is formalized, enabling distributed tracing from host application through MCP server to downstream services in a single span tree.
- Extensions are now first-class with reverse-DNS identifiers, independent versioning, and a formal SEP process; MCP Apps (server-rendered UIs) and Tasks are the first official extensions.
- Authorization is hardened with iss validation per RFC 9207, OpenID Connect application_type declaration, and documented refresh token flows.
- Three features are deprecated: Roots, Sampling, and Logging, with replacements documented and a 12-month minimum deprecation window.

## Synthesis
The MCP 2026-07-28 release candidate represents a fundamental rearchitecture of the Model Context Protocol, driven by real-world deployment experience since the 2025-11-25 specification. The headline change is statelessness: the initialize/initialized handshake and session-based routing that previously required sticky sessions and shared session stores are gone. An MCP request is now a self-contained HTTP call with protocol version, method, and name in headers, routable by any load balancer without deep packet inspection.

This stateless design doesn't preclude stateful applications. The protocol now encourages an explicit-handle pattern where tools mint identifiers that the model passes as arguments across calls. The maintainers argue this is more powerful than hidden session state because the model can compose handles across tools and reason about them directly. Server-to-client requests (like elicitation prompts) are restructured around InputRequiredResult with cryptographic requestState, so any server instance can pick up a retry.

Extensions graduate from an ad-hoc mechanism to a formal framework with reverse-DNS identifiers, independent versioning, and a dedicated SEP track. MCP Apps lets servers ship sandboxed HTML interfaces that hosts render in iframes, with UI actions going through the same audit and consent path as tool calls. Tasks moves from experimental core feature to a properly designed extension with a task handle lifecycle (tasks/get, tasks/update, tasks/cancel) that fits the stateless model.

Authorization receives significant hardening: mandatory iss validation mitigates mix-up attacks, Dynamic Client Registration supports CLI/desktop application types, and refresh token flows are documented. The observability story improves with formalized W3C Trace Context propagation and deprecation of the old Logging feature in favor of OpenTelemetry. Tools now support full JSON Schema 2020-12 including composition operators and conditionals.

The governance changes are equally important. A formal feature lifecycle policy guarantees at least 12 months between deprecation and removal. The conformance suite now gates Standards Track SEPs from reaching Final status. The maintainers position this release as a foundational clean break, after which future revisions should require minimal transport or lifecycle code changes. The final specification ships July 28, 2026, with a ten-week validation window for SDK maintainers.
