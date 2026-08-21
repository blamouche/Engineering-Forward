# Loop Engineering: How to Design AI Loops That Build, Ship, and Improve While You Sleep

**Source**: https://linas.substack.com/p/loop-engineering-complete-guide
**Date**: June 10, 2026
**Author**: Linas Beliūnas (Linas's Newsletter)
**Keywords**: loop-engineering, AI-loops, agentic-autonomy, Claude-Fable-5, Claude-Code, OpenClaw, prompt-engineering, automation, agent-orchestration

## Elevator pitch
The leverage point in AI engineering has moved from prompting individual agents to designing deterministic loops that prompt, coordinate, and improve agents autonomously — a paradigm shift championed by the creators of both OpenClaw and Claude Code.

## Takeaways
- Peter Steinberger (OpenClaw creator) and Boris Cherny (Claude Code head) independently declared that the future is designing loops that prompt agents, not prompting agents directly
- A loop is a deterministic system that manages an AI agent's context, tools, stopping rules, and coordination — the agent does judgment, the code does coordination
- The guide provides a 14-step roadmap from manual prompter to loop engineer, making the transition accessible to builders at any level
- A practical catalog of 41 pre-built loops is provided for copy-paste deployment across common engineering workflows
- Claude Fable 5 is positioned as the first frontier model built from the ground up for long-horizon agentic autonomy within these loops
- Three "debts" emerge as loops get better: context debt, eval debt, and orchestration debt — each getting worse the more capable the loop becomes
- The article targets not just engineers but founders, investors, and operators evaluating AI-native competitive advantages

## Synthesis
The article opens with two pivotal statements that crystallize a shift already underway in AI engineering. Peter Steinberger, creator of OpenClaw — the open-source AI agent project that became the most-starred new repo in GitHub history — posted: "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." Days earlier, Boris Cherny, creator and head of Claude Code at Anthropic, said on stage: "I don't prompt Claude anymore. I have loops running. They're the ones prompting Claude and figuring out what to do. My job is to write loops."

These statements reflect a fundamental change in how AI-native engineering works. Rather than treating each interaction with an LLM as a one-off prompt, engineers are building deterministic systems that manage the full lifecycle of agent interactions: deciding what to prompt, when to prompt, how to route outputs, when to stop, and how to improve. The loop becomes the unit of work, not the prompt.

The guide offers a structured 14-step progression from manual prompting to loop engineering, making the concept accessible to builders at varying levels of sophistication. It includes a catalog of 41 pre-built loops that can be deployed immediately, covering common engineering workflows from code review and test generation to deployment and incident response. The integration of Claude Fable 5 — Anthropic's newest frontier model designed specifically for long-horizon agentic autonomy — is positioned as the enabling capability that makes complex loops practical.

A critical section addresses the costs and failure modes of loops. Three types of debt emerge as loops become more capable: context debt (the accumulated context that degrades agent performance over time), eval debt (the gap between what you can measure and what actually matters), and orchestration debt (the complexity of coordinating multiple agents and tools). Each gets worse the better the loop works, creating a paradox where success amplifies the risks of failure. The article argues that understanding and managing these debts is what separates loops that scale from loops that collapse under their own complexity.

The broader implications extend beyond engineering teams. Founders building AI-native companies need to understand loops to evaluate whether their teams are building durable advantages or just riding a demo. Investors need to assess whether a company's loop infrastructure creates defensibility. Operators need to understand why competitors using loop engineering can move at fundamentally different speeds. The leverage point has moved, and the article makes the case that this shift is available to everyone right now.