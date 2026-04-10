# Multimodal Embedding & Reranker Models with Sentence Transformers

**Source**: https://huggingface.co/blog/multimodal-sentence-transformers
**Date**: Unknown
**Author**: Unknown
**Keywords**: embedding, models, multimodal, reranker, images, audio

## Elevator pitch
Sentence Transformers is a Python library for using and training embedding and reranker models for applications like retrieval augmented generation, semantic search, and more.

## Takeaways
- With the v5.4 update, you can now encode and compare texts, images, audio, and videos using the same familiar API.
- In this blogpost, I'll show you how to use these new multimodal capabilities for both embedding and reranking.
- Multimodal embedding models map inputs from different modalities into a shared embedding space, while multimodal reranker models score the relevance of mixed-modality pairs.
- This opens up use cases like visual document retrieval, cross-modal search, and multimodal RAG pipelines.
- Multimodal embedding models extend this by mapping inputs from different modalities (text, images, audio, or video) into a shared embedding space.

## Synthesis
Sentence Transformers is a Python library for using and training embedding and reranker models for applications like retrieval augmented generation, semantic search, and more. With the v5.4 update, you can now encode and compare texts, images, audio, and videos using the same familiar API. In this blogpost, I'll show you how to use these new multimodal capabilities for both embedding and reranking. Multimodal embedding models map inputs from different modalities into a shared embedding space, while multimodal reranker models score the relevance of mixed-modality pairs. This opens up use cases like visual document retrieval, cross-modal search, and multimodal RAG pipelines. Multimodal embedding models extend this by mapping inputs from different modalities (text, images, audio, or video) into a shared embedding space. This means you can compare a text query against image documents (or vice versa) using the same similarity functions you're already familiar with. Similarly, traditional reranker (Cross Encoder) models compute relevance scores between pairs of texts.
