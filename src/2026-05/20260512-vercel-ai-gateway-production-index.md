# AI Gateway Production Index
**Source**: https://vercel.com/blog/ai-gateway-production-index
**Date**: May 12, 2026
**Author**: Harpreet Arora, Yvonne Zhou
**Keywords**: Vercel, AI Gateway, production data, model spend, token volume, agentic workloads, multi-model routing, Anthropic, Google, OpenAI

## Elevator pitch
Vercel's AI Gateway Production Index, built from seven months of data across 200K+ teams, reveals that Anthropic leads in spend, Google dominates token volume, agentic workloads now carry 59% of all tokens, and production teams at scale use 35+ distinct models.

## Takeaways
- Anthropic captured 61% of spend in April 2026 vs. Google's 21% and OpenAI's 12%, but Google led token volume at 38% vs. Anthropic's 26%
- Agentic workloads account for 22.2% of requests but 58.9% of all tokens, having doubled in six months; tool-calling requests are 2.6x more token-heavy
- OpenAI's spend share tripled from March to April after GPT-5.4/5.5 releases, while Google's climbed from 8% to 21% as Flash scaled
- Teams at 10M+ requests/month average 35 distinct models in regular use — multi-model routing is standard architecture, not an optimization
- Per-token cost maps to the cost of being wrong: personal assistants run cheap ($/token low), back-office/coding agents run expensive because errors are costlier

## Synthesis
Vercel published its first AI Gateway Production Index on May 12, 2026, offering an unprecedented view into how AI models are actually used in production. Drawing from anonymized routing data across 200K+ teams and seven months of traffic serving "tens of trillions of tokens," the report cuts through benchmark theater to show real workload economics.

The headline finding is a clean separation between spend leaders and volume leaders. Anthropic commanded 61% of April spend through AI Gateway despite higher per-token pricing, while Google captured 38% of token volume. This isn't a tie — it's two different workloads. Spend follows high-stakes reasoning calls (Claude Opus for back-office, coding agents) where errors carry legal or financial risk. Volume follows low-stakes, high-throughput calls (Gemini Flash for consumer assistants, summarization) where mistakes are quickly corrected and cheaply absorbed.

The most dramatic trend is the agentic shift. Tool-calling requests grew from 11.4% to 22.2% of all requests in six months, but by token volume the share jumped from 31.6% to 58.9%. The gap between the two measures — tool-calling requests are 2.6x heavier — reveals that the AI cost surface has fundamentally changed shape. Every agent round trip (function execution, API call, database query, code run) bills against the same token meter, turning what would be a single chat exchange into a chain of tool calls. The economics of AI are shifting from "prompt → response" to "prompt → reasoning → tool → reasoning → tool → response."

At scale, multi-model routing becomes obligatory, not optional. Teams handling 10M+ requests per month averaged 35 distinct models in regular use — a routing graph with cheap classifiers for intent detection, frontier models for reasoning, embedding models for retrieval, fast models for summarization, and vision models for screenshots. The practical implication is that provider lock-in is largely a myth at high scale: switching between labs is a config change, not a vendor migration, and traffic redistributes within hours of a price hike or outage.

The report also quantifies the hidden cost of provider unreliability: 3.5% of requests (5.1% of tokens, 4.9% of spend) complete only after a fallback. The cost-weighted rescue rate exceeds the request-weighted rate because long-context, multi-step, and heavy reasoning calls — the expensive ones — are disproportionately affected by rate limits, timeouts, and errors. An SLA that measures request-level uptime misses the calls that matter most.

The overarching lesson echoes the early cloud era: expand compute first, then optimize per-unit cost. The 35-model fleets visible at the top of the spend curve follow that pattern at a faster cadence, with optimization happening at the routing layer. For teams shipping AI in production, the architecture prescription is clear: plan for multiple providers, build for fallbacks, and treat model routing as a core architectural concern from day one.
