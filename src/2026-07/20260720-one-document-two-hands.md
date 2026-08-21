# One Document, Two Hands: Solving the Decision Problem
**Source**: https://sunilpai.dev/posts/one-document-two-hands/
**Date**: 2026-07-20
**Author**: Sunil Pai
**Keywords**: agents, UI, direct manipulation, local-first, Durable Objects, Cloudflare, document model

## Elevator pitch
Sunil Pai proposes that agents should sit beside the user—not in front of the app—editing the same document simultaneously, and demonstrates this pattern with Pizzo, a music app where both the user and the agent modify shared state through the same operations.

## Takeaways
- The current pattern of putting a chat box in front of an application ("you → chat → agent → app → thing") puts the agent in the doorway, removing direct manipulation. Pai wants agents beside the user: "you + your agent → application → your thing."
- Coding agents work well because they inherited a full workshop: repositories, shells, editors, test suites. Non-coding AI products gave users a text box instead of a workshop—this is a design choice, not a model limitation.
- The agent shouldn't own the document; the document should own the document. Chat is one input surface over the work, not the container of the work—state should live in ordinary application state, not in a conversation transcript.
- Boring deterministic code should do the precise bits. In Pizzo, transposition, chord generation, and bassline creation are deterministic functions called by both the UI and the agent—there's no "normal implementation" and "AI implementation."
- Project Think uses serverless infrastructure (Cloudflare Workers + Durable Objects) so agents can sleep when idle, wake on events, and retain identity and state without running containers—critical for scaling from millions of developers to billions of users.

## Synthesis
Pai's essay articulates a design philosophy for AI agents that challenges the dominant chat-first paradigm. The core argument is simple: direct manipulation is good, chat is useful when you know the outcome but not the exact moves, and there's no reason these inputs should live in different applications. The Pizzo demo makes this concrete: drag a tempo slider because your hand is there, then ask the agent to make the progression "more wistful" because that's easier to say than choosing four replacement chords.

The "one document, two hands" metaphor reframes the agent relationship. Rather than the agent standing between the user and the application (the chat-in-front pattern), or hiding behind the application (the invisible-agent pattern), the agent sits beside the user as another editor of shared state. Both use the same operations—transpose(2) works identically whether called from a button click or an agent tool invocation. This eliminates the problem of two implementations diverging and makes the application boring and testable at the precision layer.

The infrastructure argument is equally important. Pai is building Project Think on Cloudflare's serverless model because agents that serve a billion users can't run always-on containers. Durable Objects provide addressable state that persists between invocations; Workers supply compute on demand. The agent sleeps when idle, wakes on events or alarms, and retains its identity. This "harness as app" pattern—where the application's existing state, operations, and history are the agent's context—is a fundamentally different architecture from the conversation-as-state-repository pattern that dominates current AI products.

For builders, the practical takeaway is that the same deterministic operations, state management, and persistence that serve the human-facing UI should serve the agent. The agent doesn't need its own parallel representation of the work. It needs tools that call the same functions the buttons call, editing the same document the user sees. This is both simpler to build and more robust than maintaining two synchronized representations.