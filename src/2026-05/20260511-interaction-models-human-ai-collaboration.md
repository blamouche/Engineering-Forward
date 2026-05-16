# Interaction Models: A Scalable Approach to Human-AI Collaboration
**Source**: https://thinkingmachines.ai/blog/interaction-models/
**Date**: May 11, 2026
**Author**: Thinking Machines Lab
**Keywords**: interaction models, human-AI collaboration, real-time AI, multimodal, audio-video, micro-turns, full-duplex, Thinking Machines Lab

## Elevator pitch
Thinking Machines Lab introduces "interaction models" — AI models that natively handle real-time, multimodal interaction (audio, video, text) without external scaffolding, featuring continuous micro-turn processing that enables seamless collaboration at state-of-the-art intelligence and responsiveness.

## Takeaways
- Interaction models use 200ms micro-turns with time-aligned concurrent input/output streams, eliminating artificial turn boundaries that plague current real-time systems relying on voice-activity-detection harnesses
- A split architecture pairs a real-time interaction model with an asynchronous background model for deeper reasoning, tool use, and agentic workflows — achieving reasoning-model intelligence at non-thinking-model latency
- The model (TML-Interaction-Small) dominates interaction quality benchmarks (FD-bench v1.5: 77.8 vs nearest competitor's 54.3) while being more intelligent than any non-thinking model on Audio MultiChallenge
- Encoder-free early fusion with co-trained audio/video embeddings avoids the separate encoder-decoder paradigm (Whisper, TTS), enabling joint scaling of intelligence and interactivity
- Safety work addressed modality-appropriate refusals (colloquial speech refusals) and long-horizon robustness through automated multi-turn red-teaming

## Synthesis
On May 11, 2026, Thinking Machines Lab published a research preview of "interaction models," representing a fundamental architectural shift in how AI handles human collaboration. The core insight is that interactivity should scale alongside intelligence — it should be part of the model itself rather than bolted on through external scaffolding like voice-activity-detection (VAD) components.

The technical design centers on 200ms micro-turns. Rather than the traditional turn-based paradigm where the model waits for complete user input before generating a complete response, the interaction model continuously interleaves processing 200ms of input with generating 200ms of output. This time-aligned approach means silence, overlap, and interruption remain part of the model's context — enabling natural conversation patterns like simultaneous speech (live translation) and proactive interjections ("interrupt when I say something wrong").

The system splits between two models: a real-time interaction model handling continuous presence, and an asynchronous background model for sustained reasoning, tool calling, and web browsing. The background model streams results back to the interaction model, which integrates them conversationally. This achieves what the authors describe as "reasoning-model intelligence at non-thinking-model latency."

Benchmark results position TML-Interaction-Small at a combined intelligence-interactivity frontier. On FD-bench v1.5 (measuring interrupt handling, backchanneling, background speech), it scores 77.8 versus the nearest competitor's 54.3. On Audio MultiChallenge (intelligence), it scores 43.4 versus GPT-Realtime-2.0's 37.6. The model achieves turn-taking latency of 0.40 seconds versus 1.18 seconds for GPT-Realtime-2.0.

The architectural choices are notable: encoder-free early fusion with dMel audio embeddings and hMLP image patches, all co-trained from scratch with the transformer. This contrasts with most omnimodal models that require separate encoders (Whisper-like for audio) and decoders (TTS for output). Inference optimization includes "streaming sessions" that maintain persistent GPU memory sequences to avoid per-chunk overhead, and batch-invariant kernels for training stability.

This work from Mira Murati's Thinking Machines Lab positions the company as pursuing a differentiated technical path from both OpenAI and Anthropic — betting that native interactivity, rather than pure intelligence benchmarks, represents the next frontier for useful AI.
