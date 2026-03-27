# What we wish we knew about building AI agents
**Source**: https://newsletter.posthog.com/p/what-we-wish-we-knew-before-building
**Date**: Unknown
**Author**: PostHog
**Keywords**: AI agents, MCP, product strategy, agent harness, observability

## Elevator pitch
PostHog shares hard‑won lessons from building PostHog AI, arguing that many teams should start with MCP servers and focus on context, harness choices, and observability before shipping a custom agent.

## Takeaways
- Building a custom agent isn’t always the right first step; MCP servers can validate demand.
- PostHog iterated through three harness designs before converging on the Claude Agent SDK + MCP tools.
- Context engineering (tools, skills, runtime context injection) is the primary differentiator.
- Observability and evaluation are essential early, not optional add‑ons.
- User experience issues (inconsistency, unclear capability) matter more than flashy features.

## Synthesis
PostHog’s retrospective on building PostHog AI is a practical guide to the decisions that matter most when shipping an agent in a real product. The essay starts by challenging the default impulse to build a bespoke agent. For many products, exposing capabilities via an MCP server is a faster and lower‑maintenance way to make the system accessible to agentic workflows. PostHog reports that a significant share of AI‑generated dashboards are already created through their MCP server, which underscores MCP’s value not just as an integration layer but as demand validation.

The piece emphasizes that if you do build a custom agent, the “harness” matters more than novelty. PostHog tried three designs: a coordinator routing messages to specialized sub‑agents, a single agent with modal tools, and finally a Claude Agent SDK–based system with MCP tools. The coordinator approach created a black‑box problem (the main agent lost visibility into sub‑agent actions). The single‑agent modal system improved visibility but did not scale because every capability required a new tool. Their current approach uses MCP tools plus a code‑execution sandbox, enabling the agent to be more creative without a tool for every edge case.

Context is framed as the central competitive advantage. PostHog details how they structure context using MCP tools (API‑derived capabilities), written skills (workflow templates and examples), layered runtime context injection (current view, filters, metadata), a taxonomy explorer for user events, and persistent memory collection. The argument is that the product’s own data and structure are what make the agent useful; without that, the agent struggles even on simple user questions.

The essay also stresses observability. The team regrets not having tracing, replay, curated datasets, and scoring frameworks from the start. They highlight “traces hour”—regular manual review of real interactions—to identify failure modes and guide evaluations. Metrics and LLM‑as‑judge are helpful, but the core learning comes from real usage.

Finally, the article grounds the technical guidance in product reality. Users care less about an agent’s theoretical capabilities and more about consistency, clear error messages, and an accurate understanding of what the agent can do. Building a successful agent therefore requires product discipline: reducing surprises, clarifying boundaries, and iterating based on actual user pain rather than a “coolest agent” competition.

In sum, PostHog’s lesson is to validate demand via MCP, avoid over‑engineered harnesses, invest heavily in context engineering and observability, and treat user experience as the determining factor for success.
