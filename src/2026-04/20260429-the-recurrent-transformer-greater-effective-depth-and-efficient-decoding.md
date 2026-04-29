# The Recurrent Transformer: Greater Effective Depth and Efficient Decoding

**Source**: https://www.alphaxiv.org/abs/2604.21215
**Date**: April 29, 2026
**Author**: Unknown
**Keywords**: alphaxiv, arxiv, forum, discussion, explore, trending papers

## Elevator pitch
View recent discussion. Abstract: Transformers process tokens in parallel but are temporally shallow: at position $t$, each layer attends to key-value pairs computed based on the previous layer, yielding a depth capped by the number of layers. Recurrent models offer unbounded temporal depth but suff

## Takeaways
- The piece focuses on the recurrent transformer: greater effective depth and efficient decoding.
- It is sourced from www.alphaxiv.org.
- The article was processed automatically from the queued scan-list URL.
- The summary emphasizes the main claims visible in the fetched page content.
- Further manual review may be useful for edge cases such as paywalls or dynamic rendering.

## Synthesis
View recent discussion. Abstract: Transformers process tokens in parallel but are temporally shallow: at position $t$, each layer attends to key-value pairs computed based on the previous layer, yielding a depth capped by the number of layers. Recurrent models offer unbounded temporal depth but suffer from optimization instability and historically underutilize modern accelerators. We introduce the Recurrent Transformer, a simple architectural change where each layer attends to key-value pairs computed off its own activations, yielding layerwise recurrent memory while preserving standard autoregressive decoding cost. We show that the architecture can emulate both (i) a conventional Transformer and (ii) token-to-token recurrent updates under mild assumptions, while avoiding optimization instability. Naively, prefill/training appears bandwidth-bound with effective arithmetic intensity near $1$ because keys and values are revealed sequentially; we give an exact tiling-based algorithm that preserves the mathematical computation while reducing HBM traffic from $\Theta(N^2)$ to $\Theta(N\log N)$, increasing effective arithmetic intensity to $\Theta(N/\log N)$ for sequence length $N$. On 150M and 300M parameter C4 pretraining, Recurrent Transformers improve cross-entropy over a parameter-matched Transformer baseline and achieve the improvement with fewer layers (fixed parameters), suggesting that recurrence can trade depth for width, thus reducing KV cache memory footprint and inference latency.
