# Sakana Fugu: Multi-Agent System Delivered as a Single Model
**Source**: https://sakana.ai/fugu/
**Date**: 2026-06-22
**Author**: Sakana AI
**Keywords**: Sakana, Fugu, multi-agent, model routing, orchestration, TRINITY, Conductor, ICLR

## Elevator pitch
Sakana AI's Fugu is a multi-agent orchestration system that routes each request across GPT-5.5, Gemini 3.1 Pro, and Claude using a learned coordinator—presenting the whole system to developers as a single OpenAI-compatible endpoint.

## Takeaways
- Fugu is not a single trained foundation model but a coordinator that dynamically assembles a team of frontier LLMs for each incoming request, exposed as one OpenAI-compatible API endpoint.
- The system is grounded in two ICLR 2026 papers: TRINITY (a compact coordinator trained with evolutionary optimization that assigns Thinker, Worker, and Verifier roles without merging model weights) and Conductor (an RL-trained router that designs agent communication topology).
- Fugu Ultra scores 73.7% on SWE-Bench Pro and 95.5% on GPQA Diamond, benchmark results that compare favorably with individual frontier models.
- Users can opt out of specific providers or models to meet data, privacy, compliance, or organizational requirements—the system is configurable rather than locked into a single vendor.
- Pricing is $5/1M input tokens and $30/1M output tokens (double above 272K context), with monthly subscription tiers from $20 to $200.

## Synthesis
Sakana AI, the Tokyo-based research lab founded by David Ha, Llion Jones, and Ren Ito, launched Fugu on June 22, 2026, positioning it as a fundamentally different approach to AI model access. Rather than choosing between frontier models, Fugu presents a multi-agent system that behaves like a single model from the developer's perspective. Each request is routed across GPT-5.5, Gemini 3.1 Pro, and Claude through a learned orchestration layer.

The technical foundation comes from two research contributions. TRINITY trains a compact coordinator with evolutionary optimization to assign Thinker, Worker, and Verifier roles to different models without merging weights—preserving each model's strengths while coordinating their efforts. Conductor uses reinforcement learning to design the communication topology between agents, determining how information flows through the system for each specific task.

The practical value proposition is multi-fold. First, it provides a hedge against any single frontier model being down, rate-limited, or export-restricted—developers don't need to build their own fallback logic. Second, different models excel at different tasks, and Fugu's routing learns which model to send each request to. Third, the opt-out mechanism for specific providers addresses compliance requirements that many enterprises face.

The benchmark results suggest the orchestration approach works: Fugu Ultra's 73.7% on SWE-Bench Pro and 95.5% on GPQA Diamond are competitive with individual frontier models, which validates the thesis that intelligent routing can match or exceed single-model performance on complex tasks. The pricing at $5/$30 per million tokens positions Fugu as a premium but reasonable alternative to managing multiple API keys and building custom routing logic.

This launch signals a broader trend in the AI infrastructure layer: the shift from single-model APIs to orchestrated multi-model systems that abstract away vendor complexity while potentially delivering better results through specialization and redundancy.