# TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch

**Source**: https://gdm-tipsv2.github.io/
**Date**: April 21, 2026
**Author**: Unknown
**Keywords**: gdm-tipsv2, tipsv2, advancing, vision, language, pretraining, with, enhanced

## Elevator pitch
TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment. A new family of image-text encoder models with strong dense patch-text alignment, evaluated across 9 tasks and 20 datasets

## Takeaways
- TIPSv2 is the next generation of the TIPS family of foundational image-text encoders empowering strong performance across numerous multimodal and vision tasks.
- Our work starts by revealing a surprising finding, where distillation unlocks superior patch-text alignment over standard pretraining, leading to distilled student models significantly surpassing their much larger teachers in this capability.
- We carefully investigate this phenomenon, leading to an improved pretraining recipe that upgrades our vision-language encoder significantly.
- Three key changes are introduced to our pretraining process (illustrated in the figure below): iBOT++ extends the patch-level self-supervised loss to all tokens for stronger dense alignment; Head-only EMA reduces training cost while retaining performance; and Multi-Granularity Captions uses PaliGemma and Gemini descriptions for richer text supervision.
- Combining these components, TIPSv2 demonstrates strong performance across 9 tasks and 20 datasets, generally on par with or better than recent vision encoder models, with particularly strong gains in zero-shot segmentation.

## Synthesis
TIPSv2 is the next generation of the TIPS family of foundational image-text encoders empowering strong performance across numerous multimodal and vision tasks. Our work starts by revealing a surprising finding, where distillation unlocks superior patch-text alignment over standard pretraining, leading to distilled student models significantly surpassing their much larger teachers in this capability. We carefully investigate this phenomenon, leading to an improved pretraining recipe that upgrades our vision-language encoder significantly. Three key changes are introduced to our pretraining process (illustrated in the figure below): iBOT++ extends the patch-level self-supervised loss to all tokens for stronger dense alignment; Head-only EMA reduces training cost while retaining performance; and Multi-Granularity Captions uses PaliGemma and Gemini descriptions for richer text supervision. Combining these components, TIPSv2 demonstrates strong performance across 9 tasks and 20 datasets, generally on par with or better than recent vision encoder models, with particularly strong gains in zero-shot segmentation. TIPSv2 introduces 3 pretraining improvements: iBOT++ (enhanced MIM loss), Head-only EMA (memory-efficient self-supervised losses), and Multi-granularity captions (richer text supervision). TIPSv2 produces smoother feature maps with well-delineated objects compared to prior vision-language models (e.g., TIPS and SigLIP2). While DINOv3 also exhibits smooth feature maps, TIPSv2 shows stronger semantic focus : object boundaries are more precisely delineated and regions show granular semantic details. We compare ViT-g models of several vision encoders, except for DINOv3, where we compare with the 6× larger ViT-7B. Select an image below to explore PCA components of patch embeddings.
