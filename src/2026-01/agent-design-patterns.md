# Agent Design Patterns

**Source**: https://rlancemartin.github.io/2026/01/09/agent_design/

**Date**: January 9, 2026

**Author**: Lance Martin

**Keywords**: AI agents, context management, multi-agent systems, prompt caching, sub-agents, LLM architecture

## Elevator pitch

Effective AI agent design increasingly centers on treating context as a finite resource that must be strategically distributed across storage and computational layers rather than concentrated in model context windows.

## Takeaways

- Agent task complexity is doubling every seven months, making context management the critical design challenge
- Prompt caching is the most important metric for production viability, often making higher-capacity models more cost-effective than cheaper alternatives
- Multi-layered action spaces with 12-20 core atomic tools outperform systems with dozens of directly exposed tools
- Context offloading to filesystem storage preserves information fidelity better than lossy in-context compression
- Sub-agents with isolated contexts enable parallel processing and the "Ralph Wiggum" pattern of repeated loops updating shared state

## Synthesis

This article examines the emerging architectural patterns for autonomous AI agents, written from the perspective of practical production experience. The central thesis is deceptively simple yet profound: context must be treated as a finite resource with diminishing marginal returns. This insight drives seven distinct design patterns that successful agent implementations share.

The first pattern involves granting agents computer access through filesystem and shell capabilities. Rather than operating as simple tool-calling systems, modern agents like Claude Code and Manus function as OS-level interfaces with persistent storage and execution environments. This architectural choice enables the second pattern: multi-layered action spaces. Instead of exposing dozens of specialized tools directly to the model, successful implementations use a hierarchical approach with 12-20 core atomic tools that enable hundreds of downstream actions through code execution and shell utilities.

Progressive disclosure represents the third pattern, where tools and utilities are revealed on-demand rather than loaded upfront. This preserves precious context capacity by allowing agents to access help documentation dynamically and retrieve tool definitions as needed. The fourth pattern, context offloading, complements this approach by having agents write intermediate results and trajectories to filesystem storage. This defers summarization until absolutely necessary, preserving information fidelity compared to the lossy compression that occurs when summarizing within the context window.

The fifth pattern addresses the economic realities of production deployments: prompt caching is identified as the single most important metric for viability. Models with effective caching often prove more cost-effective than nominally cheaper alternatives without it. The sixth pattern introduces context isolation through sub-agents, where specialized agents operate with isolated contexts to enable parallel processing. This includes the colorfully named "Ralph Wiggum" pattern, where repeated agent loops update shared state files rather than accumulating context.

Finally, context evolution represents the seventh pattern, where agents improve through reflection on past sessions. Learnings are distilled into diary entries, skills, or memory files that inform future operations, creating a form of persistent improvement outside the ephemeral context window.

The article also identifies emerging considerations that remain unsolved. Learned context management suggests that future models may autonomously learn optimal context strategies through recursive architectures, rather than relying on hand-crafted prompting. Multi-agent coordination at scale requires shared context mechanisms, conflict resolution, and orchestration frameworks that lack standardization. Infrastructure needs for long-running agents include better observability, human review hooks, debugging interfaces, and graceful failure handling. These open problems point toward the next frontier of agent development, where the patterns identified here will likely evolve into more sophisticated approaches.
