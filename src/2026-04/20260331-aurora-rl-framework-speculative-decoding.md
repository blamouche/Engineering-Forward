# Aurora: RL-Based Framework for Self-Improving Speculative Decoding

**Source**: https://www.together.ai/blog/aurora
**Date**: 2026-03-31
**Author**: Junxiong Wang et al. (Together AI)
**Keywords**: speculative decoding, reinforcement learning, LLM inference, optimization, Together AI, open-source

## Elevator pitch
Aurora is an open-source RL-based framework from Together AI that continuously adapts speculative decoding during live production serving, achieving 1.25x additional speedup over well-trained static speculators.

## Takeaways
- Aurora fixes the "staleness" problem in speculative decoding by continuously learning from live inference traces
- Achieves 1.25x additional speedup over a well-trained static speculator on models like Qwen3 and Llama3
- Uses reinforcement learning to update the draft model asynchronously without interrupting serving
- Algorithm-agnostic and open-sourced at github.com/togethercomputer/aurora
- Online training from scratch can outperform carefully pretrained static baselines

## Synthesis
Speculative decoding is a key technique for accelerating large language model inference: a smaller "draft" model proposes tokens that are then verified by the main model in parallel, reducing latency. The problem is that in production, draft models go stale — traffic distribution shifts over time, acceptance rates decay, and offline retraining is too slow and expensive to keep pace.

Aurora, released by Together AI, is a fully automated solution: an open-source framework based on reinforcement learning that learns directly from live serving traffic and continuously updates the speculator without interrupting inference. It closes the loop between serving and training, turning speculative decoding from a static artifact into a self-improving system.

The results are significant. Across tested models (Qwen3-Coder, Llama3, MiniMax M2.5), Aurora achieves an additional 1.25x speedup compared to a well-tuned but static offline-trained speculator. More interestingly, the system can outperform a carefully pretrained baseline even when starting online training from scratch — meaning the cost of pre-training the draft model can potentially be eliminated.

Key technical properties include: direct mitigation of distribution mismatch between training and production traffic, reduced infrastructure cost by eliminating large-scale activation-collection pipelines, and an algorithm-agnostic design compatible with future speculator architectures.

For engineering teams running LLMs at scale, Aurora addresses a real operational pain point. Speculative decoding is already widely deployed, but its gains erode over time. Aurora turns it into a maintenance-free component that self-heals. This is precisely the kind of "boring infrastructure" improvement that has an outsized impact in production: not a 10x model improvement, but a 1.25x compounding speedup that never degrades.

The full code is available on GitHub, and the research paper is published on arXiv (2602.06932). Together AI encourages community contributions, positioning this as a community-driven inference infrastructure primitive.
