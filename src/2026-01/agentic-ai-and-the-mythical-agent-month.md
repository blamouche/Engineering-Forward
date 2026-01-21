# Agentic AI and The Mythical Agent-Month

**Source**: https://muratbuffalo.blogspot.com/2026/01/agentic-ai-and-mythical-agent-month.html

**Date**: January 20, 2026

**Author**: Murat Demirbas

**Keywords**: agentic AI, Brooks' Law, software engineering, distributed systems, multi-agent systems, coordination complexity

## Elevator pitch

A distributed systems researcher argues that adding more AI agents to software projects faces the same fundamental coordination limits as adding more human developers—Brooks' Law applies to agents too.

## Takeaways

- The claim that AI agents can bypass Brooks' Law through instant context loading is not supported by empirical evidence from agent-built systems
- Agents building an LLM inference runtime achieved only 68% of human baseline performance (1.2k vs 1.76k tokens/second)
- Distributed system integration remains a hard problem for agents, with one project requiring 35 days and facing deployment failures and dependency conflicts
- Reading code tokens is fundamentally different from understanding causal chains across systems—agents face an epistemic gap
- Multi-agent systems encounter state-space explosion faster than humans when managing non-monolithic architectures

## Synthesis

Murat Demirbas, a distributed systems researcher, offers a rigorous critique of the "Self-Defining Systems" (SDS) position paper that claims AI agents can achieve "Scalable Agency" by instantly loading context without the ramp-up time that makes Brooks' Law problematic for human developers. His analysis exposes fundamental assumptions that do not hold up under scrutiny.

The core thesis of the SDS paper is that software engineering is embarrassingly parallel—that work can be easily divided among independent workers. Demirbas argues this premise is flawed at its foundation. When agents were tasked with building an LLM inference runtime, they achieved only 1.2k tokens per second compared to a human baseline of 1.76k tokens per second. This is not a minor gap that additional agents could close; it suggests hard performance ceilings that scaling cannot overcome.

The integration complexity problem becomes even more apparent when examining distributed systems. When agents attempted to build allmos_v2 on distributed components, they required 35 days and encountered deployment failures along with GLIBC mismatches. These are not random bugs but symptoms of a deeper architectural challenge: the exponential complexity inherent in distributed dependency graphs. Adding more agents to this kind of problem does not reduce complexity; it amplifies the coordination overhead.

Demirbas identifies what he calls the "epistemic gap" between agents and true system understanding. Reading code tokens is fundamentally different from comprehending the causal chains that ripple across systems. When a change in one component affects behavior in another through non-obvious pathways, understanding requires a form of knowledge that agents struggle to acquire. This gap becomes critical in multi-agent scenarios where state-space explosion occurs faster than it does with human teams.

Perhaps the most incisive observation concerns what Demirbas calls the "shell game" that SDS performs. The paper retains human responsibility for goal-setting, architecture decomposition, and evaluation design—the very activities that determine whether a project succeeds or fails. What remains for agents is essentially hyper-parameter tuning repackaged under new terminology. The hard problems of software engineering remain untouched.

The article's central insight is that coordination complexity is a mathematical law, not merely a sociological observation. Until the fundamental bottlenecks in coordination and verification are solved, adding more agents simply generates faster, more expensive merge conflicts. The mythical agent-month, like its human counterpart, promises productivity gains that distributed work inherently cannot deliver. This analysis serves as a necessary counterweight to the hype surrounding agentic AI in software development.
