# Interaction Models: A Scalable Approach to Human-AI Collaboration
**Source**: https://thinkingmachines.ai/blog/interaction-models/
**Date**: 2026-05-11
**Author**: Thinking Machines
**Keywords**: interaction models, human-AI collaboration, real-time AI, multimodal, micro-turns, audio-video, full-duplex, interactivity, agentic AI

## Elevator pitch
Thinking Machines introduces "interaction models" — AI models trained from scratch to handle real-time, multimodal interaction natively rather than through external harnesses, enabling continuous two-way collaboration that feels more like working with a person than prompting a machine.

## Takeaways
- Current AI models operate on a single-thread turn-based paradigm that creates a bandwidth bottleneck for human-AI collaboration, pushing humans out of the loop not because they aren't needed but because the interface has no room for them
- Interaction models use 200ms "micro-turns" that interleave input and output streams, enabling simultaneous speech, proactive interjections, and time-awareness without artificial turn boundaries
- The system uses a dual-model architecture: a real-time interaction model for presence and responsiveness, paired with an asynchronous background model for deep reasoning, tool use, and agentic workflows
- The model achieves state-of-the-art combined performance across both intelligence benchmarks (Audio MultiChallenge, IFEval) and interactivity benchmarks (FD-bench), dominating in latency and interaction quality
- Training interactivity into the model itself (rather than bolting it on with voice-activity-detection harnesses) means it scales with model size — scaling makes it both smarter and a better collaborator

## Synthesis
Thinking Machines Lab, founded by former OpenAI researchers, has introduced a fundamentally different approach to human-AI interaction. Their "interaction models" treat interactivity as a first-class capability trained into the model from scratch, rather than something added through external scaffolding after the fact.

The core insight is that today's frontier models suffer from a collaboration bottleneck. They operate on a strict turn-based paradigm: the model waits for the user to finish, then generates a response, during which it perceives nothing. This creates a narrow, high-latency channel that limits how much human knowledge, intent, and judgment can reach the model. The team cites research showing that users of frontier models found interactive, synchronous use patterns disappointing compared to autonomous agent harnesses — but argues this is a failure of interface design, not evidence that humans should be removed from the loop.

The technical solution is ingenious. Instead of complete user-turns and model-responses, interaction models work in 200-millisecond "micro-turns." Input and output tokens are treated as continuous streams that are interleaved, so silence, overlap, and interruption remain part of the model's context. This eliminates the need for voice-activity-detection (VAD) components — dumb harness pieces that cannot distinguish between a thoughtful pause and a turn-yielding cue. The model can interject proactively ("tell me when I write a bug"), speak while listening (live translation), and maintain time-awareness ("how long did it take me to run that mile?").

Architecturally, the system splits responsibilities between two models sharing context. The interaction model stays present with the user in real-time, while a background model handles tasks requiring sustained reasoning — tool calls, browsing, planning. Results from the background model stream back asynchronously and are woven into the conversation at natural moments. This gives users both the responsiveness of a non-thinking model and the intelligence of a reasoning one.

The model uses encoder-free early fusion for multimodal inputs: audio enters as dMel spectrograms through a lightweight embedding layer, images are split into 40×40 patches encoded by an hMLP, and audio output uses a flow head. All components are co-trained with the transformer from scratch. This contrasts with approaches that use large standalone encoders (Whisper-like) or decoders (TTS model-like), which Thinking Machines argues introduces unnecessary complexity.

On the inference side, the team had to solve novel engineering challenges. Existing LLM serving libraries are optimized for large batches, not frequent small prefills. They implemented "streaming sessions" where the server appends 200ms chunks into a persistent GPU memory sequence, avoiding repeated memory allocations. This has been upstreamed to SGLang. They also optimized MoE kernels using a gather+gemv strategy instead of grouped gemm, following prior work from PyTorch and Cursor.

The benchmarks tell a compelling story. Their model, TML-Interaction-Small, dominates interactivity metrics — turn-taking latency of 0.40 seconds versus 0.57-2.14 seconds for competitors — while being more intelligent than any non-thinking model. On Audio MultiChallenge it scores 43.4% APR, competitive with GPT-Realtime-2.0's 48.5% thinking mode. On FD-bench V1.5 (measuring interruption handling, backchannel, and background speech), it scores 77.8 versus competitors' 39.0-54.3.

What's most significant is the philosophical stance. Thinking Machines explicitly invokes Sutton's "Bitter Lesson" — the principle that hand-crafted components will eventually be outpaced by general capabilities that leverage computation. By making interactivity part of the model rather than a harness, they ensure it benefits from scaling laws. A bigger model becomes not just smarter but a better collaborator.

Safety received novel treatment too. Real-time interaction stresses safety differently: refusals must sound colloquial in speech, and multi-turn conversations create new attack surfaces. The team generated refusal training data using TTS and automated red-teaming harnesses to maintain parity with text-based safety while sounding natural.

The implications for the industry are significant. Most real-time AI products today are Rube Goldberg machines of VAD, ASR, LLM, and TTS components. If Thinking Machines' approach proves scalable, it suggests a future where interaction quality is not a UX afterthought but an emergent property of model capability — and where the gap between prompt-and-response and genuine collaboration finally closes.
