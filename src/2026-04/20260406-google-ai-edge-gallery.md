# Google AI Edge Gallery

**Source**: https://simonwillison.net/2026/Apr/6/google-ai-edge-gallery
**Date**: April 6, 2026
**Author**: Simon Willison
**Keywords**: Gemma, on-device AI, iPhone, local models, mobile AI

## Elevator pitch
Simon Willison highlights Google’s new iPhone app for running small Gemma models locally, framing it as an important milestone in turning vendor-hosted models into consumer on-device products.

## Takeaways
- Google released an official iPhone app that runs Gemma 4 and some Gemma 3 family models locally.
- The app supports image Q&A, short audio transcription, and a skills demo with interactive widgets.
- Willison says the experience is surprisingly useful and fast for a 2.54GB on-device model.
- The product is notable because it is an official first-party distribution channel for local models on mobile.
- The current version still looks early, with missing logs and some instability in follow-up interactions.

## Synthesis
This short note is valuable because it points to something bigger than the app itself: model vendors are starting to ship polished consumer experiences for local inference. That changes the conversation from “can open models run on phones?” to “what kinds of products become possible once first-party mobile distribution is normal?”

Google’s app matters partly because Gemma has mostly been framed as a developer model family. Packaging it into a usable iPhone app turns that capability into a product signal. It suggests the frontier between research model, open-weight model, and consumer app is collapsing faster than many expected.

The feature set is also revealing. Image Q&A, short transcription, and tool-like widget demos are exactly the kinds of constrained experiences that fit local models well: privacy-sensitive, latency-sensitive, and bounded enough to work on-device. That is likely where local mobile AI will win first.

The rough edges matter too. Missing persistent logs and occasional freezes show that local AI productization is still immature. But the direction is clear: vendors are no longer treating mobile on-device inference as a side experiment. They are starting to ship it as a mainstream surface.
