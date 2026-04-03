# Aurora: Online Speculative Decoding via Reinforcement Learning
**Source**: https://www.together.ai/blog/aurora
**Date**: March 31, 2026
**Author**: Junxiong Wang, Fengxiang Bie, Jisen Li, Zhongzhu Zhou, Zelei Shao, Yubo Wang, Yinghui Liu, Qingyang Wu, Avner May, Sri Yanamandra, Ce Zhang, Tri Dao, Percy Liang, Shuaiwen Leon Song, Ben Athiwaratkun, Chenfeng Xu, Xiaoxia Wu
**Keywords**: speculative decoding, reinforcement learning, LLM inference optimization, online learning, adaptive systems, throughput

## Elevator pitch
Aurora introduces a serve-to-train flywheel that uses reinforcement learning to continuously adapt speculative decoding draft models during live inference, achieving 1.25x additional speedup over static speculators.

## Takeaways
- Reformulates speculative decoding as an asynchronous reinforcement learning problem, with accepted tokens as positive rewards and rejected tokens as counterfactual feedback
- Achieves 1.25x additional speedup over well-trained static speculators in production
- Adapts in real-time to distribution shifts without service interruption
- Eliminates the need for expensive offline activation-collection and large-scale distillation pipelines
- Open-source code and research paper are publicly available

## Synthesis
Speculative decoding has emerged as one of the most practical techniques for accelerating LLM inference in production: a smaller, faster "draft" model proposes token sequences that the larger target model verifies in parallel, improving throughput without degrading output quality. The limitation of existing approaches is that these draft models are trained offline on static datasets and quickly become misaligned with the actual distribution of requests a deployment receives — a problem that grows as models are updated or deployed in new contexts.

Aurora directly addresses this staleness problem by reframing online speculative training as an asynchronous reinforcement learning problem. The system continuously learns from live inference data: when the target model accepts a draft token, that acceptance functions as a positive reward signal; when it rejects a token, the counterfactual information about what would have been accepted provides corrective feedback. This closed loop allows the draft model to continuously recalibrate toward the actual distribution of production traffic.

The practical implications are significant. Traditional speculative decoding pipelines require maintaining large-scale distillation infrastructure to collect activations and periodically retrain draft models — an expensive and operationally complex process that teams often deprioritize until staleness becomes measurable as a performance regression. Aurora replaces this with a lightweight, always-on training process that runs asynchronously alongside serving, meaning the draft model improves continuously without requiring any manual intervention or service disruption.

The 1.25x additional speedup over a well-trained static speculator is noteworthy because it compounds on top of the baseline speculative decoding gains. More importantly, the paper demonstrates that online training from scratch can exceed carefully pretrained baselines — suggesting that the continuous adaptation to real traffic patterns provides information that offline training on static datasets cannot capture, regardless of how well-curated those datasets are.

The research comes from a team spanning Together AI, Stanford, and other institutions, and the open-source release (code, paper, and project website) positions Aurora as a practical tool for teams running LLM inference at scale. For engineering teams managing the cost and latency of production LLM deployments, the ability to continuously optimize the draft model against actual workloads — rather than against a proxy dataset — represents a meaningful operational advantage. The asynchronous design is particularly well-suited to production deployments where any training-induced latency increase would be unacceptable.
