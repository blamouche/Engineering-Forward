# Introducing the Ettin Reranker Family
**Source**: https://huggingface.co/blog/ettin-reranker
**Date**: May 19, 2026
**Author**: Tom Aarsen
**Keywords**: Ettin, reranker, cross-encoder, Sentence Transformers, ModernBERT, retrieval, MTEB, distillation

## Elevator pitch
Tom Aarsen releases six new Sentence Transformers cross-encoder rerankers built on JHU's Ettin ModernBERT encoders, spanning 17M to 1B parameters, all state-of-the-art at their size with full training recipes and data open-sourced.

## Takeaways
- Six model sizes (17M, 32M, 68M, 150M, 400M, 1B parameters) covering the full quality-speed spectrum, all supporting up to 8K context tokens via ModernBERT's long-context pretraining.
- Distillation recipe uses pointwise MSE on mixedbread-ai/mxbai-rerank-large-v2 scores, trained on a curated subset of LightOn's embedding datasets — all open-source.
- When paired with embedding models, the 1B reranker achieves the highest average NDCG@10 across MTEB(eng, v2) Retrieval tasks, with even the 17M model providing meaningful gains over retriever-only baselines.
- Using Flash Attention 2 with sequence unpadding achieves 1.7x-8.3x speedup over default fp32+SDPA loading, making larger models viable in production pipelines.
- The author used the new train-sentence-transformers Agent Skill with an AI coding agent to bootstrap the training recipe — the models themselves were partially built by AI-assisted workflows.
- All models are Apache 2.0 licensed and work with 3 lines of Python via Sentence Transformers' CrossEncoder API, with a full retrieve-then-rerank example provided.

## Synthesis
The Ettin Reranker family is a textbook example of what makes the open-source AI ecosystem valuable: someone takes a strong open foundation model (Ettin encoders), applies a well-documented distillation recipe on publicly available datasets, and releases the full training pipeline — weights, data, code, and evaluation — so anyone can reproduce, fine-tune, or improve the results.

The technical insight is in the architecture. Cross-encoders (rerankers) are inherently more accurate than bi-encoders (embedders) for relevance scoring because they let query and document attend to each other through every transformer layer. But they're also more expensive: you can't pre-compute document embeddings. The production answer is retrieve-then-rerank: a fast embedder retrieves top-K candidates, then a cross-encoder re-orders them with high accuracy. The Ettin family covers this pipeline at every budget point, from 17M parameters (negligible latency) to 1B (maximum quality).

A surprising empirical finding: CLS pooling outperformed mean pooling, despite ModernBERT using global attention only every third layer. The residual global attention layers apparently carry enough signal to make CLS the better choice, which isn't obvious from the architecture alone.

The meta-story is also noteworthy: Aarsen used the new train-sentence-transformers Agent Skill with an AI coding agent to bootstrap the training recipe. The fact that state-of-the-art reranker models were trained with AI assistance — and that the training pipeline itself is now reproducible by anyone with an AI coding agent — suggests we're entering a phase where model training workflows are themselves AI-augmented, further accelerating the open-source flywheel.
