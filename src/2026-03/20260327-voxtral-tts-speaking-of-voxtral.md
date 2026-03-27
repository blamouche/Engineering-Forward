# Speaking of Voxtral: Voxtral TTS
**Source**: https://mistral.ai/news/voxtral-tts
**Date**: Unknown
**Author**: Mistral AI
**Keywords**: text-to-speech, multilingual, low latency, voice agents

## Elevator pitch
Mistral releases Voxtral TTS, a 4B‑parameter multilingual text‑to‑speech model focused on naturalness, low latency, and enterprise voice‑agent workflows.

## Takeaways
- Supports 9 languages with expressive, emotion‑aware speech and dialect coverage.
- Emphasizes low time‑to‑first‑audio and real‑time factor ~9.7×.
- Zero‑shot voice adaptation with 3–25 seconds of reference audio.
- Available via API and Mistral Studio; open‑weights model on Hugging Face (CC BY‑NC).
- Designed to pair with Voxtral Transcribe for full speech‑to‑speech pipelines.

## Synthesis
Voxtral TTS is Mistral’s first text‑to‑speech model, aimed at enterprise voice agents that need fast, natural, and customizable speech generation. The model is relatively compact at 4B parameters and claims strong human‑evaluated naturalness across nine languages (English, French, German, Spanish, Dutch, Portuguese, Italian, Hindi, Arabic) while keeping latency low.

A key capability is voice adaptation: with as little as a few seconds of reference audio, the model can mimic a speaker’s cadence, accent, and emotional tone. Mistral highlights zero‑shot cross‑lingual adaptation, allowing a voice prompt in one language to guide speech generation in another, which is useful for speech‑to‑speech translation stacks.

The architecture combines a transformer decoder with a flow‑matching acoustic model and a neural audio codec, optimized for streaming. Mistral reports ~70ms model latency for typical inputs and the ability to generate long audio by interleaving output. The release is positioned as the output layer in enterprise voice pipelines, complementing Voxtral Transcribe for end‑to‑end speech workflows.

Voxtral TTS is available via API ($0.016 per 1k characters) and through Mistral Studio, with open weights released under a non‑commercial license for experimentation. The pitch is clear: low‑latency, high‑naturalness speech that can be tailored to brand voice and deployed at scale.
