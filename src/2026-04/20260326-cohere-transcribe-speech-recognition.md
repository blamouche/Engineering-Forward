# Cohere Transcribe: State-of-the-Art Speech Recognition
**Source**: https://cohere.com/blog/transcribe
**Date**: March 26, 2026
**Author**: Cohere Team
**Keywords**: speech recognition, ASR, Cohere, transcription, enterprise AI, open source

## Elevator pitch
Cohere launches Transcribe, a 2B-parameter conformer model achieving 5.42% word error rate and top rank on HuggingFace's Open ASR Leaderboard, combining best-in-class accuracy with production-ready throughput for enterprise deployments.

## Takeaways
- Transcribe achieves 5.42% WER, ranking first on HuggingFace's Open ASR Leaderboard, surpassing OpenAI's Whisper and ElevenLabs Scribe
- Built on a conformer-based encoder-decoder architecture with 2 billion parameters, supporting 14 languages
- Available under Apache 2.0 license via HuggingFace, Cohere API with free tier, and Model Vault managed inference
- Extends Cohere's platform beyond language models into multimodal AI for enterprise speech intelligence
- Outperforms competitors in both accuracy and throughput metrics without requiring trade-offs between speed and quality

## Synthesis
Cohere has unveiled Transcribe, a new automatic speech recognition model designed to advance enterprise speech intelligence capabilities. The model represents a significant achievement in accuracy and practical deployment, addressing a growing need as speech becomes central to AI-enabled business workflows.

The standout feature is Transcribe's accuracy. With a word error rate of 5.42%, the model currently ranks first on HuggingFace's Open ASR Leaderboard, surpassing competitors including OpenAI's Whisper Large v3 and ElevenLabs Scribe v2. This performance holds across diverse real-world scenarios including multi-speaker environments, varying acoustics, and diverse accents. The company validated findings through human preference evaluations where annotators assessed transcription quality across multiple languages, with Transcribe outperforming alternatives while preserving meaning and avoiding hallucinations that plague some systems.

Built on a conformer-based encoder-decoder architecture, Transcribe processes audio waveforms by converting them to log-Mel spectrograms for analysis. The 2-billion parameter model balances accuracy with efficiency. The system supports 14 languages spanning European, Asia-Pacific, and Middle Eastern regions, reflecting global business needs.

Throughput performance distinguishes Transcribe operationally. The model sustains best-in-class processing speeds within its parameter tier. This combination of accuracy and speed addresses practical constraints: slow transcription impacts user experience and operational costs even when accurate. Transcribe extends the Pareto frontier, delivering exceptional accuracy without sacrificing performance.

The model is openly available through HuggingFace under an Apache 2.0 license, enabling local deployment and edge computing scenarios. Alternatively, enterprises can access Transcribe through Cohere's API with free tier options, or through Model Vault for production workloads without infrastructure management overhead.

Cohere positions Transcribe as the foundation for broader speech intelligence capabilities. Future integration with North, their enterprise AI orchestration platform, suggests evolution toward sophisticated speech analytics, meeting transcription, and real-time customer support applications.

The release signals Cohere's expansion beyond language models into multimodal AI. Speech recognition, historically dominated by specialized providers or massive tech companies, now has a credible open alternative optimized for enterprise contexts. The commitment to open-source distribution democratizes access while Model Vault monetization provides sustainable commercial pathways. Performance gains reflect deliberate optimization for real-world conditions rather than benchmark gaming.
