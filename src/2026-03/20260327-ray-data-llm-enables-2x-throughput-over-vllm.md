# Ray Data LLM enables 2x throughput over vLLM’s synchronous LLM engine at production-scale
**Source**: https://www.anyscale.com/blog/ray-data-llm-2x-throughput-vs-vllm
**Date**: Unknown
**Author**: Unknown
**Keywords**: Ray Data, batch inference, vLLM, throughput, asynchronous execution

## Elevator pitch
Anyscale presents Ray Data LLM, a batch‑inference stack that combines Ray Data with vLLM’s async engine to deliver higher throughput and better fault tolerance than synchronous LLM pipelines.

## Takeaways
- Ray Data LLM targets offline, throughput‑heavy LLM workloads (synthesis, curation, evaluation).
- Async execution at both batch and engine levels prevents long generations from stalling shorter ones.
- The system disaggregates tokenization, engine execution, and detokenization for resource control.
- Row‑level fault tolerance lets pipelines continue on per‑request failures.
- Benchmarks show ~2x throughput vs synchronous vLLM under mixed decode lengths.

## Synthesis
The post argues that most LLM infrastructure is optimized for interactive latency, while many production workloads—synthetic data generation, filtering, large‑scale evaluation—care about throughput and reliability. In this context, Anyscale introduces Ray Data LLM, a library built on Ray Data that orchestrates large‑scale batch inference with vLLM’s asynchronous engine.

The article first contrasts naive approaches. Running vLLM’s offline inference directly on a large dataset requires loading everything into CPU memory and offers no streaming or fault tolerance—untenable for production scale. A distributed alternative uses Ray Data with synchronous vLLM engines via map_batches. This improves scale and adds Ray’s resilience, but still suffers from a key limitation: synchronous decoding forces shorter requests to wait for longer ones, creating pipeline bubbles. It also lacks token‑level continuous batching, limiting GPU utilization.

Ray Data LLM addresses these bottlenecks by using vLLM’s async engine and by invoking map_batches asynchronously. This allows concurrent processing of variable‑length generations and enables continuous batching at the token level. The system further disaggregates tokenization, model execution, and detokenization, giving operators control over how CPU, GPU, and memory are allocated at each stage. This architecture is designed to maximize throughput while supporting streaming input datasets that exceed memory.

Operationally, Ray Data LLM emphasizes resilience. If an individual request fails—e.g., due to an oversized prompt—the pipeline does not crash. Instead, the error is captured at the row level and the job continues. The system also exposes row‑level latency metrics, improving observability and making it easier to diagnose slow or problematic requests. The design is modular, allowing teams to chain multiple prompt stages or models in a single Ray Data pipeline for complex data workflows.

Benchmark results show why async matters. Using a bimodal distribution of decode lengths (short non‑reasoning and long reasoning traces), the study finds that async execution increasingly outperforms synchronous pipelines as variance grows. The result is a reported 2x throughput advantage over synchronous vLLM at production scale. The argument is that async overlap removes synchronization barriers at both batch and request levels, so performance gains scale with request variability.

Overall, the post positions Ray Data LLM as an optimized system for large‑scale, offline LLM workloads where throughput, resiliency, and cost efficiency dominate. For teams running batch pipelines, the message is that async execution plus streaming data orchestration yields meaningful gains over synchronous inference stacks.
