# The New American AI Model Designed to be Customized: Inkling by Thinking Machines
**Source**: https://blog.bytebytego.com/p/the-new-american-ai-model-designed
**Date**: 2026-08-18
**Author**: ByteByteGo
**Keywords**: Inkling, Thinking Machines, Mira Murati, MoE, sparse models, AI architecture, long context

## Elevator pitch
Thinking Machines (founded by ex-OpenAI CTO Mira Murati) released Inkling, a 975B-parameter MoE model with Apache 2.0 weights that activates only 41B parameters per token, uses a 5:1 sliding-window-to-full-attention ratio for 1M-token context, and introduces learned relative positioning instead of RoPE — a deeply engineered model that prioritizes customizability over raw scale.

## Takeaways
- Inkling is a 975B-parameter mixture-of-experts model where each layer has 256 experts but only 6 activate per token, plus 2 shared experts — meaning roughly 41B parameters process any single token (~4% of the total model).
- The model alternates 55 sliding-window attention layers with 11 full-attention layers (5:1 ratio), enabling a 1M-token context window while keeping attention costs manageable for the majority of layers.
- Rather than RoPE, Inkling uses a learned relative-position encoding that Thinking Machines says performed and extrapolated better in their testing — a notable departure from the current standard.
- The model natively handles images and audio without a separately pretrained encoder, using a lightweight hMLP stem that adds under 1% compute overhead.
- Inkling's "thinking effort" setting (0-1) adjusts how much reasoning the model does before answering; on Terminal Bench 2.1, it matches NVIDIA's Nemotron 3 Ultra with a third of the tokens generated.

## Synthesis
Inkling is the first model from Thinking Machines, Mira Murati's startup after leaving OpenAI, and its architecture reveals deliberate choices that differ from the frontier-model consensus. The 256-expert, 6-active-per-token MoE design keeps per-token inference cheap while requiring the full 975B parameters in memory — at least 2TB of GPU memory for full precision, or four B300 cards for the quantized version. This is a model designed for data centers, not laptops, but the Apache 2.0 licensing means anyone can download and retrain it.

The attention architecture is the most distinctive choice. By running 55 of 66 layers as sliding-window (local) attention, Inkling makes million-token context computationally feasible. Information travels between distant positions through the 11 full-attention layers, which serve as integration points. The tradeoff is that long-range information passes through fewer layers, which can cause the model to miss specific details buried deep in a document.

The learned position encoding over RoPE is another deliberate choice that signals Thinking Machines' willingness to challenge established practices when their testing showed better results. Combined with native multimodality (no separate encoder needed) and a controllable reasoning effort setting, Inkling is positioned as a model designed for customization — you can fine-tune it, quantize it, and adjust how hard it thinks. The frontier model wars increasingly hinge on architectural efficiency, and Inkling's choices make a clear statement about where Thinking Machines believes the efficiency gains lie.