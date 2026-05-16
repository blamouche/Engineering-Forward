# Interaction Models: A Scalable Approach to Human-AI Collaboration
**Source**: https://thinkingmachines.ai/blog/interaction-models/
**Date**: May 11, 2026
**Author**: Thinking Machines
**Keywords**: interaction models, human-AI collaboration, real-time AI, full-duplex, multimodality, micro-turns, Thinking Machines Lab, Mira Murati, AI architecture, streaming inference, SGLang

## Elevator pitch
Thinking Machines Lab announces a research preview of "interaction models"—AI models trained from scratch to handle real-time, multimodal interaction natively rather than through external scaffolding, enabling continuous two-way collaboration across audio, video, and text with simultaneous tool calls, achieving state-of-the-art combined performance in intelligence and responsiveness.

## Takeaways
- Interaction models are trained from scratch for native real-time interaction across audio, video, and text, rather than bolting interactivity onto turn-based models with external Voice Activity Detection harnesses.
- The architecture uses 200ms "micro-turns" with interleaved input and output streams, enabling near real-time concurrency including simultaneous speech, visual interjections, and parallel tool calls.
- A split design pairs a real-time interaction model with an asynchronous background model for deeper reasoning and agentic workflows, giving users both responsiveness and full intelligence.
- The system adopts encoder-free early fusion: minimal pre-processing of audio (dMel embeddings) and video (40x40 patches via hMLP), with all components co-trained from scratch.
- Inference optimizations include streaming sessions contributed to SGLang, gather+gemv MoE kernels, and bitwise trainer-sampler alignment with minimal (<5%) end-to-end performance overhead.

## Synthesis
Thinking Machines Lab's announcement of interaction models represents one of the most architecturally ambitious proposals in the current AI landscape. Rather than accepting that interactivity is something you layer onto a model after the fact—the approach taken by virtually all commercial real-time AI systems today—the team argues that interactivity should be a first-class property of the model itself, scaling alongside intelligence as models grow larger and training data expands.

The framing argument is compelling: current frontier models experience reality as a single thread. Until the user finishes speaking or typing, the model waits, blind to what the user is doing or how they are doing it. Until the model finishes generating, its perception freezes. This creates what the authors call a "collaboration bottleneck"—a narrow channel that limits how much of a person's knowledge, intent, and judgment can reach the model, and how much of the model's work can be understood. The analogy to trying to resolve a crucial disagreement over email rather than in person is apt.

The technical architecture is built around two key ideas. First, "micro-turns" of roughly 200ms—continuously interleaving input processing and output generation rather than treating turns as discrete alternating blocks. This means silence, overlap, and interruption all remain part of the model's context rather than being handled by an external harness. Second, a split between a real-time interaction model and an asynchronous background model: the interaction model maintains continuous presence and responsiveness while delegating deeper reasoning, tool use, and longer-horizon work to the background model, integrating results as they arrive. Both models are intelligent (the interaction model alone is competitive on benchmarks), creating a system where users get the planning power of reasoning models at the latency of non-thinking ones.

Several implementation details are notable. The encoder-free early fusion approach—using lightweight embedding layers rather than large standalone encoders for audio and video—is philosophically aligned with the "bitter lesson" principle that general learning beats hand-crafted components. The inference optimizations are practical: existing LLM inference libraries are not designed for frequent small prefills, so the team implemented streaming sessions and contributed a version upstream to SGLang. The gather+gemv strategy for MoE kernels (borrowing from prior work at PyTorch and Cursor) and bitwise trainer-sampler alignment for debugging are engineering details that signal production-level thinking, not just a research paper.

The capabilities list is ambitious: seamless dialog management without external turn-detection, proactive verbal and visual interjections, simultaneous speech, time-awareness, and concurrent tool calls while speaking. The implicit argument is that all of these interaction modes—which today require separate, hand-crafted harnesses—should be emergent properties of a single scaled model. If successful, this would represent a meaningful step toward AI interfaces that meet humans where they are, rather than forcing humans to adapt to AI's limitations.
