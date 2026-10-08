# Building Resilient Systems with Sam Newman: Microservices, Cognitive Surrender, and Modular AI Architecture
**Source**: The Pragmatic Engineer (pragmaticengineer@substack.com)
**Date**: 2026-10-07
**Author**: Gergely Orosz / The Pragmatic Engineer
**Keywords**: Sam Newman, microservices, distributed systems, resilience, Building Resilient Distributed Systems, cognitive surrender, cognitive debt, AI in software development, modular architecture, observability, idempotency, independent deployment

## Elevator pitch
Sam Newman — author of "Building Microservices" — joins the Pragmatic Engineer podcast to discuss when to use microservices (they're an architecture of "last resort"), his three rules of distributed systems, how AI is changing software development, and why we must resist "cognitive surrender" to LLMs. Plus: his new book "Building Resilient Distributed Systems."

## Takeaways
- Sam was in the room when the term "microservices" was coined at an architecture symposium in the Lake District in the early 2010s, when James Lewis pitched "micro apps" and someone suggested "microservices"
- Microservices defined: (1) independently deployable services — the clear definition, and (2) services split by business function rather than technical layer — the softer definition
- Three rules of distributed systems: information takes time to travel, sometimes the thing you want to talk to isn't there, and resources are not infinite. Most outages are caused by #3 (resource pools running out)
- Four concepts of resiliency (from David Woods): robustness (continue functioning), rebound (recover quickly), extensibility (deal with surprises), and adaptability (change to support new functions)
- Idempotency: two approaches — idempotency keys (clean but hard to retrofit) vs fingerprints (easy to retrofit but can reject legitimate requests)
- On AI: hedge vendor options, aim to be multi-vendor/multi-model, and consider swapping LLM-powered functionality for deterministic code that runs faster and cheaper
- "Cognitive surrender": AI is causing more context switching and less critical thinking, not freeing us from drudgery as promised. "The original pitch of AI was it was going to free us from drudgery... However, much of our current use of AI is not freeing us up from critical thinking!"
- LLMs are not world models: "they have no concept of causality... I think we expect LLMs to do more than they actually can do, because they seem so smart"
- Starting with modules encourages better software architecture: think about module boundaries first, then let AI roam freely but only inside the module structure you designed

## Synthesis
Sam Newman's framing of microservices as an "architecture of last resort" is a powerful corrective to the industry's decade-long love affair with distributed systems. His three rules — distilled from the eight fallacies of distributed computing — are the kind of practical wisdom that comes from decades of consulting. The observation that most outages come from resource exhaustion (#3) rather than network partitions is actionable: teams should focus their resilience engineering on capacity planning and resource pooling before investing in circuit breakers.

The "cognitive surrender" concept is the most important takeaway for the AI era. Sam distinguishes between using AI to free us from drudgery (good) and using AI in ways that reduce critical thinking (bad). His observation that people are working longer hours with more context switching — not necessarily AI's fault but a consequence of how we're using it — is a warning that the productivity gains from AI may be illusory if they come at the cost of deeper understanding. His practice of using NotebookLM for research but manually clicking through every link it surfaces is a model for AI-assisted work that maintains intellectual integrity.

The modular architecture advice for AI is particularly prescriptive: design module boundaries carefully, then let AI work within them. This is both a software architecture principle and an AI safety principle. If LLMs have no concept of causality (as Sam argues), constraining their blast radius through module boundaries is the pragmatic equivalent of the guardrails that Sam says won't work long-term. The reference to Opus 5.5 formatting a developer's hard drive — because it ran with --dangerously-skip-permissions — is a concrete example of what happens when LLMs operate without module boundaries.