# Lighthouse Attention: ~17× Faster Forward+Backward at 512K Context

**Source:** [Nous Research](https://nousresearch.com/lighthouse-attention) — May 2026  
**Paper:** [arXiv 2605.06554](https://arxiv.org/abs/2605.06554)  
**Code:** [GitHub](https://github.com/ighoshsubho/lighthouse-attention)

## TL;DR
A selection-based hierarchical attention mechanism that runs ~17× faster than standard attention at 512K context on a single B200, delivering 1.4–1.7× end-to-end pretraining speedup at 98K context. Symmetric Q/K/V pooling across a multi-resolution pyramid, with parameter-free ℓ₂-norm scoring and selection outside the attention kernel — no custom sparse kernel needed.

## Key Design Decisions

### 1. Symmetric Pooling
- Q, K, V all pooled by the same factor at every level of the hierarchy
- This enables the dense-attention call to drop from O(N·S·d) to O(S²·d)
- Contrasts with prior work (NSA, HISA, etc.) that kept queries at full resolution

### 2. Parameter-Free Scoring
- Per-head ℓ₂ norms of Q and K projections used as scores
- No learned scorer head, no auxiliary loss, no Gumbel-softmax, no straight-through estimator
- Dilated softmax-attention scorer is a strictly stronger signal — results are a lower bound

### 3. Selection Outside the Kernel
- Top-K selected entries gathered into contiguous, causally-sorted dense sub-sequence
- FlashAttention runs on this dense sub-sequence — no custom sparse attention kernel
- Forward/backward bit-for-bit identical to dense Transformer's

## The Four Stages
1. **Pyramid Pool** — average-pool Q/K/V into L-level pyramid (pooling factor p)
2. **Top-K Cascade** — coarse-to-fine selection via ℓ₂ norms; rejected coarse entries kept for causal continuity
3. **FlashAttention** — on gathered dense sub-sequence of length S
4. **Scatter-Back** — output scattered back to base positions

## Training Recipe: Two-Stage
- **Stage 1 (Lighthouse)**: train with selection enabled
- **Stage 2 (SDPA-resume)**: resume with selection disabled → brief tail under standard attention
- Every recovered run matches or beats dense-from-scratch at the same token budget

## Key Results (530M Llama-3, 16K steps, 50B tokens)
- Final loss: 0.698–0.710 vs 0.724 (dense baseline)
- 75–106 B200-hours saved (1.40–1.69× speedup)
- Stage-1 throughput: 84–126K tokens/s/GPU vs ~46K for dense SDPA
- Pyramid hyperparameters forgiving: L∈{3,4,5}, p∈{2,4,8} all within ~0.02 nats

## Context Parallelism
- 1M-token training across 32 B200s (4 nodes, CP degree 8)
- No changes to inner attention kernel — selection output is a contiguous tensor

## Limitations
- Symmetric Q/K/V pooling presumes all queries co-occur (violated by autoregressive decoding)

## Relevance to Engineering-Forward
Lighthouse Attention is a significant advance for long-context pretraining economics. The "train sparse, resume dense" paradigm and kernel-agnostic design make it directly applicable to production training pipelines.
