# Open Weights Isn't Open Training
**Source**: https://www.workshoplabs.ai/blog/open-weights-open-training
**Date**: 2026-03-09
**Author**: Addie Foote
**Keywords**: open source AI, open weights, open training, transparency, reproducibility, model governance, data openness, AI policy

## Elevator pitch
"Open weights" models release the parameters but not the full training pipeline, creating a misleading equivalence with true open source software that obscures how much remains proprietary and unreproducible.

## Takeaways
- The dominant definition of "open" in AI has collapsed to mean weights-available, omitting training data, preprocessing pipelines, fine-tuning recipes, and evaluation frameworks.
- This selective openness allows companies to claim open-source credibility while retaining the proprietary advantages that actually determine model capability and behavior.
- Reproducibility is functionally impossible without training data and code: releasing weights lets people use a model but not verify, audit, or replicate how it was built.
- Regulatory and governance frameworks that treat open-weights models as equivalent to truly open systems may be systematically misled about what "openness" actually provides.
- The gap between weights-open and training-open is growing as post-training processes (RLHF, constitutional AI, fine-tuning) increasingly determine model behavior over raw pretraining.

## Synthesis
The software analogy that underlies "open source AI" breaks down in an important way: releasing source code for a software program gives you everything needed to build and run it. Releasing model weights gives you an artifact—the output of a process—but not the process itself. The distinction matters for reproducibility, auditability, and trust.

Foote's argument lands hardest on governance. When policymakers debate open vs. closed AI, they typically mean weights-available vs. weights-restricted. But the policy questions that matter most—who controls model behavior, what data shapes its values, how bias enters during training—require access to the training process, not just the trained output. A weights-open model trained on unknown data with undisclosed RLHF procedures provides very limited accountability compared to a model whose full training pipeline is documented and replicable.

The commercial incentives driving this gap are straightforward. Training data is expensive to collect and curate; training runs consume substantial compute; fine-tuning recipes encode significant engineering knowledge. Companies releasing weights but not training pipelines get credit for openness while protecting the assets that actually produce competitive advantage.

The post-training layer is particularly significant. Pretraining on large text corpora is increasingly commoditized, but RLHF, constitutional AI methods, and instruction tuning inject value and shape model personality, safety properties, and capabilities in ways that downstream users cannot inspect from weights alone. As post-training sophistication increases, the gap between "open weights" and genuine transparency will widen further.
