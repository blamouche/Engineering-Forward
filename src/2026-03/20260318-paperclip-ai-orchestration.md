# Paperclip – Open-source orchestration for zero-human companies
**Source**: https://github.com/paperclipai/paperclip
**Date**: 2026-03-18
**Author**: paperclipai
**Keywords**: AI agents, orchestration, multi-agent coordination, business automation, governance, cost control, open-source

## Elevator pitch
Paperclip is an open-source platform that manages teams of AI agents like a company, providing orchestration, governance, and cost control for autonomous business operations.

## Takeaways
- Company-Level Abstraction: Paperclip treats agent coordination as organizational management rather than technical workflow automation, with org charts, budgets, and governance structures.
- Agent Agnostic: The system works with any agent type—OpenClaw, Claude Code, Cursor, Codex, or custom implementations—requiring only heartbeat connectivity.
- Cost & Resource Management: Built-in budget enforcement prevents runaway token spending through monthly per-agent limits and atomic task checkout mechanisms.
- Persistent State & Context: Agents maintain continuity across heartbeat cycles and inherit goal hierarchy, eliminating context loss on reboots.
- Multi-Tenant Architecture: Single deployments support unlimited isolated companies with separate audit trails and complete data segmentation.

## Synthesis
Paperclip addresses a critical coordination gap in AI agent development. While individual agents (like Claude Code or OpenClaw) excel at specific tasks, orchestrating multiple agents toward coherent business objectives requires infrastructure typically absent in agent frameworks.

The platform's core insight is that managing autonomous systems mirrors human organizational challenges. Rather than building another workflow tool, Paperclip implements genuine business structures: reporting hierarchies, role definitions, budget allocation, and governance approvals. This approach makes abstract coordination concrete—developers configure org charts and delegate tasks using familiar management patterns.

The system solves several practical problems simultaneously. First, it eliminates tab sprawl—the common scenario of keeping dozens of agent terminals open and losing track of progress. Second, it establishes financial accountability through atomic budget enforcement, preventing "runaway loop" scenarios where agents exhaust API quotas undetected. Third, it creates institutional memory by persisting agent state across restarts and maintaining immutable audit logs of all decisions.

Technically, Paperclip distinguishes itself through atomic execution guarantees ensuring no duplicate work, persistent agent context across scheduled heartbeats, and runtime skill injection allowing agents to learn new workflows without retraining. The multi-company isolation feature enables portfolio management—deploying a single instance to orchestrate multiple independent autonomous businesses.

The project explicitly defines its boundaries. It's not a chatbot framework, workflow builder, prompt manager, or code review system. Instead, it's organizational infrastructure for agent teams, comparable to how human companies use project management and financial systems to coordinate employees.

The open-source MIT-licensed model emphasizes self-hosting and local control, with deployments requiring Node.js 20+ and pnpm. Early-stage roadmap items include easier OpenClaw integration, cloud agent support, and a "ClipMart" marketplace for shareable company templates.

This represents a meaningful category shift: from "How do we build better individual agents?" to "How do we manage teams of autonomous agents as functional organizations?" For teams running multiple concurrent agents, Paperclip offers a governance layer that trades the flexibility of ad-hoc coordination for predictability, cost control, and auditability.
