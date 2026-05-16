# Interaction Models: A Scalable Approach to Human-AI Collaboration
**Source**: https://thinkingmachines.ai/blog/interaction-models/
**Date**: May 11, 2026
**Author**: Thinking Machines Lab
**Keywords**: interaction models, human-AI collaboration, real-time AI, multimodal, micro-turn, full-duplex, audio-video, Thinking Machines

## Elevator pitch
Thinking Machines Lab introduces "interaction models" — AI models that natively handle real-time, multimodal interaction without external scaffolding, enabling natural human-AI collaboration through simultaneous audio, video, and text streams.

## Takeaways
- Interaction models are trained from scratch to handle real-time interaction inherently, using a multi-stream micro-turn design (200ms chunks) rather than bolting interactivity onto turn-based models via harnesses.
- The architecture splits work between a real-time interaction model (for presence and responsiveness) and an asynchronous background model (for deep reasoning, tool use, and long-horizon work), sharing context between both.
- Key capabilities include seamless dialog management, verbal and visual interjections, simultaneous speech, time-awareness, and concurrent tool calls/search/UI generation — all happening continuously.
- The system uses encoder-free early fusion: minimal pre-processing of audio (dMel + embedding) and video (40x40 patches + hMLP), with all components co-trained from scratch.
- Inference is optimized with streaming sessions in SGLang (upstreamed), gather+gemv MoE kernels, and bitwise trainer-sampler alignment for deterministic training.

## Synthesis
Thinking Machines Lab's announcement of interaction models represents a fundamental rethinking of how AI systems should interface with humans. The core argument is compelling: current frontier models are optimized for autonomous work, not collaboration. They process reality in a single thread — waiting idly while the user speaks, freezing perception during generation — creating what the authors call a "collaboration bottleneck" that progressively pushes humans out of the loop.

The solution is architecturally elegant. Rather than scaffolding interactivity onto turn-based models (the "harness" approach used by most real-time speech systems), Thinking Machines trains interaction models natively in the continuous-time domain. The system operates in 200ms micro-turns, continuously interleaving input processing and output generation across audio, video, and text. There are no artificial turn boundaries, no voice-activity-detection components, no separate dialog management — the model itself tracks whether the speaker is thinking, yielding, self-correcting, or inviting a response.

The dual-model architecture is particularly clever. A real-time interaction model handles presence and responsiveness — it's what the user experiences directly. But when deeper reasoning is needed, it delegates to an asynchronous background model that handles planning, tool use, web browsing, and agentic workflows. The background model's results are woven back into the conversation as they arrive. This split means users get the full intelligence of reasoning models at the latency of non-thinking ones.

The encoder-free early fusion approach is also notable. Rather than relying on large, standalone encoders (Whisper-like for audio, separate TTS for output), audio enters as dMel features through a lightweight embedding layer, video as 40x40 patches through an hMLP, and audio output comes from a flow head — all co-trained from scratch with the transformer. This simplicity aligns with the "bitter lesson" principle that general, scalable approaches outperform hand-crafted components.

The inference optimization story reveals the depth of systems work required. Standard LLM inference libraries aren't designed for frequent small prefills with strict latency constraints. Thinking Machines implemented streaming sessions that append 200ms chunks into a persistent GPU sequence, avoiding repeated memory reallocations. They contributed this feature upstream to SGLang. They also optimized MoE kernels with gather+gemv strategies (as pioneered by PyTorch and Cursor) and achieved bitwise trainer-sampler alignment for deterministic training — a detail that suggests serious production engineering maturity.

The paper's benchmarks claim state-of-the-art combined performance in both intelligence and responsiveness, though the blog post is framed as a research preview rather than a production release. The framing is strategic: Thinking Machines positions interactivity not as a feature to be added after achieving intelligence, but as something that should scale alongside it. This challenges the dominant paradigm where labs chase benchmark scores first and worry about usability later.
