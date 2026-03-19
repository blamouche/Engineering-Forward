# How OpenAI Codex Works
**Source**: https://blog.bytebytego.com/p/how-openai-codex-works
**Date**: 2026-03-18
**Author**: Alex Xu (ByteByteGo)
**Keywords**: OpenAI Codex, agent loop, context management, multi-surface architecture, App Server, AGENTS.md, prompt caching, JSON-RPC

## Elevator pitch
OpenAI Codex's success is more about engineering infrastructure than the AI model—a three-layer architecture (agent loop, context management, multi-surface App Server) where "the model is a component, the agent is the system."

## Takeaways
- The agent loop: Codex iterates through reason → execute (file edits, shell commands, tests) → incorporate results → reason again, using tool calls as the execution mechanism.
- Context management: prompts stack from environment context, project instructions (AGENTS.md), permissions, and conversation history; quadratic growth mitigated by prompt caching since old prompts form exact prefixes; filled windows compact into encrypted payloads.
- Multi-surface App Server: core agent logic wrapped in bidirectional JSON-RPC protocol enables VS Code, web, desktop, and third-party IDE deployment from a single codebase.
- Initial MCP exposure failed because MCP couldn't support rich interaction patterns like streaming progress and mid-task approval requests.
- Key insight: "The model is a component, the agent is the system. Most engineering goes into the system."

## Synthesis
The "model is a component, the agent is the system" observation is the most important insight in this architecture description. It directly challenges the assumption that AI product quality is primarily determined by model quality. Codex's capability comes from the infrastructure decisions: how context is managed, how tool results are incorporated, how multiple surfaces share a single agent core, how context compaction preserves state across long sessions.

The AGENTS.md file concept is elegant: project-level instructions that persist across sessions without requiring developers to maintain them in prompts. This externalizes the "what this codebase is and how to work with it" context into a version-controlled file that improves with the codebase rather than requiring constant re-specification.

The quadratic context growth problem is fundamental to multi-turn agent interactions and the prompt caching mitigation is smart. Each turn adds to the context; reviewing the full history for every new turn creates polynomial scaling. The insight that old prompts form exact prefixes of new prompts means the cache hit rate approaches 1 for older context—the most expensive computation (processing many previous turns) is cached from previous calls.

The MCP failure is instructive about protocol-product fit. MCP's design for tool discovery and standardized interaction works well for simple tool calls. It fails for rich agent interactions that need streaming progress indicators, mid-task approval dialogs, and synchronous communication patterns. Building a custom JSON-RPC protocol was extra work but enabled the interaction quality that makes Codex usable in practice.
