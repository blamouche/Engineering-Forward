# Multi-agent coordination patterns: Five approaches and when to use them

**Source**: https://claude.com/blog/multi-agent-coordination-patterns
**Date**: April 13, 2026
**Author**: Anthropic
**Keywords**: Anthropic, multi-agent systems, coordination patterns, agent design

## Elevator pitch
Anthropic’s guide is a useful field manual for multi-agent design: start with the simplest coordination pattern that fits, then escalate only when the task’s structure—not aesthetic preference—demands it.

## Takeaways
- Anthropic’s guide is a useful field manual for multi-agent design: start with the simplest coordination pattern that fits, then escalate only when the task’s structure—not aesthetic preference—demands it.
- Anthropic maps five coordination patterns—generator-verifier, orchestrator-subagent, agent teams, message bus, and shared state—to the kinds of problems they solve well. That alone is valuable, because teams often over-engineer multi-agent systems by choosing the fanciest architecture before they have evidence a simpler loop fails.
- The article’s core message is architectural restraint. Generator-verifier works when quality criteria are explicit. Orchestrator-subagent works when decomposition is clear. Agent teams help when work persists and can stay independent for long stretches. Message bus and shared-state patterns only make sense once the interaction graph becomes richer or more emergent.
- The practical lesson is that multi-agent complexity should be earned. Each step up the ladder introduces new failure modes—routing errors, bottlenecks, debugging difficulty, conflicts over shared resources. If a basic verifier loop or an orchestrator with bounded subagents handles the problem, that is usually the better engineering choice.

## Synthesis

Anthropic maps five coordination patterns—generator-verifier, orchestrator-subagent, agent teams, message bus, and shared state—to the kinds of problems they solve well. That alone is valuable, because teams often over-engineer multi-agent systems by choosing the fanciest architecture before they have evidence a simpler loop fails.

The article’s core message is architectural restraint. Generator-verifier works when quality criteria are explicit. Orchestrator-subagent works when decomposition is clear. Agent teams help when work persists and can stay independent for long stretches. Message bus and shared-state patterns only make sense once the interaction graph becomes richer or more emergent.

The practical lesson is that multi-agent complexity should be earned. Each step up the ladder introduces new failure modes—routing errors, bottlenecks, debugging difficulty, conflicts over shared resources. If a basic verifier loop or an orchestrator with bounded subagents handles the problem, that is usually the better engineering choice.
