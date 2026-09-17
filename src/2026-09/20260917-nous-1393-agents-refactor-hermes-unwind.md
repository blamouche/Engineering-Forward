# 1,393 Agents Took a Million-Line Codebase Apart
**Source**: Unwind AI (unwindai@mail.beehiiv.com) — https://www.theunwindai.com/p/chatgpt-co-inventor-launches-a-super-fast-ai-model-for-agents
**Date**: 2026-09-16
**Author**: Unwind AI
**Keywords**: Nous Research, Hermes, agent swarm, refactoring, dogfooding, multi-agent, codebase, parallel agents, agent orchestration, token spend

## Elevator pitch
Nous Research published a detailed dogfood post on refactoring Hermes with 1,393 agents and ~$19K in token spend—an operating manual for agent swarms that covers planning, sharding, and orchestrating parallel agents at scale on a real million-line codebase.

## Takeaways
- **1,393 agents, $19K in tokens**: Nous refactored Hermes (their own product) using 1,393 parallel agents spending approximately $19,000 in token costs. This is one of the largest disclosed agent swarm operations on a real production codebase.
- **Plan the work, then shard it**: The post reads as an operating manual for agent swarms—plan the work first, shard the codebase into manageable units, then dispatch agents to work in parallel on each unit.
- **Dogfooding as validation**: By running the refactoring on their own product, Nous validates Hermes's multi-agent capabilities under real conditions rather than synthetic benchmarks.
- **Cost transparency**: The $19K token spend for 1,393 agents on a million-line codebase provides a concrete data point for estimating the cost of large-scale agent operations.
- **The pattern is replicable**: The approach—plan, shard, dispatch, verify—can be applied to other large codebases, making agent swarms a practical tool for major refactoring projects rather than a research demo.

## Synthesis
Nous Research published a dogfood post on refactoring Hermes—their own AI agent platform—using 1,393 agents and approximately $19,000 in token spend. The post is described by Unwind AI as "properly nerdy" and "the best read as an operating manual for agent swarms." This is one of the largest disclosed agent swarm operations on a real production codebase, not a synthetic benchmark or research demo.

The key insight is that large-scale agent refactoring follows a clear pattern: plan the work first, shard the codebase into manageable units that individual agents can handle, then dispatch agents to work in parallel. This is the same pattern that scales human engineering teams—break the work down, assign units, integrate results—but executed by AI agents at a scale and speed that human teams cannot match.

The $19K token spend for 1,393 agents on a million-line codebase provides a concrete data point for the industry. At roughly $13.70 per agent, the cost is modest compared to human engineering hours, though the post presumably discusses the overhead of planning, coordination, and verification that surrounds the raw agent execution.

The fact that Nous ran this on their own product (Hermes) is significant. Dogfooding under real conditions—real code, real dependencies, real edge cases—provides stronger validation than benchmarks. If the agents can successfully refactor the platform that orchestrates them, that's a recursive proof of capability.

The Unwind AI newsletter also covers several other significant launches in the same issue: TypeSafe's Jev (a System One model for software decisions that's 20-200x faster and 40-400x cheaper than text-generating models because it doesn't generate text—it returns typed probabilistic values), Gemini 3.8 Live (extended thinking that fixes the silent-wait problem by speaking while reasoning), Claude's Salesforce integration, Devin on Mac, and GPT-5.5's retirement on October 14. The Jev launch was already covered separately, but the Hermes refactoring post stands out as the most operationally detailed piece for engineering teams considering agent swarms.