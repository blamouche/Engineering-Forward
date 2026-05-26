# How to Build an AI Agent from Scratch (With Working Code)
**Source**: https://linas.substack.com/p/how-to-build-an-ai-agent-from-scratch
**Date**: April 13, 2026
**Author**: Linas Beliūnas
**Keywords**: AI agents, Python, agent architecture, LangChain, agentic workflow, prompt chaining, routing, tool design, context window, cost tracking

## Elevator pitch
A hands-on, code-first guide that walks through building a functional AI agent in Python — from the core agent loop to web search, synthesis, error handling, and cost tracking — accompanied by a design framework and five workflow patterns that help decide when a full agent is even necessary versus a simpler chain.

## Takeaways
- The core loop that powers every agent (LangChain, CrewAI, and all frameworks) follows a consistent pattern; understanding it demystifies agent frameworks entirely.
- Before writing code, a simple design framework of 4 questions and a one-line formula turns a vague idea into a buildable specification — skipping this step is why most first agents fail.
- Five workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizers) solve most problems without needing a full autonomous agent, saving cost and complexity.
- Real-world hard parts receive dedicated attention: context window math showing how fast 200K tokens fill up, actual dollar costs per query, five common failure modes, and a troubleshooting guide.
- The guide requires only basic LLM experience; no prior knowledge of agent frameworks, tool design, or orchestration is assumed.

## Synthesis
Linas Beliūnas delivers a rare artifact in the AI agent literature: a tutorial that takes you from a blank Python file to a working, production-aware agent, with every decision explained and every piece of code functional. Unlike the hundreds of articles explaining what agents are conceptually, this guide bridges the gap between understanding and execution.

The foundation of the guide is the core agent loop — the same underlying pattern that powers LangChain, CrewAI, and every major agent framework. By building it manually in pure Python without abstractions, the guide renders these frameworks transparent rather than magical. The agent built in the tutorial takes a user question, performs web search for current information, synthesizes the results, handles failures gracefully, and reports exactly what the interaction cost — both in tokens and dollars.

A key insight woven throughout is that not every problem needs a full autonomous agent. The guide presents a pre-code design framework consisting of four diagnostic questions and a one-line formula to determine whether the task genuinely requires agentic behavior. It then introduces five workflow patterns — prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizers — that often solve problems more reliably and cheaply than a full agent loop. This framework-first approach addresses what Beliūnas identifies as the most common failure mode: building an autonomous agent when a simple chain would have sufficed.

The guide's focus on practical reality sets it apart. Rather than glossing over production concerns, it dedicates substantial attention to the hard parts nobody talks about: context window mathematics showing precisely how quickly a 200K token window fills during iterative tool calls, actual dollar cost tracking per query across different models, and a catalog of five specific failure modes with corresponding troubleshooting strategies. This pragmatic orientation makes the guide valuable not just for first-time builders but also for experienced developers looking to harden their agent implementations.

The target audience is deliberately broad — anyone who has used an LLM before is the only prerequisite — but the depth satisfies practitioners. By the end, readers understand not just how to build one agent following a recipe, but the structural principles that enable them to design their next agent independently, evaluate whether agentic architecture is appropriate, and anticipate the cost and reliability tradeoffs that real deployments entail.
