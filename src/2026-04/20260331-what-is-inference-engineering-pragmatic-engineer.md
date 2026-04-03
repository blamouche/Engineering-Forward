# What is Inference Engineering? Deepdive
**Source**: https://newsletter.pragmaticengineer.com/p/what-is-inference-engineering
**Date**: March 31, 2026
**Author**: Gergely Orosz (featuring Philip Kiely)
**Keywords**: inference engineering, LLM serving, quantization, speculative decoding, KV cache, tensor parallelism, disaggregation, open-source models

## Elevator pitch
A detailed breakdown of inference engineering — the discipline of optimizing production LLM serving — covering quantization, speculative decoding, caching, parallelism, and disaggregation, and when teams should invest in it.

## Takeaways
- Inference engineering covers three layers: runtime optimization (single instance), infrastructure scaling (cluster/multi-cloud), and developer tooling
- Five core techniques: quantization (30-50% gains), speculative decoding, KV caching, tensor/expert parallelism, and prefill/decode disaggregation
- The shift toward open-source models democratizes inference engineering beyond frontier labs
- Autoscaling on Kubernetes is the baseline; high-scale deployments require multi-cloud strategies treating distributed GPUs as unified compute pools
- Investment is justified when product scaling creates performance constraints that off-the-shelf APIs cannot address cost-effectively

## Synthesis
Inference engineering has emerged as a distinct discipline precisely because the cost and latency profile of LLM serving at scale cannot be addressed through general-purpose software engineering practices. The Pragmatic Engineer's deep dive, co-authored with Philip Kiely, provides a structured framework for understanding what the field covers and when teams should invest in it.

The three-layer framing is analytically useful. Runtime optimization — improving how efficiently a single instance serves a model — is the foundational layer that affects everything else. Infrastructure scaling addresses how to distribute inference across multiple machines and data centers. Developer tooling creates the abstraction layer that allows teams to work efficiently without understanding all the complexity below. Most teams encounter these layers in order as they scale, and the deep dive describes the techniques relevant at each layer.

Among the five core optimization techniques, prefill/decode disaggregation is the least understood but increasingly important. The prefill phase (processing the input context) is computationally intensive; the decode phase (generating tokens one at a time) is memory-bandwidth limited. Running these phases on the same hardware creates a resource mismatch — neither phase can be optimally served. Disaggregation separates them onto dedicated hardware, allowing each to be tuned independently. This is particularly valuable for long-context workloads where the prefill cost would otherwise dominate.

The KV cache discussion deserves attention. The key-value cache stores intermediate computations from previous tokens, avoiding recomputation during generation. When multiple requests share common prefixes (system prompts, conversation history), cross-request caching can dramatically reduce compute requirements. As AI applications increasingly use long, repeated system prompts, the cost savings from effective KV cache sharing compound.

The democratization point is significant for the industry. Inference engineering was previously confined to frontier labs because the techniques are only worthwhile at scale, and only frontier labs were serving models at sufficient scale. Open-source model deployment has changed this calculus — any company running their own model serving now benefits from the same techniques, and the tools (vLLM, TensorRT-LLM, and others) have lowered the barrier to applying them.
