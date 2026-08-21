# Google Is Building a Chip with Gemini Baked into the Silicon
**Source**: https://thenextweb.com/news/google-frozen-chip-gemini-silicon
**Date**: 2026-07-20
**Author**: The Next Web
**Keywords**: Google, Gemini, AI chips, Frozen v2, custom silicon, TPU, inference

## Elevator pitch
Google is reportedly developing "Frozen v2," a server chip that hardwires Gemini's neural network architecture directly into silicon, potentially achieving 6–10x efficiency gains over its latest TPUs.

## Takeaways
- Google's "Frozen v2" project bakes Gemini's model architecture into dedicated silicon, creating a chip that is the model rather than just running it.
- The chip could be 6–10x more efficient than Google's latest custom AI chips in tokens served per unit of power, though deployment isn't expected before 2028.
- The initiative responds partly to a severe AI capacity crunch inside Google, with Cloud turning away external customers due to internal demand.
- Unlike general-purpose GPUs and TPUs, Frozen v2 locks the model architecture into the hardware—weights remain updatable, but the underlying structure is fixed.
- If successful, the approach would push the custom AI silicon race from running any model to fusing specific models with the metal, forcing competitors to respond.

## Synthesis
Google's "Frozen v2" project represents a significant inflection in the custom AI silicon race. Rather than continuing to build general-purpose accelerators that can run any model, Google is betting on hardwiring Gemini's neural network architecture directly into chip circuitry. The approach is analogous to how early cryptographic accelerators moved from software implementations to dedicated silicon—but applied to an entire frontier AI model.

The efficiency claims are striking: 6–10x improvement in tokens per watt over current TPUs. If achieved, this would dramatically reshape the economics of running large models at scale, particularly for inference workloads that dominate production AI costs. The trade-off is rigidity: the chip's architecture is fixed to today's Gemini design, meaning it becomes less useful as model architectures evolve. Google partially mitigates this by keeping weights updatable, but the fundamental structure is frozen at fabrication time.

The strategic context matters. Google is responding to an internal capacity crunch severe enough that Cloud has turned away external customers. This isn't just about efficiency—it's about survival at scale. The chip would be a new product line separate from TPUs, not a replacement, suggesting Google sees room for both general-purpose and model-specific silicon in its infrastructure.

The broader implication is that the custom silicon race is entering a new phase. Companies like Google are no longer just designing chips that run models—they're designing chips that embody models. If Google proves this approach works at scale, every major AI lab with sufficient volume will face pressure to consider whether model-specific silicon delivers enough efficiency to justify the design risk. The question is whether AI architectures move too fast for this approach, or whether the economics of inference at Google's scale make it irresistible regardless.