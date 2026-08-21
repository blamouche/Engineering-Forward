# Token Spend Out of Control: The Case for Smarter Routing
**Source**: https://blog.bytebytego.com/p/token-spend-out-of-control-the-case
**Date**: 2026-06-08
**Author**: ByteByteGo (Scott Breitenother and Sid Sijbrandij, Kilo)
**Keywords**: model-routing, token-cost, llm-agents, kilo-gateway, cost-optimization, inference

## Elevator pitch
LLM agents burn millions of tokens by resending full context on every loop iteration to the most expensive model available — model routing cuts costs 40-70% by sending each request to the cheapest model that can handle it, as demonstrated by Kilo's production system handling millions of requests.

## Takeaways
- LLM agents are expensive because they run in loops: each step resends the full growing context (instructions, tool schemas, results, intermediate thinking) to the model, and a single late-stage request can carry 100K+ tokens
- Frontier models cost 10x+ more per token than small models; teams using frontier models for everything pay frontier prices for routine work
- A router looks at each request, decides which model is good enough, and sends it there — routing on known task type is a static lookup (cheap, reliable, debuggable); routing by predicting difficulty from request text requires training and upkeep
- UC Berkeley/Anyscale study: routing cut cost ~50% while keeping 95% of frontier model quality; field results typically land at 40-70% savings
- Kilo's production numbers: 80-90% of requests don't need frontier models; balanced tier cost 10x less per request than top tier; forcing routine traffic onto top-tier would have cost $87K extra in Q1 2026
- Caching alone doesn't solve the volume problem: even with 80%+ cache reuse, total spend stays high because non-cacheable context is still large; routing and caching address different parts of cost
- Key lesson: set a monthly budget and treat it as fixed; optimize for most useful work within budget, not lowest price per request

## Synthesis
The ByteByteGo deep dive on model routing addresses one of the most pressing infrastructure challenges in AI agent engineering: the cost of running agents in production. The article explains why LLM agents are fundamentally more expensive than chatbot interactions — agents run in loops, resending the full context (which grows with each step) to the model on every iteration. A session that starts at a few thousand tokens can carry well over 100K tokens by the time the agent has read a dozen files and run a dozen tools. Combined with the tendency to default to the most expensive frontier model, costs scale rapidly.

The solution the article advocates is model routing: a system that examines each request and sends it to the cheapest model that can handle it. The router needs two components — a unified entry point that speaks a standard request format across providers, and a decision mechanism. There are two decision approaches: routing on a known signal (task type maps to model — cheap, reliable, easy to debug) or predicting difficulty from the request text (requires training data and ongoing maintenance). Kilo uses the first approach: its coding agent always knows what mode it's in (planning, writing code, debugging), so the routing decision is a static lookup.

The production numbers from Kilo are compelling. Across millions of requests in Q1 2026, 80-90% did not need frontier models. The balanced tier cost over 10x less per request than the top tier for the same coding work. The team estimated that forcing routine traffic onto top-tier models would have cost approximately $87,000 more per quarter. Even with cache reuse above 80% on many features, total spend remained high because the non-cacheable portion of each context was still large — caching helps but doesn't solve the volume problem alone.

The article's broader lessons apply to any team running agents at scale: set a fixed monthly budget rather than optimizing per-token rates (cheaper rates lead to more usage); measure token counts per request and tag by task type to find where spend actually concentrates; route on the strongest signal you already have rather than building a classifier; and give the router access to the full model range from frontier to small. The article concludes that routing is transitioning from a cost optimization to a prerequisite for ambitious agent deployments.