# Introducing Computer Use in Gemini 3.5 Flash
**Source**: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/
**Date**: 2026-06-24
**Author**: Mateo Quiros (Google DeepMind)
**Keywords**: Google, Gemini, computer use, agents, agentic AI, Gemini 3.5 Flash

## Elevator pitch
Google has built computer use natively into Gemini 3.5 Flash, enabling agents that can see, reason, and act across browser, mobile, and desktop environments — a significant evolution from the standalone Gemini 2.5 computer-use model.

## Takeaways
- Computer use is now a built-in capability in Gemini 3.5 Flash, not a separate model — simplifying deployment
- The model can interact across browser, mobile, and desktop environments, enabling enterprise automation tasks
- Google includes targeted adversarial training to mitigate prompt injection risks for agents in live environments
- Two optional enterprise safeguard systems are available: explicit user confirmation for sensitive actions and automatic task stopping on injection detection
- Early customers include Browserbase, Browser Use, and UiPath for agentic automation
- Developers can start building via Gemini API and Gemini Enterprise Agent Platform
- The integration signals that computer use is moving from experimental to production-grade

## Synthesis
Google's decision to embed computer use directly into Gemini 3.5 Flash rather than keeping it as a separate specialized model is a meaningful architectural and product signal. Previously, computer use was available only through a standalone Gemini 2.5 model, requiring developers to manage a separate endpoint. By making it a built-in tool in the main Flash model — alongside existing capabilities like function calling, Search grounding, and Maps grounding — Google is telling developers that computer use is no longer an experiment; it's a first-class capability.

The technical approach emphasizes safety-in-depth. Rather than relying solely on prompt-level defenses, Google offers two enterprise safeguard systems: one that requires explicit user confirmation for irreversible actions, and another that automatically halts tasks if indirect prompt injection is detected. This "defense-in-depth" approach is critical because agents operating in live environments face fundamentally different threat models than chat-based AI. An agent with browser access can be manipulated through the web pages it visits, not just through direct user prompts.

The benchmarks and partnerships signal production readiness. Browserbase, Browser Use, and UiPath are early adopters, representing a spectrum from browser automation to enterprise RPA. The availability through both the Gemini API and the Enterprise Agent Platform means developers can start small and scale to enterprise deployments without changing tooling.

For the engineering community, the key insight is that agentic AI is converging on a small set of interaction paradigms: function calling for structured APIs, tool use for bounded environments, and computer use for open-ended GUI interaction. Google's move makes all three available in a single model, reducing the complexity of building multi-modal agents.