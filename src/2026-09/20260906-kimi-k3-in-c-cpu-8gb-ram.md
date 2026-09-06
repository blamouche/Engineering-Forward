# Kimi K3 in C: A 2.78T-Parameter Model Running on One CPU With 8 GB of RAM
**Source**: https://github.com/FareedKhan-dev/kimi-k3-in-c
**Date**: 2026-08-31
**Author**: Fareed Khan
**Keywords**: Kimi K3, CPU inference, C99, memory-efficient inference, mixture-of-experts, MoE, mxfp4 quantization, linear attention, SIMD, AVX2, systems programming

## Elevator pitch
A from-scratch C99 inference engine runs Kimi K3 — all 2.78 trillion parameters — on a single CPU with just 8.24 GB of RAM and a 176 KB binary, proving that frontier-scale models can technically execute on consumer hardware if you accept extreme latency tradeoffs.

## Takeaways
- The entire engine is 176 KB of portable C99 with zero dependencies: no BLAS, no framework, no GPU — just raw SIMD (AVX2) and careful memory management
- The model checkpoint is 1.56 TB on disk, but only the dense trunk and a small resident working set need to live in RAM; the 1.45 TB of routed MoE experts are streamed directly from NVMe in their packed 4-bit (mxfp4) form and never resident
- At 8 GB RAM, inference produces 32.69 seconds per token; at 128 GB (full model resident), it drops to 5.6 seconds per token — the output is byte-identical across all memory budgets
- The key architectural insight is a "fit cascade": four decisions about where bytes live (resident trunk depth, expert streaming, 4-bit packed weights, memory-mapped IO) take the model from cluster-scale to laptop-scale without changing results
- This is not a production serving solution — it's a systems programming exercise that reframes the "you need a cluster" assumption into a concrete engineering question about which bytes must be in memory versus which can sit on disk

## Synthesis
Fareed Khan's kimi-k3-in-c project is a remarkable feat of systems engineering that strips a 2.78-trillion-parameter mixture-of-experts model down to its essential bytes and runs it on a single CPU. The implementation is written in portable C99, compiles to a 176 KB binary, and uses no external libraries — not even BLAS. All linear algebra is hand-written with AVX2 SIMD intrinsics.

The core insight is about memory hierarchy, not compute. Kimi K3 is a MoE model where the dense trunk is relatively small but the routed expert layers are enormous (1.45 TB of expert weights). Khan's engine keeps the dense trunk resident in memory to a configurable depth and streams expert weights directly from NVMe storage in their packed 4-bit (mxfp4) format, multiplying them on the fly without ever materializing the full expert in RAM. This means the same model produces byte-identical output whether running in 8 GB or 224 GB of RAM — only the speed changes.

The performance tradeoff is severe: 26.5 seconds per token at 8 GB, 19.8 seconds at 64 GB, and 5.6 seconds at 128 GB. Nobody will serve production traffic with this engine. But the project's value is conceptual: it transforms the vague assumption that "frontier models require clusters" into a precise systems question about which bytes must be resident, which can be streamed, and how much latency you're willing to tolerate for access. The fit cascade — four explicit decisions about data placement — is a clean framework that other engineers can apply when thinking about model deployment on constrained hardware.

The project also demonstrates the value of from-scratch implementations for understanding systems. By building the inference engine without frameworks, Khan forces every architectural decision into the open: the memory budget, the streaming strategy, the quantization format, the SIMD paths. The codebase covers linear attention, MoE routing, mxfp4 dequantization, and memory-mapped I/O, all in readable C99. For anyone interested in how large models actually run at the byte level, this repository is an excellent educational resource.