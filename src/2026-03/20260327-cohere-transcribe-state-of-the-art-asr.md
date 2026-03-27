# Cohere Transcribe: state-of-the-art speech recognition
**Source**: https://cohere.com/blog/transcribe
**Date**: Unknown
**Author**: Cohere
**Keywords**: ASR, speech recognition, open weights, Conformer, WER

## Elevator pitch
Cohere releases Transcribe, a 2B‑parameter open‑weights ASR model that tops the Open ASR Leaderboard while maintaining production‑ready throughput.

## Takeaways
- Open‑weights Conformer model trained from scratch; Apache 2.0 license.
- Supports 14 languages across European, APAC, and MENA regions.
- Ranks #1 on Hugging Face’s Open ASR Leaderboard (avg WER 5.42%).
- Designed for practical deployment with strong throughput (RTFx).
- Available via Hugging Face, Cohere API, and Model Vault.

## Synthesis
Cohere’s Transcribe is positioned as a production‑grade ASR model, not just a research demo. The 2B‑parameter Conformer encoder‑decoder is trained from scratch to minimize word error rate while keeping inference efficiency high. Cohere emphasizes that this combination—low WER and fast throughput—matters more than raw accuracy alone for real‑world transcription workloads.

Benchmark results show Transcribe leading the Open ASR Leaderboard with a 5.42% average WER, beating Whisper Large v3 and other proprietary or open alternatives. Cohere also highlights human preference evaluations where transcripts are judged on accuracy, coherence, named‑entity handling, and hallucination avoidance, claiming strong real‑world quality across multiple languages.

The model supports 14 languages and is released under Apache 2.0, enabling local or edge deployment. Cohere also offers managed access via Model Vault and an API for experimentation and enterprise use, signaling a dual strategy of open distribution plus commercial hosting.

Overall, the release signals a push to make high‑quality speech recognition a first‑class enterprise component, with Transcribe serving as a foundation for broader speech intelligence workflows within Cohere’s North platform.
