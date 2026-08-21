# How ChatGPT Optimizes its Agent Loop: Harness, API, and Inference
**Source**: https://blog.bytebytego.com/p/how-chatgpt-optimizes-its-agent-loop
**Date**: 2026-07-29
**Author**: ByteByteGo
**Keywords**: openai, chatgpt, agent-loop, optimization, harness, inference, kv-cache, speculative-decoding

## Elevator pitch
OpenAI shared detailed engineering techniques for making AI agent loops more efficient across three layers: harness, API, and inference—revealing how persistent WebSockets, delta tokenization, and GPU-level optimizations dramatically reduce cost per successful task.

## Takeaways
- AI agent applications like Codex and ChatGPT Work are multi-layered systems; queries don't go directly to the LLM but pass through harness, API, and inference layers each with optimization opportunities
- The harness layer cuts repeated work through persistent WebSockets, stable prompt prefixes, deferred tool discovery, and a "Code Mode" that avoids sending full file contents on every turn
- The API layer tokenizes only the delta (new tokens since last request), runs safety checks in parallel with inference, and uses cache-aware routing to reuse KV cache across turns
- The inference layer employs speculative decoding, KV cache management, and separating prefill from decode to maximize GPU utilization and reduce latency
- GPT-5.6 Sol with max reasoning scores higher than Fable 5 on coding benchmarks while costing less than half as much—efficiency gains compound across all three layers

## Synthesis
OpenAI's engineering team lifted the curtain on the infrastructure behind Codex and ChatGPT Work, revealing a three-layer optimization architecture that most AI agent builders are not yet implementing. The article is notable for its specificity: real production techniques from a frontier lab, shared with enough detail to be actionable.

The **harness layer** is the outermost shell, managing the conversation between user and agent. Its key optimizations include persistent WebSocket connections that eliminate HTTP handshake overhead on every turn, stable prompt prefixes that can be cached server-side so only the delta needs processing, and deferred tool discovery that avoids sending tool schemas until they're actually needed. Code Mode is particularly clever: instead of re-sending entire file contents on every turn, the harness sends only diffs, dramatically reducing token counts for code-editing tasks.

The **API layer** sits between the harness and the inference engine. Its standout technique is delta tokenization—only tokenizing new tokens added since the last request rather than re-tokenizing the entire conversation. Safety checks run in parallel with inference rather than sequentially, reducing end-to-end latency. Cache-aware routing directs requests to GPU nodes that already have relevant KV cache in memory, maximizing cache hit rates.

The **inference layer** is where the most hardware-level optimizations live. Speculative decoding uses a smaller, faster model to draft tokens that the larger model then verifies in parallel, effectively trading compute for latency. Separating the prefill phase (processing the prompt) from the decode phase (generating tokens) allows different GPU allocations for each. KV cache management ensures that context from earlier turns stays warm in GPU memory.

The article's broader point is that the cost per successful task—not just raw model capability—is the metric that matters for AI products. Every layer of the stack offers compounding efficiency gains, and frontier labs are investing heavily in these optimizations. Teams building AI agents who ignore these techniques will find themselves at a significant cost disadvantage, regardless of which model they use.