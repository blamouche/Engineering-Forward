# PyTorch 2.12 Release Blog
**Source**: https://pytorch.org/blog/pytorch-2-12-release-blog
**Date**: 2026-05-13
**Author**: PyTorch Foundation
**Keywords**: PyTorch, release, performance, CUDA, ROCm, quantization, distributed training, torch.accelerator, linalg, Adagrad, Microscaling

## Elevator pitch
PyTorch 2.12 delivers up to 100x faster batched eigendecomposition, a device-agnostic graph API, Microscaling quantization support, and expanded ROCm features as the framework matures from research tool to production platform.

## Takeaways
- Batched linalg.eigh on CUDA is up to 100x faster through cuSolver backend optimization, resolving a longstanding performance gap
- New torch.accelerator.Graph API provides unified graph capture/replay across CUDA, XPU, and out-of-tree backends
- torch.export now supports Microscaling (MX) quantization formats for deploying aggressively compressed models
- Adagrad optimizer now supports fused=True, joining Adam, AdamW, and SGD with single-kernel implementations
- ROCm users gain expandable memory segments, rocSHMEM symmetric memory collectives, and FlexAttention pipelining

## Synthesis
The PyTorch 2.12 release represents another significant step in the framework's evolution from a research-first library into a unified, hardware-agnostic platform for production training and inference. Built from 2,926 commits by 457 contributors, this release continues the trajectory established by the 2.x series, emphasizing cross-backend performance, exportability for deployment, and distributed training improvements.

The headline performance improvement is in batched eigendecomposition (linalg.eigh), where PyTorch deprecated the legacy MAGMA backend in favor of cuSolver's syevj_batched kernel. The result is up to 100x speedups for workloads processing batches of small-to-medium matrices—previously individual matrix solves were dispatched inefficiently, but now cuSolver processes them as a single GPU operation. This is particularly impactful for scientific computing and ML workloads. Another performance win comes from fused Adagrad, which now executes the entire optimizer step in a single CUDA kernel, reducing launch overhead and memory traffic, joining the existing family of fused optimizers (Adam, AdamW, SGD).

The compiler and export improvements reflect PyTorch's push toward production deployment. The new torch.accelerator.Graph API provides a device-agnostic abstraction for graph capture and replay, with initial XPU support and extensibility to out-of-tree backends. Torch.export now handles Microscaling (MX) quantization formats—float8_e8m0fnu dtypes used for aggressive model compression—unblocking full export-to-deployment workflows for teams targeting cost-constrained environments. Additionally, torch.cond control flow can now be captured within CUDA Graphs using CUDA 12.4's conditional IF nodes, enabling GPU-side evaluation of data-dependent branching.

Distributed training improvements are substantial. Custom operators can now accept ProcessGroup objects directly, streamlining distributed workflows. Profiler enhancements expose flow IDs, activity types, and NCCL collective correlation across ranks via sequence numbers. FlightRecorder now supports ncclx and gloo backends alongside existing nccl/xccl, with broader torchcomms operation tracking.

Platform support expands significantly: CUDA Graph kernel annotations enable easier post-hoc analysis by injecting metadata into profiler traces; CUDA Green Contexts gain workqueue limits for resource partitioning. The ROCm ecosystem receives particular attention with expandable memory segments, rocSHMEM symmetric memory collectives, and FlexAttention pipelining—all bringing feature parity closer between NVIDIA and AMD infrastructure. The release epitomizes PyTorch's current philosophy: becoming faster across more backends while enabling deployment on an increasingly diverse set of platforms.
