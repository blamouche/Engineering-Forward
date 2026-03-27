# Open SWE: An Open-Source Asynchronous Coding Agent
**Source**: https://github.com/langchain-ai/open-swe
**Date**: Unknown
**Author**: LangChain
**Keywords**: coding agents, LangGraph, Deep Agents, sandboxes, orchestration, Slack, Linear, GitHub

## Elevator pitch
Open SWE is LangChain’s open-source framework for building internal coding agents, combining sandboxed execution, curated tools, and multi-agent orchestration with Slack/Linear/GitHub integrations.

## Takeaways
- Open SWE packages the internal-agent architecture used at companies like Stripe, Ramp, and Coinbase into a configurable open-source stack.
- Each task runs inside an isolated cloud sandbox with full permissions inside the boundary and no production access.
- The framework relies on LangGraph + Deep Agents for orchestration, subagents, and middleware hooks.
- Tooling is intentionally curated: a small set of high-leverage tools plus built‑in file and task utilities.
- Integrations center on Slack, Linear, and GitHub, with automatic PR creation and comment workflows.

## Synthesis
Open SWE is presented as an open-source “internal coding agent” blueprint for engineering organizations that want to automate code changes without building a bespoke agent system from scratch. It is designed to replicate the architecture patterns of internal tools such as Stripe’s Minions, Ramp’s Inspect, and Coinbase’s Cloudbot. The project sits on top of LangGraph and Deep Agents, which gives it a composable orchestration layer and a native way to spawn subagents. Instead of forking a monolithic agent, Open SWE composes building blocks to make upgrades and customization feasible over time.

A key architectural decision is strict isolation. Every task runs in its own cloud sandbox where the repository is cloned and the agent is granted full permissions inside that environment. This keeps the blast radius contained and avoids direct production access. Sandboxes can be provided by multiple vendors such as Modal, Daytona, Runloop, or LangSmith, and the framework can be extended to additional providers. The point is to let the agent operate with high autonomy, but only inside a controlled, disposable boundary.

Tooling is intentionally minimal and curated. Instead of hundreds of tools, Open SWE focuses on a small set that enables real engineering work: executing shell commands, fetching web content, making HTTP requests, committing and opening pull requests, and posting back to Linear or Slack. On top of this, it inherits the Deep Agents utilities such as file read/write/edit, searching, and spawning subagents. The emphasis is on quality and fit rather than tool sprawl—an explicit lesson drawn from internal agent deployments.

Context injection is another major theme. The system reads repo-level rules (like AGENTS.md) to shape how the agent operates, and it pulls in full Linear issue context or Slack thread history to minimize discovery time. The system is built to keep thread continuity, so follow‑up messages route to the same running task. Middleware hooks provide deterministic safety nets, such as automatically opening a pull request if the agent completes work without doing so. These hooks can also enforce checks like running tests or formatting.

The integration surface is built for where engineers already work. Slack mentions can trigger tasks and collect updates; Linear comments can spawn runs and receive results; GitHub PR comments can request fixes on agent‑created branches. This keeps the agent workflow in existing collaboration channels and reduces adoption friction. It also aligns with a practical perspective: agents succeed when they meet engineers inside their normal toolchains rather than forcing a new interface.

Overall, Open SWE positions itself as a reference architecture for production‑grade coding agents: sandboxed execution, curated tools, tight context, orchestration with subagents and middleware, and first‑class integration into the communication and issue‑tracking systems that teams already use. It is not presented as a replacement for human engineers, but as a pattern for safely delegating scoped, repeatable coding tasks with built‑in guardrails and a clear path to customization.
