# Meet Stable Audio 3.0: Open-Weight Models Built for Artistic Experimentation
**Source**: https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models
**Date**: 2026-05-20
**Author**: Louisa Marshall
**Keywords**: Stability AI, Stable Audio, open-weight, music generation, SFX, LoRA, licensed data, on-device

## Elevator pitch
Stability AI has released Stable Audio 3.0, a family of four open-weight audio generation models trained on fully licensed data, supporting variable-length generation up to six minutes, full music composition on portable devices, LoRA fine-tuning, and audio inpainting — all with commercial output ownership.

## Takeaways
- Four models: Small SFX (sound effects on-device), Small (full music on-device), Medium (higher musicality, 6+ min), Large (API/enterprise, highest quality)
- Trained entirely on licensed data; users own their outputs and can commercialize them under the Community License
- Small model is the first capable of full music composition on-device and offline
- Variable-length generation at per-second granularity, up to 6:20 minutes
- Supports LoRA fine-tuning, audio inpainting (single/multi-segment editing, causal continuation)

## Synthesis
Stability AI is bringing its open-weight philosophy to generative audio with Stable Audio 3.0, a four-model family designed to do for music and sound what Stable Diffusion did for images. The release is strategically positioned: in a market where AI music generation is increasingly scrutinized for copyright concerns, Stability AI emphasizes that all models are trained on fully licensed data and that users own their outputs under the Community License.

The technical leap is significant. The previous Stable Audio Open Small generated just 11-47 seconds; 3.0 Small can produce up to two minutes of full musical composition on-device — a first for portable, offline audio generation. The Medium and Large variants extend to over six minutes with a novel semantic-acoustic autoencoder that enables variable-length generation at per-second granularity.

The practical tooling is equally notable. LoRA fine-tuning support means musicians and developers can customize models on their own audio libraries without full retraining. Audio inpainting enables single-segment edits, multi-segment modifications, and causal continuation — turning the model from a simple generator into an interactive composition tool.

The business strategy pairs open weights (Small, Medium, SFX on Hugging Face) with enterprise monetization — organizations over $1M revenue need an Enterprise License, and the Large model is API/self-hosted only. Combined with Stability AI's partnerships with Universal Music Group and Warner Music Group, the release positions the company at the intersection of open-source ethos and licensed professional tooling, betting that a responsible, artist-centric platform can outcompete unlicensed alternatives on product experience.
