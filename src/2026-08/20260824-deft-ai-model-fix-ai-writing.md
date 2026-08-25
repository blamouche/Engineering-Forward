# I Tried the AI Model Built to Fix AI Writing
**Source**: https://every.to/i-tried-the-ai-model-built-to-fix-ai-writing
**Date**: 2026-08-24
**Author**: Katie Parrott (Every)
**Keywords**: Deft, DFT v1, AI writing, distribution fine-tuning, LLM prose, stochastic parrots

## Elevator pitch
A new research lab called Deft has built a writing-focused model using "distribution fine-tuning" that makes AI prose less predictable—but not necessarily better.

## Takeaways
- Deft's DFT v1 model uses "distribution fine-tuning," a post-training method that compares batches of model outputs against human writing distributions rather than grading individual responses
- The model produces more varied sentence structures and openings than conventional LLMs, reducing the "AI smell" of repetitive patterns like "not X, but Y" and lists of three
- However, the writing is denser, harder to parse, and poorly sequenced—Deft's own reading score rated its output at 11th-grade level
- Strict mode (which should only use provided source material) failed: the model invented dates, dialogue, and details not in the brief
- The API is limited to sending complete assignments to Deft's system rather than allowing iterative collaboration with the model
- The core insight is that making AI writing more stochastic is necessary but insufficient—good writing also requires information hierarchy, sequencing, and reader theory of mind

## Synthesis
Deft's approach targets a real and well-documented problem: the sameness of AI-generated prose. The "stochastic parrot" critique, coined by Bender and Gebru, identified that LLMs generate from probabilities without communicative intent. Deft's distribution fine-tuning method is a novel technical response—instead of optimizing each response individually, it optimizes the statistical distribution of a batch of outputs to match human writing patterns. This is a genuinely different post-training signal.

The results, however, reveal the gap between reducing predictability and improving quality. DFT v1's prose varied its syntax but lacked the structural intelligence that makes writing effective: knowing when a term needs explaining, how to order information, and when to lean in versus pull back. The model made local decisions sentence by sentence without a stable model of the whole piece. This suggests that the "AI writing" problem is not solely a distribution problem—it is also a planning and theory-of-mind problem.

The review also highlights a practical limitation: Deft's API returns completed documents rather than enabling iterative collaboration. For writers whose process involves going back and forth with a model—keeping certain parts, reworking others, building from an outline—this one-shot workflow is a significant constraint. The model needs to support compound writing workflows where sections can be independently revised, sources can be pinned, and instructions persist across turns.

The broader takeaway for the AI writing space is that distribution-level training is a promising direction, but it must be combined with better instruction following, information architecture, and iteration support to produce writing that is not just different but genuinely better.