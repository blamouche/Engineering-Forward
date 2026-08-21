# MiniMax Sparse Attention (MSA): FlashAttention and Block-Sparse Kernels for NVIDIA SM100
**Source**: https://github.com/MiniMax-AI/MSA
**Date**: 2026-06-15
**Author**: MiniMax AI
**Keywords**: MiniMax, sparse attention, FlashAttention, NVIDIA SM100, CUDA, CUTLASS, CuTe-DSL, FP8, paged decode, top-k attention

## Elevator pitch
MiniMax open-sources MSA, a production-grade attention kernel library for NVIDIA SM100 (Blackwell) that ships dense FlashAttention and block-sparse top-k attention in two JIT-compiled stacks (csrc and CuTe-DSL), supporting BF16/FP8/NVFP4/FP4 with paged FP8 decode—bringing sparse attention from research to deployable infrastructure.

## Takeaways
- Two JIT-compiled stacks share one Python package: csrc (dense FMHA + sparse top-k indexer, compiled from Jinja templates) and CuTe-DSL (full sparse attention with forward + paged FP8 decode, compiled via cute.compile)
- Supports multiple precision formats: BF16, FP8, NVFP4, and FP4 for sparse prefill, with paged FP8 decode—critical for cost-efficient large-model serving on Blackwell
- The sparse attention workflow is a two-pass design: a dense proxy pass computes per-block max scores from a cheap Q slice, then `sparse_topk_select` picks the top-k KV blocks for the final sparse attention pass
- Distributed via Hugging Face's `kernels` library for easy integration: `from kernels import get_kernel; kernel_module = get_kernel("MiniMaxAI/msa")`
- Requires NVIDIA SM100 (Blackwell), CUDA toolkit with nvcc, Python ≥ 3.10; first JIT compilation takes 30s–several minutes but is cached for subsequent runs
- Released under MIT license with comprehensive benchmarking suite covering dense/paged/sparse prefill and decode in FP8 and BF16

## Synthesis
MSA is significant because it bridges the gap between sparse attention research and production deployment on the latest NVIDIA hardware. Most sparse attention implementations are research artifacts—they work on older GPUs, lack FP8/FP4 support, or don't integrate with production serving stacks. MSA targets SM100 specifically, meaning it's designed for the hardware that will power frontier model inference in 2026-2027.

The two-pass sparse attention design is architecturally interesting. Rather than computing full attention and then pruning, MSA uses a "proxy" pass with a cheap Q slice to estimate which KV blocks matter, then performs full attention only on the selected top-k blocks. This is the same pattern used by MiniMax's production models, making MSA not just a research release but the actual kernel infrastructure they run internally.

The CuTe-DSL stack is particularly noteworthy. CuTe (CUTLASS Tensor Engine) is NVIDIA's high-level DSL for writing portable, high-performance CUDA kernels. By shipping a CuTe-DSL implementation alongside the csrc stack, MiniMax provides both a low-level C++ path (for maximum performance) and a higher-level DSL path (for maintainability and portability across future NVIDIA architectures). The paged FP8 decode support means MSA can be dropped into existing paged-attention serving frameworks (like vLLM) that use page tables for KV cache management.

The MIT license and Hugging Face kernels distribution are strategic choices that lower adoption friction. A serving team can integrate MSA with two lines of Python, test it against their existing FlashAttention implementation, and switch if the sparse path delivers better throughput on their workload. The benchmark suite (bench_sparse_attention_ops.py) provides the TSV output needed for CI-integrated performance regression testing.

For inference engineers, MSA represents the next generation of attention kernel infrastructure for Blackwell. As MoE models with large KV caches become standard, sparse attention is moving from optional optimization to necessity—and MSA is one of the first open-source implementations that targets the hardware where these models will actually run.