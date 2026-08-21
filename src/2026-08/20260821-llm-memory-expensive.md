# Why An LLM's Memory Gets Expensive and How to Fix It
**Source**: https://blog.bytebytego.com/p/why-an-llms-memory-gets-expensive
**Date**: 2026-08-04
**Author**: ByteByteGo
**Keywords**: kv-cache, llm, inference, gpu-memory, optimization

## Elevator pitch
The KV cache is the hidden cost driver behind long-context LLM inference — for a 70B model at 128K tokens, it consumes roughly 40GB of GPU memory — and understanding its mechanics is essential for optimizing serving costs.

## Takeaways
- The KV cache stores key and value vectors for every token processed, avoiding recomputation at each step, but grows linearly with sequence length and becomes the dominant memory cost at long contexts
- For a 70B-parameter model at 128K context, the KV cache alone requires ~40GB of GPU memory, exceeding the model weights themselves and limiting concurrent users per GPU
- Grouped-Query Attention (GQA) reduces KV cache size by sharing key-value heads across multiple query heads — Llama 3.1 uses 8 KV heads for 32 query heads, cutting cache memory by 4x
- Multi-Query Attention (MQA) is the extreme version where all query heads share a single KV head, maximizing cache savings but slightly reducing model quality
- PagedAttention (used in vLLM) solves memory fragmentation by managing KV cache in fixed-size pages rather than contiguous blocks, reducing waste from 60-80% to under 4% and enabling higher throughput

## Synthesis
ByteByteGo's deep dive into LLM memory costs is a masterclass in making infrastructure internals accessible. The article traces the cost problem from first principles: every attention step compares a new token against all prior tokens using key-value pairs, and caching those pairs eliminates redundant computation but creates a new bottleneck. The KV cache grows with context length and user count, and at long contexts it exceeds the model weights themselves.

The technical solutions are presented in order of adoption difficulty. GQA and MQA are model-architecture decisions made at training time — they reduce the number of KV heads and thus the cache size, but can't be retrofitted onto an already-trained model. PagedAttention is a systems-level optimization that can be applied to any model at serving time, and the article explains how it borrows the virtual memory paging concept from operating systems to manage KV cache blocks dynamically rather than pre-allocating contiguous memory.

The article also covers emerging approaches like KV cache compression (pruning unimportant tokens), quantization (storing cache entries in lower precision), and hybrid strategies that combine multiple techniques. The practical takeaway is that for anyone deploying LLMs at scale, the KV cache is the variable that determines how many users you can serve concurrently and at what cost — and the gap between naive and optimized serving can be 10x or more.