# RCLI: On-Device Voice AI Assistant for macOS
**Source**: https://github.com/RunanywhereAI/rcli
**Date**: 2026-03-15
**Author**: RunanywhereAI
**Keywords**: voice AI, macOS, Apple Silicon, local inference, privacy, STT, TTS, RAG, on-device AI, Metal GPU

## Elevator pitch
RCLI runs a complete speech-to-text + LLM + text-to-speech + vision pipeline natively on Apple Silicon, enabling sub-200ms voice control of macOS without sending data to the cloud.

## Takeaways
- Full on-device pipeline: STT, LLM, TTS, and VLM all run on the Metal GPU without cloud dependencies, achieving sub-200ms end-to-end latency.
- Controls 40 macOS actions via voice including app launching, Spotify control, and messaging.
- Local RAG enables document querying without data leaving the device.
- On-device vision supports both camera and screen capture analysis.
- Built primarily in C++ (91.3%) with native macOS components; MIT licensed with a proprietary MetalRT GPU engine.
- v0.3.7 released March 15, 2026, with 133 commits indicating active development.

## Synthesis
RCLI represents one end of the spectrum in the current debate about local vs. cloud AI: a maximalist bet that consumer hardware is now capable enough to run a meaningful AI pipeline entirely on-device. The Apple Silicon value proposition—unified memory architecture with high-bandwidth access for both CPU and GPU—is what makes this technically feasible at consumer price points.

The privacy angle is the primary differentiator. Cloud-dependent voice assistants send audio, transcriptions, and queries to external servers by design. For users handling sensitive information—legal documents, financial data, personal communications—this is a meaningful concern that RCLI directly addresses. The local RAG feature extends this: document querying that never leaves the device solves a real problem for professionals who want AI assistance with confidential materials.

Sub-200ms latency is a usability threshold rather than just a benchmark number. Voice interaction feels natural below roughly 200ms; above it, the conversation rhythm breaks. Achieving this on-device at consumer hardware levels is a technical accomplishment that validates the Apple Silicon bet.

The architectural choice of C++ for the core engine reflects the performance requirements—Python bindings would introduce latency overhead incompatible with the real-time pipeline. The proprietary MetalRT GPU engine for the core inference layer, despite MIT licensing for the surrounding system, suggests the project's commercial strategy may involve the engine as a foundation for other products.
