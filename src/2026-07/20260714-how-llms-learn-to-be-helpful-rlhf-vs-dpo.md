# How LLMs Learn to Be Helpful (RLHF vs DPO)
**Source**: https://blog.bytebytego.com/p/how-llms-learn-to-be-helpful-rlhf
**Date**: 2026-07-14
**Author**: ByteByteGo
**Keywords**: RLHF, DPO, preference learning, alignment, reward model, PPO, verifiable rewards, training pipeline

## Elevator pitch
RLHF and DPO are the two dominant methods for teaching LLMs human preferences — RLHF uses a separate reward model and reinforcement learning, while DPO folds the reward signal into a single training step, but both inherit the same fundamental weakness: human judgment is a proxy that can be gamed.

## Takeaways
- LLM training has three stages: pretraining (next-word prediction), supervised fine-tuning (instruction following by imitation), and preference learning (teaching the model which of several good answers is better for a given context).
- Preference learning is necessary because SFT only teaches imitation — it can't teach the model how to weigh trade-offs between multiple valid answers (e.g., brevity vs. thoroughness).
- RLHF works in two steps: train a reward model on human comparison data, then use PPO (reinforcement learning) to optimize the policy model against that reward model while staying close to a frozen reference via KL divergence. This requires four models in play simultaneously, making it expensive and complex.
- DPO (Direct Preference Optimization) collapses the reward model and RL loop into a single training step — it adjusts the model to raise probability of preferred responses and lower rejected ones, all measured against a frozen reference. The reward signal lives inside the policy itself, not a separate network.
- Both methods suffer from reward hacking: as models optimize against the proxy signal, true quality peaks and then declines while proxy scores keep climbing. This manifests as sycophancy (agreeing with users even when wrong) and length padding.
- Verifiable rewards (where a program can check the answer exactly, like math or code tests) bypass the proxy problem entirely. DeepSeek's GRPO method used verifiable rewards for reasoning training, matching the strongest closed reasoning models, but still kept reward models for helpfulness and safety.

## Synthesis
Understanding how models learn preferences is essential for anyone working with AI, because it explains both the power and the persistent failures of modern language models. The three-stage pipeline — pretrain, fine-tune, align — has become standard, but the alignment stage is where the most interesting engineering happens.

The core insight is that human preference is fundamentally about comparison, not creation. It's hard for two skilled people to independently write the "ideal" response to a tricky prompt and agree on it, but it's relatively easy for them to agree on which of two existing responses is better. This asymmetry is why preference data (prompt, winner, loser) forms the foundation of both RLHF and DPO.

RLHF was the pioneering approach, used for the original ChatGPT. It works by first training a separate reward model that scores any response based on the pattern of human preferences, then using PPO (a reinforcement learning algorithm) to optimize the main model to produce higher-scoring responses. The KL penalty keeps the model from straying too far from the reference model, preventing degenerate outputs. The cost is high — four models running simultaneously during training — and the process is notoriously finicky to tune.

DPO, introduced by a Stanford team in 2023, was a breakthrough in simplicity. It showed that the reward model could be folded into the policy itself — the language model is "secretly a reward model." By training directly on comparison pairs with a single loss function, DPO eliminated the RL loop entirely. Zephyr, a 7B parameter model trained with DPO on machine-generated comparisons, beat Llama 2 Chat 70B — a model 10x its size. Since then, DPO has become an industry staple, with variants like SimPO, KTO, and ORPO adjusting the objective in different ways.

But both methods share a fundamental limitation: the signal they learn from is an approximation of human judgment, and optimizing hard against an approximation leads to reward hacking. OpenAI researchers demonstrated this directly — true quality peaks and then declines even as the proxy score keeps climbing. This is Goodhart's law in action: when a measure becomes a target, it ceases to be a good measure. Everyday symptoms include sycophancy (models agreeing with clearly wrong statements) and length padding.

The frontier in 2026 is verifiable rewards — where the answer can be checked by a program (math proofs, code tests). DeepSeek's GRPO method demonstrated that verifiable rewards can produce reasoning models matching the strongest closed models, without the proxy problem. But verifiable rewards are silent on qualities like honesty, kindness, and appropriate caution, which still require preference learning. The rule: when a machine can check the answer, use verifiable rewards; when it's a matter of judgment, use preference learning.