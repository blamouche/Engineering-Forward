# Biohub Releases a World Model of Protein Biology
**Source**: https://biohub.org/news/world-model-of-protein-biology
**Date**: 2026-05-28
**Author**: Biohub
**Keywords**: biohub, protein-biology, esmc, esmfold2, esm-atlas, protein-design, ai-science, open-source

## Elevator pitch
Biohub has released an open discovery engine for protein biology — ESMC, ESMFold2, and ESM Atlas — that lets researchers predict protein structures, design new protein binders against cancer targets in days instead of months, and navigate 6.8 billion protein sequences, all freely available to the global scientific community.

## Takeaways
- ESMC is a state-of-the-art language model trained on roughly 2.8 billion protein sequences that has internalized the fundamental properties governing protein biology
- ESMFold2 is a structure prediction and design engine that transforms ESMC's representations into atomically-resolved 3D models of biomolecular complexes, outperforming AlphaFold 3 on antibody-antigen binding prediction
- ESM Atlas makes ESMC's representations navigable across 6.8 billion protein sequences and 1.1 billion predicted structures
- Researchers used ESMFold2 to design protein binders against five targets central to cancer and immunology — a computational search completed in days rather than months or years
- Lab-validated binders exhibited high affinity, specificity, and stability — properties critical for clinical utility
- All three models are freely available to the global scientific community, making this an open-source contribution to drug discovery and biological research

## Synthesis
Biohub's release of a world model of protein biology marks a significant moment for AI-driven science, combining three interconnected tools into an open discovery engine available to researchers worldwide. ESMC, trained on approximately 2.8 billion protein sequences, has learned the biological rules that govern how proteins are built, fold, and function — serving as a foundation model for protein biology. ESMFold2 translates ESMC's sequence representations into atomically-resolved 3D structures of biomolecular complexes, achieving state-of-the-art accuracy in predicting protein-protein and antibody-antigen interactions.

The practical validation is striking. In experiments described in a preprint, researchers used ESMFold2 to design protein binders against five targets central to cancer and immunology. The computational search was completed in days — work that traditionally took months or years. The resulting binders were then lab-validated, exhibiting high affinity, specificity, and stability, the properties critical for clinical utility. This demonstrates that AI-driven protein design has moved from theoretical capability to producing real therapeutic candidates.

ESM Atlas completes the ecosystem by making ESMC's representations navigable across 6.8 billion protein sequences and 1.1 billion predicted structures. The scale of this database — combined with the predictive and design capabilities of ESMC and ESMFold2 — creates a compositional grammar for protein biology that researchers can explore, predict, and design within. ESMFold2 outperforms AlphaFold 3 on the challenging task of predicting true binding poses of antibody-antigen complexes when using ESMC representations alone, and becomes the strongest predictor on both benchmarks when provided with the same evolutionary information. The decision to make all three tools freely available amplifies their impact, positioning this as an open-source infrastructure contribution to the global drug discovery and biological research communities.