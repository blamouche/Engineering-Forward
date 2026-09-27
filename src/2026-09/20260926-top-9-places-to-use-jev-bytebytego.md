# EP227: Top 9 Places to Use Jev
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-09-26
**Author**: ByteByteGo
**Keywords**: Jev, TypeSafe AI, System One Model, LLM, RAG, AI Agent, Agentic AI, MCP, function calling, Claude Code, model routing, guardrails, reranking, evals, bulk labeling, real-time decisions, confidence gate

## Elevator pitch
ByteByteGo's EP227 covers three system-design topics: (1) Jev — TypeSafe AI's "System One Model" that is 100x faster and cheaper than frontier LLMs, best used for decisions around LLM generation rather than generation itself; (2) a crisp taxonomy distinguishing LLMs, RAG, AI agents, and agentic AI; and (3) a side-by-side comparison of MCP vs function calling. A bonus section visualizes Claude Code's context window as a 9-layer burger.

## Takeaways
- **Jev's 9 use cases**: Model routing, guardrails, gating tool-calls, triage inbox, reranking, LLM evals, bulk labeling, real-time decisions, and confidence gates. The bottom line: use the LLM for generation, use Jev for the decisions around it.
- **LLM vs RAG vs Agent vs Agentic AI**: An LLM generates tokens one at a time from learned parameters. RAG adds a retriever before the LLM to ground responses. An AI agent has a goal, plans, calls tools, observes results, and loops. Agentic AI orchestrates multiple agents toward a shared objective through planning, tool use, and feedback.
- **MCP vs function calling**: Both let an LLM access tools. In local function calling, functions run on the user's machine. In MCP, functions can live on remote servers, enabling connection to thousands of publicly hosted tools.
- **Claude Code as a burger**: Before each model call, Claude Code assembles a context window from 9 sources — system prompt, environment info, CLAUDE.md, auto memory, path-scoped rules, tool metadata, conversation history, tool results, and compact summaries.
- **Practical implication**: The emergence of small, fast, cheap "System One" models like Jev signals a bifurcation in AI infrastructure — heavyweight LLMs for generation and lightweight classifiers for the decision layer surrounding them.

## Synthesis
This newsletter issue captures a maturing mental model of AI infrastructure: not one model to rule them all, but a stack where different model tiers serve different roles. Jev's positioning as a "System One" model (borrowing Kahneman's terminology) is deliberate — it handles the fast, cheap, intuitive decisions while the LLM plays "System Two" for deep generation. The 9 use cases (routing, guardrails, gating, triage, reranking, evals, labeling, real-time, confidence) are precisely the bottlenecks where a frontier LLM is overkill. The MCP vs function-calling distinction clarifies a confusion point for many engineers: the difference is about where the function executes (local vs remote), not about the LLM's role. And the "Claude Code as a burger" metaphor elegantly demystifies what goes into an agent's context window — useful for anyone building agent-based systems who needs to reason about what the model actually "sees" before generating.