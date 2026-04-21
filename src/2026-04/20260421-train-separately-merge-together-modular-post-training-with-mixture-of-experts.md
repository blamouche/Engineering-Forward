# Train separately, merge together: Modular post-training with mixture-of-experts

**Source**: https://allenai.org/blog/bar
**Date**: April 21, 2026
**Author**: Unknown
**Keywords**: allenai, train, separately, merge, together, modular, post, training

## Elevator pitch
BAR is a recipe for post-training language models one capability at a time—train domain experts independently, merge them into a single mixture-of-experts model, and upgrade any expert without impacting the others

## Takeaways
- Train separately, merge together: Modular post-training with mixture-of-experts April 20, 2026 Jacob Morrison, Sanjay Adhikesaven, Akshita Bhagia, Matei Zaharia, Noah A.
- Smith, and Sewon Min - Ai2 Share Models Tech Report Code After pretraining, language models go through a series of mid- and post-training stages to become practically useful—learning to follow instructions, reason through problems, reliably call tools, and so on.
- But updating or extending a model following these stages is often challenging.
- The most reliable option, retraining from scratch with new capabilities included from the start, is expensive and requires full access to the original training setup.
- Training further on new data is cheaper, but it can cause the model to lose capabilities it already had.

## Synthesis
Train separately, merge together: Modular post-training with mixture-of-experts April 20, 2026 Jacob Morrison, Sanjay Adhikesaven, Akshita Bhagia, Matei Zaharia, Noah A. Smith, and Sewon Min - Ai2 Share Models Tech Report Code After pretraining, language models go through a series of mid- and post-training stages to become practically useful—learning to follow instructions, reason through problems, reliably call tools, and so on. But updating or extending a model following these stages is often challenging. The most reliable option, retraining from scratch with new capabilities included from the start, is expensive and requires full access to the original training setup. Training further on new data is cheaper, but it can cause the model to lose capabilities it already had. And because post-training typically involves multiple stages – each with its own data and objectives – adding new skills means rerunning or adjusting each stage to accommodate them without breaking what came before. We present BAR (Branch-Adapt-Route), a recipe for modular post-training that sidesteps these issues. Rather than training a single model on all data at once, BAR trains independent domain experts – each through its own complete training pipeline – and composes them into a unified model via a mixture-of-experts (MoE) architecture. Each expert can be developed, upgraded, or replaced without touching the others. We're releasing the recipe , a technical report , and the checkpoints used to validate the approach.
