# PyTorch 2.12 Release Blog
**Source**: https://pytorch.org/blog/pytorch-2-12-release-blog
**Date**: 2026-05-13
**Author**: PyTorch Foundation
**Keywords**: PyTorch, machine learning framework, CUDA, ROCm, torch.compile, distributed training, quantization, MX formats, GPU optimization, linalg, Adagrad

## Elevator pitch
PyTorch 2.12 delivers up to 100x faster batched eigendecomposition on CUDA, a new device-agnostic graph capture API, Microscaling quantization support for compressed model deployment, and fused Adagrad optimization—continuing the framework's evolution from research-first tool into a unified, hardware-agnostic production platform.

## Takeaways
- Batched linalg.eigh on CUDA achieves up to 100x speedup by replacing legacy MAGMA backend with optimized cuSolver syevj_batched kernel dispatch
- The new torch.accelerator.Graph API provides a unified graph capture/replay interface across CUDA, XPU, and out-of-tree backends, enabling cross-hardware parity
- torch.export now supports Microscaling (MX) quantization formats (MXFP4, MXFP6, MXFP8), unblocking export of aggressively compressed models for cost-constrained deployments
- Adagrad joins Adam, AdamW, and SGD with fused=True single-kernel optimizer implementation, reducing kernel launch overhead
- torch.cond control flow can now be captured and replayed inside CUDA Graphs using CUDA 12.4 conditional IF nodes, enabling GPU-native branching

## Synthesis
The PyTorch 2.12 release, comprising 2,926 commits from 457 contributors, continues the framework's multi-year transformation from a research-oriented tool into a production-grade, cross-backend platform. The release builds on the foundations laid by PyTorch 2.10 (cross-backend performance primitives, TorchScript deprecation) and 2.11 (differentiable collectives, FlashAttention-4) to deliver meaningful improvements across performance, export, and distributed training.

The headline performance improvement is a reworking of batched eigendecomposition on CUDA. By deprecating the legacy MAGMA backend in favor of cuSolver's syevj_batched kernel—which processes many small/medium matrices as a single GPU operation—workloads that previously took minutes now run in seconds. This is particularly impactful for scientific computing and ML workloads dependent on batched eigenvalue problems, and it resolved a longstanding performance gap with CuPy.

The torch.accelerator.Graph API represents a significant step toward PyTorch's hardware-agnostic ambitions. By providing a unified abstraction over backend-specific graph implementations, it enables code written for CUDA graph capture to work across XPU and out-of-tree backends without modification. Combined with the new is_capturing() method on streams, this brings cross-backend parity to graph and stream management—a critical capability as the hardware landscape diversifies beyond NVIDIA.

For model deployment, the addition of Microscaling quantization format support in torch.export is particularly timely. As teams move large language models to cost-constrained and edge environments, aggressive quantization using MX formats (which share a block-scale exponent across multiple values) has become increasingly popular. The previous inability to export models using these formats was a significant deployment blocker; 2.12 resolves this by correctly serializing the float8_e8m0fnu dtype used as the shared exponent.

The distributed training improvements are pragmatic and focused: ProcessGroup objects can now be passed directly to custom ops, eliminating string-based group name lookups. Profiler enhancements expose flow IDs, NCCL sequence numbers for cross-rank correlation, and unfinished event tracking. FlightRecorder gains ncclx and gloo backend support. On the AMD side, ROCm users gain expandable memory segments, rocSHMEM symmetric memory collectives, and FlexAttention pipelining.

The release reflects PyTorch's maturing role in the AI ecosystem: no longer just the framework researchers prefer, but increasingly the platform that carries models from experimentation through to optimized production deployment across an expanding array of hardware targets, with the performance characteristics that production workloads demand.
