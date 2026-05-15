# Reinforcing Recursive Language Models
**Source**: https://www.alphaxiv.org/blog/reinforcement-learning-for-rlms
**Date**: May 13, 2026
**Authors**: Daniel Kim, Rehaan Ahmad
**Keywords**: recursive language models, RLMs, reinforcement learning, GRPO, fine-tuning, evidence selection, small models, Qwen

## Elevator pitch
Researchers demonstrate that reinforcement learning fine-tuning can train a small 4B-parameter model to function as a recursive language model (RLM), matching Claude Sonnet 4.6's performance on evidence selection tasks at a fraction of the size and cost.

## Takeaways
- A single 4B model (Qwen3.5-4B) was trained via RL to serve as both parent decomposer and child sub-agent in a recursive language model architecture, using a shared policy where child rollouts inherit parent advantages.
- On an evidence selection task over scientific documents, the RL-tuned 4B RLM matched Claude Sonnet 4.6 with an identical RLM harness, despite being orders of magnitude smaller and cheaper.
- Cold-start supervised fine-tuning (SFT) was essential: without it, the 4B model achieved 0 pass@16 scores, as the RLM harness syntax and REPL environment navigation are outside the competence edge of small models.
- Stepwise training was necessary because successive RLM turns don't share prefixes—each turn must be a separate training sample, with advantage broadcast from final rollout steps to earlier turns.
- Rubric-based LLM judges proved more robust than verifiable rewards like F1 scores, which were too noisy for tasks where multiple valid text selections could answer the same question.

## Synthesis
This work from the alphaXiv team represents a practical advance in making recursive language models (RLMs) deployable in production settings. RLMs are a powerful inference strategy that store long contexts as external objects the model inspects programmatically, spawning sub-calls to decompose complex problems. But their unpredictable latency and need for extensive prompt engineering have limited adoption. The researchers tackle this by asking: can we train small, cheap models to behave as native RLMs through reinforcement learning?

The answer is a clear yes, with caveats. Using GRPO-based RL on Qwen3.5-4B, the team trained a single shared policy that handles both parent decomposition and child sub-agent roles—a design choice that simplifies the training pipeline by avoiding separate reward signals for each role. The key insight is that child rollouts inherit the advantage of their parent root rollouts, with child contributions averaged so no single root is overweighted for spawning more sub-calls.

The practical results are striking: on an evidence selection task involving multiple scientific papers, the 4B RLM matches Claude Sonnet 4.6—a model likely 100x+ larger and more expensive. But the path to this result reveals important lessons. Cold-start SFT was mandatory; without it, small models cannot navigate the RLM harness at all. Stepwise training adaptations were needed because the RLM's per-turn prompt rewriting breaks the usual "one rollout = one training example" assumption. And rubric-based LLM judges were essential for reward assignment because verifiable metrics like F1 proved too noisy for tasks with multiple correct answers.

The broader implication is that the efficiency frontier for complex reasoning tasks may not require frontier-scale models. Purpose-built, RL-tuned small models with recursive architectures could match generalist giants on specific tasks, pointing toward a future where AI deployment emphasizes architectural cleverness and task-specific training over raw scale.
