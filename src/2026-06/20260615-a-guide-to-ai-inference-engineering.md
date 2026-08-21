# A Guide to AI Inference Engineering
**Source**: https://blog.bytebytego.com/p/a-guide-to-ai-inference-engineering
**Date**: 2026-06-15
**Author**: ByteByteGo
**Keywords**: inference engineering, LLM serving, prefill, decode, KV cache, batching, prefix caching, quantization, speculative decoding, parallelism, disaggregation, GPU, TTFT, tokens per second

## Elevator pitch
ByteByteGo's comprehensive guide to AI inference engineering explains how the prefill-decode split drives every optimization technique in production LLM serving—from batching and prefix caching to quantization, speculative decoding, parallelism, and disaggregation.

## Takeaways
- LLM inference has two phases with opposite bottlenecks: prefill is compute-bound (TTFT), decode is memory-bandwidth-bound (TPS)—techniques that help one often don't help the other
- Open models (2M+ on Hugging Face, 25x growth in 5 years) have made self-hosting viable: ~80% cost reduction at scale, better latency tuning, and 4-nines uptime vs. 2-nines for public APIs
- Six core optimization techniques: batching (throughput vs. latency trade-off), prefix caching (reuses KV cache for shared prompt prefixes), quantization (30-50% performance gain from precision reduction), speculative decoding (draft model proposes, target verifies), parallelism (tensor/pipeline/expert parallel across GPUs), and disaggregation (separate hardware for prefill and decode)
- Quantization tolerances vary: linear weights handle it well, activations are sensitive, KV cache more so, and attention layers are most sensitive because errors compound across token sequences
- Cursor's Composer 2.0 is a representative example of self-hosted open-model inference engineering delivering autocomplete latency below closed APIs

## Synthesis
ByteByteGo's guide is a structured walkthrough of why inference engineering looks the way it does, organized around a single structural insight: every LLM inference call consists of two phases with fundamentally different physical demands on the GPU.

The prefill phase processes the entire input prompt through every layer in parallel, producing the first output token and the KV cache. This phase is compute-bound—the GPU's math units are the limiting factor, and more raw compute makes it faster. Time to first token (TTFT) is the key metric. The decode phase generates subsequent tokens one at a time, each requiring a full forward pass through all layers. This phase is memory-bandwidth-bound—math throughput sits idle while the GPU reads model weights from memory for each pass. Tokens per second (TPS) is the key metric.

This split organizes the entire field's optimization techniques into three groups. Techniques that accelerate prefill include prefix caching (reusing KV cache values when prompts share opening segments) and prompt structure optimization (putting variable content late so shared prefixes cache effectively). Techniques that accelerate decode include speculative decoding (a smaller draft model proposes tokens, the main model verifies them in a single forward pass). Techniques that restructure the system around the split include batching (weaving multiple requests together for throughput at the cost of per-user latency) and disaggregation (running prefill and decode on entirely separate hardware).

Quantization helps both phases but with important nuances. A typical step down in precision yields 30-50% better performance, but different model components tolerate it differently. Linear weights handle compression well, but attention layers are the most sensitive because small precision errors compound across the token sequence—each token's calculation builds on previous ones, so errors snowball. Most production setups leave attention at full precision.

The build-versus-buy calculus has shifted. Off-the-shelf APIs remain right for early-stage products, but self-hosting becomes compelling when API costs grow, latency requirements outgrow vendor offerings, or reliability needs exceed typical 2-nines SLAs. Cursor's Composer 2.0 demonstrates that with sufficient inference engineering investment, self-hosted open models can beat closed APIs on latency for specific workloads—a pattern likely to repeat across the industry.