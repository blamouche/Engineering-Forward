# Building agents that reach production systems with MCP

**Source**: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
**Date**: April 22, 2026
**Author**: Anthropic
**Keywords**: MCP, Anthropic, production agents, integrations, tools, protocols

## Elevator pitch
Anthropic argues that MCP is emerging as the default integration layer for production agents because it standardizes auth, discovery, and semantics across remote systems better than direct API calls or CLIs.

## Takeaways
- Anthropic contrasts direct APIs, CLIs, and MCP as three integration patterns with different tradeoffs.
- It argues MCP becomes most compelling when agents run in the cloud and need reusable remote integrations.
- The company recommends intent-based tools, remote servers, and code-execution patterns for large surfaces.
- Tool search and programmatic tool calling are presented as context-saving client-side patterns.
- Skills and MCP are framed as complementary layers: one gives access, the other gives procedural know-how.

## Synthesis
Anthropic’s MCP post is really about the infrastructure layer that sits between models and production systems. The company argues that direct API calls and CLIs are both useful starting points, but they do not scale cleanly once agents need to work across many services, clients, and execution environments. MCP is positioned as the protocol answer to that problem: one integration surface that standardizes discovery, authentication, and semantics so an agent can connect to many systems without bespoke glue code each time.

The most convincing part of the argument is environmental. As Anthropic notes, production agents increasingly run in the cloud, and the systems they need to reach are remote, authenticated, and distributed across many products. That is exactly where CLI-based approaches become awkward and direct API integrations become expensive to duplicate. MCP promises a common layer that is portable across Claude, ChatGPT, Cursor, VS Code, and other clients.

The design guidance is also practical. Anthropic recommends grouping tools around intent rather than mirroring every endpoint, using remote servers for distribution, and exposing code-execution patterns when the surface area is too large for hand-authored tools. On the client side, it emphasizes progressive disclosure, especially tool search and programmatic tool calling, to keep context usage under control. That matters because context pressure is one of the hidden costs of agent integrations.

Stepping back, the article is part technical guidance and part ecosystem strategy. Anthropic has a clear interest in making MCP the standard protocol for agent integrations. But the case it makes is still strong: as agents leave the sandbox and start touching real production systems, teams will want a reusable, inspectable, cross-platform way to connect them. MCP’s momentum suggests the market increasingly agrees.
