# Inference Cost at Scale with Napkin Math
**Source**: https://injuly.in/blog/napkin-inference-cost/index.html
**Date**: 2026-06-15
**Author**: InJuly (injuly.in)
**Keywords**: inference cost, napkin math, matrix multiplication, GPU economics, LLM serving, token pricing, FLOPs

## Elevator pitch
A practical engineering guide that breaks down LLM inference cost from first principles—starting with the cost of a single matrix multiplication and building up to per-token and per-request economics—giving engineers the mathematical intuition to reason about serving costs without needing a full benchmark suite.

## Takeaways
- The fundamental unit of inference cost is the matrix multiplication: for a W×H weight matrix and B×H input batch, the cost is 2·B·W·H FLOPs per matmul, and all LLM inference reduces to repeated matmuls of this form
- Per-token generation cost is dominated by the KV-cache attention matmuls in the decode phase, where batch size (concurrent requests) is the key lever for amortizing fixed GPU costs
- GPU utilization in practice is far below theoretical peak—real-world TFLOPS are often 30-50% of advertised due to memory bandwidth bottlenecks, kernel inefficiency, and batch fragmentation
- The napkin math framework lets engineers estimate serving cost per token by combining: model parameter count, precision (FP16/INT8/INT4), GPU FLOP/s, GPU memory bandwidth, and target concurrency
- Token pricing in production should be derived from cost-per-GPU-hour divided by achievable tokens-per-second, not from benchmarking alone—this is the bridge between hardware economics and API pricing

## Synthesis
This article fills a gap in the AI engineering literature: most resources either treat inference cost as a black box (use the provider's pricing page) or dive into full benchmark infrastructure. The napkin math approach gives engineers a middle ground—enough mathematical structure to reason about costs quickly, without requiring a production benchmarking suite.

The starting point is deliberately minimal: the cost of one matrix multiplication. For an LLM, every layer's forward pass is two matmuls (attention projection and FFN), so the total per-token cost is approximately 2·N_params FLOPs for the prefill phase and 2·N_layers·(attention_cost) for decode. The article builds from this foundation to show how batch size, sequence length, and model size interact.

The most practically useful insight is the emphasis on memory bandwidth as the real bottleneck in decode. During autoregressive generation, each token requires loading the full model weights from memory, making the computation memory-bound rather than compute-bound. This means that INT4 quantization—which reduces memory footprint by 4x—can deliver close to 4x throughput improvement in decode, even though it only reduces FLOPs by 4x on paper. The gap between theoretical and effective FLOP/s is where most cost optimization lives.

For teams building LLM-powered products, the napkin math framework provides the foundation for make-or-buy decisions: at what request volume does self-hosting become cheaper than API calls? The answer depends on model size, quantization, GPU choice, and target latency—all of which can be estimated with the formulas in this article before committing to infrastructure. This is essential reading for any engineer responsible for inference cost optimization.