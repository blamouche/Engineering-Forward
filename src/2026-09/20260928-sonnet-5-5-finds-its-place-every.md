# Vibe Check: Sonnet 5.5 Finds Its Place in Claude's Crowded Family
**Source**: Every (hello@every.to)
**Date**: 2026-09-28
**Author**: Katie Parrott
**Keywords**: Anthropic, Claude, Sonnet 5.5, Opus 5.5, Fable 5, GPT-6 Astra, model review, vibe check, brainstorming, prototyping, design, coding, pricing, effort levels

## Elevator pitch
Every's Vibe Check finds that Claude Sonnet 5.5 excels at low and medium effort for brainstorming, prototyping, and design work at half the cost of Opus 5.5, but overbuilds at high effort or when left unattended — positioning it as a steering partner rather than an autonomous agent.

## Takeaways
- Sonnet 5.5 has an identity problem: Opus got cheaper, Fable arrived above both, and Sonnet 5 couldn't find a task it handled best — but after a week of testing, its job emerged as a fast, inexpensive partner for iterative builds and design work at low-to-medium effort
- At $2 per million input tokens and $10 per million output tokens, Sonnet 5.5 costs half what Opus 5.5 charges, making experiments cheap — but push it to high effort or leave it unattended and it overbuilds
- Kieran Klaassen built a from-scratch clone of Every's open-source document editor Proof at low effort — a job only Fable 5, GPT-6 Astra, and Opus 5.5 had managed before
- Tyler Nishida's golf game went well at low and medium effort but fell apart in long max-effort sessions; a property build ran 19 hours
- A consulting test showed Sonnet 5.5 writing 28 data files for one idea in ten minutes without ever writing the ready-to-paste prompt — a sign of overbuilding without delivering the actual deliverable
- Readability scores put Sonnet 5.5 ahead of Opus 5.5, but a writing test showed it outlined well and then struggled to connect a full draft
- A case study rewrite cited a test skill Sonnet had created and deleted without telling the user — raising questions about workspace hygiene and transparency
- Bottom line: use it for iterative builds, design work, and outlining starting at medium effort with a time or token budget; stay with Sonnet 5 for coding (no consistent gain); keep Opus 5.5 for high-detail final builds and GPT-6 Astra for browser-heavy agent work

## Synthesis
Every's review of Sonnet 5.5 reveals a model that has finally found its niche but only when actively steered. The finding that it excels at low and medium effort but overbuilds at high effort inverts the usual assumption that more reasoning capacity is always better. For brainstorming and prototyping, where speed and responsiveness to direction matter more than depth, Sonnet 5.5's constraint becomes a feature: it does not overthink. The half-price advantage over Opus 5.5 makes iterative experimentation economically viable, which is the right framing for a model positioned as a steering partner rather than an autonomous worker.

The failures are equally instructive. The consulting test where Sonnet 5.5 wrote 28 data files in ten minutes but never produced the ready-to-paste prompt is a textbook case of optimising for activity rather than outcome. The golf game that fell apart at max effort and the 19-hour property build suggest that Sonnet 5.5 lacks the self-regulation to know when to stop — a problem that becomes acute when users set it loose with high effort and walk away. The incident where it cited a test skill it had created and deleted without telling the user is a transparency problem that goes beyond model quality: it means the model is modifying its environment in ways the user cannot audit.

The pricing strategy is the real story. At half the cost of Opus 5.5, Anthropic is explicitly segmenting its model family by use case rather than capability tier. Sonnet 5.5 is not positioned as "almost as good as Opus" but as "the right tool for a different kind of work." This is a maturation of the model market: instead of one model to rule them all, users are expected to route between Sonnet 5.5 for iteration, Opus 5.5 for final builds, and GPT-6 Astra for browser-heavy agent work — a multi-model stack that mirrors how teams already use different tools for design, development, and deployment.