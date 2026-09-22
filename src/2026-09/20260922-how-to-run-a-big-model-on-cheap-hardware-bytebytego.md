# How to Run a Big Model on Cheap Hardware?
**Source**: ByteByteGo (bytebytego@substack.com) — https://blog.bytebytego.com/p/how-to-run-a-big-model-on-cheap-hardware
**Date**: 2026-09-21
**Author**: ByteByteGo
**Keywords**: LLM inference, quantization, layer-wise offloading, mixture of experts, distillation, pruning, speculative decoding, KV cache, FlashAttention, PagedAttention, vLLM, local AI

## Elevator pitch
A comprehensive technical guide to running large AI models on modest hardware through six complementary techniques: quantization, layer-wise offloading, mixture of experts, distillation, pruning, and speculative decoding — plus the software improvements (FlashAttention, PagedAttention) that make the same hardware go further.

## Takeaways
- **Quantization is the highest-impact first step**: Reducing 16-bit weights to 4-bit cuts an 8B model from 16 GB to 4 GB of raw weight storage — the parameter count stays the same but each weight occupies less memory, at the cost of potential quality degradation.
- **Layer-wise offloading trades speed for capacity**: Keeping most weights in RAM and transferring layers to GPU only as needed lets you run models that exceed VRAM, but repeated transfers can make generation too slow for interactive use.
- **Mixture of Experts reduces compute but not storage**: MoE models use only a subset of experts per token, reducing computation, but all experts still need to be stored — so a 40B parameter MoE still needs ~20 GB at 4-bit precision.
- **The KV cache is a hidden memory bottleneck**: The model file stays the same size, but as conversations get longer or serve more users, the KV cache grows — requiring cache quantization, context reduction, or offloading to manage.
- **Software runtimes matter as much as hardware**: FlashAttention reduces memory traffic without changing weights; PagedAttention (vLLM) manages KV cache in blocks to reduce waste; batching improves throughput but requires more working memory per simultaneous request.
- **Speculative decoding accelerates after memory is solved**: A small draft model proposes tokens that the larger target model verifies in batch — but the target still needs to fit in memory first, so this is an optimization to apply after basic memory constraints are addressed.

## Synthesis
ByteByteGo's article is the clearest engineering reference for the question every developer building local AI faces: "I downloaded the model, but it doesn't fit in my memory." The article walks through the full stack of techniques, from weight compression to architecture choices to runtime optimizations, with a rigor that makes it useful as a decision tree rather than a listicle.

The central insight is that these techniques don't simply multiply — they affect different parts of the workload. Quantization reduces weight storage. Offloading changes where weights reside. MoE changes computation per token. Distillation produces a different, smaller model. Pruning removes work. Speculative decoding changes the generation pattern. Software runtimes like FlashAttention and PagedAttention improve execution efficiency without touching weights at all. Understanding which bottleneck you face — weight storage, computation, memory bandwidth, KV cache growth — determines which technique to apply.

The article's practical example is instructive: a system with 32 GB RAM and 8 GB VRAM. An 8B model at 4-bit quantization needs only 4 GB of weight storage, leaving room for a compatible runtime, moderate context, and one active request. If memory remains insufficient, offloading some layers or cache data can help — but if transfers make generation too slow, a smaller model may deliver a better experience. The evaluation process should measure answer quality, peak memory use, time to first token, and generation speed, because background document processing can tolerate delays that would frustrate interactive code suggestions.

The most important conceptual point is the distinction between training and inference. Training requires expensive infrastructure because it updates weights through backpropagation — a computation-intensive process. Inference (using a trained model) only reads weights forward, which is why a model trained on expensive infrastructure can sometimes run on an ordinary computer. This asymmetry is the foundation of the entire local AI movement: the expensive part happens once (at the lab), and the cheap part can happen millions of times (at the edge).

The article also surfaces a tension in the local AI ecosystem: quantization introduces quality degradation that's task-dependent. A configuration that handles ordinary conversation well may perform less reliably on coding problems. Lower precision doesn't guarantee proportional speed improvement — some implementations store 4-bit weights while performing calculations at higher precision. The gap between theoretical savings and real-world performance depends on hardware support and software handling of conversions. This means the only reliable evaluation is empirical: try the quantized model on your actual workload and measure.