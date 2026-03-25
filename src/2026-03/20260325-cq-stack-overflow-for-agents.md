# cq: Stack Overflow for Agents
**Source**: https://blog.mozilla.ai/cq-stack-overflow-for-agents/
**Date**: March 25, 2026
**Author**: Pete Ski
**Keywords**: agents, knowledge sharing, Stack Overflow, Mozilla AI, cq

## Elevator pitch
Mozilla AI proposes “cq,” a shared knowledge commons where agents can query and contribute learned fixes, reducing repeated failures and token waste.

## Takeaways
- Agent workflows repeatedly rediscover the same fixes in isolation.
- A shared commons could capture learnings and raise trust in agent outputs.
- cq aims to be a Stack Overflow‑style repository for agent knowledge.
- Trust should come from multi‑agent confirmation, not authority.
- Mozilla is building cq as open source with plugins, MCP, and review UI.

## Synthesis
The Mozilla AI post introduces “cq,” an experiment in creating a Stack Overflow for agents. The motivation is a familiar pattern: LLMs and agent systems repeatedly run into the same issues—API quirks, build failures, edge‑case behaviors—and each agent burns tokens rediscovering the fix. Meanwhile, the human developer ecosystem’s knowledge commons (Stack Overflow) has declined as developers shift to chat tools, leaving a gap in shared, durable knowledge. cq is proposed as a way to restore that commons for agents, letting them query past learnings before attempting unfamiliar tasks.

The essay frames the problem as waste and trust. Agents fail in similar ways across teams and organizations, yet those failures are rarely shared. The result is duplicated effort, higher compute costs, and brittle outputs. cq’s approach is to store knowledge units learned by one agent and make them available to others, with confidence signals derived from repeated confirmations across different codebases. In this model, knowledge earns trust through use and verification rather than through authority or static documentation.

Mozilla positions cq as more than a repository: it is an open, structured exchange. The system is intended to support querying before action, proposing new learnings after discoveries, and human‑in‑the‑loop review to prevent low‑quality information from polluting the commons. The post references a working proof of concept including a plugin for Claude Code and OpenCode, an MCP server that manages local knowledge stores, a team API for sharing across organizations, and a UI for review. The goal is to evolve from static README‑style knowledge into a dynamic, trustworthy corpus.

A key argument is that “agent” framing can be dangerous if it centralizes power within a few vendors. Mozilla’s position is that agent tooling should be open and standardized, and cq is an attempt to build infrastructure that keeps knowledge portable across systems rather than locked into a single platform. This aligns with Mozilla’s broader emphasis on open standards and public‑benefit technology.

The post uses the metaphor of “matriphagy”—offspring consuming their parent—to describe how LLMs were trained on the web’s knowledge, then hollowed out the communities that created it. cq is pitched as a response: a new commons designed for the agent era that can replenish knowledge rather than extract it.

Overall, the piece argues that reliable agent workflows require shared, structured knowledge. By making learnings portable and verifiable, cq aims to reduce repeated failures and increase trust in agent outputs, while keeping the ecosystem open and community‑driven.
