# Inside Thinking Machines' Interaction Models
**Source**: https://blog.bytebytego.com/p/inside-thinking-machines-interaction
**Date**: 2026-06-30
**Author**: ByteByteGo
**Keywords**: thinking-machines, interaction-models, real-time-ai, human-ai-collaboration, ai-architecture

## Elevator pitch
Thinking Machines proposes a fundamentally different way to build AI systems for real-time interaction — replacing the turn-based paradigm with continuous, bidirectional communication between humans and AI.

## Takeaways
- Current language models work in a single thread: they wait for user input to finish, then generate a response, freezing perception during generation — a fundamental bandwidth bottleneck.
- Thinking Machines argues that most AI labs' focus on autonomous capability sidelines humans, and that real work benefits from continuous collaboration where humans clarify, redirect, and give feedback in real time.
- The proposed "interaction model" replaces the turn-based paradigm with continuous perception, where the model sees and hears the user in parallel with generating its own output.
- Thinking Machines' approach enables real-time, fluid AI-human collaboration akin to working with a colleague rather than sending emails back and forth.
- The research lab publishes under the name Connectionism and offers developer-facing products, positioning itself as focused on human-AI collaboration rather than pure autonomy.

## Synthesis
Most AI interaction today follows a turn-based pattern: you type or speak, the model processes, then responds. During generation, the model's perception freezes — it cannot see or hear anything new until it finishes its turn. Thinking Machines, a relatively new AI research lab, argues this is a fundamental bottleneck that makes AI collaboration feel like resolving disagreements over email rather than having a real-time conversation.

The lab's core thesis is that the dominant framing in AI — pushing autonomous capability, where the model takes a task and works independently — sidelines humans. Instead, Thinking Machines advocates for "interaction models" that support continuous, bidirectional communication. In their proposed architecture, the model perceives user input in parallel with generating its own output, enabling real-time course correction, clarification, and redirection.

This is not merely an interface change; it is an architectural one. Current models are built around the assumption that input comes in discrete turns. Building models that can perceive and generate simultaneously requires rethinking how attention, context, and generation work together. The research preview shows how this architecture could enable more fluid AI-human collaboration — closer to pair programming with a skilled colleague than delegating a task via email.

The implications for engineering are significant. If the interaction model paradigm catches on, it would change how we design AI coding agents, customer service bots, and collaborative tools. Rather than agents that run autonomously for hours and return results, we might see more agents that work alongside humans in real time, receiving mid-course corrections and adapting on the fly. This could reduce the "delegation tax" of describing tasks precisely upfront and instead allow iterative refinement during execution.