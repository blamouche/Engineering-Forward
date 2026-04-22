# Sign-Bit Flips in Neural Networks
**Source**: https://mkimhi.github.io/DNL/
**Date**: Unknown
**Author**: Ido Galil, Moshe Kimhi, Ran El-Yaniv
**Keywords**: model security, neural networks, bit flips, attacks, robustness

## Elevator pitch
This work shows that a handful of targeted sign-bit flips in stored model weights can catastrophically destroy vision and language models, making model storage integrity look like a much bigger security issue.

## Takeaways
- Deep Neural Lesion identifies critical parameters without needing training data or expensive optimization.
- The attack requires only write access to model weights, a realistic threat model in compromised systems.
- Results suggest devastating failure from one or two flips in some vision systems and a few more in language models.
- Early-layer, high-magnitude parameters appear especially vulnerable across architectures.
- The paper argues selective hardening of the most critical weights can substantially improve resilience.

## Synthesis
The DNL work on sign-bit flips is striking because it compresses catastrophic model failure into an alarmingly small number of changes. Instead of needing retraining sabotage, poisoned data, or large-scale corruption, the authors show that flipping the sign bit of a tiny set of carefully chosen weights can collapse performance in both vision and language systems.

The setup matters. Their threat model assumes only write access to stored model parameters, something that could plausibly occur through compromised firmware, DMA attacks, Rowhammer-style exploits, or rootkits. No access to training data is required. No heavy optimization loop is required either. The method is intentionally data-free and lightweight, which makes it harder to dismiss as an unrealistic lab curiosity.

The reported results are severe. For some image classifiers, two sign flips are enough to produce a near-total accuracy collapse. Detection and segmentation systems also degrade dramatically with one or two flips in backbone networks. On the language side, the paper reports major reasoning collapse in models such as Qwen3 and Nemotron after only a small number of targeted perturbations. The degraded outputs are not merely a bit worse, they often become nonsensical, repetitive, or effectively unusable.

Why is the attack so effective? The authors argue that early-layer, high-magnitude weights play an outsized role in shaping downstream representations. Flipping the sign on one of those parameters does not make a subtle change. It can invert critical features at the very start of computation, corrupting the whole representational pipeline that follows. This pattern appears across CNNs, transformers, and MoE-style architectures, which makes the vulnerability feel structural rather than architecture-specific.

The paper also makes an important defensive point. Because vulnerability is concentrated, selective hardening of the top 0.1 to 1 percent most critical weights may provide meaningful protection without prohibitive overhead. That is a useful observation because full integrity protection across massive models can be expensive, while targeted protection may be feasible.

The broader implication is uncomfortable. As models become operational infrastructure, protecting data pipelines and API perimeters is not enough. Model artifacts themselves become a security boundary. If a few low-level bit changes can silently destroy a deployed system, storage integrity and hardware-level protection need much more attention.

This work makes neural network security look less like a pure prompt or access problem and more like classic systems security. The model weights are the asset, and compromising them can be devastating with surprisingly little effort.
