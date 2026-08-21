# How Baseten Built the World's Fastest API for GLM-5.2
**Source**: https://www.baseten.co/blog/how-we-built-the-worlds-fastest-api-for-glm-52/
**Date**: 2026-06-24
**Author**: Baseten Engineering Team
**Keywords**: GLM-5.2, Baseten, inference, NVFP4, PD disaggregation, multi-token prediction, NVIDIA Dynamo

## Elevator pitch
Baseten achieved 280+ tokens per second on GLM-5.2 through a combination of NVFP4 quantization, KV-aware routing, prefill-decode disaggregation, and multi-token prediction — a masterclass in production LLM inference optimization.

## Takeaways
- Baseten serves GLM-5.2 at over 280 TPS as measured by Artificial Analysis, the fastest publicly reported
- NVFP4 quantization from FP8 weights preserves model quality on agentic benchmarks like BFCL while enabling faster tensor cores and reduced VRAM bandwidth burden
- KV-aware routing with NVIDIA Dynamo tools routes requests to replicas with cached context, reducing TTFT to ~800ms
- Prefill-decode disaggregation yields 2x higher TPS by running prefill and decode on separate engines with different configurations
- GLM-5.2's Multi-Token Prediction (MTP) heads are leveraged for speculative decoding, further boosting TPS
- GLM-5.2 is a 744B parameter MoE model with 40B active parameters and 1M token context window
- Notion is already using GLM-5.2 via Baseten's API in production
- The disaggregation uses NVIDIA Dynamo for prefill queuing, conditional disaggregation, and NIXL-based KV transfer

## Synthesis
Baseten's GLM-5.2 API optimization is a detailed engineering case study in how to squeeze maximum performance from a frontier MoE model in production. The post breaks down four distinct optimization layers that compound to deliver the 280+ TPS result, and each layer is worth understanding independently.

The first layer is quantization. Baseten performed an in-house NVFP4 quantization from the original FP8 weights using NVIDIA ModelOpt. The key claim is that on the BFCL function calling benchmark — representative of agentic workloads — the quantized model performs equivalently to FP8 within margin of error. This is significant because NVFP4's dual scale factors preserve dynamic range better than naive INT4, making it viable for production inference on Blackwell GPUs.

The second layer is KV-aware routing. For long-context agentic workloads, prefill is expensive. By routing requests to replicas that already have relevant KV cache, Baseten avoids redundant computation. The data is revealing: of the 7.9-second average time to first answer token, 7.1 seconds are reasoning tokens versus only 0.8 seconds for input processing. Bringing TTFT down to 800ms through caching is a major win.

The third layer is prefill-decode disaggregation. Rather than having a single GPU node handle both phases, Baseten runs them on separate engines. This allows independent scaling (more prefill engines than decode engines), independent configuration optimization, and eliminates resource contention. The result: 2x higher TPS compared to aggregated deployment.

The fourth layer is speculative decoding using GLM-5.2's MTP heads. Unlike external draft models, MTP is built into the model architecture, reducing the cost of generating draft tokens and increasing acceptance rates. Baseten notes there is still headroom to unlock, suggesting future gains.

For infrastructure teams, the lesson is that production LLM inference is no longer a single optimization problem — it's a systems engineering challenge that spans quantization, caching, disaggregation, and speculative execution. Each layer compounds on the others.