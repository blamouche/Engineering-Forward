# Reinforcing Recursive Language Models
**Source**: https://www.alphaxiv.org/blog/reinforcement-learning-for-rlms
**Date**: May 13, 2026
**Author**: Daniel Kim, Rehaan Ahmad
**Keywords**: Recursive Language Models, RLMs, reinforcement learning, GRPO, fine-tuning, small models, evidence selection, Qwen, REPL, agent architecture

## Elevator pitch
Researchers RL fine-tuned a 4B parameter model to behave as a recursive language model (RLM), achieving performance matching Claude Sonnet 4.6 on evidence selection tasks at a fraction of the cost, by training a single shared policy for both parent and child RLM roles.

## Takeaways
- A single 4B model was trained to play both parent (decomposer) and child (sub-agent) RLM roles using a unified GRPO objective with advantage inheritance from parent to child rollouts
- The RL fine-tuned 4B model matched Claude Sonnet 4.6 on multi-paper evidence selection while being dramatically smaller and cheaper
- Key training innovations include: cold-start SFT on teacher traces to bootstrap REPL competence, stepwise training (each turn is a separate sample), and rubric-based LLM judges instead of noisy F1 rewards
- Without RL, even with good prompts, Qwen3.5-4B had 0 pass@16 scores on RLM tasks — the harness is fundamentally outside small models' "edge of competence"
- Code, training scripts, and the RLM scaffold implementation are open-sourced on SkyRL

## Synthesis
Published on May 13, 2026, this alphaXiv blog post by Daniel Kim and Rehaan Ahmad presents a significant advance in making Recursive Language Models (RLMs) practical for production deployment. RLMs, first introduced in prior work, allow language models to spawn sub-models inside a programmatic (Python REPL) environment, recursively decomposing complex queries over large contexts. However, deploying RLMs in production has been hampered by unpredictable latency and brittle prompt engineering. The authors tackle this by showing that reinforcement learning can train small, efficient models to behave as native RLMs.

The core innovation is a unified training objective that handles both parent and child RLM roles under a single policy. Rather than training separate models for the decomposer (parent) and worker (child) roles — which would require two sets of reward signals — the authors extend GRPO to a recursive structure. Parent rollouts receive rewards via rubric-based LLM judges, and children inherit their parent's advantage. Child loss contributions are normalized by the number of children per parent (1/kg) to prevent parent trajectories with many sub-calls from dominating gradient updates. This elegant formulation generalizes to arbitrary recursion depths.

The task used for evaluation is evidence selection: given a question and up to 10 arXiv papers, extract relevant snippets. The REPL environment exposes built-in functions (search, extract_section, list_papers, get_paper_abstract) alongside rlm_query and rlm_query_batched for spawning sub-RLMs. The dataset was synthetically generated — 1,000 queries over groups of up to 10 papers.

Several training details proved critical. First, cold-start SFT on teacher traces from a large model (Qwen3.5-397B) was mandatory: without it, Qwen3.5-4B scored 0 pass@16. However, SFT on the full training dataset caused entropy collapse, so only a few dozen held-out examples were used. Second, stepwise training was necessary because the RLM scaffold rewrites the user prompt each turn (no prefix sharing) — a rollout of N turns produces N training samples, with only final-turn rollouts used for advantage calculation. Third, rubric-based LLM judges replaced noisy verifiable rewards (F1) that couldn't handle the many-to-many mapping between valid evidence selections and ground truth.

The results are compelling. On the single-paper variant, RL lifted Qwen3.5-4B's judge score from 0.6 to 0.8. On the multi-paper variant requiring true recursive sub-calls, the 4B model jumped from 0.3 to 0.6 on the training set — and crucially, matched Claude Sonnet 4.6's performance on the full RLM task despite being orders of magnitude smaller and cheaper. At scale, the training hit 512 concurrent rollouts (16 prompts × 8 samples × up to 4 children), requiring fixes for race conditions around REPL timeouts.

The implications extend beyond this specific task. The training methodology — shared policy, advantage inheritance, child normalization — provides a blueprint for RL fine-tuning RLMs on any decomposable task. And the demonstration that a 4B model can match a frontier model's RLM performance suggests that the future of long-context, multi-document reasoning may belong to small, specialized, RL-trained recursive agents rather than ever-larger monolithic models.
