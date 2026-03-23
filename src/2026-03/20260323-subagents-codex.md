# Subagents – Codex
**Source**: https://developers.openai.com/codex/subagents
**Date**: March 23, 2026
**Author**: Unknown
**Keywords**: Codex, subagents, orchestration, workflows, configuration

## Elevator pitch
OpenAI’s Codex subagent system enables parallel, specialized agent threads with configurable limits, custom agent profiles, and orchestration controls.

## Takeaways
- Subagents run specialized tasks in parallel, coordinated by the parent agent.
- Codex spawns subagents only on explicit user request to control cost and scope.
- Custom agent profiles are defined via TOML with names, descriptions, and instructions.
- Global settings cap threads, depth, and runtime to manage cost and recursion risk.
- The workflow is designed for large, parallelizable tasks like reviews or audits.

## Synthesis
The Codex subagents documentation explains how OpenAI’s coding agent can delegate work to multiple specialized agents running in parallel. Subagents are designed for tasks that benefit from fan‑out—codebase exploration, multi‑part reviews, or batch analyses—where a single model would be too slow or context‑limited. Instead of a monolithic session, Codex can spawn multiple workers, each with its own model configuration and instructions, then aggregate results into a consolidated response.

A key principle is explicit control. Codex does not spawn subagents automatically; users must request delegation. This avoids runaway cost and ensures the user is aware that additional model calls and tools will be used. The system also reuses the parent session’s runtime settings, including sandbox and approval policies, which keeps security and governance consistent across threads.

Custom agents are configured through TOML files located in user or project directories. Each custom agent defines a name, description, and developer instructions, and can optionally include model choice, reasoning effort, sandbox mode, MCP servers, and skills. These profiles allow users to create narrow, opinionated agents—reviewers, explorers, documentation researchers—so the subagent workflow can assign tasks to the right specialist. The documentation stresses that custom agent files are configuration layers rather than full manifests, and that the name field is the source of truth for identification.

Global settings under the Codex configuration define limits on concurrency and recursion. The `agents.max_threads` parameter caps concurrent subagent threads, while `agents.max_depth` prevents runaway delegation chains by limiting how many nested spawn levels are allowed. These guardrails are framed as necessary trade‑offs: deeper recursion can increase token usage and reduce predictability, even if it offers broader parallelism. The documentation suggests keeping defaults unless a specific need exists.

The page provides concrete examples of subagent usage. One sample prompt delegates a PR review across multiple dimensions—security, code quality, bugs, race conditions, test flakiness, maintainability—assigning one subagent per point and consolidating results. Another example describes a multi‑agent code review workflow with a read‑only explorer, a reviewer focused on correctness and security, and a documentation researcher connected to an MCP server. This pattern formalizes “divide and conquer” in software work while preserving oversight and safety.

Codex also supports batch workflows like `spawn_agents_on_csv`, which spawns one agent per row in a CSV and produces structured outputs. This enables scalable audits and repeated checks across many items, with explicit output schemas and runtime limits. Results are exported back to CSV with metadata for tracking outcomes and errors.

Overall, the subagents system is presented as a practical orchestration layer for agentic coding: parallelization, specialization, and configurable governance. It broadens what Codex can do by enabling focused agents to work simultaneously, while emphasizing explicit user control to keep cost, scope, and safety in check.
