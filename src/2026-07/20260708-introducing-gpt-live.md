# Introducing GPT-Live
**Source**: https://simonwillison.net/2026/Jul/8/introducing-gptlive
**Date**: 2026-07-08
**Author**: Simon Willison
**Keywords**: GPT-Live, OpenAI, voice model, ChatGPT, GPT-5.5, real-time voice, full-duplex

## Elevator pitch
OpenAI launches GPT-Live, a full-duplex voice model for ChatGPT that can listen and speak simultaneously, delegate hard tasks to GPT-5.5 in the background, and maintain conversation flow for at least an hour.

## Takeaways
- GPT-Live is a full-duplex voice model: it can listen and speak at the same time, handle natural conversational cues, and continue talking while processing background tasks.
- For complex questions requiring deeper reasoning, web search, or extended computation, GPT-Live delegates to GPT-5.5 behind the scenes and brings the result back into the conversation when ready.
- The previous ChatGPT voice mode was based on a GPT-4o-era model with a 2024 knowledge cutoff, which had become a significant limitation—Willison had mostly stopped using it as a brainstorming partner.
- During preview, the model had a notable bug where it would interrupt users to laugh at things that weren't intended as jokes, which OpenAI has since addressed.
- Willison's longest conversation with the new model lasted a full hour while walking his dog, suggesting the model can sustain extended interactions without degrading.

## Synthesis
Simon Willison's writeup on GPT-Live captures the significance of OpenAI's latest voice model upgrade. The core innovation is full-duplex capability: the model can listen and speak simultaneously, a fundamental shift from the turn-taking paradigm that has constrained voice AI interactions. This enables natural conversational dynamics—interruptions, back-channeling, and real-time task delegation.

The delegation feature is particularly noteworthy. When a question requires web search, deeper reasoning, or complex computation, GPT-Live hands it off to GPT-5.5 while continuing the conversation. The user doesn't experience a pause; the model maintains flow and interweaves the background result when it arrives. This architecture effectively creates a two-tier system where a fast, conversational model handles real-time interaction while a more capable model processes harder problems asynchronously.

The upgrade addresses a real pain point. The previous voice mode, based on a GPT-4o-era model with a 2024 knowledge cutoff, had become largely unusable for substantive tasks. Willison notes he had "mostly stopped using voice mode because the age and relative weakness of the model greatly limited how useful it was as a brainstorming partner." GPT-Live appears to fix this gap.

The model isn't without quirks. During preview, it exhibited an unusual behavior of interrupting the user to laugh at things that weren't intended as jokes—something Willison reported and OpenAI has since adjusted. This anecdote highlights the ongoing challenge of tuning conversational AI to match social expectations.

For developers and AI builders, the key takeaway is architectural: the delegation pattern—fast model for real-time interaction, capable model for background processing—is likely to become a standard pattern for voice and multimodal AI systems.