# Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention

**Source:** [Sebastian Raschka's AI Magazine](https://magazine.sebastianraschka.com/p/recent-developments-in-llm-architectures) — May 16, 2026  
**Author:** Sebastian Raschka, PhD

## TL;DR
Survey of recent open-weight LLM architectures (April–May 2026) focusing on long-context efficiency innovations: KV-cache sharing (Gemma 4), per-layer embeddings (Gemma 4 E-models), compressed convolutional attention (ZAYA1-8B), attention budgeting (Laguna XS.2), and multi-head compression + compressed attention (DeepSeek V4).

## Key Points

### 1. KV Sharing Across Layers (Gemma 4 E2B/E4B)
- Later transformer layers reuse key-value tensors from earlier layers instead of computing their own
- Reduces KV cache by ~50%: saves 2.7 GB at 128K context for E2B, ~6 GB for E4B
- Layers still compute their own query projections
- Cross-layer attention: sliding-window layers share with previous sliding-window; full-attention layers share with previous full-attention

### 2. Per-Layer Embeddings — PLE (Gemma 4 "E" models)
- "E" = effective parameters: E2B is 2.3B effective / 5.1B total; E4B is 4.5B effective / 8B total
- Per-layer embedding lookup outside the repeated transformer blocks
- Each block receives its own small token-specific embedding slice
- Parameter efficiency without increasing main transformer compute

### 3. Compressed Convolutional Attention (ZAYA1-8B)
- New attention variant combining convolutional patterns with compression for long-context efficiency

### 4. Attention Budgeting (Laguna XS.2)
- Layer-wise attention budget allocation — not all layers get full attention compute

### 5. mHC + Compressed Attention (DeepSeek V4)
- Multi-head compression combined with compressed attention mechanisms
- Continues the trend of KV-cache minimization for reasoning/agent workloads

## Broader Context
- Reasoning models and agent workflows keep more tokens around longer
- KV-cache size, memory traffic, and attention cost are now the primary bottlenecks
- Most recent attention variants (GQA, MQA, MLA, sliding window, sparse attention) are all designed to shrink the KV cache

## Relevance to Engineering-Forward
Architecture innovations directly impact what's economically feasible for long-context agent workflows. Understanding KV cache optimization is essential for anyone deploying LLMs in production agent pipelines.
