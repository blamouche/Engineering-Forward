# OpenOats: A Meeting Note-Taker That Talks Back
**Source**: https://github.com/yazinsai/OpenGranola
**Date**: 2026-03-20
**Author**: yazinsai
**Keywords**: meeting notes, macOS, transcription, LLM, knowledge base, privacy, Apple Silicon, Ollama

## Elevator pitch
OpenOats is a privacy-first macOS app that transcribes conversations in real time and surfaces relevant information from your personal knowledge base during calls, running entirely on-device using Apple Silicon speech recognition.

## Takeaways
- Real-time transcription of both conversation participants with knowledge base lookup surfacing relevant context automatically
- Fully offline speech recognition via Apple's Speech framework—audio never leaves the device
- Supports local (Ollama) or cloud (OpenRouter) LLMs; when using cloud, only text is transmitted, never audio
- Hidden from screen sharing by default for discretion in remote calls
- Available via Homebrew, DMG, or source (Swift 6.2); MIT licensed

## Synthesis
OpenOats addresses a common gap in AI-assisted work: the inability to access your own knowledge during live conversations. While AI tools have become excellent at processing information before or after meetings, they have been mostly absent from the meeting itself. OpenOats changes this by running continuously during calls, transcribing speech, and proactively surfacing relevant material from a user's personal knowledge base at the moment it's needed.

The privacy architecture is the project's most distinctive engineering decision. Apple's native Speech framework handles transcription entirely on-device using the power of Apple Silicon, meaning audio data never traverses a network. This is not merely a privacy policy choice—it is an architectural constraint enforced at the hardware level. Users concerned about recording compliance or confidentiality can verify that their audio stays local without relying on vendor promises.

The intelligence layer is modular. Users can route LLM queries to Ollama for fully local processing or to cloud providers via OpenRouter when more capable models are needed. The critical privacy distinction: when cloud providers are used, only text is transmitted. The voice-to-text conversion happens locally first, stripping the personal dimension of the recording before any external service sees the content.

The "hidden from screen sharing" feature reflects practical deployment thinking. Enterprise users in remote meetings regularly share their screens; an AI assistant surfacing suggestions in a visible overlay could create awkward dynamics or violate meeting norms. Running hidden by default respects context while preserving functionality.

The knowledge base integration uses embeddings from Voyage AI or compatible endpoints, enabling semantic search across stored documents. The pipeline tracks conversation state, ranks relevance, and generates suggestions without requiring the user to formulate explicit queries. This ambient intelligence model—where context is provided automatically rather than retrieved on demand—represents an emerging interaction pattern for professional AI tools.
