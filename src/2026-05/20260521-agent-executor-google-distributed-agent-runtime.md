# Introducing Agent Executor, Google's Distributed Agent Runtime
**Source**: https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime/
**Date**: 2026-05-21
**Author**: Jaana Dogan, Ethan Bao
**Keywords**: Google Cloud, Agent Executor, agent runtime, distributed agents, Kubernetes, Agent Substrate, open-source, durable execution, sandbox

## Elevator pitch
Google has open-sourced Agent Executor, a distributed runtime standard for AI agents that provides durable execution, secure sandbox isolation, session consistency, and trajectory branching — paired with Agent Substrate, a new Kubernetes control plane designed to handle hundreds of millions of agent tool calls that would overwhelm traditional orchestration.

## Takeaways
- Agent Executor (github.com/google/ax) is an open-source runtime for long-running agents, supporting resume after outages, human-in-the-loop, and network disconnections
- Built-in secure sandbox isolation prevents harmful side effects in code-generating or multi-tenant agent scenarios
- Supports trajectory branching via checkpoints, enabling evaluation of alternative agent decision paths
- Harness-agnostic: works with Google Antigravity, ADK, LangChain/LangGraph, A2A protocol, and custom agents
- Agent Substrate extends Kubernetes with a new control plane for ephemeral agent tool calls, avoiding the limits of standard Kubernetes for millions of short-lived operations

## Synthesis
Google has announced Agent Executor, a new open-source runtime that addresses the operational difficulties of running AI agents in production at scale. As agents take on increasingly complex, long-running tasks — sometimes spanning hours or days — the infrastructure required to keep them reliable, resumable, and isolated has become a critical bottleneck. Agent Executor is Google's answer, learned from internal experience.

The runtime provides five native capabilities: durable execution (automatic resume after outages or human-in-the-loop interruptions), secure sandbox isolation (preventing side effects in multi-tenant or code-generating scenarios), session consistency (single-writer architecture for distributed state), connection recovery (reconnecting clients with backfilled responses), and trajectory branching (checkpointing to explore alternative agent paths without losing context).

The architectural decision to be harness-agnostic is strategic. Agent Executor works with Google's own Antigravity harness and Managed Agents API, but also with LangChain/LangGraph, ADK, A2A protocol agents, and custom implementations. This positions it as infrastructure rather than a platform lock-in play — enterprises can deploy on their own compute with their own models and maintain data sovereignty.

The companion announcement of Agent Substrate is equally significant. Standard Kubernetes is optimized for thousands of long-running services; agent workloads generate millions of sub-second tool calls that would overwhelm a conventional control plane. Agent Substrate introduces a minimal control plane on top of Kubernetes that moves agents on and off compute capacity in real-time, optimizing for agentic "chatter" rather than persistent services. Together, the two projects represent Google's bet that the next infrastructure layer isn't just about serving models — it's about running agents reliably at internet scale.
