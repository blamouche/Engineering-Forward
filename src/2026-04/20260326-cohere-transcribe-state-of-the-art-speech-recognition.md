# Cohere Transcribe: state-of-the-art speech recognition
**Source**: https://cohere.com/blog/transcribe
**Date**: March 26, 2026
**Author**: Cohere Team
**Keywords**: speech recognition, ASR, automatic speech recognition, transcription, Conformer, multilingual, open-source, enterprise

## Elevator pitch
Cohere releases Transcribe, an open-source 2B-parameter ASR model that achieves 5.42% word error rate to top HuggingFace's Open ASR Leaderboard, outperforming Whisper Large v3 across 14 languages with Apache 2.0 licensing.

## Takeaways
- 5.42% word error rate places Transcribe at the top of HuggingFace's Open ASR Leaderboard, beating both open and closed-source alternatives
- 2-billion parameter Conformer encoder-decoder architecture supports 14 languages across European, Asia-Pacific, and MENA regions
- Apache 2.0 license enables unrestricted commercial use and modification
- Available via open-source download, API integration, or managed inference through Model Vault
- Plans for deeper integration with North (Cohere's agent orchestration platform) will extend Transcribe into broader speech intelligence

## Synthesis
Cohere's entry into the ASR space with Transcribe is notable primarily for its competitive positioning: by targeting the top of HuggingFace's Open ASR Leaderboard and explicitly claiming to outperform Whisper Large v3, Cohere is directly challenging the model that has dominated open-source speech recognition since OpenAI released it. Whisper's dominance was such that many organizations treating it as a commodity infrastructure component, so displacing it requires demonstrating a meaningful gap in performance.

The 5.42% word error rate is the headline metric, and the Conformer architecture — which combines convolutional neural network layers for local feature extraction with transformer attention for global context — is a proven choice for production ASR systems. At 2 billion parameters, Transcribe sits in a weight class that requires serious compute for training but is manageable for inference, particularly with the managed deployment option through Model Vault.

The 14-language coverage is useful but the specific language set (European, Asia-Pacific, MENA) will determine how broadly the model is adopted. Enterprise ASR deployments are increasingly multilingual, and any language gaps represent a significant barrier for multinational organizations.

The Apache 2.0 licensing is strategically important. OpenAI's Whisper is also open-source, so Cohere matching or exceeding Whisper's performance under a similarly permissive license removes a key reason to stick with the incumbent. For organizations that have built internal ASR infrastructure on Whisper, the switching cost is primarily integration work rather than licensing negotiation.

The roadmap toward North integration is the most commercially interesting element. Pure transcription is a commoditizing capability; the differentiated value lies in what happens after the audio is converted to text. If Transcribe can serve as the audio input layer for North's agent orchestration, Cohere gains a pathway from ASR into enterprise speech intelligence use cases — meeting summarization, call center analytics, real-time compliance monitoring — where the combination of accurate transcription and intelligent downstream processing creates defensible differentiation.

For engineering teams evaluating ASR options, Transcribe adds a strong competitor to an already crowded space. The decision between Transcribe, Whisper variants, and cloud ASR services will ultimately depend on the language coverage match, infrastructure constraints, and whether the North integration roadmap aligns with the organization's agent strategy.
