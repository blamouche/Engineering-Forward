# What Would AI Email Cost?
**Source**: https://www.tomtunguz.com/cost-of-ai-email/
**Date**: May 14, 2026
**Author**: Tomasz Tunguz
**Keywords**: AI email, cost optimization, inference segmentation, local models, SaaS pricing, GPU economics, model matching

## Elevator pitch
Tomasz Tunguz calculates that AI-powered email processing would cost $22-130/month using state-of-the-art models, suggesting a viable $500/year SaaS product — but shows that matching models to workloads and running inference locally can reduce costs by 100x.

## Takeaways
- Fully AI-powered email using frontier models costs $22-130/month in raw compute, with a midpoint of $26/month
- A SaaS company targeting 75% gross margin would price this at roughly $500/year — about twice the cost of Google Enterprise plans
- Smaller models reduce costs by 10-20x, but the real optimization comes from matching the model to the workload
- Running models locally drops the cost to near-zero by leveraging users' own GPU hardware
- The next 12-24 months of AI software will be defined by this kind of inference segmentation: deterministic rules where possible, matched model tiers where needed

## Synthesis
Tomasz Tunguz applies his characteristic data-driven approach to a concrete question: what would it actually cost to have AI process your email? Using state-of-the-art model pricing for the reasoning and generation involved — reading, classifying, drafting replies, extracting action items — the raw compute cost ranges from $22 to $130 per month. At the midpoint of $26 per month, a SaaS company seeking standard 75% gross margins would need to charge roughly $500 per year, excluding hosting and serving costs.

At $350-500 per year, AI email sits at roughly twice the price of a Google Enterprise plan ($11-18/month), positioning it as a premium productivity layer rather than a commodity feature. Tunguz suggests this price point would find willing buyers in enterprise contexts, where the time savings from automated triage, drafting, and action extraction could easily justify the cost. The economics hold up at scale, with volume discounts bringing enterprise pricing into a comfortable range.

But the real insight lies in Tunguz's cost optimization analysis. Smaller models cut costs by 10-20x, and running models locally on users' own hardware drives the marginal cost to near-zero. This leads to what Tunguz identifies as the defining challenge for AI software in the next 12-24 months: segmentation of inference. Some components, like email filters, are purely deterministic rules that should never touch a model. Others, like summarization, work fine on smaller local models. Only the most complex tasks — multi-source synthesis, nuanced drafting — genuinely require frontier models.

This layered approach to inference — deterministic rules where possible, mid-tier models for routine work, frontier models for the hard stuff — can reduce overall cost by 100x. In an environment of severe GPU shortages, Tunguz argues, this segmentation of inference is not just an optimization but an inevitability. The companies that master this matching of models to workloads will have a fundamental cost advantage over those that route everything through the most expensive endpoint.
