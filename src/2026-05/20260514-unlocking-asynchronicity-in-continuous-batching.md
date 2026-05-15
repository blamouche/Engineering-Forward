# Unlocking asynchronicity in continuous batching
**Source**: https://huggingface.co/blog/continuous_async
**Date**: May 14, 2026
**Author**: Rémi Ouazan Reboul, Pedro Cuenca, Aritra Roy Gosthipaty (Hugging Face)
**Keywords**: LLM inference, continuous batching, CUDA streams, GPU utilization, asynchronous batching, KV cache, throughput optimization

## Elevator pitch
Hugging Face demonstrates how to eliminate 24% GPU idle time in LLM inference by separating CPU batch preparation from GPU compute using CUDA streams and events — achieving near-zero overhead asynchronous continuous batching.

## Takeaways
- In synchronous continuous batching, CPU and GPU take turns: nearly 24% of total generation time is wasted with an idle GPU waiting for the CPU
- The fix uses three CUDA streams: H2D (host-to-device transfers), compute, and D2H (device-to-host transfers), none touching the synchronizing default stream
- CUDA events enforce cross-stream ordering: record() marks completion points, wait() blocks a stream until the event fires, all on-GPU with no CPU involvement
- Preparing batch N+1 while batch N computes requires predicting which requests will finish — solved by overbooking: assume all finish and adjust if wrong
- On an H200 at ~$5/hour, a 24% speedup means significant cost savings for production inference workloads

## Synthesis
This technical deep-dive from Hugging Face tackles a subtle but significant inefficiency in LLM serving: synchronous continuous batching wastes nearly a quarter of GPU time because the CPU and GPU take turns rather than working in parallel. The post walks through building asynchronous batching from first principles using CUDA primitives — streams and events — that are widely available but underutilized in inference engines.

The core mechanism uses three non-default CUDA streams to decouple input transfers, compute, and output transfers. CUDA events enforce ordering across streams entirely on the GPU side, eliminating CPU synchronization overhead. The trickier challenge is preparing batch N+1 based on batch N's outputs before batch N has finished — solved through logical overbooking: the CPU optimistically assumes all requests will continue and adjusts the batch if some finish early.

The practical impact is significant: 24% more throughput at zero model or kernel change cost. For an H200 at ~$5/hour running inference 24/7, that translates to roughly $876/month in recovered GPU time. The implementation is part of Hugging Face's transformers library, making it accessible to practitioners without CUDA expertise.

This represents the kind of systems-level optimization that compounds as models scale and inference volumes grow — not as flashy as a new architecture, but arguably more impactful for real-world deployment economics.
