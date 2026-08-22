# JetBrains Mellum 2: Open-Source 12B MoE Coding Model
**Source**: https://arxiv.org/pdf/2605.31268
**Date**: 2026-06-02
**Author**: JetBrains Research
**Keywords**: Mellum-2, JetBrains, open-weight, MoE, coding-model, code-completion, agentic-coding, Apache-2, speculative-decoding, Multi-Token-Prediction

## Elevator pitch
JetBrains open-sources Mellum 2 — a 12B-parameter MoE model with 2.5B active parameters per token, trained on 10.6T tokens, that matches 7B dense model throughput while offering the knowledge capacity of a 12B model, designed as a "focal model" for high-frequency coding tasks where frontier models are overkill.

## Takeaways
- 12B total parameters with only 2.5B active per token via MoE (64 experts, 8 activated) — 12B knowledge capacity at 2.5B inference cost
- Trained on ~10.6T tokens with a three-phase "web early, curated late" curriculum (code ratio 23% → 42% → 59%)
- Matches Qwen2.5-7B throughput in single-request mode (192 vs 193 tok/s) and pulls 21% ahead under concurrent load
- Ships in three variants: base, instruct (answers directly), and thinking (explicit reasoning traces before responding)
- Released under Apache 2.0 with six checkpoints covering the full training pipeline from base through RL-tuned

## Synthesis
JetBrains released Mellum 2, an open-weight 12B-parameter Mixture-of-Experts language model designed as a "focal model" — fast and specialized rather than competing with frontier models on breadth. The concept is that practical AI products require focal models: fast, specialized components that handle high-frequency tasks efficiently, complementing frontier models rather than replacing them.

The architecture is a pure MoE design with 12B total parameters across 64 expert subnetworks, activating only 8 per token — equivalent to 2.5B active parameters per forward pass. This gives the model the knowledge capacity of a 12B model with the inference cost of a 2.5B model. The design uses Grouped-Query Attention with only 4 KV heads, Sliding Window Attention on three of every four layers, and a single Multi-Token Prediction (MTP) head used both as an auxiliary pre-training objective and as a built-in draft for speculative decoding. The configuration has 2304 hidden size with 64 experts distributed across MoE layers.

The training curriculum follows the "web early, curated late" paradigm on ~10.6T tokens. The data mixture progressively shifts from diverse web content toward curated code and mathematical content, with code ratio increasing from 23% to 42% to 59% across three phases. Batch size doubles between phases, with an extended capability-sharpening phase that decays the learning rate linearly to zero. The model was systematically ablated across dense versus MoE backbones, GQA configurations, Multi-head Latent Attention, Sliding Window Attention patterns, and expert sparsity ratios.

Performance benchmarks against Qwen2.5-7B and Qwen3-8B on a single H100 GPU show compelling results. In single-request mode, Mellum 2 matches Qwen2.5-7B almost exactly — 192 tokens per second versus 193. Under concurrent load (where production deployments actually operate), it pulls 21% ahead of Qwen2.5-7B and 79% ahead of Qwen3-8B. The cost profile follows directly: with only 2.5B active parameters, a model serving 10,000 pull requests per day can run on a single mid-range GPU that would require multiple high-end GPUs for a dense 7B model.

While the original Mellum (released April 2025) was a 4B dense model focused narrowly on code completion in JetBrains IDEs, Mellum 2 expands dramatically: it generates and edits code, calls tools, plans and executes multi-step agentic workflows, holds long conversations about code, and in its thinking variant produces explicit reasoning traces before answering. Three post-trained variants ship alongside the base model: an "instruct" version for direct answers, and a "thinking" version for harder multi-step and agentic tasks. Six checkpoints cover the full training pipeline from base pre-train through RL-tuned instruct and thinking variants, all released under Apache 2.0 on Hugging Face.