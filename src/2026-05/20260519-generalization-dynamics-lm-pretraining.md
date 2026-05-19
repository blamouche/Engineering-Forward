# Generalization Dynamics of LM Pre-training

**Source:** https://jiaxin-wen.github.io/blog/generalization-dynamics
**Date:** 2026-05-19

## Summary

Researchers from UC Berkeley and Stanford (Google DeepMind) challenge the conventional assumption that language models stably mature from pattern-matching parrots to generalizable intelligence during pre-training. Their key finding: "mode-hopping."

Key discoveries:
- LMs frequently and suddenly hop between parrot-like and intelligence-like modes throughout pre-training
- On a math eval, OLMo3 32B hits 81% accuracy at 2.17T tokens, collapses to 0% at 2.19T, then rebounds to 81.7% at 2.21T
- Mode-hopping is not explained by standard optimization dynamics — it's locally stable and resistant to checkpoint averaging
- The phenomenon is framed as a "capacity allocation problem" where generalizable circuits compete with shallow early-training circuits
- The data in each pre-training window decides which circuits win

Applications demonstrated: (i) select intermediate checkpoints that generalize better than final checkpoints, (ii) select pre-training data to control generalization dynamics, (iii) falsify the belief that "simpler solutions generalize better."

**Tags:** #lm-training #generalization #research #deep-learning #mode-hopping
