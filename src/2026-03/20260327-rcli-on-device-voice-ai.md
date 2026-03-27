# RCLI: On‑device voice AI for macOS
**Source**: https://github.com/RunanywhereAI/rcli
**Date**: Unknown
**Author**: RunAnywhereAI
**Keywords**: on-device, voice AI, macOS, local inference, RAG

## Elevator pitch
RCLI is a fully local voice AI stack for Apple Silicon that combines STT, LLM, TTS, vision, and macOS actions with sub‑200ms latency and no cloud dependency.

## Takeaways
- End‑to‑end on‑device pipeline: STT + LLM + TTS + VLM with local RAG.
- Supports ~40 macOS actions via AppleScript/shell with voice control.
- Uses MetalRT on M3+ for high‑speed GPU inference; M1/M2 fall back to llama.cpp.
- Provides a TUI for push‑to‑talk, model management, actions, and diagnostics.
- Includes document ingestion for local Q&A with hybrid retrieval.

## Synthesis
RCLI is positioned as an offline, on‑device voice assistant for macOS, built specifically for Apple Silicon. The project bundles a complete speech pipeline—voice activity detection, streaming and offline transcription, LLM reasoning, and TTS—alongside a vision module for camera and screen analysis. Everything runs locally, avoiding cloud latency or API keys.

A central differentiator is MetalRT, a proprietary GPU inference engine optimized for Apple Silicon (M3+). It claims high throughput and sub‑200ms voice interaction latency. For earlier chips, RCLI falls back to open‑source llama.cpp, keeping the system functional on M1/M2. The tooling wraps these engines in a unified CLI and TUI, allowing model downloads, hot‑swaps, and live hardware monitoring.

RCLI also targets productivity by wiring the LLM to macOS actions. Users can control system functions, media apps, and shortcuts by voice. The assistant supports local RAG: documents are ingested into a hybrid retrieval index, and queries can be answered with grounded context. Vision features let users query images, camera frames, or screen captures.

The project emphasizes practical usability: one‑line install via brew or script, a guided setup that downloads ~1GB of models, and built‑in actions for common workflows. It highlights a growing trend toward local, privacy‑preserving AI assistants that trade model size for low latency and full on‑device control.
