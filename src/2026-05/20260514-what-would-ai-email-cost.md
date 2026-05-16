# What Would AI Email Cost?
**Source**: https://www.tomtunguz.com/cost-of-ai-email/
**Date**: May 14, 2026
**Author**: Tomasz Tunguz
**Keywords**: AI email, cost optimization, inference segmentation, local models, SaaS pricing, GPU shortage, agentic email

## Elevator pitch
Tomasz Tunguz calculates that fully agentic AI email would cost $22–$130/month in raw inference and $500/year as a SaaS product, but argues that intelligent workload segmentation — matching model size to task complexity and running simpler tasks locally — can reduce costs by 100x.

## Takeaways
- State-of-the-art model inference for AI email costs $22–$130/month raw; a SaaS company targeting 75% gross margin would charge roughly $500/year, about twice what Google Enterprise costs today.
- Smaller models cut costs by 10–20x immediately, but the real optimization breakthrough comes from segmenting inference workloads.
- Running models locally on the user's own GPU drops the marginal inference cost to zero — the hardware is a sunk cost that depreciates whether used or not.
- The key engineering challenge for the next 12–24 months is determining which components can execute deterministically (like email filters, which are just rules) versus which genuinely need frontier models.
- With basic heuristics and workload-model matching, overall costs can drop by 100x, making the GPU shortage-driven segmentation of inference "inevitable."

## Synthesis
Tomasz Tunguz, GP at Theory Ventures, tackles a deceptively simple question: what would an AI-powered email system actually cost? Building on his previous post about the future of AI email, he walks through a cost analysis that illuminates the economic realities of building agentic software products in 2026.

The raw numbers are striking. Using state-of-the-art model inference, the monthly cost ranges from $22 to $130 depending on the model tier. At a midpoint of $26/month in raw inference cost, a SaaS company targeting a standard 75% gross margin would need to charge roughly $350 per year before accounting for hosting and serving costs. With those operational costs included, Tunguz estimates a $500/year price point with a 15% discount at scale. To put this in context, Google Enterprise currently costs $11–$18/month — meaning a fully agentic AI email solution would cost roughly twice as much as the incumbent enterprise email offering.

But Tunguz doesn't stop at the headline number. The more interesting part of his analysis is the cost optimization path. Smaller models immediately cut costs by a factor of 10 to 20, but the real breakthrough comes from what he calls "inference segmentation" — matching the model to the workload. Email filters, for instance, are essentially deterministic rules that don't need any model at all. By identifying which components of an email system can run as simple heuristics versus which genuinely require frontier-model reasoning, the overall cost drops dramatically.

The most provocative point is about local inference. When models run on the user's own hardware, the marginal inference cost drops to zero — the GPU is a sunk cost that depreciates regardless. Tunguz frames this as a critical strategic insight: the next 12 to 24 months of AI software development will be defined by this type of crude-but-effective cost optimization. Companies that can intelligently route tasks between deterministic rules, small local models, and cloud frontier models will have a massive cost advantage.

This connects to Tunguz's broader thesis about inference market segmentation, which he argues is "inevitable" given the tremendous GPU shortage. The companies that win will be those that treat inference not as a monolithic "call the best model" operation but as a tiered system where every workload gets exactly the compute it needs and nothing more. The economics make this not just an optimization but an existential requirement for AI-native SaaS businesses.
