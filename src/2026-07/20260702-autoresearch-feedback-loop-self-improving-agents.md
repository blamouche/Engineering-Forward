# Autoresearch: The Feedback Loop Behind Self-Improving Agents
**Source**: https://www.latent.space/p/autoresearch-introspection
**Date**: 2026-07-02
**Author**: Latent Space / Roland Gavrilescu
**Keywords**: autoresearch, self-improving agents, feedback loops, agent harnesses, Introspection, Pi framework, autonomous software factories, outer loop

## Elevator pitch
Autoresearch builds an "outer loop" where agents help maintain and improve the primary system using feedback signals, evals, and human input—a shift from static agent harnesses to self-improving systems that learn from their own operations.

## Takeaways
- Autoresearch involves building an outer loop where agents maintain and improve the primary system, using feedback signals, evals, and human input to make progress over time
- Introspection, one of the startups building infrastructure for self-improving systems, is co-founded by CEO Roland Gavrilescu
- The shift is from agent harnesses (static execution frameworks) to feedback loops (dynamic, self-improving systems)
- The open-source Pi framework plays a role in enabling these self-improving agent architectures
- Autonomous software factories must first learn from humans before they can operate independently—the human-in-the-loop phase is not optional but foundational

## Synthesis
Latent Space's interview with Roland Gavrilescu, co-founder and CEO of Introspection, covers the emerging paradigm of "autoresearch"—an approach where AI agents don't just execute tasks but actively participate in improving the system they operate within. The concept represents a shift from static agent harnesses (which define how agents execute tasks) to dynamic feedback loops (which allow agents to learn from their own execution and improve over time).

The core idea is an "outer loop" that runs alongside the primary agent execution loop. While the inner loop handles task execution—writing code, running tests, producing outputs—the outer loop collects feedback signals, evaluation results, and human input, and uses these to refine the agent's behavior, prompts, and tool usage. This creates a system that compounds learning over time rather than starting fresh with each session.

Introspection is building infrastructure specifically for these self-improving systems. The interview covers the open-source Pi framework, which provides primitives for building feedback-driven agent architectures. The framework enables developers to define evaluation criteria, collect execution traces, and feed insights back into the agent's context for future runs.

A key insight from the discussion is that autonomous software factories—the vision of fully automated development pipelines—must first learn from humans before they can operate independently. The human-in-the-loop phase is not a limitation to be removed but a foundational training period. Agents need human feedback to calibrate their judgment, understand edge cases, and develop reliable decision-making patterns. Only after this calibration can they operate with meaningful autonomy.

The practical implication for engineering teams is that the most valuable agent infrastructure investments are not in better task execution but in better feedback collection and integration. Teams that build robust evaluation pipelines, capture human corrections systematically, and feed these back into agent context will see compounding improvements in agent performance over time. Those that treat agents as stateless execution engines will plateau quickly.