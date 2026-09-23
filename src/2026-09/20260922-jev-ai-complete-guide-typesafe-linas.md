# How to Use Jev AI: The Complete Guide to TypeSafe's System One Model
**Source**: Linas's Newsletter (linas@substack.com)
**Date**: 2026-09-22
**Author**: Linas (Linas's Newsletter)
**Keywords**: Jev, TypeSafe, Diogo Almeida, decision models, model cascades, agent controllers, semantic routing, OpenAI, ChatGPT, Vercel, OpenRouter, Cloudflare

## Elevator pitch
Linas publishes a comprehensive guide to Jev — TypeSafe's decision model that cannot write a single word but may matter more to software builders than any model release this year — covering where it creates value, how to architect it between deterministic code and generative models, and how to move from demo to production.

## Takeaways
- **Jev is a decision model, not a language model**: Built by Diogo Almeida (formerly OpenAI), Jev takes predefined options and returns a typed choice plus calibrated confidence — "a 2016-style classifier with 2026-level intelligence" at $0.042 per million input tokens with free output.
- **The pattern: state → bounded question → typed judgment → code acts**: Software creates a state, gives Jev a bounded question, Jev returns a typed judgment with probabilities, and code decides what that judgment is allowed to change.
- **Real-world results within a week of launch**: Matthew Berman analyzed 724 ads from 37 brands in 40 seconds for 9 cents; Vechen used Jev to control GPT-6 Astra's reasoning effort, reporting 50% lower costs; Jarrod Watts built a trading bot making decisions every 300ms on Monad.
- **Jev as semantic control layer**: The bigger opportunity is using Jev to decide when an agent should think harder, which evidence deserves context-window space, which requests can bypass a frontier model, and which cases need a human — replacing expensive LLM calls at decision points.
- **Jev is not magic**: It performs well when the decision is crisp, the answer space is bounded, and evidence is present in the state. It fails when the question hides several judgments, requires missing information, or depends on long-form reasoning.
- **The guide covers**: Where Jev creates economic value, dividing responsibility between Jev/code/LLMs/humans, building model cascades and agent controllers, writing state and questions, calibrating probabilities, and moving from demo to shadow mode to production.
- **Rapid distribution**: Jev is already on Vercel's AI Gateway, OpenRouter, and Cloudflare Workers AI, with hundreds of public builds catalogued within a week of launch.

## Synthesis
Linas's guide is the first comprehensive treatment of Jev as an architectural primitive rather than a curiosity. The framing — "a model that cannot write a single word, and it may matter more to people who build software than any model release this year" — is provocative but defensible. The reason it holds is that most AI product decisions are not generative at all: they're routing decisions, classification calls, risk assessments, and control-flow choices that currently get delegated to expensive LLMs because no cheaper, more reliable alternative existed. Jev fills that gap with a purpose-built tool.

The three real-world examples Linas cites reveal the pattern most clearly. The ad analysis (724 ads, 40 seconds, 9 cents) shows Jev replacing what would have been a costly multi-call LLM workflow with a single batch decision. The reasoning-effort controller (50% lower Astra costs) shows Jev acting as a meta-controller — deciding when a downstream model needs to think harder — which is an architectural pattern that scales far beyond a single use case. The trading bot (decisions every 300ms) shows Jev operating inside a tight real-time loop where an LLM call would be too slow and too expensive.

The economic argument is the strongest part of Linas's analysis. At $0.042 per million input tokens with free output, Jev is cheap enough to insert at decision points where an LLM call would previously have been excessive. This changes the architecture of AI systems: instead of a single expensive model making every decision, you get a layered system where cheap decisions (Jev) gate expensive ones (LLMs). The analogy to model cascades is apt, but Jev makes cascades practical at a granularity that wasn't feasible before.

The honest limitations section is what separates this guide from hype. Jev fails when "the question hides several judgments, requires information that is missing, or depends on long-form reasoning." This is the correct framing: Jev is a tool for a specific class of decisions, not a replacement for reasoning models. The guide's emphasis on state design, question design, calibration, fallbacks, and verification is the right level of engineering rigor. The progression from demo to shadow mode to controlled automation to production is the correct deployment path for any decision-making component in a production system.