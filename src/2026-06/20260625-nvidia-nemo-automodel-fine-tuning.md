# Accelerating Transformers Fine-Tuning with NVIDIA NeMo AutoModel
**Source**: https://huggingface.co/blog/nvidia/accelerating-fine-tuning-nvidia-nemo-automodel
**Date**: 2026-06-24
**Author**: Adil Asif, Alexandros Koumparoulis (NVIDIA)
**Keywords**: NVIDIA, NeMo AutoModel, fine-tuning, MoE, Transformers v5, Expert Parallelism, DeepEP

## Elevator pitch
NVIDIA NeMo AutoModel delivers 3.4-3.7x higher training throughput and 29-32% less GPU memory on MoE fine-tuning compared to native Transformers v5, with a single import line change.

## Takeaways
- NeMo AutoModel subclasses AutoModelForCausalLM, requiring only an import change for existing HuggingFace code
- Achieves 3.4-3.7x higher training throughput and 29-32% less GPU memory on MoE fine-tuning vs native Transformers v5
- Built on Transformers v5's MoE foundations: expert backends, dynamic weight loading, and distributed execution
- Adds Expert Parallelism (EP), DeepEP fused all-to-all dispatch, and TransformerEngine kernels on top of v5
- DeepEP + grouped GEMM reduced cost per iteration by 47% on DeepSeek V3 671B compared to all-gather baselines
- Enables full fine-tuning of Nemotron 3 Ultra 550B across 16 H100 nodes (128 GPUs) — v5 runs out of memory at this scale
- Single-node benchmarks on Qwen3-30B-A3B and Nemotron 3 Nano 30B-A3B show consistent gains
- save_pretrained() still emits standard HF checkpoints compatible with vLLM and SGLang

## Synthesis
NVIDIA's NeMo AutoModel represents a significant practical advance for anyone fine-tuning Mixture-of-Experts models. The key engineering insight is that by building on top of Transformers v5's MoE primitives — rather than replacing them — NeMo AutoModel achieves dramatic performance improvements while preserving the familiar HuggingFace API. Developers change one import line and get a model that is more than three times as fast.

The three performance pillars are Expert Parallelism, DeepEP, and TransformerEngine. Expert Parallelism shards MoE experts across GPUs, which is what enables training at scales where v5 simply runs out of memory. DeepEP overlaps communication with expert computation, reducing the overhead that makes distributed MoE training expensive. TransformerEngine provides fused kernels that accelerate the actual math. Together, these create a progression from v4's eager for-loop through v5's grouped matrix multiplication to NeMo AutoModel's DeepEP + GMM + TE pipeline.

The full fine-tuning result for Nemotron 3 Ultra 550B is particularly notable. At 16 H100 nodes (128 GPUs), this is the regime where Expert Parallelism becomes essential rather than optional. The fact that v5 cannot fit this workload in memory while AutoModel can illustrates the practical difference between theoretical distributed training support and production-grade sharding.

For engineering teams, the practical message is straightforward: if you are fine-tuning MoE models (and increasingly, frontier models are MoE), NeMo AutoModel is now the path of least resistance. The compatibility with vLLM and SGLang for inference means the fine-tuning-to-serving pipeline remains seamless, and the MIT-licensed model weights ensure no vendor lock-in on the model side.