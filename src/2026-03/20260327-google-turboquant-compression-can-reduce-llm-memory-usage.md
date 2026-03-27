# Google’s TurboQuant compression can reduce LLM memory usage by 6x
**Source**: https://arstechnica.com/ai/2026/03/google-says-new-turboquant-compression-can-lower-ai-memory-usage-without-sacrificing-quality/
**Date**: Unknown
**Author**: Ryan Whitwam
**Keywords**: quantization, KV cache, compression, efficiency, TurboQuant

## Elevator pitch
Ars Technica explains Google’s TurboQuant, a two‑stage quantization method that shrinks KV cache memory up to 6× and speeds attention without accuracy loss.

## Takeaways
- TurboQuant targets KV‑cache memory as a major LLM bottleneck.
- PolarQuant converts vectors to polar coordinates for compact storage.
- QJL adds 1‑bit error correction to preserve attention accuracy.
- Google reports 6× KV‑memory reduction and ~8× attention speedups.
- Works without retraining; can apply to existing models.

## Synthesis
The article summarizes Google Research’s TurboQuant as a compression technique that makes LLM inference cheaper by shrinking the key‑value cache. The KV cache stores intermediate vectors that let models maintain context, but it grows fast and consumes memory. TurboQuant aims to compress these vectors with minimal quality loss.

The method uses two steps. PolarQuant converts vector representations from Cartesian to polar coordinates, making them easier to compress while avoiding expensive normalization. That introduces residual errors, so Google adds Quantized Johnson‑Lindenstrauss (QJL), a 1‑bit correction layer that preserves distances and yields more accurate attention scores.

Google’s reported results show up to 6× memory reduction and 8× attention speedups on H100 GPUs with no degradation on long‑context benchmarks for Gemma and Mistral. The approach can quantize KV caches to 3‑bit precision without retraining, which makes it attractive for applying to existing models.

The piece notes the broader implication: cheaper inference could either lower costs or enable larger models on the same hardware. On constrained devices like phones, the compression could be especially useful, potentially bringing higher‑quality local inference without cloud offloading.
