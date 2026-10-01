# How DoorDash Built a Toolbox for AI Agents
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-09-30
**Author**: ByteByteGo
**Keywords**: DoorDash, Agent Gateway, MCP, Model Context Protocol, AI agents, tool access, authentication, authorization, OAuth, credential injection, tool catalog, bundles, filters, observability, agent security

## Elevator pitch
DoorDash built a centralized Agent Gateway to govern how AI agents discover and use tools across the enterprise — handling authentication, authorization, credential injection, tool-surface curation, and observability in a shared platform that processes millions of tool calls per week.

## Takeaways
- MCP provides a common interface for tool discovery (tools/list) and invocation (tools/call), but DoorDash needed more: access control, credential management, tool curation, rate limiting, and observability
- The Agent Gateway has two core components: a proxy (data plane, handles traffic) and a registry (control plane, stores governance configuration)
- Three concerns separated: Access (identity + permissions), Tool-surface Curation (which tools agents see), Operations (monitoring, rate limits, costs)
- Four credential arrangements: Internal Service Identity, Gateway-held Token (vendor keys kept from agents), Per-user OAuth (user-granted access stored encrypted), Service Principal (team automation with short-lived credentials)
- Credential injection keeps raw downstream credentials — vendor keys, OAuth refresh tokens — out of agents entirely, giving a central place to manage, rotate, audit, and revoke
- For clients supporting MCP elicitation, the gateway can present a connection prompt while keeping the original tool request open; for others, it returns a structured response with a connection URL
- Tool-surface curation uses bundles (combining tools from multiple MCP servers behind one endpoint) and filters (determining which tools appear based on bundle, agent, user group, environment)
- Discovery and execution are separate: discovery controls what's presented to the agent, invocation controls whether a request is allowed to proceed — a tool in a discovery response doesn't remove the need to authorize execution
- The gateway records structured events for each call with consistent fields (server, tool, bundle, owner, identities, authorization result, timing, sizes) enabling auditing, metrics, and investigation
- DoorDash reports 200+ registered MCP servers, 30+ agents/services, thousands of employees using the platform, and millions of tool calls each week
- Planned improvements: stronger agent identity with cryptographic identities and short-lived delegated credentials, dynamic tool discovery using task context, and evaluation of tool quality and security