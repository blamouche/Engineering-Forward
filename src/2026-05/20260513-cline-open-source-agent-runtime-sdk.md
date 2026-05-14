# Cline Releases Open-Source Agent Runtime SDK for Coding Agents
**Source**: https://www.testingcatalog.com/cline-releases-open-source-agent-runtime-sdk-for-coding-agents
**Date**: May 13, 2026
**Author**: Nero Soares (TestingCatalog)
**Keywords**: Cline, agent runtime, SDK, open source, coding agents, CLI, VS Code, JetBrains, TypeScript, agentic loop, Terminal Bench, Claude, LLM providers

## Elevator pitch
Cline released @cline/sdk, an open-source, layered TypeScript agent runtime that powers its CLI, VS Code, and JetBrains surfaces, enabling any team to build portable coding agents with native agent teams, subagents, scheduled jobs, and cross-platform connectors.

## Takeaways
- @cline/sdk is a ground-up rebuild of Cline's agentic loop as a standalone, portable runtime, decoupled from any specific IDE or UI surface
- The layered architecture separates concerns: @cline/shared (types), @cline/llms (provider layer supporting 7+ LLM backends), @cline/agents (stateless agentic loop), @cline/core (stateful orchestration with session lifecycle and persistence)
- Cline CLI on claude-opus-4.7 scores 74.2% on Terminal Bench 2.0, ahead of Claude Code at 69.4% on the same model, and reaches 55.1% with open-weight kimi-k2.6 vs OpenCode at 37.1%
- The SDK natively supports agent teams, subagents with handoff notes, scheduled CRON jobs, checkpointing, MCP connectors, and a plugin system for domain-specific extensions
- Sessions survive UI restarts and can migrate across surfaces—the agent loop remains stateless while the runtime layer provides durable persistence

## Synthesis
Cline's release of @cline/sdk represents a significant architectural milestone in the coding agent ecosystem. Rather than continuing to bolt features onto an IDE-bound architecture, the team undertook a ground-up rebuild, extracting the core agentic loop into a standalone, portable TypeScript SDK. This is the same project that claims to have pioneered the real agentic coding experience with Claude Sonnet 3.5 in 2024, before Claude Code, Codex, and the broader wave of coding agents emerged.

The SDK's layered architecture reflects hard-won lessons from years of production use. The @cline/llms layer provides a clean provider abstraction covering Anthropic, OpenAI, Google, AWS Bedrock, Mistral, LiteLLM, and any OpenAI-compatible endpoint—with provider logic completely decoupled from the agent loop. This means switching between models is a configuration change rather than a code change, a design decision that seems obvious in retrospect but is inconsistently implemented across the ecosystem.

The stateless agentic loop in @cline/agents paired with stateful orchestration in @cline/core enables a capability that most coding agents lack: durable, portable sessions. A coding session is no longer tied to a specific UI restart. Work can move from CLI to VS Code mid-session. The agent loop itself remains stateless and reusable while the runtime layer handles persistence, making long-running autonomous work genuinely feasible.

Benchmark results provide credible evidence of the rebuild's impact. Cline CLI with claude-opus-4.7 achieves 74.2% on Terminal Bench 2.0, notably ahead of Claude Code (69.4%) on the identical model. The gap is even more pronounced on open-weight models, where Cline CLI with kimi-k2.6 reaches 55.1% versus OpenCode's 37.1%. These numbers suggest that the agent runtime—the prompting strategy, context management, and tool presentation—is a meaningful performance differentiator independent of the underlying model.

The SDK also ships with capabilities that reflect where the agent market is heading: native agent teams and subagents with handoff notes, a plugin system for domain-specific extensions, scheduled CRON jobs, checkpointing, MCP connectors, and experimental connector channels for Telegram, WhatsApp, and Slack. With 7 million developers served and surfaces spanning CLI, VS Code, JetBrains, and a Kanban orchestration layer, Cline's SDK release positions it as infrastructure rather than just a product.
