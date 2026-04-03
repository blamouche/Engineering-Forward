# Ollama is now powered by MLX on Apple Silicon in preview
**Source**: https://ollama.com/blog/mlx
**Date**: March 30, 2026
**Author**: Unknown
**Keywords**: MLX, Apple Silicon, Ollama, machine learning framework, inference optimization, NVFP4, unified memory, macOS

## Elevator pitch
Ollama integrates Apple's MLX framework to deliver dramatically faster LLM inference on Apple Silicon, achieving 1810 tokens/s prefill and 112 tokens/s decode on M5 hardware.

## Takeaways
- Ollama integrates Apple's MLX machine learning framework in a preview release for Apple Silicon devices
- Achieves 1810 tokens/s prefill and 112 tokens/s decode on M5, M5 Pro, and M5 Max chips
- Adds NVFP4 quantization support to reduce memory demands while maintaining accuracy
- Enhanced caching with cross-conversation reuse, checkpoint snapshots, and smarter eviction strategies
- Requires Macs with 32GB+ unified memory; integrates with Claude Code and other developer tools

## Synthesis
Ollama's MLX integration represents a significant shift in the local AI inference story for Apple Silicon users. Apple's MLX framework is designed specifically for the unified memory architecture of M-series chips, where CPU and GPU share a single memory pool — a hardware advantage that conventional inference frameworks optimized for discrete GPU memory hierarchies cannot fully exploit. By adopting MLX as its execution backend, Ollama can leverage this architecture more effectively than previous implementations.

The performance numbers are concrete and meaningful for developer use cases. A 1810 tokens/s prefill rate means that loading context into memory — the bottleneck for long-context operations — is dramatically faster. The 112 tokens/s decode rate for generation is competitive with dedicated GPU inference on lower-tier cloud hardware. For developers running models locally on Apple Silicon, these numbers change the practical calculus: tasks that previously required cloud API calls due to latency constraints may now be viable locally.

The NVFP4 quantization support is notable because it adopts a precision format that was originally developed in NVIDIA's ecosystem. The inclusion signals a pragmatic approach to model format compatibility — rather than requiring Apple-specific quantization formats, Ollama is meeting developers where models are already being distributed.

The caching improvements deserve attention. Cross-conversation cache reuse reduces the cost of repeated context loading, which matters for users who run multiple related queries in sequence. The checkpoint snapshot approach — storing intermediate computation states — allows the system to avoid recomputing when returning to a conversation after other operations. Combined, these caching strategies mean that the performance benefits compound in realistic usage patterns, not just in isolated benchmark scenarios.

The integration with Claude Code and Claude tools is strategically significant: developers using AI-assisted workflows who are already running Ollama for local models can now use it as a faster execution backend without changing their toolchain. The Qwen3.5-35B-A3B optimization for coding also shows that the team is prioritizing the developer use case specifically, recognizing that developers running local models for code completion and generation represent a key segment of Ollama's user base.

The 32GB+ memory requirement reflects the reality that running large, capable models locally still demands substantial hardware. This positions the MLX integration as a tool for developers with well-equipped machines, rather than a solution for commodity hardware.
