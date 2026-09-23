# How OpenAI Built GPT-Live
**Source**: ByteByteGo (bytebytego@substack.com)
**Date**: 2026-09-22
**Author**: ByteByteGo Team
**Keywords**: GPT-Live, OpenAI, voice AI, full-duplex, WebRTC, WARP, realtime serving, voice models, speech-to-speech, Moshi

## Elevator pitch
ByteByteGo's deep dive into OpenAI's GPT-Live-1 full-duplex voice model reveals the three generations of voice AI architecture, the engineering tricks that make real-time simultaneous listening and speaking possible, and the serving system optimizations that keep audio frames flowing at millisecond cadence.

## Takeaways
- **Three generations of voice systems**: Cascaded (ASR→LLM→TTS), turn-based speech-to-speech, and full-duplex — each solving the limitations of the previous, with full-duplex eliminating the turn detector entirely.
- **Separating talking from thinking**: GPT-Live's core innovation is delegation — a small, fast voice model handles conversation while a capable frontier model (GPT-5.5) performs reasoning and tool calls asynchronously, keeping the conversation flowing during expensive operations.
- **WARP protocol for fast session setup**: OpenAI built WebRTC Abridged Roundtrip Protocol to shrink the standard six-step WebRTC handshake to a single round trip, saving over a third of a second on mobile networks.
- **Cheap continuous inference via session pinning**: Each conversation stays loaded on one model instance in GPU memory, so only new audio frames are processed rather than re-reading the full conversation — a critical cost optimization for always-on models.
- **Managed handoff between model instances**: A replacement instance is prepared with the full conversation before the switch happens, enabling context compaction and instance rotation without interrupting the user.
- **Async path with pre-warming**: The frontier model session is created at conversation start and pre-loaded with context, so when the first delegation arrives, the model is ready to produce tokens immediately.
- **Evaluation requires p999, not p95**: In full-duplex systems, p95 events happen several times per minute, so the system must be engineered around p999 latency and fast recovery.
- **Silent launch as evaluation technique**: Routing a small percentage of sessions to a new system while users continue with the old one catches production issues that tests miss — like a CPU-side service running out of capacity before GPUs.

## Synthesis
This is a masterclass in real-time systems engineering. The article's greatest contribution is making the architectural leap from turn-based to full-duplex voice models comprehensible — the idea that the model continuously produces audio tokens (including silence tokens) on a fixed clock, and that turn detection becomes a learned behavior rather than a separate component, is the kind of paradigm shift that defines a generation of technology.

The delegation architecture — a small voice model for conversation, a large frontier model for thinking — is the most practically relevant insight for builders. It resolves the speed-quality tradeoff that has plagued voice AI: you no longer have to choose between a fast-but-dumb model and a slow-but-smart one. The voice model keeps the user engaged (acknowledging questions, thinking out loud) while the frontier model works asynchronously. This pattern generalizes beyond voice: any system with real-time constraints can benefit from separating the interactive layer from the reasoning layer.

The serving optimizations reveal how different full-duplex is from traditional request-response serving. Session pinning (keeping a conversation in GPU memory), managed handoffs (preparing replacement instances before switching), and WARP (collapsing the connection setup) are all responses to the fundamental constraint that audio frames must arrive on a fixed clock. The p999 requirement is particularly striking: in a system that runs continuously, traditional percentile targets are meaningless because slow frames are guaranteed in every session. This shifts the engineering focus from preventing slow frames to recovering from them fast.

The evaluation section is a gift to any team building real-time AI systems. The three-layer approach — conversational behavior scoring, stream health monitoring, and silent launch testing — is a complete framework that most teams haven't articulated this clearly. The insight that "users hear the worst frame" and therefore average latency is an insufficient metric should be taped to the wall of every voice AI engineering team.