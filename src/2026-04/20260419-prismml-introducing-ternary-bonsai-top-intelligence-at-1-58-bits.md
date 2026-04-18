# PrismML — Introducing Ternary Bonsai: Top Intelligence at 1.58 Bits

**Source**: https://prismml.com/news/ternary-bonsai
**Date**: April 19, 2026
**Author**: Unknown
**Keywords**: prismml, introducing, ternary, bonsai, intelligence, bits

## Elevator pitch
Today, we’re announcing Ternary Bonsai, a new family of 1.58-bit language models designed to balance strict memory constraints with high accuracy requirements

## Takeaways
- Today, we’re announcing Ternary Bonsai, a new family of 1.58-bit language models designed to balance strict memory constraints with high accuracy requirements.
- This release builds on the efficiency frontier we began exploring with the recently released 1-bit Bonsai models.
- The 1-bit family showed that extreme compression could still produce commercially useful language models.
- Ternary Bonsai targets a different point on that curve: a modest increase in size for a meaningful gain in performance.
- The models are available in three sizes: 8B, 4B, and 1.7B parameters.

## Synthesis
Today, we’re announcing Ternary Bonsai, a new family of 1.58-bit language models designed to balance strict memory constraints with high accuracy requirements. This release builds on the efficiency frontier we began exploring with the recently released 1-bit Bonsai models. The 1-bit family showed that extreme compression could still produce commercially useful language models. Ternary Bonsai targets a different point on that curve: a modest increase in size for a meaningful gain in performance. The models are available in three sizes: 8B, 4B, and 1.7B parameters. By using ternary weights {-1, 0, +1}, these models achieve a memory footprint approximately 9x smaller than standard 16-bit models while outperforming most peers in their respective parameter classes on standard benchmarks. Ternary Bonsai implements 1.58-bit representation throughout the entire network architecture. There are no higher-precision escape hatches. Embeddings, attention layers, MLPs, and the LM head all use the same 1.58-bit representation. The models employ a group-wise quantization scheme in which each weight is constrained to one of three values: {-s, 0, +s}.
