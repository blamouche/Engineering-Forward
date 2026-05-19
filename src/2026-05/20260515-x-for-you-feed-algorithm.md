# X For You Feed Algorithm
**Source**: https://github.com/xai-org/x-algorithm
**Date**: May 15, 2026
**Author**: xAI
**Keywords**: X algorithm, For You feed, recommendation system, Grok, transformer, ranking, social media, open source

## Elevator pitch
xAI open-sourced the core recommendation system powering X's "For You" feed, including a Grok-based transformer model that predicts engagement probabilities, a banger classifier for post quality scoring, and runnable end-to-end inference pipeline.

## Takeaways
- The algorithm combines in-network posts (accounts you follow) with out-of-network content discovered through ML-based retrieval, all ranked by a Grok-based transformer.
- All hand-engineered features and most heuristics have been eliminated — the transformer does all heavy lifting by analyzing engagement history.
- The "banger classifier" (Grox) scores posts on quality and slop, with a "not_dwelled" signal penalizing posts users scroll past.
- A pre-trained mini Phoenix model (256-dim embeddings) is packaged as a ~3GB archive distributed via Git LFS for out-of-the-box inference.
- Components include Thunder (in-network retrieval), Phoenix (out-of-network retrieval + ranking), Home Mixer (orchestration), and Grox (content understanding including spam detection and policy enforcement).
- The system includes ads blending with brand-safety tracking that respects sensitive content boundaries.

## Synthesis
xAI's open-source release of the X "For You" feed algorithm represents a significant transparency move in social media recommendation systems. The repository contains the full recommendation pipeline powering X's primary content feed, combining familiar social graph signals with ML-based retrieval and a Grok-based transformer ranking model.

The architecture centers on Phoenix, a Grok-based transformer that predicts engagement probabilities (likes, replies, reposts, clicks) for each candidate post. The final score is a weighted combination of these predicted engagements, with an author diversity scorer attenuating repeated-author scores to ensure feed variety. The system has eliminated all hand-engineered features and most heuristics — a design choice that delegates all ranking intelligence to the transformer model's understanding of user engagement history.

The May 2026 update added significant new capabilities: a runnable end-to-end inference pipeline replacing separate ranking and retrieval scripts, a pre-trained mini Phoenix model for out-of-the-box inference, a Grox content-understanding pipeline for spam detection and policy enforcement, and an ads blending module with brand-safety tracking. The Home Mixer orchestration layer hydrates extensive user context including followed topics, starter packs, impression bloom filters, mutual follow graphs, and served history.

For content creators, the Grox "banger classifier" is particularly significant — it scores every post on quality (0-1) and slop (1-3), with the dreaded "not_dwelled" signal triggered by users scrolling past without engaging. This transparency lets creators understand (and optimize for) the ranking mechanics, though it also raises questions about whether algorithm-aware content creation leads to homogenization of the feed.
