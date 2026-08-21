# DiffusionGemma: 4x Faster Text Generation

**Source**: https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/
**Date**: June 10, 2026
**Author**: Brendan O'Donoghue and Sebastian Flennerhag (Google DeepMind)
**Keywords**: DiffusionGemma, text diffusion, Gemma 4, Mixture of Experts, MoE, parallel decoding, local inference, NVIDIA, open model, Apache 2.0

## Elevator pitch
Google releases DiffusionGemma, an experimental open model that uses text diffusion instead of autoregressive decoding to generate entire blocks of text simultaneously, achieving up to 4x faster inference on GPUs — over 1,000 tokens per second on a single H100.

## Takeaways
- DiffusionGemma is a 26B Mixture of Experts (MoE) model that activates only 3.8B parameters during inference, fitting within 18GB VRAM on consumer GPUs when quantized
- The model generates 256 tokens in parallel with each forward pass using bi-directional attention, enabling every token to attend to all others — a significant advantage for non-linear tasks like code infilling and mathematical graphs
- On a single NVIDIA H100, DiffusionGemma achieves over 1,000 tokens per second; on an RTX 5090, over 700 tokens per second
- The model iteratively refines its own output through multiple passes, starting from random placeholder tokens and locking in correct tokens progressively — similar to AI image generation
- Output quality is lower than standard Gemma 4 models, making DiffusionGemma suited for speed-critical interactive workflows rather than maximum-quality production outputs
- Released under Apache 2.0 license with support for MLX, vLLM, Hugging Face Transformers, and NVIDIA NeMo; official llama.cpp support coming soon

## Synthesis
Google's DiffusionGemma represents a fundamentally different approach to text generation that could reshape local AI inference. While traditional autoregressive LLMs act like a typewriter — generating one token at a time from left to right — DiffusionGemma drafts an entire 256-token paragraph simultaneously, similar to how AI image generators start with visual static and iteratively refine it into a clear picture.

The key innovation is shifting the decode bottleneck from memory-bandwidth to raw compute. In cloud environments, autoregressive models are efficient because servers can batch thousands of requests together. But locally for a single user, the word-by-word process leaves the GPU underutilized, spending most of its time waiting for the next "keystroke." DiffusionGemma reverses this inefficiency by giving the processor a larger chunk of work at once, upgrading inference from a sequential typewriter to a printing press that stamps entire text blocks simultaneously.

The bi-directional attention mechanism is particularly noteworthy. Because every token can attend to all others during parallel generation, DiffusionGemma excels at tasks where tokens depend on future context — code infilling, Sudoku, amino acid sequences, and mathematical graphs. Unsloth demonstrated this by fine-tuning DiffusionGemma to play Sudoku, a task that autoregressive models struggle with. However, the speed advantage is specifically designed for local and low-concurrency inference; in high-QPS cloud serving, autoregressive models can saturate compute efficiently, making DiffusionGemma's parallel decoding offer diminishing returns. The model trades overall quality for speed, positioning it as a complementary tool rather than a replacement for production-grade autoregressive models.