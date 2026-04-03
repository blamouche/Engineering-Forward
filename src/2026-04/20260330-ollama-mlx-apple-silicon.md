# Ollama is now powered by MLX on Apple Silicon in preview
**Source**: https://ollama.com/blog/mlx
**Date**: March 30, 2026
**Author**: Ollama Team
**Keywords**: Ollama, MLX, Apple Silicon, local inference, LLM, performance

## Elevator pitch
Ollama integrates Apple's MLX framework to nearly double inference performance on Apple Silicon, with prefill speeds increasing to 1,810 tokens/s and decode speeds doubling to 112 tokens/s on M5 chips.

## Takeaways
- MLX integration delivers dramatic performance gains: prefill up from 1,154 to 1,810 tokens/s, decode nearly doubled from 58 to 112 tokens/s using Qwen3.5-35B-A3B
- Requires Apple M5, M5 Pro, or M5 Max with 32GB+ unified memory
- NVFP4 quantization support maintains model accuracy while reducing memory bandwidth requirements
- Three new caching improvements target agentic and coding applications with lower memory utilization and smarter eviction policies
- The update positions Ollama as a bridge between sophisticated AI capabilities and accessible local execution on consumer hardware

## Synthesis
Ollama has announced a major performance upgrade for Apple Silicon devices through integration with MLX, Apple's machine learning framework. This development represents a significant step toward enabling sophisticated AI applications on consumer-grade Mac hardware.

The announcement emphasizes dramatic performance gains across Apple Silicon devices. Testing data demonstrates substantial improvements: prefill performance increased from 1,154 to 1,810 tokens per second, while decode performance nearly doubled from 58 to 112 tokens per second. These metrics were measured using Alibaba's Qwen3.5-35B-A3B model with NVFP4 quantization. The integration specifically targets Apple's M5, M5 Pro, and M5 Max chips, leveraging their new GPU Neural Accelerators.

The core technical advancement involves MLX's unified memory architecture, which enables more efficient resource utilization. This architecture appears particularly suited for local inference tasks where latency and memory efficiency are critical. The framework allows Ollama to maximize the capabilities of Apple's integrated GPU and neural processing hardware without requiring external accelerators.

A notable innovation is NVFP4 support, which maintains model accuracy while reducing memory bandwidth and storage requirements. This approach aligns Ollama's performance characteristics with production environments that use similar quantization schemes, addressing a practical gap in local AI development.

The update introduces three caching improvements designed for agentic and coding applications. Lower memory utilization is achieved through cache reuse across conversations. Intelligent checkpoints store cache snapshots at strategic prompt locations, reducing redundant processing. Smarter eviction policies preserve shared prefixes longer, benefiting multi-turn conversations. These optimizations specifically target use cases like Claude Code and other AI coding assistants.

The preview centers on the Qwen3.5-35B-A3B model with parameters tuned for coding tasks, suggesting a deliberate focus on productivity-oriented AI applications rather than general-purpose use. Plans to expand model support and introduce streamlined processes for importing custom fine-tuned models indicate the framework's evolution will remain platform-flexible.

This development democratizes access to capable language models on consumer hardware, reducing reliance on cloud-based inference. The partnership approach acknowledging contributions from MLX, NVIDIA, GGML/llama.cpp, and Alibaba teams reflects the collaborative nature of open-source ML infrastructure development. For developers and researchers, this represents a meaningful step toward practical on-device AI without compromising performance.
