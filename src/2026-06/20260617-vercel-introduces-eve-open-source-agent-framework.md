# Introducing Eve: Vercel's Open-Source Agent Framework

**Source**: https://vercel.com/blog/introducing-eve
**Date**: 2026-06-17
**Author**: Shar Dara, Kevin Corbett, Casey Gowrie, Andrew Barba, Allen Zhou, Dima Voytenko, JJ Kasper, John Phamous, Timo Lins, Rui Conti
**Keywords**: vercel, eve, agents, open-source, framework, infrastructure, durable-execution

## Elevator pitch

Vercel launches eve, an open-source agent framework that provides production-ready infrastructure—durable execution, sandboxed compute, human-in the-loop approvals, subagents, and evals—so developers can define what their agents do without hand-rolling the plumbing.

## Takeaways

- Eve treats an agent as a directory: agent.ts (model), instructions.md (personality), tools/, skills/, subagents/, channels/, and schedules/—each file describes one component, making the agent's architecture immediately readable.
- Production infrastructure is built in: durable execution, sandboxed compute, human-in-the-loop approvals, subagents, and evals come out of the box rather than requiring assembly from scratch.
- Vercel positions eve as the Next.js for agents—ending the era where every team hand-rolls the same plumbing for each new agent, with nothing carrying over between projects.
- Agent configuration supports provider fallbacks through AI Gateway, and optional fields for compaction and model options provide flexibility without complexity.
- The framework integrates with Vercel Connect for scoped, runtime credential exchange—replacing long-lived provider tokens with short-lived, task-scoped credentials.

## Synthesis

Vercel's launch of eve addresses a fundamental gap in the agent ecosystem: the gap between prototype and production. Today, building an agent means defining what it does and then spending disproportionate time assembling the infrastructure to run it reliably—durable execution, sandboxing, approvals, monitoring, evals. Eve inverts this by making production the default, not the project.

The framework's design philosophy is immediately apparent in its file structure. An eve agent is a directory where each file maps to a single concern: agent.ts configures the model, instructions.md defines personality, tools/ holds capabilities, skills/ encodes domain knowledge, subagents/ manages delegation, channels/ specifies where the agent lives (Slack, web, etc.), and schedules/ defines when it acts autonomously. This is more than organizational hygiene—it's an architectural statement that agents should be as readable and maintainable as well-structured codebases.

The comparison to Next.js is deliberate and instructive. Before Next.js, every React project assembled its own routing, SSR, and build pipeline. Next.js made opinionated choices that let developers focus on their application logic. Eve aims to do the same for agents: provide the boring-but-essential infrastructure so teams can focus on what their agent actually does.

The integration with Vercel Connect is particularly notable for security-conscious teams. Rather than storing long-lived API tokens in environment variables—shared across every user, never expiring, granting full access—Connect enables runtime credential exchange. When an agent needs to act, it proves its identity and receives a short-lived, scoped token. This is OAuth-style thinking applied to agent auth, and it's a pattern every team building production agents should adopt.

For engineering teams, eve represents a meaningful reduction in agent development friction. The question is whether the market will coalesce around a single framework or remain fragmented. Vercel's bet is that agents are where the web was before Next.js—and that the framework that makes production trivial will win.