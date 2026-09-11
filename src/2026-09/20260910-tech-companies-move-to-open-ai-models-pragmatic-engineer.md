# The Pulse: Tech Companies Move to Open AI Models
**Source**: https://newsletter.pragmaticengineer.com/p/tech-companies-move-to-open-ai-models
**Date**: 2026-09-10
**Author**: The Pragmatic Engineer (Gergely Orosz)
**Keywords**: open models, AI cost optimization, Uber, Pinterest, AT&T, model routing, LiteLLM, Anthropic pricing, Claude Code, Databricks, Stripe, Coinbase, Ramp

## Elevator pitch
The Pragmatic Engineer reports on a major trend: tech companies including Uber, Pinterest, AT&T, Stripe, Coinbase, and Ramp are achieving massive AI cost savings — 50% to 90%+ — by dropping proprietary frontier models in favor of open weight models and smart model routing, with Anthropic's Opus 5 now looking 100x overpriced compared to alternatives like GPT-5.6 Luna and DeepSeek.

## Takeaways
- Uber cut cost per AI request by 34% and cost per AI session by 52% through open weight models, optimized model selection, cheaper subagent models, reduced model effort, prompt caching, and context compaction
- Pinterest achieves cost per transaction at less than 8% of what comparable closed models cost by post-training open source models on its own data within its secure cloud infrastructure
- AT&T cut its AI bill by 56% with only a 2% decrease in output quality after moving workloads to open models via router provider LiteLLM
- Anthropic's Opus 5 is 100x more expensive than models like GPT-5.6 Luna xhigh and DeepSeek, making it increasingly hard to justify for cost-conscious engineering teams
- Databricks' research across Stripe, Coinbase, Uber, and Ramp confirms open models offer the biggest savings, followed by smart model routing; spending controls and context optimization trail far behind
- Ramp data confirms AI spend at the top 1% of businesses declined 10% in August — the first concrete evidence of enterprise AI spend contraction
- Emerging CPU shortage driven by AI agents' heavy tool usage follows earlier GPU and memory shortages

## Synthesis
This Pragmatic Engineer issue crystallizes what may be the most important AI infrastructure trend of 2026: the economics of frontier models are breaking down. The article assembles quantitative evidence from multiple companies that the gap between proprietary and open model capabilities has narrowed enough that the 2-100x price premium of frontier models is no longer defensible for most workloads.

Uber's approach is the most detailed case study. The ridesharing giant blew through its annual AI budget in three months, then systematically optimized: running open weight models on inference providers (2-20x cheaper), benchmarking all models weekly on real work, defaulting to Medium effort for best cost-to-output ratio, using cheaper subagent models for smaller tasks, triggering context compaction at 400K tokens, and caching prompts. The result: flat cost despite significantly more usage since March.

Pinterest's approach is even more aggressive — post-training open models on its own data yields superior performance to closed models at less than 8% of the cost. AT&T's experience via LiteLLM routing shows 56% savings with just 2% quality degradation. The Databricks cross-company analysis confirms the pattern: open models and model routing are the two highest-impact levers, with spending controls and context optimization being secondary.

The pricing pressure on Anthropic is the strategic subtext. Opus 5 at 100x the cost of GPT-5.6 Luna xhigh and DeepSeek represents a pricing cliff that more companies will walk off. The Ramp data showing a 10% decline in AI spend at top companies in August is the first hard evidence that the AI spending boom may have peaked — not because companies are using less AI, but because they're getting smarter about what they pay for it.