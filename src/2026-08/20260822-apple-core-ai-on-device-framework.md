# Apple Core AI: On-Device Foundation Models for Developers
**Source**: https://developer.apple.com/documentation/coreai
**Date**: 2026-06-09
**Author**: Apple
**Keywords**: apple, on-device-ai, core-ai, swift, foundation-models, tool-calling, structured-generation

## Elevator pitch
Apple's Core AI framework, announced at WWDC 2026, gives developers Swift-native access to on-device foundation models with tool calling, structured generation, and full Apple Intelligence integration — no cloud round-trips, no API keys, no usage-based pricing.

## Takeaways
- First time Apple has opened its on-device models as a developer-facing framework: write Swift, define tools, and the model runs locally on the device
- Tool calling in Swift enables agentic workflows entirely on-device without a server — custom tools can be invoked by the local model
- Structured generation provides typed, schema-conforming outputs rather than raw text, eliminating post-processing hacks
- Apple Intelligence is now co-developed with Google using Gemini models, running on-device and through Private Cloud Compute with multimodal capabilities
- No cloud dependency means user data stays on-device with no API costs, rate limits, or cold starts
- Core AI ships with iOS 27, macOS 27, and the latest Xcode; documentation is live at developer.apple.com/documentation/coreai

## Synthesis
Apple's Core AI framework marks a significant shift in how the company positions its on-device AI capabilities for developers. Announced at WWDC 2026, the framework provides Swift-native access to Apple's on-device foundation models, enabling developers to build agentic workflows that run entirely on the user's device. This is the first time Apple has exposed its on-device models as a developer-facing API, moving from a closed system to an open developer platform.

The framework supports tool calling in Swift, meaning developers can define custom tools that the on-device model invokes during inference. This enables agentic patterns — agents that take actions, call functions, and chain operations — without any server round-trips. Combined with structured generation, which produces typed, schema-conforming outputs, the framework eliminates the common workaround of parsing raw text into structured data.

The bigger architectural story is Apple's partnership with Google. Apple Intelligence is now co-developed with Google using Gemini models as the foundation, running both on-device and through Private Cloud Compute. A system orchestrator automatically coordinates AI features across apps, providing multimodal capabilities including image generation, visual Q&A, and speech generation. This represents a departure from Apple's earlier ChatGPT integration approach at WWDC 2024.

The privacy and cost implications are significant for iOS and macOS developers. Models run locally with zero cloud dependency, meaning user data stays on-device with no API costs, rate limits, or network latency. Core AI ships with iOS 27, macOS 27, and the latest Xcode, and documentation is available at developer.apple.com/documentation/coreai.