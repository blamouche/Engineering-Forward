# Why I Believe in SOTA Models Over Custom Ones
**Source**: https://danielmiessler.com/blog/sota-models-over-custom-ones
**Date**: 2026-03-10
**Author**: Daniel Miessler
**Keywords**: SOTA models, fine-tuning, custom models, context engineering, model selection, AI strategy, general intelligence

## Elevator pitch
Custom and fine-tuned models are usually the wrong choice: general-purpose state-of-the-art models combined with intelligent context management outperform narrow specializations because broad knowledge enriches even specialized tasks.

## Takeaways
- Specialization is misleading: tasks that appear narrow (email labeling, threat detection, report writing) actually benefit from broader intelligence, just as a highly experienced human generalist often outperforms a narrow specialist.
- Custom model training creates maintenance burden, versioning complexity, and capability gaps that compound over time as SOTA models rapidly improve.
- The economic trajectory favors general models: they're becoming cheaper and more capable faster than the cost of custom training is declining.
- Context engineering—intelligent management of what information goes into a SOTA model's context—typically closes the gap that fine-tuning addresses, without the overhead.
- Smaller general models (Sonnet, Haiku) deployed with optimized context often outperform larger custom models at lower cost.

## Synthesis
Miessler's argument is essentially a bet on generalization as a more durable capability than specialization. The human analogy is apt: when we hire for most professional roles, we weight general intelligence, experience, and judgment heavily alongside domain knowledge—precisely because work is more heterogeneous in practice than job descriptions suggest. Email labeling isn't purely pattern matching; it requires understanding context, tone, and organizational dynamics that a narrow classifier can't capture.

The maintenance argument against custom models is underappreciated in conversations about fine-tuning strategy. Custom models require labeled data that ages, training pipelines that need maintenance, evaluation frameworks that need updating, and deployment infrastructure separate from the SOTA model stack. This overhead is justifiable when the performance gap is large and persistent—but as general model capabilities improve rapidly, that gap narrows faster than the maintenance cost decreases.

The context engineering alternative is gaining traction as a practical framework: instead of training a model to know something, give it the information at inference time. This approach scales differently—adding a new domain requires updating the context, not retraining a model. For most enterprise use cases where requirements change regularly, this is a significant operational advantage.

The cases where custom models still make sense are real: regulated environments with data that can't be sent to API providers, latency requirements that require model size optimization, or capability gaps where fine-tuning provides durable advantage. But these cases are narrower than the current enthusiasm for custom model development suggests.
