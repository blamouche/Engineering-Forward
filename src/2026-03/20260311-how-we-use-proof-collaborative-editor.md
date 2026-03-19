# Transcript: How We Use Proof, a Collaborative Editor for Humans and AI
**Source**: https://every.to/podcast/transcript-how-we-use-proof-a-collaborative-editor-for-humans-and-ai
**Date**: 2026-03-11
**Author**: Dan Shipper
**Keywords**: Proof, collaborative editor, AI agents, agent experience, provenance tracking, open source, compound engineering, Every.to

## Elevator pitch
Proof's design philosophy—"you can be agent native without having an agent in your product"—separates agent experience (AX) from user experience (UX) as co-equal design priorities in a lightweight collaborative editor for humans and AI.

## Takeaways
- Origin: every.to's teams needed a way to share AI-generated content for feedback, evolving from a provenance tracking concept into a full collaborative editor.
- "Agent native without having agents in your product": agent-native design means making external agent access seamless, not embedding agents within the UI.
- Agent experience (AX) as a design primitive on par with UX: a paradigm shift that treats agents as first-class users requiring their own experience design.
- Practical uses at Every: planning loops with iterative agent refinement, creative writing with provenance tracking, and low-friction brainstorming with compound engineering plugins.
- Intentionally lightweight: unlike GitHub, Notion, or Linear, Proof avoids organizational connotations—it's a sketch pad, not a document management system.
- Anticipated challenge: multi-agent collaboration and distinguishing monologued content from AI-generated text.

## Synthesis
The "agent native without having agents in your product" framing is a useful design principle that extends beyond Proof. Most discussions of AI product design focus on where to embed AI capabilities—chatbots, suggestion panels, generate buttons. Shipper's observation points toward a different model: rather than building AI into your product, build your product to be accessible by AI tools that users already have. This shifts the design question from "what AI features should we add?" to "how do we make our product accessible to the agents our users are building?"

The agent experience (AX) concept is the most significant contribution. UX design has decades of frameworks—personas, journey maps, usability principles—built around understanding and optimizing for human users. As agents become active participants in digital workflows, products need analogous frameworks for understanding and optimizing agent access patterns. Proof's emphasis on external connectivity over internal agent integration reflects an early attempt to think through what AX means in practice.

Brandon Gell's planning loop use case illustrates why lightweight matters. Planning documents that go through multiple rounds of agent refinement and human feedback don't benefit from heavyweight document management features—they need fast iteration with low cognitive overhead. A Notion page for a planning document carries organizational implications (who can see it, what project it belongs to, how it fits in the hierarchy) that slow down the workflow. A Proof document has none of that overhead.

The multi-agent challenge Shipper anticipates is genuinely hard: when multiple agents contribute to a document, both attribution and coordination become complex. A "traffic cop" LLM for agent sequencing and conflict resolution mirrors the role that orchestration layers play in multi-agent systems—the same architectural challenge showing up at the document level.
