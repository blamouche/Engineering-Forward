# How to Make LLMs 3X Faster
**Source**: https://blog.bytebytego.com/p/how-to-make-llms-3x-faster
**Date**: 2026-08-26
**Author**: ByteByteGo
**Keywords**: speculative decoding, LLM inference, GPU memory bandwidth, autoregressive decoding, draft model, acceptance rate, parallel verification

## Elevator pitch
Speculative decoding uses a small draft model to generate candidate tokens that a large target model verifies in a single forward pass, converting the GPU's underutilized compute capacity into 2-3x faster LLM generation without changing the output distribution.

## Takeaways
- During token generation, GPU compute utilization drops to 20-40 percent because a 70B model must read ~140GB of weights from VRAM for every single token, while the actual arithmetic on those weights is comparatively tiny
- Transformers compute predictions at every position in one forward pass, so evaluating 4-5 candidate tokens costs roughly the same as evaluating one—this is the key insight behind speculative decoding
- The lossless guarantee: the acceptance rule ensures the output distribution is statistically identical to the target model running alone, whether using greedy decoding or sampling with adjusted probabilities
- Acceptance rate is governed by workload: structured/repetitive output (code, summarization, extraction) yields 80-90% acceptance, while open-ended creative writing produces low acceptance; below ~50%, the overhead outweighs the benefit
- Four draft sources exist: a separate small model (original approach), extra prediction heads on the target model (DeepSeek-V3), a cheaper version of the same model via quantization/layer skipping, or a search over existing text in the prompt
- Gains shrink under concurrency: speedup drops from 1.96x at batch size 1 to 1.21x at batch size 128, and can fall below baseline throughput under heavy load—vLLM dynamically disables speculation above a configurable batch size

## Synthesis
Speculative decoding is a technique that makes LLM token generation 2-3x faster without changing the output, by exploiting a fundamental inefficiency in how autoregressive models work. The problem is memory bandwidth: a 70B model must read roughly 140GB of weights from GPU VRAM for every single token generated, but the arithmetic performed on those weights is small—one narrow vector flowing through enormous weight matrices. During prompt processing, compute utilization is 90-95% because all input tokens share the same weight read. During generation, it falls to 20-40% because each weight read serves exactly one token. That unused capacity is what speculative decoding converts into speed.

The mechanism works by pairing the large target model with a much smaller draft model (10-20x fewer parameters, same family, same tokenizer). The draft model generates K candidate tokens (typically 3-5) through its own sequential loop—cheap because each pass is a fraction of the target's cost. These candidates are appended to the context and verified by the target model in a single forward pass, which computes predictions at every position simultaneously. Working left to right, matching candidates are kept and the first mismatch truncates the rest—but the target model's prediction at the mismatch position is already computed, so you always get at least one correct token per pass, even if all candidates fail.

The output is provably lossless. Under greedy decoding, a candidate is kept when it matches the target model's top choice at that position. Under sampling, both models produce full probability distributions, and an acceptance rule adjusts the odds so the final token distribution is exactly the target model's own, regardless of what the draft suggested. DeepSeek reported 80-90% acceptance rates for the second predicted token in production with DeepSeek-V3, translating to roughly 1.8x generation throughput. The technique works best for structured, repetitive output (code, summarization, extraction) where the small model can reliably predict the large model's behavior, and worst for open-ended creative writing where divergence is high. Under high concurrency, the spare compute disappears—gains drop from 1.96x at batch size 1 to 1.21x at batch size 128—and serving systems like vLLM dynamically disable speculation above a configurable batch size threshold.