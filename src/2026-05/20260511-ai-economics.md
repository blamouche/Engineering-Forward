# AI Economics
**Source**: https://sriramkrishnan.substack.com/p/ai-economics
**Date**: 2026-05-11
**Author**: Sriram Krishnan
**Keywords**: AI economics, OpenAI, Anthropic, xAI, GPU supply, token economics, inference costs, revenue per token, cloud infrastructure, Meta, Google, Microsoft, Amazon

## Elevator pitch
The AI industry has crystallized into distinct economic profiles: OpenAI struggles with consumer-heavy low-revenue usage, Anthropic can't get enough GPUs for its enterprise demand, and xAI has massive GPU supply with zero demand—while big tech players position to profit from infrastructure regardless of which model wins.

## Takeaways
- Three core metrics define AI lab economics: tokens per watt-year (supply), revenue per token (demand), and revenue per watt-year (the combined measure)
- OpenAI has 900M+ monthly users but low revenue per token from consumer-heavy free/paid mix, while Anthropic's 300K+ businesses (1,000+ spending >$1M/year) create high revenue but rate-limiting shortages
- Meta open-sources Llama as a strategic move: one-time training cost with zero inference cost, creating pricing pressure on competitors even if Llama is only 60-90% as good
- Microsoft and Amazon profit from cloud infrastructure regardless of who wins the model race—investing in multiple labs and securing multi-billion cloud deals
- No AI lab has reached the self-funding threshold for its next cluster; all still rely on outside capital (investors, IPOs, sovereign funds)

## Synthesis
Sriram Krishnan, a longtime tech operator and investor, presents a lucid framework for understanding the AI industry's economic dynamics as of May 2026. The piece is structured around two key dimensions: the distinct identities of the major players and the core economic metrics that determine their trajectories.

The player analysis reveals a market of complementary imbalances. OpenAI dominates consumer mindshare with 900M+ monthly active users but faces a debilitating usage mix problem—high volumes of free and low-value consumer prompts generate minimal revenue while consuming substantial inference compute. Anthropic has the inverse problem: 300K+ business customers with over 1,000 spending more than $1M annually creates excellent revenue-per-token economics, but demand consistently exceeds GPU capacity, forcing constant rate-limiting. xAI sits at an extreme with Colossus' massive GPU supply and virtually no model demand, leading to its dual strategy of acquiring Cursor for developer demand and leasing capacity to Anthropic.

Big tech players operate on different logics entirely. Google owns the full stack (TPUs, data centers, cloud, applications) and treats AI as both defensive (Gemini protecting Search ad revenue) and offensive (Cloud monetizing infrastructure demand). Meta, with $200B in ad revenue largely immune to AI disruption, open-sources Llama as a strategic pricing weapon—zero ongoing inference cost for Meta, but market pressure on competitors' pricing. Microsoft and Amazon follow similar cloud-infrastructure plays: invest billions in AI labs, secure multi-billion cloud commitments, and profit from infrastructure regardless of which model prevails. Amazon's neutrality is notable, having invested in both OpenAI and Anthropic.

The economics section introduces a clean analytical framework. Training is a one-time capital investment (building the factory); inference is the factory running 24/7, compounding with scale. Tokens per watt-year measures supply-side efficiency—how much output per unit of sustained power. Revenue per token captures demand-side dynamics: price per million tokens, usage mix (free vs consumer vs enterprise), and GPU utilization rates. Revenue per watt-year is the composite metric determining whether a lab can self-fund its next cluster. Krishnan notes a critical observation from Jensen Huang's GTC 2026 presentation: "Tokens per Watt × Available Watt" only addresses supply; revenue doesn't automatically follow efficient infrastructure, as xAI demonstrates. The fundamental question remains unresolved: no AI lab has crossed the self-funding threshold, making the industry structurally dependent on external capital for its next generation of clusters.
