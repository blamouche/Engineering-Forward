# Build programmatic agents with the Cursor SDK

**Source**: https://cursor.com/blog/typescript-sdk
**Date**: April 30, 2026
**Author**: Cursor
**Keywords**: agents, sdk, typescript, cloud, developer-tools

## Elevator pitch
Cursor is turning its coding agent runtime into a programmable SDK so teams can launch local, self-hosted, or cloud agents without rebuilding the full agent stack.

## Takeaways
- The SDK exposes the same runtime, harness, and model access used by Cursor's desktop, CLI, and web agents.
- Teams can run agents locally, on self-hosted workers, or on dedicated cloud VMs with durable sessions and PR creation.
- Cursor is packaging context management, MCP support, skills, hooks, and subagents as reusable infrastructure.
- The pitch is that organizations want agents embedded in CI/CD pipelines, internal tools, and customer-facing products, not just interactive editors.
- Cursor frames coding agents as a platform layer, not only a developer assistant.

## Synthesis
Cursor is extending its product from an interactive coding assistant into a programmable agent platform. The new TypeScript SDK gives developers direct access to the same runtime, harness, and model routing that power Cursor's own desktop app, CLI, and cloud agents. Instead of building bespoke orchestration around context management, sandboxing, session durability, and model integration, teams can call Cursor agents with a few lines of code and choose whether they run locally, inside self-hosted infrastructure, or on dedicated cloud VMs. That matters because many organizations are moving from ad hoc agent experiments toward operational use cases such as CI triage, PR automation, repository maintenance, and internal workflow tools. Cursor is effectively arguing that the hard part is no longer just model quality, but the surrounding execution layer that lets agents run safely and persistently against real codebases. By exposing MCP support, skills, hooks, subagents, and cloud execution through one SDK, the company is trying to become infrastructure for programmatic software agents, not only an end-user application. The broader signal is that coding-agent vendors increasingly see the market shifting from human-in-the-loop pair programming toward agent backends that can be embedded in products and pipelines.
