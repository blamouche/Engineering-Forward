# What Would AI Email Cost?
**Source**: https://www.tomtunguz.com/cost-of-ai-email/
**Date**: 2026-05-14
**Author**: Tomasz Tunguz
**Keywords**: AI email, cost analysis, local inference, model optimization, GPU economics, inference segmentation, SaaS pricing, agentic email

## Elevator pitch
Tomasz Tunguz calculates that fully agentic AI email would cost $22-$130/month in raw model compute, but demonstrates how basic model-to-workload matching and local inference can cut costs by 100x, making the economic case that inference segmentation is inevitable.

## Takeaways
- At state-of-the-art model pricing, AI email costs $22-$130/month in raw compute, translating to roughly a $500/year SaaS product at 75% gross margins — about twice Google Enterprise pricing.
- Smaller models cut costs 10-20x, but the real breakthrough comes from running models locally on users' GPUs, where marginal cost drops to zero.
- Tunguz advocates a three-tier cost optimization strategy: deterministic email filters handled as rules (not AI), smaller models for routine tasks, and frontier models only when necessary.
- This workload-to-model matching — "segmentation of inference" — will define the next 12-24 months of AI software development.
- With ongoing GPU shortages, the economic pressure to segment inference workloads across model sizes grows more acute.

## Synthesis
Following his previous piece on the future of AI email, Tomasz Tunguz turns to the economics, providing a concrete cost model for what agentic email would actually cost to operate. Using state-of-the-art models, the raw compute cost ranges from $22 to $130 per month depending on usage patterns. Taking the middle case of $26/month in raw costs, a software vendor targeting 75% gross margins would need to charge roughly $350/year, or an estimated $500/year once hosting and serving costs are included — approximately double what Google Enterprise currently costs ($11-18/month).

The analysis quickly moves beyond sticker prices to optimization strategy. Smaller, less capable models reduce costs by 10 to 20 times immediately. But Tunguz identifies local inference as the decisive economic lever: running models on users' own GPUs drops marginal cost to zero, eliminating the cloud compute bill entirely. This creates a three-tier optimization framework: deterministic tasks like email filtering should be simple rules, not AI at all; routine classification and drafting can use small models; and only the most complex reasoning tasks require frontier models.

Tunguz frames this "segmentation of inference" as the defining challenge for the next 12-24 months of AI software development. The approach mirrors how software engineering has always worked — matching the right tool to the right problem — but applied to the AI layer itself. Given the tremendous shortage of GPUs driving up cloud inference costs, this segmentation isn't just economically advantageous; Tunguz argues it is inevitable. The companies that master this workload-to-model matching will have a structural cost advantage that compounds with scale.
