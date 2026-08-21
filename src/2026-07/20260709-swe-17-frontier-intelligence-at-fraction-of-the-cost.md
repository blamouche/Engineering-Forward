# SWE-1.7: Frontier Intelligence at a Fraction of the Cost
**Source**: https://cognition.com/blog/swe-1-7
**Date**: 2026-07-09
**Author**: Cognition
**Keywords**: SWE-1.7, Cognition, Devin, reinforcement learning, code generation, agent, RL training, multi-cluster training, entropy

## Elevator pitch
Cognition launches SWE-1.7, a model that reaches frontier-level coding performance at dramatically lower cost, challenging the idea of a "post-training ceiling" through novel RL techniques including entropy preservation, multi-cluster training, and self-compaction.

## Takeaways
- SWE-1.7 scores 42.3% on FrontierCode 1.1 Main, approaching GPT-5.5 (43.0%) and Opus 4.7 (38.5%) at a fraction of the cost—under $8 per rollout vs. $10+ for Opus 4.8.
- Built on a Kimi K2.7 base, the model's large gains from additional RL training challenge the idea of a "post-training ceiling," suggesting RL can push capabilities much further than previously believed.
- Key technical innovations: top-p sampling with sampling distribution replay to prevent entropy collapse; multi-cluster training across three continents with compressed weight deltas; high-quality data curation pipeline; and self-compaction for extending task horizons beyond the raw context window.
- Multi-cluster training uses compressed weight deltas reduced by over 99%, enabling RL training across four datacenters worldwide—only the trainer needs a single high-bandwidth cluster, while inference engines can run anywhere.
- Self-compaction teaches the model to summarize its working state and resume from the summary, allowing it to tackle tasks that would otherwise exceed context limits.

## Synthesis
Cognition's SWE-1.7 represents a significant step in the cost-performance frontier for coding agents. The model reaches near-frontier performance on multiple benchmarks—42.3% on FrontierCode 1.1 Main, 81.5% on Terminal-Bench 2.1, and 77.8% on SWE-Bench Multilingual—while costing substantially less per inference than the leading models from OpenAI and Anthropic.

The technical contribution is substantial. The paper's most interesting finding is that entropy collapse—the tendency for RL training to narrow the model's output distribution—is a major cause of training plateau, and that top-p sampling combined with sampling distribution replay can prevent it. When low-probability tokens are sampled, they produce gradients that sharpen the distribution, reducing entropy. Top-p sampling prevents these tokens from being sampled, but naively applying it creates a training-inference mismatch. The solution is to record the "kept set" of tokens available at rollout time and renormalize probabilities with those masks in the trainer.

The multi-cluster training architecture is pragmatically important. Cognition can't access the massive single-cluster GPU installations that larger labs use, so they built infrastructure to distribute RL training across four datacenters on three continents. Only the trainer needs a single high-bandwidth cluster; inference rollout engines are self-contained and can run anywhere. Weight updates are shipped as compressed deltas reduced by over 99%, enabling aggressive learning rates without staleness problems.

Self-compaction addresses a fundamental agent limitation: tasks that exceed the context window. The model learns to summarize its working state and resume from the summary, using an alternating length penalty to keep summaries concise without sacrificing correctness. This extends effective task horizons well beyond what the raw context length would allow.

For the broader field, SWE-1.7's results suggest that the "post-training ceiling" narrative may be premature. Starting from a Kimi K2.7 base that had already undergone extensive RL post-training, Cognition extracted significant additional gains, implying that current RL techniques may have more headroom than assumed.