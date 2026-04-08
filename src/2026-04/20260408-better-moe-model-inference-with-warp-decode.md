# Better MoE model inference with warp decode

**Source**: https://cursor.com/blog/warp-decode
**Date**: 2026
**Author**: Cursor
**Keywords**: moe inference, blackwell, gpu kernels, warp decode, performance engineering

## Elevator pitch
Cursor describes a new Blackwell-optimized MoE decode approach that reorganizes parallelism around outputs rather than experts, reducing bookkeeping and improving both throughput and numerical fidelity.

## Takeaways
- Warp decode flips the traditional MoE inference organization from expert-centric to output-centric.
- The design removes multiple staging and data-layout steps that dominate small-batch decode overhead.
- Cursor reports major throughput gains on B200 GPUs plus better numerical closeness to FP32 reference.
- The article is a sharp example of hardware-aware inference work translating directly into product velocity.
- It also shows why inference engineering is now a serious competitive layer, not just an optimization footnote.

## Synthesis
This is a strong mechanical-sympathy piece. The clever move is not a magical new algorithm, but changing the unit of parallelism to fit the realities of Blackwell decode workloads. At small-batch autoregressive decode, expert-centric data movement creates too much overhead relative to the actual math, so Cursor rethinks the problem around independently computed outputs. The result is less staging, fewer buffers, and better scheduler freedom. The broader lesson is that frontier model performance increasingly depends on these “boring” inference details. When model quality is expensive to improve, a big systems win that makes training loops cheaper and deployment faster has outsized leverage.
