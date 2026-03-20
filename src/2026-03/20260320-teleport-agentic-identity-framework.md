# Teleport Agentic Identity Framework
**Source**: https://goteleport.com/docs/agentic-identity-framework/
**Date**: 2026-03-20
**Author**: Teleport / Gravitational
**Keywords**: agentic security, AI agents, identity management, MCP, access control, audit, infrastructure security

## Elevator pitch
Teleport's Agentic Identity Framework provides cryptographic identities, fine-grained access controls, and comprehensive audit trails for AI agents operating across infrastructure, addressing the security vacuum left by the rapid adoption of autonomous agents.

## Takeaways
- The framework issues cryptographic identities to agents, enabling delegation flows and long-running workload attestation without shared secrets
- MCP server integration provides authorization for agent calls to databases, services, and infrastructure with full audit capability
- Continuous discovery detects shadow agent deployments and policy violations before they escalate
- Features include rate limiting, budget controls, and prompt/response tracking for LLM applications
- Many capabilities are still in development, reflecting the early maturity of agentic security tooling

## Synthesis
As autonomous AI agents gain access to production infrastructure, databases, and internal services, the security challenge shifts from "who is using this system" to "what is this agent authorized to do, and can we prove it did only that." Teleport's Agentic Identity Framework addresses this challenge by extending the company's established infrastructure access controls into the agentic layer.

The framework organizes around four pillars. Agentic Identity handles the fundamental problem of establishing who an agent is: cryptographic identities are issued to agents, delegation flows enable agents to act on behalf of users with limited scope, and long-running workload attestation avoids the security risks of shared secrets or long-lived credentials. This mirrors how modern human identity systems work but is adapted for the non-interactive, automated patterns that agents exhibit.

Agentic Access builds on identity to control what agents can actually do. By integrating at the MCP (Model Context Protocol) server layer, Teleport can intercept, authorize, and log every tool call an agent makes—whether to a database, an internal service, or a piece of infrastructure. This creates a complete record of agent actions that satisfies audit and compliance requirements.

Agentic Security extends the access controls with continuous discovery—automatically finding agent deployments and MCP endpoints that haven't been formally registered, reducing the shadow deployment problem that has plagued both cloud and on-premise infrastructure. Policy violation detection operates continuously rather than on scheduled scans.

The Scheduling and Orchestration pillar integrates with modern workflow tools to ensure that even complex, multi-step agentic tasks operate within defined security boundaries. Rate limiting, budget controls, and prompt/response tracking complete the picture by enabling organizations to constrain agent behavior at the cost, velocity, and content dimensions simultaneously. The number of features marked "in progress" or "not yet started" on the documentation page is itself informative—it reflects the genuine frontier status of enterprise agentic security.
