# AI Gateway production index
**Source**: https://vercel.com/blog/ai-gateway-production-index
**Date**: May 12, 2026
**Authors**: Harpreet Arora, Yvonne Zhou
**Keywords**: Vercel, AI Gateway, production data, model adoption, Anthropic, Google, OpenAI, agentic workloads, multi-model architecture

## Elevator pitch
Vercel's AI Gateway production index, built on seven months of traffic from 200K+ teams, reveals that Anthropic leads in spend (61%) while Google leads in token volume (38%), agentic workloads now carry 59% of all tokens, and high-scale teams routinely use 35+ distinct models.

## Takeaways
- Cost and volume tell opposing stories: Anthropic captures 61% of spend through premium models like Claude Opus, while Google leads token volume at 38% through cheap, fast models like Gemini Flash—the same customers use both tiers.
- Spend per token correlates with the cost of being wrong: personal assistants run cheap (40% of tokens, 20% of cost), while back-office agents run expensive (15% of tokens, 6% of cost) because errors carry legal or financial risk.
- Agentic workloads have doubled in six months: 58.9% of all tokens are now in tool-call requests (up from 31.6%), with agentic requests being 2.6× more token-heavy than non-agentic ones.
- Teams at 10M+ monthly requests average 35 distinct models in a routing graph: cheap classifiers, frontier reasoners, embedding models, fast summarizers, and vision models—all swappable in hours.
- New model versions absorb family traffic within weeks: Claude Sonnet 4.6 took most Sonnet family share in its first full month, and 3.5% of all requests are rescued by fallback routing after provider failures.

## Synthesis
Vercel's AI Gateway production index offers a rare, ground-truth view of how AI models are actually used in production, cutting through the noise of static benchmarks and vendor marketing. Drawing from tens of trillions of tokens served across hundreds of models to over 200,000 teams, the data reveals a market far more nuanced than "who's winning AI."

The headline split between spend and volume leadership is instructive. Anthropic dominates spend at 61%, but Google commands token volume at 38%. This isn't contradictory—it reflects a two-tier model architecture that has become standard: cheap, fast models like Gemini Flash handle high-volume, low-stakes consumer workloads, while expensive reasoning models like Claude Opus power back-office, legal, and financial applications where an error's cost exceeds the per-call savings. The same customer base appears on both leaderboards, routing different call types to different models.

The agentic shift is the most consequential trend in the data. Tool-calling requests have doubled their share of total tokens to 58.9% in just six months, even though they represent only 22.2% of requests. This gap—agentic requests being 2.6× heavier—reflects the fundamental economic shift from chat-shaped to agent-shaped workloads, where each prompt spawns chains of tool calls that compound token consumption. For infrastructure providers, this means revenue growth outpaces request growth; for application developers, it means cost modeling must account for agentic amplification.

Perhaps the most strategically significant finding is the absence of lock-in at scale. Teams processing 10M+ requests monthly average 35 distinct models arranged in a routing graph, where any component can be swapped in hours. New model versions absorb family traffic within weeks of release, and 3.5% of requests complete successfully only because of automated fallback routing. The data suggests that as AI adoption matures, multi-model orchestration becomes standard infrastructure, and the competitive moat shifts from model exclusivity to routing intelligence and reliability engineering.
