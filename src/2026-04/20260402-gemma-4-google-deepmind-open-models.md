# Gemma 4: Byte for Byte, the Most Capable Open Models
**Source**: https://simonwillison.net/2026/Apr/2/gemma-4/
**Date**: April 2, 2026
**Author**: Simon Willison
**Keywords**: Gemma 4, Google DeepMind, open models, Apache 2.0, MoE, per-layer embeddings, multimodal, audio input

## Elevator pitch
Google DeepMind releases Gemma 4 in four sizes (2B, 4B, 26B MoE, 31B) under Apache 2.0, with per-layer embeddings for efficient on-device deployment, multimodal video/image processing, and native audio input on E2B/E4B variants.

## Takeaways
- Four variants: E2B, E4B (with native audio input), 26B-A4B (Mixture-of-Experts), and 31B
- Per-Layer Embeddings technology: each decoder layer gets its own token embedding, optimizing on-device efficiency
- All models process video and images at variable resolutions; E2B/E4B add native audio input for speech recognition
- 31B achieves Arena AI text score 1452, 85.2% MMLU multilingual, 89.2% AIME 2026, 80.0% LiveCodeBench
- Available via HuggingFace, Ollama, Kaggle, LM Studio; Apache 2.0 license

## Synthesis
The Gemma 4 release advances Google DeepMind's open model strategy with a model family specifically optimized for deployment efficiency rather than simply scaling capability. The "byte for byte, the most capable" positioning reflects the same efficiency focus as the parameter count reduction in TimesFM — demonstrating that Google's research investments in architectural efficiency are producing models that outperform larger alternatives in the open model space.

Per-Layer Embeddings (PLE) is the most technically distinctive feature. Standard transformers use shared token embeddings across all decoder layers — the same representation of a token is available to every layer. PLE gives each decoder layer its own small embedding for every token, allowing lower layers (which tend to handle syntactic features) and higher layers (which handle semantic features) to use token representations optimized for their specific role in the processing hierarchy. The efficiency benefit for on-device deployment suggests that PLE reduces the memory bandwidth requirements during inference, which is the key bottleneck on mobile and edge hardware.

The multimodal capabilities across all four variants — video and image processing at variable resolutions — reflects the maturation of multimodal as a baseline capability rather than a premium feature. OCR and chart analysis are highlighted as specific strengths, indicating these are areas where the training data and fine-tuning specifically invested.

Native audio input on the E2B and E4B variants positions these models for speech-based applications that can run entirely on device. Combined with the small parameter counts (2B and 4B effective parameters), these are viable for mobile deployment where cloud round-trips for speech recognition are impractical.

Willison's practical testing note — the 31B model malfunctioned in LM Studio while the 26B-A4B and smaller models worked reliably — is useful ground truth for practitioners evaluating which variants to deploy. The 26B-A4B MoE model, with only 4B parameters active at inference time, is likely the most practically interesting for deployment contexts where the full 31B cost is prohibitive.
