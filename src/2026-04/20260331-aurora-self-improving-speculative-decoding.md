# Aurora: Self-Improving Speculative Decoding via Online Reinforcement Learning
**Source**: https://www.together.ai/blog/aurora
**Date**: March 31, 2026
**Author**: Junxiong Wang, Fengxiang Bie, Jisen Li, Zhongzhu Zhou, Zelei Shao, Yubo Wang, Yinghui Liu, Qingyang Wu, Avner May, Sri Yanamandra, Ce Zhang, Tri Dao, Percy Liang, Shuaiwen Leon Song, Ben Athiwaratkun, Chenfeng Xu, Xiaoxia Wu
**Keywords**: speculative decoding, LLM inference, reinforcement learning, online learning, Together AI

## Elevator pitch
Aurora introduces a continuous online learning system that improves speculative decoding draft models directly from live production traffic, achieving 1.25x additional speedup over well-trained static speculators.

## Takeaways
- Aurora implements a "serve-to-train flywheel" where the draft model continuously improves from live inference traffic using reinforcement learning
- The system maps speculative decoding to RL semantics: draft model as policy, verifier as environment, and token acceptance/rejection as reward signals
- A "Discard Sampling" technique trains the model on rejected tokens, teaching what not to generate
- Tested on 40,000 prompts across five domains, Aurora adapts to domain shifts within approximately 10,000 requests
- The decoupled, asynchronous architecture allows continuous weight updates without service interruption

## Synthesis
Aurora represents a fundamental rethinking of speculative decoding—a critical optimization technique for LLM inference. Rather than treating draft model training as a static, offline task completed once before deployment, the authors propose a continuous learning system that improves the speculator directly from live production traffic.

Traditional speculative decoding pipelines suffer from predictable degradation. As target models update and serving traffic patterns shift, draft models become stale. Offline retraining pipelines are expensive at scale, requiring petabyte-level storage for activation collection. Most critically, laboratory optimization metrics such as acceptance rates do not necessarily translate to real-world speedup gains, which depend on actual kernel performance, numeric precision, and hardware behavior.

Aurora implements a "serve-to-train flywheel" using reinforcement learning. The system decouples inference and training into separate, asynchronous servers. During inference, accepted and rejected tokens from speculative decoding are streamed to a data buffer. A training server continuously fetches batches, performs gradient updates, and hot-swaps improved weights back without service interruption.

The system elegantly maps speculative decoding to RL semantics: the draft model becomes a policy, the verifier becomes an environment, and token acceptance/rejection provides reward signals. Crucially, Aurora learns from both accepted tokens through imitation and rejected proposals through "Discard Sampling" that teaches what not to generate. A specialized Tree Attention mechanism efficiently processes the branching structure of speculative results in single batched passes.

Tested on 40,000 prompts spanning five domains including math, SQL, code, finance, and conversation, Aurora achieved remarkable results. When traffic induces abrupt domain shifts, the system adapts within approximately 10,000 requests. Most strikingly, the system achieved 1.25x additional speedup over a well-trained static speculator, demonstrating compound benefits atop existing offline investments. Online training from scratch occasionally exceeded carefully pretrained baselines.

This work challenges conventional wisdom that speculative decoding requires extensive offline pretraining. The unified training-serving loop unlocks real-time utility feedback, reduces infrastructure costs, and remains compatible with future speculator algorithms. By eliminating expensive activation-collection pipelines and learning directly from live traces, Aurora reduces operational burden. The algorithm-agnostic framework supports diverse user demands and heterogeneous traffic patterns without service interruption, shifting speculative decoding from a static, offline task to a dynamic, online learning process.
