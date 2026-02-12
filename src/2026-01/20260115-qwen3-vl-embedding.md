# Qwen3-VL-Embedding

**Source**: https://qwen.ai/blog?id=qwen3-vl-embedding

**Date**: January 8, 2026

**Author**: Qwen Team (Alibaba)

**Keywords**: Qwen, Embedding, Multimodal, RAG, Vector Search, Reranker, Vision-Language, Information Retrieval

## Elevator pitch

Alibaba's Qwen team introduces Qwen3-VL-Embedding and Qwen3-VL-Reranker, state-of-the-art multimodal embedding models that process text, images, screenshots, and videos for retrieval and cross-modal understanding tasks.

## Takeaways

- Qwen3-VL-Embedding achieves state-of-the-art results on multimodal benchmarks with 77.8 overall score on MMEB-V2 and 70.58 on MMTEB
- The model suite supports over 30 languages, making it suitable for global applications
- Two-stage architecture combines an embedding model for initial recall with a reranker for precise relevance scoring
- Available in 2B and 8B parameter variants with support for quantization and flexible vector dimensions via Matryoshka Representation Learning
- Handles diverse inputs including text, images, screenshots, videos, and mixed modality content within a single model

## Synthesis

Alibaba's Qwen team has released Qwen3-VL-Embedding and Qwen3-VL-Reranker, marking a significant advancement in multimodal information retrieval. Built upon the recently open-sourced Qwen3-VL foundation model, this suite represents the cutting edge in cross-modal understanding and retrieval technology.

The architecture follows a two-stage retrieval paradigm that has become standard in modern search systems. The embedding model employs a dual-tower approach, mapping single-modal or mixed-modal inputs into high-dimensional semantic vectors. It extracts hidden states from the [EOS] token to generate final representations, enabling efficient large-scale retrieval operations. The complementary reranker uses a single-tower architecture with cross-attention mechanisms, performing pointwise relevance scoring through special token probability prediction.

What distinguishes this release is its comprehensive multimodal capability. Unlike previous embedding models that typically handle text or at most text-image pairs, Qwen3-VL-Embedding processes text, images, screenshots, and videos both individually and in combination. This opens up application scenarios including image-text retrieval, video search, multimodal RAG pipelines, visual question answering, and multimodal content clustering.

The benchmark results demonstrate state-of-the-art performance across multiple evaluation suites. On MMEB-V2, the 8B model achieves an overall score of 77.8, with particularly strong results on visual document tasks (82.4) and image tasks (80.1). Video task performance at 67.1 shows the model's capability in this emerging domain. On MMTEB, the model scores 70.58 overall with retrieval performance reaching 81.08. The reranker variant further improves these results, achieving 79.2 on MMEB-v2 retrieval tasks.

From a practical deployment perspective, the models offer several developer-friendly features. Configurable embedding dimensions through Matryoshka Representation Learning allow developers to trade off between vector size and quality based on their specific constraints. Task-specific instruction customization enables optimization for particular use cases. Quantization support makes deployment more cost-effective without significant performance degradation.

The two model sizes—2B with 28 layers and 2048 embedding dimension, and 8B with 36 layers and 4096 embedding dimension—provide flexibility for different compute budgets. Both support 32K sequence length, accommodating long documents and extended video content. The models integrate with popular frameworks including Hugging Face Transformers and vLLM, with flash attention optimization available for improved inference speed.

The multilingual support covering over 30 languages, inherited from the Qwen3-VL foundation, positions these models for global deployment scenarios. This comprehensive language coverage combined with multimodal capabilities makes Qwen3-VL-Embedding particularly valuable for international applications requiring cross-modal search and understanding across diverse content types.
