# Cline Releases Open-Source Agent Runtime SDK for Coding Agents
**Source**: https://www.testingcatalog.com/cline-releases-open-source-agent-runtime-sdk-for-coding-agents/
**Date**: 2026-05-13
**Author**: Nero Soares (TestingCatalog)
**Keywords**: Cline, agent SDK, coding agents, open source, TypeScript, CLI, VS Code, JetBrains, agent runtime, agent teams, MCP

## Elevator pitch
Cline has shipped @cline/sdk, an open-source agent runtime rebuilt from scratch to be portable across surfaces — CLI, VS Code, JetBrains — with native agent teams, scheduled jobs, and a pluggable architecture that lets any team build their own coding agents.

## Takeaways
- The SDK is a layered TypeScript stack with clean separation: @cline/shared for types, @cline/llms for provider abstraction (8+ providers), @cline/agents for the stateless agent loop, and @cline/core for stateful orchestration
- Provider switching is now a config change, not a code change — provider logic is entirely outside the agent loop
- Sessions survive UI restarts and can migrate across surfaces; the agent loop is stateless and reusable while the runtime is durable and portable
- Cline CLI on claude-opus-4.7 scores 74.2% on Terminal Bench 2.0, beating Claude Code at 69.4% on the same model
- Agent teams, subagents, scheduled CRON jobs, checkpointing, web search, MCP connectors, and cross-platform connector channels are all native

## Synthesis
Cline's release of @cline/sdk marks a significant architectural evolution for one of the longest-running open-source coding agent projects. Rather than continue layering features onto an architecture that had grown inseparable from its VS Code host, the team made the hard call to rebuild the core agent loop from scratch as a standalone, portable SDK — then migrated their own products onto it.

The architecture is notable for its clean separation of concerns. At the bottom, @cline/shared provides foundational types and utilities. @cline/llms owns the entire provider layer, supporting Anthropic, OpenAI, Google, AWS Bedrock, Mistral, LiteLLM, and OpenAI-compatible endpoints. Critically, provider logic is kept entirely outside the agent loop — switching models is a configuration change, not a code change, which dramatically simplifies both maintenance and experimentation.

The agent loop lives in @cline/agents, which runs stateless iteration, tool orchestration, and event emission. Above it, @cline/core manages stateful concerns: session lifecycle, persistence, and configuration discovery. Application surfaces — CLI, VS Code, JetBrains — connect at the top without owning the runtime. Teams can install the full stack or pull individual packages.

This rebuild unlocks capabilities that were architecturally impossible before. Sessions no longer die when the UI restarts. A session can migrate across surfaces — start in VS Code, continue in the CLI. The improved harness also rewrote prompts, tightened context management, and rethought tool surface design. The Terminal Bench results validate the approach: Cline CLI running claude-opus-4.7 achieves 74.2%, notably ahead of Claude Code's 69.4% on the same model.

The SDK ships with agent teams and subagents as first-class concepts. A session can delegate to specialist agents, track progress, and exchange handoff notes without a separate orchestration layer. Plugins allow domain-specific behavior without forking. Scheduled CRON jobs, checkpointing, web search, and MCP connectors are all built in. An experimental connector channel system even lets agents surface to Telegram, WhatsApp, Slack, and other platforms.

For the broader ecosystem, this represents an important bet on openness. By releasing the runtime as open source and providing a skill-based distribution mechanism (npx skills add cline/sdk-skill), Cline is positioning itself as infrastructure rather than just a tool — a shared foundation that any team can build on, with Cline's own products becoming reference implementations rather than walled gardens.
