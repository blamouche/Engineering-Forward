# Parcae: Doing more with fewer parameters using stable looped models

**Source**: https://www.together.ai/blog/parcae
**Date**: April 19, 2026
**Author**: Unknown
**Keywords**: together, parcae, doing, more, with, fewer, parameters, using

## Elevator pitch
Parcae is a stable looped language model that matches the quality of a Transformer twice its size — a 770M model reaching 1.3B-level performance. We introduce the first scaling laws for looping and show that increasing recurrence, not just data, is a compute-efficient path to bet.

## Takeaways
- All blog posts Research Published 4/15/2026 Parcae: Doing more with fewer parameters using stable looped models Authors Hayden Prairie, Zachary Novack, Taylor Berg-Kirkpatrick, Dan Fu Table of contents 40+ Models Chosen for Production...40+ Models Chosen for Production...40+ Models Chosen for Production...
- Links in this article Paper Code Hugging Face Summary We present Parcae, one of the first stable architectures for looped language models , achieving the quality of a Transformer twice the size with clean, predictable training.
- Parcae creates a new medium to scale quality by increasing recurrence rather than purely scaling data, opening up an efficient frontier for training memory-constrained on-device models.
- Getting the most out of your parameters Traditional scaling laws tell us that to achieve the best performance, we need to scale FLOPs, often with more parameters or data.
- But as models move to the edge and inference costs skyrocket, we wonder: Can we scale quality without inflating memory footprint?

## Synthesis
All blog posts Research Published 4/15/2026 Parcae: Doing more with fewer parameters using stable looped models Authors Hayden Prairie, Zachary Novack, Taylor Berg-Kirkpatrick, Dan Fu Table of contents 40+ Models Chosen for Production...40+ Models Chosen for Production...40+ Models Chosen for Production... Links in this article Paper Code Hugging Face Summary We present Parcae, one of the first stable architectures for looped language models , achieving the quality of a Transformer twice the size with clean, predictable training. Parcae creates a new medium to scale quality by increasing recurrence rather than purely scaling data, opening up an efficient frontier for training memory-constrained on-device models. Getting the most out of your parameters Traditional scaling laws tell us that to achieve the best performance, we need to scale FLOPs, often with more parameters or data. But as models move to the edge and inference costs skyrocket, we wonder: Can we scale quality without inflating memory footprint? To that end, we’ve been exploring looped architectures, models that increase compute by passing activations through the same layers multiple times. While promising, these models have been unstable to train. We tackle this issue directly and introduce Parcae , a stable looped architecture that: Is better than prior looped models : Parcae achieves up to 6.3% lower validation perplexity than previous large-scale looped recipes. Punches above its weight : Our 770M Parcae matches the quality of a 1.3B parameter transformer trained on the same data, achieving the same performance with roughly half the parameters. Scales Predictably: We establish the first scaling laws for looping , finding that compute-optimal training requires increasing looping and data in tandem .
