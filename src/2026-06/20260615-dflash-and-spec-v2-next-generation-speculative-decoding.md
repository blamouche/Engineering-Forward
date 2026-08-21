# DFlash and Spec V2: Next-Generation Speculative Decoding for LLM Inference
**Source**: https://www.lmsys.org/blog/2026-06-15-next-generation-speculative-decoding-dflash-v2/
**Date**: 2026-06-15
**Author**: Z Lab, Modal, and SGLang Teams
**Keywords**: DFlash, speculative decoding, SGLang, Spec V2, KV injection, block diffusion, LLM inference, Qwen 3.5, Modal, Z Lab, throughput, latency

## Elevator pitch
Z Lab, Modal, and SGLang jointly released DFlash—a speculative decoding technique using block diffusion with KV injection that achieves >4.3x throughput over baseline and 1.5x over native MTP for Qwen 3.5 397B-A17B, now available as the default Spec V2 engine in SGLang.

## Takeaways
- DFlash uses a block diffusion draft model to generate an entire block of tokens in parallel (single forward pass), unlike sequential autoregressive drafters like EAGLE-3
- KV injection directly inserts target model hidden representations into the draft model's KV cache, achieving higher acceptance lengths than EAGLE-3's input-only feature approach
- For Qwen 3.5 397B-A17B on HumanEval at concurrency 1: >4.3x baseline throughput and 1.5x over native MTP speculation
- Spec V2's overlap scheduler reduces host-device synchronization, improving performance by over 33% (from ~11.4 to ~15.3 ktok/s for Qwen 3-8B on a single B200)
- DFlash draft models are now available on Hugging Face for Qwen 3.5 397B-A17B, and Xiaomi's MiMo v2.5-Pro-UltraSpeed already uses DFlash to achieve over 1k output tps

## Synthesis
This collaboration between Z Lab, Modal, and SGLang represents a meaningful advance in speculative decoding, the technique that accelerates LLM inference by using a smaller draft model to propose tokens that are verified in parallel by the target model. The innovation addresses two bottlenecks simultaneously: draft generation speed and token acceptance quality.

DFlash's first innovation is block diffusion drafting. Traditional speculative decoding methods like EAGLE-3 generate draft tokens one by one—the same sequential autoregression that makes LLM inference slow, just in a smaller model. DFlash instead generates an entire block of tokens in a single forward pass using a diffusion-based draft model. This is far more hardware-friendly: a 5-layer DFlash drafter generating 16 tokens has lower latency than a single-layer EAGLE-3 producing 4 tokens. The ablation studies show that even at lower acceptance lengths, DFlash's faster drafting delivers higher end-to-end speedup.

The second innovation is KV injection. EAGLE-3 uses target model features only at the input of the draft model, and this signal fades in deeper draft models. DFlash instead injects target features into the KV cache of every draft layer, keeping the drafter strongly conditioned on the target's context throughout generation. This allows deeper, higher-quality drafters. The ablation shows DFlash in autoregressive mode (without diffusion) still outperforms EAGLE-3 due to higher acceptance lengths.

The SGLang integration story is equally important. The V2 speculative decoding engine's overlap scheduler eliminates host-device synchronization points—specifically overlapping host-side cleanup after batch N-1 with GPU work on batch N, and overlapping host KV allocation for batch N with GPU work on batch N-1. This delivered a 33% performance improvement on top of DFlash's own gains.

The practical impact is significant: the released DFlash model for Qwen 3.5 397B-A17B outperforms the model's native MTP speculation across all tested settings (GSM8K, HumanEval, MT-Bench) and concurrencies (1 to 32). Xiaomi's adoption for achieving 1k+ output tps in production validates the technique beyond benchmarks. The model is released in triplicate across Z Lab, Modal, and LMSYS Hugging Face organizations, and the training approach can be applied to most target LLMs.