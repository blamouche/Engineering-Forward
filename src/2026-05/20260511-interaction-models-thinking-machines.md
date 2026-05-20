# Interaction Models: A Scalable Approach to Human-AI Collaboration
**Source**: https://thinkingmachines.ai/blog/interaction-models/
**Date**: May 11, 2026
**Author**: Thinking Machines Lab
**Keywords**: interaction models, human-AI collaboration, real-time AI, multimodal AI, audio-video models, micro-turns, full-duplex, AI interfaces, Thinking Machines

## Elevator pitch
Thinking Machines Lab introduces "interaction models" — AI models trained natively for real-time, multimodal human collaboration using micro-turns and concurrent input/output streams, moving beyond the turn-based paradigm that pushes humans out of the loop.

## Takeaways
- Current AI interfaces are turn-based, creating a narrow bandwidth that limits how much human knowledge and intent can reach the model
- Interaction models use 200ms micro-turns to process continuous audio/video/text streams, enabling natural collaboration with interjections, simultaneous speech, and real-time tool use
- The system splits work between a real-time interaction model (responsive, present) and an asynchronous background model (deep reasoning, tool use, agentic workflows)
- Encoder-free early fusion — minimal pre-processing of audio (dMel) and video (40x40 patches) that's co-trained with the transformer — avoids the "harness" approach that most real-time systems rely on
- Key capabilities include seamless dialog management, verbal and visual interjections, simultaneous speech, time-awareness, and concurrent tool calling while conversing

## Synthesis
Thinking Machines Lab's announcement of "interaction models" represents a fundamental rethinking of how AI should work with humans. The core insight is that the dominant turn-based interaction paradigm — you type/speak, the model responds, repeat — is actively harmful to collaboration. It creates what they call a "bandwidth bottleneck" where human knowledge, intent, and judgment cannot fully reach the model, and the model's ongoing work cannot be fully understood by the human.

The technical approach is ambitious and distinctive. Rather than bolting interactivity onto an existing model through external scaffolding (voice activity detection, turn boundary prediction, separate TTS systems), they train interactivity directly into the model. The key architectural decision is time-aligned micro-turns: 200ms chunks of continuous interleaved input and output tokens. This is fundamentally different from the alternating token sequences that turn-based models see. In the interaction model, silence, overlap, interruption, and timing remain part of the model's native context — there are no artificial turn boundaries.

The system architecture splits responsibilities cleverly. A real-time interaction model maintains constant presence with the user, handling conversation flow, interjections, and quick responses. When deeper reasoning is needed, it delegates to an asynchronous background model that handles sustained reasoning, tool use, browsing, and other long-horizon tasks. Both share context, and the background model's results are woven back into the conversation naturally. This split lets users benefit from both responsiveness and full intelligence — planning and agentic workflows at the latency of non-thinking models.

The encoder-free early fusion approach is also noteworthy. Rather than using separate large encoders (Whisper-like for audio, ViT-like for video), they apply minimal pre-processing — dMel spectrograms for audio, 40x40 patches with a lightweight hMLP for video — and co-train everything from scratch. This means scaling the model improves both intelligence and interactivity simultaneously, following the "bitter lesson" that general-purpose learning outperforms hand-crafted components.

The practical implications are significant. Capabilities like proactive interjections ("interrupt when I say something wrong"), reactions to visual cues ("tell me when I've written a bug"), simultaneous speech (live translation), and concurrent tool use while conversing all emerge from the architecture rather than requiring special-purpose harnesses. It's a vision of AI interaction that feels more like collaborating with a colleague and less like prompting a tool — and it may represent the direction that AI interfaces need to go for humans to remain genuinely "in the loop" as models become more capable.
