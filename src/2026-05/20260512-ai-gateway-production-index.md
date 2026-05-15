# AI Gateway Production Index
**Source**: https://vercel.com/blog/ai-gateway-production-index
**Date**: 2026-05-12
**Author**: Harpreet Arora, Yvonne Zhou
**Keywords**: AI Gateway, Vercel, production AI, model routing, Anthropic, Google, OpenAI, agentic workloads, multi-model architecture, fallback, spend share

## Elevator pitch
Vercel's AI Gateway Production Index, based on seven months of production traffic from 200K+ teams processing tens of trillions of tokens, reveals that Anthropic leads in spend (61%) while Google leads in volume (38%), agentic workloads now carry 59% of all tokens, and production teams at scale routinely use 35+ distinct models.

## Takeaways
- Anthropic dominates spend share (61% in April 2026) through high-stakes enterprise workloads on Claude Opus, while Google leads token volume (38%) through cheap Gemini Flash calls—the same customer base uses both for different layers
- OpenAI's spend share tripled from March to April after GPT-5.4/5.5 releases, showing how quickly model updates can shift market position
- Agentic (tool-calling) requests carry 58.9% of all tokens despite being only 22.2% of requests, meaning tool-using requests are 2.6x more token-heavy—the cost surface has shifted from chat-shaped to agent-shaped
- Teams at 10M+ monthly requests average 35 distinct models in regular use, running routing graphs where every model is swappable within hours
- 3.5% of requests complete after fallback rerouting, but cost-weighted rescue rate is 4.9% because expensive calls fail more often—provider SLA uptime diverges from real application experience

## Synthesis

Vercel's AI Gateway Production Index is one of the most valuable data artifacts in the AI industry this year, precisely because it measures what people actually do, not what they say they do. With tens of trillions of tokens passing through 200K+ teams, this isn't a survey or a benchmark bake-off—it's a direct observation of production behavior at scale.

The headline finding is the spend-versus-volume split. Anthropic commands 61% of spend but only 26% of token volume, while Google captures 38% of volume but only 21% of spend. This isn't a contradiction; it's two sides of the same application architecture. The same customer base routes high-stakes reasoning calls to Claude Opus (expensive, reliable, quality-critical) and cheap, fast calls to Gemini Flash. Spend follows the cost of being wrong: back-office workflows where errors trigger legal or financial risk pay premium per-token rates, while personal assistants where mistakes are individually cheap and quickly corrected run on the cheapest viable model.

This "cost of being wrong" framework is the report's most useful analytical lens. Personal assistants account for 40% of token volume but only 20% of cost. Back-office agents flip the ratio: 15% of volume but 6% of cost, with per-token costs roughly 4x higher. The B2B/B2C split confirms the pattern: B2B applications cost roughly twice as much per token as B2C. Every workload's per-token economics are a stake map of how expensive a wrong answer is to that use case.

The agentic workload data is perhaps the most consequential trend. Tool-calling requests have doubled from 31.6% to 58.9% of all tokens in six months—and they're not just more requests, they're structurally more expensive. An agent making ten tool calls bills roughly ten times the tokens of a simple chat. The cost surface of production AI has shifted from chat-shaped to agent-shaped while headline request counts barely moved. This has profound implications for infrastructure planning: if your cost model assumes chat-like token consumption and your users are deploying agents, you're modeling the wrong thing.

The multi-model architecture finding challenges the dominant narrative about provider lock-in. Teams at 10M+ monthly requests average 35 distinct models—a cheap classifier for intent detection, a frontier model for reasoning, an embedding model for retrieval, a fast model for summarization, a vision model for screenshots. Every model is swappable within hours. Provider switching isn't a migration project; it's a config change. The "lock-in" story inverts at scale: the highest-volume teams are the least locked in.

The adoption velocity data is equally striking. When Claude Sonnet 4.6 shipped, it absorbed most of the Sonnet family's traffic within its first full month. Predecessor models stayed live and routable, but teams migrated anyway because the switch was trivial. Labs no longer control the upgrade timeline of their own product lines—the routing layer does.

The fallback data reveals a hidden cost that SLAs don't capture. 3.5% of requests complete after a fallback reroute, but the cost-weighted rescue rate runs at 4.9%. That gap exists because the requests that fail are systematically bigger and more expensive: long context windows hit rate limits, multi-step agent runs accumulate failure, heavy reasoning calls time out under sustained load. A provider's request-level SLA uptime diverges from what the application actually experiences on exactly the calls that paid for the premium model. For anyone building production AI, fallback routing isn't a nice-to-have—it's a requirement that pays for itself in rescued revenue on your most expensive calls.
