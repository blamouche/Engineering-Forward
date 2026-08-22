# Nvidia Nemotron 3 Ultra: 550B Open-Weights Hybrid Mamba-Transformer
**Source**: https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/
**Date**: 2026-06-02
**Author**: NVIDIA Research
**Keywords**: Nemotron, open-weights, MoE, Mamba-2, LatentMoE, Multi-Token-Prediction, NVFP4, 1M-context, agentic-reasoning, distillation

## Elevator pitch
Nvidia releases Nemotron 3 Ultra — a 550B total / 55B active parameter hybrid Mamba-Transformer MoE model with 1M token context, 6x higher inference throughput than comparable open LLMs, and full open-source release including checkpoints, datasets, and training recipes.

## Takeaways
- 550B total / 55B active parameters using LatentMoE (Mamba-2 + MoE + Attention hybrid) with Multi-Token Prediction (MTP) for faster inference via native speculative decoding
- Achieves 5.9x, 4.8x, and 1.6x higher inference throughput than GLM-5.1-754B, Kimi-K2.6-1T, and Qwen-3.5-397B respectively on 8K input / 64K output
- Supports 1M token context length with on-par accuracy to state-of-the-art open LLMs across diverse benchmarks
- Pretrained in NVFP4 on 20 trillion tokens, post-trained with SFT, RL, and Multi-teacher On-Policy Distillation (MOPD)
- Full open-source: pre-trained, post-trained, and quantized checkpoints plus training datasets released on HuggingFace

## Synthesis
NVIDIA introduces Nemotron 3 Ultra, the most capable model in the Nemotron 3 family and the company's most intelligent open-weights model to date. The model targets the growing demand for long-running autonomous agentic tasks by combining state-of-the-art accuracy with dramatically higher inference throughput.

The architecture is a hybrid Mamba-2 Transformer Latent Mixture-of-Experts (LatentMoE) design. LatentMoE projects tokens into a smaller latent dimension for expert routing and computation, improving accuracy per byte compared to standard Granular MoEs. The model interleaves Mamba-2 and MoE layers with select Attention layers — the hybrid Mamba-Attention approach significantly improves inference throughput by reducing attention cost and KV cache footprint. Multi-Token Prediction (MTP) layers use a shared-weight design across prediction heads, improving training signal quality and enabling faster inference via native speculative decoding. The model has 108 layers, 8192 model dimension, 64 Q-heads, 2 KV-heads, 512 experts per layer with 22 activated, and 2 MTP layers.

Training followed a three-phase curriculum on ~10.6 trillion tokens. The data mixture progressively shifts from diverse web content (23% code) toward curated code and mathematical content (59% code in the final phase), with batch-size doubling and an extended capability-sharpening phase. The pre-training used NVFP4 quantization-aware training — the majority of linear layers use NVFP4 for weights, activations, and gradients, while select layers (latent projections, MTP layers, QKV/attention projections, embeddings) are maintained in BF16 or MXFP8 for training stability. Context was extended to 1M tokens after pre-training.

Post-training used an agent-focused pipeline: Supervised Fine Tuning (SFT), Reinforcement Learning (RL), and Multi-teacher On-Policy Distillation (MOPD). The model supports inference-time reasoning budget control, allowing configurable thinking via chat template (`enable_thinking=True/False`). The throughput advantages are significant: 5.9x higher than GLM-5.1-754B-A40B, 4.8x higher than Kimi-K2.6-1T-A32B, and 1.6x higher than Qwen-3.5-397B-17B on 8K input / 64K output settings, while maintaining on-par accuracy across agentic and reasoning benchmarks.

The full open-source release includes four checkpoints (NVFP4 quantized, BF16 post-trained, BF16 base, and GenRM for RLHF), four training datasets (173B tokens of fresh code, synthetic legal data, specialized factual/moral data, and post-training datasets), and model recipes via the NVIDIA Nemotron Developer Repository. The model scores 48 on the Artificial Analysis Intelligence Index, well ahead of the next strongest open model (Gemma 4 31B at 39), and serves over 300 tokens per second on a pre-release Deep Infra endpoint.