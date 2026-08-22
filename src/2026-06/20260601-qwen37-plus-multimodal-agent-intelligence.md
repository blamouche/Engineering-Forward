# Qwen3.7-Plus: Multimodal Agent Intelligence
**Source**: https://qwen.ai/blog?id=qwen3.7-plus
**Date**: 2026-06-01
**Author**: Qwen Team (Alibaba)
**Keywords**: Qwen3.7-Plus, multimodal, agent-model, GUI-grounding, ScreenSpot-Pro, vision, Alibaba, Model-Studio, API-only, 1M-context

## Elevator pitch
Alibaba's Qwen team releases Qwen3.7-Plus — a multimodal agent model that unifies vision and language into a single agent foundation, capable of operating GUIs, writing code from visual references, and completing end-to-end tasks across GUI and CLI environments, at roughly one-sixth the price of Qwen 3.7 Max.

## Takeaways
- Multimodal agent model that perceives real-world scenes, reads screens, operates GUIs, and writes code from visual references — blending GUI and CLI interactions in a single agent loop
- 79.0 on ScreenSpot Pro (GUI grounding), ahead of GPT-5.4 (67.4) and Claude Opus 4.6 (49.5) in vendor benchmarks
- Priced at $0.40/$1.60 per 1M input/output tokens — roughly 6x cheaper than Qwen 3.7 Max ($2.50/$7.50)
- 1M token context window, 65K max output, with preserved thinking across context
- Ships proprietary and API-only on Alibaba Cloud Model Studio — a departure from Alibaba's open-weight Qwen lineage

## Synthesis
Alibaba's Qwen team released Qwen3.7-Plus as a multimodal agent model that unifies vision and language into a single, versatile agent foundation. The model operates as a multimodal interactive hybrid agent — perceiving real-world scenes, reading screens, operating graphical interfaces, writing code from visual references, and completing end-to-end tasks across both GUI and CLI environments within a single agent loop. Crucially, it is a perception model, not a generative one: it accepts text, images, and video as input and returns text only — it can read a screen and ground a click target, but won't generate images.

The pricing story is the real headline. At $0.40/$1.60 per 1M input/output tokens, Qwen3.7-Plus costs roughly 6x less on input and 5x less on output than Qwen 3.7 Max ($2.50/$7.50). This positions it as a default for budget-sensitive agent pipelines where multimodal perception is needed but frontier reasoning can be delegated to a text-only model. The model first surfaced as Qwen3.7-Plus-Preview on the public LM Arena leaderboard around May 14, 2026, giving developers roughly 18 days of live inference signal before GA.

The standout capability is GUI grounding: Qwen reports 79.0 on ScreenSpot Pro, ahead of GPT-5.4 (67.4) and Claude Opus 4.6 (49.5) in its own benchmark table. However, this score is vendor-stated and was run with thinking disabled, so should be treated as a directional signal. The model performs consistently across agent scaffolds — Claude Code, OpenClaw, Qwen Code, and other frameworks — generalizing across deployment environments.

Three engineering choices make it a genuine agent platform rather than a chat model with vision. First, a 1M token context window with preserved thinking across context — the model maintains reasoning state over long multi-step tasks. Second, built-in safety guardrails keep autonomous tools within preset operational limits when editing files or executing commands. Third, an agentic reinforcement learning loop allows the model to refine its accuracy based on real-world execution feedback.

The most notable strategic shift: Qwen3.7-Plus ships proprietary and API-only. No open-weight checkpoints were published on Hugging Face at launch — a real departure from Alibaba's open-source Qwen lineage. The model is exposed as the API endpoint `qwen3.7-plus` on Alibaba Cloud Model Studio (DashScope), reachable through OpenAI-compatible chat-completions and responses APIs across Beijing, Singapore, and US-Virginia regional endpoints. Independent signal is thin: Artificial Analysis placed it at #53 of 164 on its Intelligence Index with ~52.9 tokens/sec output speed (ranked ~#101), and unusually high verbosity (~110M output tokens during testing against a 29M median). The full Qwen3.7-Plus sibling strategy positions Plus for visual/agentic tasks while the text-only Qwen 3.7 Max provides the reasoning foundation.