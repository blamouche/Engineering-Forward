# How Open-Weight Models Changed the AI Landscape
**Source**: https://blog.bytebytego.com/p/how-open-weight-models-changed-the
**Date**: 2026-06-16
**Author**: ByteByteGo
**Keywords**: open-weight models, MoE, attention strategies, DeepSeek, Kimi K2, Qwen3, Llama 4, GLM-5, ML, AI architecture

## Elevator pitch
Open-weight LLMs have created an unprecedented cycle of indirect public collaboration between competing AI teams, with each building on published weights and technical reports from predecessors—converging on Mixture-of-Experts architecture while diverging in attention strategies, sparsity choices, and post-training approaches.

## Takeaways
- Every frontier open-weight LLM in 2025-2026 uses Mixture-of-Experts (MoE) architecture, where total parameters (knowledge capacity) and active parameters (inference cost) are two very different numbers
- Three attention strategies compete: GQA (Qwen3, Llama 4), MLA (DeepSeek, Kimi K2), and Sparse Attention (DeepSeek V3.2, GLM-5)—each optimizing for simplicity, memory efficiency, or context length respectively
- Expert count varies wildly from 16 to 384 across models, reflecting genuine disagreement on sparsity; some include shared experts (DeepSeek V3, Llama 4, Kimi K2) while others drop them (Qwen3)
- Post-training is now where models diverge most: reinforcement learning with verifiable rewards (DeepSeek R1), distillation (Llama 4 from 2T-param Behemoth), and synthetic agentic data (Kimi K2)
- A "borrow-and-build" pattern has emerged: DeepSeek V2 introduced MLA, V3 refined MoE, Kimi K2 scaled it and contributed MuonClip optimizer, GLM-5 adopted sparse attention and contributed the Slime training framework

## Synthesis
ByteByteGo's analysis maps the emerging taxonomy of open-weight LLMs with characteristic clarity. The article traces how DeepSeek's December 2024 V3 release set off a chain reaction: Moonshot AI used its technical report to build Kimi K2 at trillion-parameter scale, inventing a new optimizer (MuonClip) when training instability surfaced; Zhipu AI then adopted DeepSeek's sparse attention innovation for GLM-5 and contributed the Slime RL framework. Each team built on predecessors while adding reusable innovations back to the ecosystem.

The technical core is the MoE architecture, which all frontier open-weight models now share. But within that skeleton, teams make three critical design choices: attention strategy (GQA vs. MLA vs. sparse attention), sparsity level (16 to 384 experts), and post-training approach. These choices reflect different optimization targets—engineering simplicity, memory efficiency, context length, or training stability.

Perhaps most importantly, the article makes clear that "open weight" is not "open source." Published weights plus detailed technical reports enable this borrow-and-build cycle, but the training data and full training code remain private. The license landscape varies from MIT to custom restrictions. The framework for reading these models—MoE skeleton, three design bet dimensions, and the borrow-and-build pattern—will likely outlast any specific model release. Architecture is converging; training is where the real differentiation now lives.