# AI Economics
**Source**: https://sriramkrishnan.substack.com/p/ai-economics
**Date**: 2026-05-11
**Author**: Sriram Krishnan
**Keywords**: AI economics, OpenAI, Anthropic, xAI, Meta, Google, Microsoft, Amazon, tokens per watt, revenue per token, inference, training, GPU, cloud infrastructure

## Elevator pitch
Sriram Krishnan deconstructs the AI industry's emerging economic framework, mapping each major lab's strategic position around the core tension between supply-side efficiency (tokens per watt) and demand-side monetization (revenue per token), with no lab yet reaching the self-funding threshold for their next training cluster.

## Takeaways
- OpenAI has massive consumer volume but suffers from low revenue per token due to free/paid user mix; Anthropic has premium enterprise demand but lacks sufficient GPU capacity
- xAI has enormous GPU supply via Colossus but zero demand—a cautionary tale that building infrastructure doesn't automatically generate revenue
- Meta's open-source Llama strategy is an economic weapon: one-time training cost, zero inference cost for Meta, designed to pressure competitors' pricing
- The key metric is revenue per watt-year—the intersection of tokens per watt (supply efficiency) and revenue per token (demand quality)—which determines whether a lab can self-fund its next cluster
- Microsoft and Amazon are structurally indifferent to which model wins, having invested in multiple labs and secured cloud compute deals that pay them regardless

## Synthesis

Sriram Krishnan's framework for AI economics is one of the clearest attempts yet to map the strategic landscape of the foundation model race. He begins by profiling each major lab through the lens of a single organizing tension: supply versus demand.

OpenAI commands 900M+ monthly active users—a staggering consumer footprint—but that volume creates a usage mix problem. Free users and casual consumers generate enormous inference costs with low revenue per token. The compounding effect of millions of low-value prompts means OpenAI burns cash serving demand that doesn't pay its way. This is fundamentally a demand quality problem, not a demand quantity problem.

Anthropic sits at the opposite pole. With 300K+ business customers and over a thousand spending more than $1M annually, Anthropic has the usage mix every lab dreams of: high revenue per token, predictable enterprise patterns, paid inference that justifies its cost. But this creates a GPU supply crisis—Anthropic is constantly rate-limited, unable to serve all the premium demand it has. Hence the headline deal with xAI/SpaceX to lease Colossus capacity.

xAI is the cautionary tale. The Colossus supercluster represents enormous GPU supply, but without competitive models to utilize it, the supply sits idle. xAI's pivot to acquiring Cursor and leasing capacity to Anthropic reflects the hard truth that compute without demand is just stranded capital.

The second tier of players—Meta, Google, Microsoft, Amazon—operate with different incentives entirely. Meta's open-source Llama strategy is perhaps the most cunning: a one-time training cost with zero ongoing inference expense for Meta itself, while the mere existence of a free, competent model creates downward pricing pressure on OpenAI and Anthropic. It's economic warfare by open source. The tradeoff is talent retention—researchers want frontier-scale compute, not ad optimization.

Google owns the full stack (TPUs, data centers, cloud, applications) giving it the lowest AI cost structure, but faces an existential threat: every query that goes to ChatGPT or Claude is a lost Search ad impression. Its strategy is defensive (Gemini protecting Search) and offensive (TPUs and Cloud monetizing AI infrastructure demand).

Microsoft and Amazon have the most structurally elegant positions. Both are cloud infrastructure providers that invested billions in AI labs (Microsoft in OpenAI, Amazon in both OpenAI and Anthropic) with multi-billion dollar cloud compute commitments baked in. They get paid regardless of who wins the model race. Amazon is building custom Titanium chips with Anthropic, deepening the lock-in.

The economic framework Krishnan proposes rests on two metrics. Tokens per watt-year captures supply-side efficiency—how much output you squeeze from physical infrastructure through better hardware, smarter batching, and efficient inference stacks. Revenue per token captures demand quality—price times utilization times usage mix. Revenue per watt-year, the intersection of both, is the single number that determines whether a lab can self-fund its next training cluster.

No lab has crossed the self-funding threshold yet. Every new model generation requires more compute than the last, and every lab still relies on outside capital—investors, IPOs, cloud partners, sovereign funds. The race to be first to self-funding profitability is the quiet war beneath the public model benchmarks. It may determine the industry's structure more than any technical breakthrough.
