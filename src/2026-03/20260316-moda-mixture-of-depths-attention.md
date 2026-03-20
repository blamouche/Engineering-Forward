# MoDA: Mixture-of-Depths Attention
**Source**: https://github.com/hustvl/MoDA
**Date**: 2026-03-16
**Author**: Lianghui Zhu et al. (HUST & ByteDance Seed)
**Keywords**: attention mechanism, transformer, MoDA, FlashAttention, LLM efficiency, depth attention, hardware-aware

## Elevator pitch
MoDA (Mixture-of-Depths Attention) improves deep transformer models by allowing each attention head to reference historical depth key-value pairs from preceding layers, achieving 97.3% of FlashAttention-2's efficiency with measurable perplexity and task performance gains.

## Takeaways
- Each attention head processes both current-layer and historical depth key-value pairs from preceding layers, addressing signal degradation in deep models
- Achieves 97.3% of FlashAttention-2's efficiency at 64K sequence length—near-zero performance overhead
- On 1.5B-parameter models: 0.2 average perplexity improvement, 2.11% average performance gain across 10 downstream tasks
- Only 3.7% additional computational overhead compared to standard attention
- Hardware-efficient through optimized memory access patterns and chunk-aware KV cache organization

## Synthesis
MoDA addresses a well-known problem in deep transformer models: signal degradation as information passes through many sequential layers. In standard attention, each layer's attention heads can only reference the current layer's representations. Important signals identified in earlier layers may become diluted or lost as they propagate through deeper layers, limiting the model's ability to maintain coherent long-range dependencies across the full network depth.

The MoDA solution is conceptually elegant. By allowing each attention head to attend not only to the current layer's key-value pairs but also to cached key-value pairs from preceding layers, the model creates direct cross-layer connections that bypass the sequential signal degradation problem. Earlier layers' representations remain directly accessible to later layers through these depth attention connections, allowing the model to reference earlier processing without relying solely on residual stream propagation.

The hardware efficiency achievement is the most technically impressive aspect. Naively implementing cross-layer attention would introduce substantial computational overhead, as maintaining and accessing historical KV caches adds memory bandwidth requirements. The research team's contribution is an implementation that achieves 97.3% of FlashAttention-2's efficiency at 64K sequence lengths through careful optimization of memory access patterns and chunk-aware organization of depth KV caches. The 3.7% overhead is negligible in practice.

The performance gains—0.2 perplexity improvement and 2.11% average task performance increase on 1.5B-parameter models—are modest in absolute terms but meaningful relative to the computational cost. Techniques that improve model quality without proportional increases in parameters or training compute are particularly valuable because they can be applied to any model size. For production deployments where compute efficiency directly translates to operational cost, a technique that improves quality at near-zero overhead represents genuine engineering value.
