# Microsoft Announces 3 New MAI Models: Transcribe, Voice, and Image
**Source**: https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/
**Date**: April 2, 2026
**Author**: Mustafa Suleyman (Microsoft AI)
**Keywords**: Microsoft, MAI, MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2, Azure, Foundry, speech-to-text, voice generation

## Elevator pitch
Microsoft releases three MAI models — speech-to-text (2.5x faster, #1 on FLEURS for 11 languages), voice generation (60s audio in 1s, custom voice cloning), and image generation (2x faster) — available in Azure Foundry.

## Takeaways
- MAI-Transcribe-1: 2.5x faster batch transcription than existing Azure offerings, ranked #1 on FLEURS for 11 core languages, $0.36/hour
- MAI-Voice-1: custom voice creation from seconds of audio, generates 60s of audio in 1s, 90ms time-to-first-audio, $22/1M characters
- MAI-Image-2: 2x faster than previous generation, optimized for skin tones and in-image text, top 3 on Arena.ai, $5/1M input tokens
- All three available through Microsoft Foundry and MAI Playground with built-in safety guardrails
- WPP using MAI-Image-2 at scale for enterprise adoption

## Synthesis
Microsoft's simultaneous release of three multimodal models across speech, voice synthesis, and image generation signals a deliberate push to compete across the full multimodal API stack rather than selectively. The naming convention — MAI (Microsoft AI) rather than Azure-prefixed — positions these as flagship models that reflect Microsoft's AI research capabilities, distinct from Azure's cloud infrastructure branding.

MAI-Transcribe-1's position as first on FLEURS for 11 core languages is significant given that Cohere also launched a state-of-the-art ASR model (Transcribe) in the same news cycle. Both models are claiming top performance on open benchmarks, indicating that the ASR space is experiencing a capability step-up with multiple providers releasing competitive models simultaneously. The $0.36/hour pricing is aggressive, likely intended to displace established cloud ASR services with favorable unit economics.

MAI-Voice-1's custom voice creation from seconds of audio is a capability with both creative and professional applications. The ability to create a synthetic voice that matches a specific person's characteristics from a short sample enables personalized AI assistants, consistent brand voices, and accessibility applications. The 90ms time-to-first-audio is the metric that determines whether voice generation is suitable for interactive applications — below ~150ms, users do not perceive the delay as unnatural.

MAI-Image-2's enterprise adoption by WPP provides a real-world validation point. WPP's scale — one of the world's largest advertising companies — implies high-volume image generation for campaigns across many clients. If MAI-Image-2 handles this at quality and cost that WPP accepts, it demonstrates production-ready performance for commercial image generation workflows.

The competitive implication is that Microsoft is now offering viable alternatives to OpenAI's APIs (DALL-E, Whisper, TTS) across all three modalities directly through Azure Foundry. Organizations that have built Azure-centric AI infrastructure can expand their multimodal capabilities without introducing additional vendor relationships.
