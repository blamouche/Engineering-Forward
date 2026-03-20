# IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse
**Source**: https://github.com/THUDM/IndexCache
**Date**: 2026-03-20
**Author**: Yushi Bai et al. (Tsinghua University & Z.AI)
**Keywords**: sparse attention, IndexCache, DeepSeek, prefill optimization, LLM inference, SGLang, vLLM, performance

## Elevator pitch
IndexCache eliminates up to 75% of redundant token-selection computations in sparse attention by caching and reusing indices across adjacent transformer layers that share 70-100% of selected tokens, achieving 1.82x prefill speedup at 200K context.

## Takeaways
- Lightning indexer in DeepSeek Sparse Attention consumes up to 81% of prefill time at 200K context—IndexCache targets this bottleneck directly
- Adjacent transformer layers share 70-100% of selected token indices, making most independent index computation redundant
- Full (F) layers compute their own indices; Shared (S) layers reuse cached indices from nearest F layer—reducing indexer computations by ~75%
- Performance: 1.82x prefill speedup, 1.48x decode speedup, 1.2x end-to-end speedup on GLM-5 (744B)—with negligible quality degradation
- Integrates with SGLang and vLLM via simple configuration; zero additional GPU memory required

## Synthesis
IndexCache identifies and exploits a structural redundancy in sparse attention systems that—once seen—is difficult to unsee. When a transformer layer selects the top-k most relevant tokens for attention, adjacent layers are independently doing this same selection. If two adjacent layers end up selecting nearly identical token sets (which empirical analysis shows happens 70-100% of the time), the second layer's selection computation produces almost exactly the same result as the first, wasting substantial compute.

The IndexCache solution is elegantly simple: partition layers into Full (F) layers that compute their own indices and Shared (S) layers that simply reuse the cached indices from the nearest Full layer. This reduces total indexer computations by approximately 75%. The remaining 25% (the F layers) are distributed to provide a regular quality check that ensures the cached indices don't drift too far from optimal.

The performance numbers are notable. At 200K context lengths—where the lightning indexer bottleneck is most severe—IndexCache achieves 1.82x prefill speedup. This is a dramatic improvement in exactly the scenario where long-context applications most need it. Decode speedup (1.48x) is also significant. The 1.2x end-to-end speedup on the full 744B GLM-5 model reflects that inference involves more than just the indexer, but even this modest end-to-end improvement represents meaningful cost reduction at production scale.

The integration approach is notable for its pragmatism. Rather than requiring architectural changes to deployed models, IndexCache integrates with existing SGLang and vLLM inference frameworks through simple configuration parameters. Zero additional GPU memory is required—the cached indices replace computation without adding memory pressure. For production teams already using DeepSeek-style sparse attention, this is a configuration change rather than an infrastructure overhaul.

The quality preservation is the critical finding. Sparse attention techniques that improve speed at the cost of accuracy are rarely deployed in production. IndexCache's negligible quality degradation—resulting from the F layers periodically refreshing the cache—makes it a candidate for deployment without model retraining or evaluation overhead.
