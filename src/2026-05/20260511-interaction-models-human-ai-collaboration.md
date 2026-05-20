# Interaction Models: A Scalable Approach to Human-AI Collaboration
**Source**: https://thinkingmachines.ai/blog/interaction-models/
**Date**: May 11, 2026
**Author**: Thinking Machines Lab
**Keywords**: interaction models, human-AI collaboration, real-time AI, multimodal AI, speech-to-speech, full-duplex, micro-turns, Thinking Machines, AI interfaces, streaming AI, human-in-the-loop

## Elevator pitch
Thinking Machines Lab announces a research preview of "interaction models" — natively interactive AI trained from scratch to handle real-time audio, video, and text in continuous micro-turns, achieving both state-of-the-art responsiveness and competitive intelligence benchmarks, solving the "collaboration bottleneck" that push-turn-based models can't address.

## Takeaways
1. Current frontier AI models operate on a turn-based single-thread model that creates a "collaboration bottleneck" — humans get pushed out of the loop not because they're unnecessary, but because the interface has no room for them.
2. Thinking Machines' interaction model processes 200ms micro-turns continuously, enabling simultaneous speech, verbal/visual interjections, time-awareness, and concurrent tool use — all natively, without external harnesses.
3. The system splits into a real-time "interaction model" for responsiveness and an asynchronous "background model" for deep reasoning and agentic workflows, sharing context seamlessly.
4. On benchmarks, TML-Interaction-Small dominates interaction quality (FD-bench) while outperforming all non-thinking models on intelligence (Audio MultiChallenge), with the lowest turn-taking latency (0.40s vs 1.18s for GPT-Realtime-2.0 minimal).
5. The architecture uses encoder-free early fusion, batch-invariant kernels for training stability, and custom inference optimizations, with refusal safety calibrated for natural speech-based interactions.

## Synthesis
Thinking Machines Lab's announcement of "interaction models" represents a fundamental rethinking of how AI should interface with humans. The core argument is that the dominant turn-based paradigm — where the user speaks or types, the model processes, then responds — creates a "collaboration bottleneck" that artificially limits how much human knowledge, intent, and judgment can reach the model, and how much of the model's work the human can understand.

The team draws on communication theory to make its case: effective collaboration requires copresence (shared context), contemporality (real-time feedback), and simultaneity (concurrent production and reception). Current models fail on all three dimensions. As the authors note, even Anthropic's own model card acknowledges that autonomous, long-running agent harnesses "better elicited the model's coding capabilities" than interactive synchronous use — a concession that, as Thinking Machines points out, reveals how broken the current interaction paradigm is.

The technical innovation centers on a "time-aligned micro-turn" design. Rather than consuming a complete user turn and generating a complete response, the model continuously interleaves 200ms chunks of input processing and output generation across audio, video, and text. This eliminates artificial turn boundaries and the need for external harnesses like voice-activity-detection components. The result: the model can interject verbally when it notices a bug in code, translate simultaneously while the user speaks, or search the web concurrently while maintaining conversation.

The architecture splits intelligence across two cooperating models. A real-time "interaction model" handles presence and responsiveness — answering follow-ups, taking new input, maintaining conversational thread. When deeper reasoning is needed, it delegates to an asynchronous "background model" that handles planning, tool use, and agentic workflows, with results streamed back and interleaved naturally into the conversation. This split approach lets users benefit from both sub-second responsiveness and the full depth of reasoning models.

Benchmark results are impressive. TML-Interaction-Small achieves 77.8 on FD-bench V1.5 (vs. 54.3 for Gemini 3.1-flash-live minimal and 46.8 for GPT-Realtime-2.0 minimal), with turn-taking latency of just 0.40 seconds (vs. 1.18s for GPT-Realtime-2.0). On Audio MultiChallenge intelligence benchmarks, it scores 43.4 APR vs. 37.6 for GPT-Realtime-2.0 minimal and 26.8 for Gemini 3.1-flash-live minimal. With the background agent enabled, it becomes the top-performing instant model on streaming benchmarks that require reasoning or tool calls.

The safety approach is tailored to the real-time speech modality — using text-to-speech models to generate natural-sounding refusal training data and automated red-teaming for multi-turn robustness. If Thinking Machines can productize this technology, it could fundamentally reshape how people work with AI, moving from a prompting paradigm to genuine collaboration.
