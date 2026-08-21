# How Microsoft Ships AI Agents at Enterprise Scale
**Source**: https://blog.bytebytego.com/p/how-microsoft-ships-ai-agents-at
**Date**: 2026-07-13
**Author**: ByteByteGo (Alex Xu)
**Keywords**: microsoft, foundry, ai-agents, production, harness, context-layer, evaluation, retrieval, enterprise

## Elevator pitch
Microsoft's VP of Products for Core AI explains the five-layer production harness that turns LLM prototypes into reliable enterprise agents, centering on retrieval-as-a-subagent and giving agents their own identity.

## Takeaways
- A prototype agent works in a demo but fails in production because everything *around* the model breaks—data, tools, identity, guardrails—so the "harness matters as much as the model"
- The production harness has five layers: inference (swappable models), agent runtime (orchestration loop), observability & governance, identity (agents as directory principals), and context (the hardest problem)
- Classic one-shot RAG breaks when questions are ambiguous or need multi-source joins; the fix is *retrieval-as-a-subagent*—a planner-driven loop that queries, evaluates, retries, and returns structured "I don't know" instead of hallucinations
- Microsoft's context layer ships as four headless services—Foundry IQ (unstructured), Fabric IQ (structured), Web IQ (real-time web), Work IQ (M365 productivity surface)—all called via MCP
- Rubric-based evaluation (domain-specific yes/no checks) plus a self-improving Agent Optimizer that rewrites prompts, swaps models, and promotes the best candidate beats generic metrics like groundedness and coherence

## Synthesis
Microsoft operates over 80,000 enterprises on its Foundry platform and its 365 Copilot alone serves 20+ million users, making it one of the largest production agent deployments in the world. Marco Casalaina, VP of Products for Microsoft Core AI, lays out the engineering reality: the model is the easy part. Everything that makes an agent work in production—the harness—determines whether it survives contact with real users.

The harness has five layers. At the bottom, the **inference layer** provides a single interface to 11,000+ swappable models so teams can swap models without rewriting their harness. Above it, the **agent runtime** handles the orchestration loop, tool calls, and conversation state while leaving routing and orchestration to ordinary code rather than forcing every step through the LLM. The **observability and governance layer** (Foundry Control Plane) gives a single view of every running agent with health scoring, token usage, latency, and drift detection piped into Azure Monitor. The **identity layer** extends Entra (Microsoft's enterprise identity platform) to treat agents as their own class of principal with role assignments and audit trails, so a misbehaving agent is bounded by the same controls as a misbehaving employee.

The top layer—**context**—is where Microsoft is investing most heavily. Classic RAG is a one-shot pattern: embed the question, search one index, return top-k. It breaks on ambiguous questions, heterogeneous corpora, or answers that require combining sources. Microsoft's answer is *retrieval-as-a-subagent*: wrap retrieval in an agentic loop that plans queries, tries sources, evaluates results, and retries or returns a structured "I don't know" when iteration runs out. The same loop applies to tool discovery—instead of listing every tool in the prompt, agents search for the right tool at call time.

On evaluation, Microsoft has moved beyond generic metrics (groundedness, coherence) to **rubric-based evaluation**—specific, use-case-tied yes/no checks like "did the agent ask for missing information?" or "did it verify availability before confirming?" The Agent Optimizer drafts rubrics from production traces, and when a rubric fails, it can rewrite the system prompt, adjust tool usage, swap the underlying model, or tune skills—running several candidates in parallel and promoting the best one. Evaluation becomes a self-improving loop, not a pre-ship checkbox.

The key lesson: treating the harness as an afterthought is the most common reason enterprise agents never reach production. Retrieval should be agentic, agents that take actions should have recognizable identities, and guardrails should sit at the tool boundary—not just the model's edges.