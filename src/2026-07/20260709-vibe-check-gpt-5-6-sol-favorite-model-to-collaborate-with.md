# Vibe Check: GPT-5.6 Sol Is Our Favorite Model to Collaborate With
**Source**: https://every.to/vibe-check/gpt-5-6-sol
**Date**: 2026-07-09
**Author**: Katie Parrott (Every)
**Keywords**: GPT-5.6 Sol, OpenAI, AI models, LLM evaluation, collaborative AI, coding with AI, knowledge work, agent workflows

## Elevator pitch
GPT-5.6 Sol is fast, resourceful, and easy to steer, making it Every's favorite model for collaborative knowledge work — but Anthropic's Fable still leads on the biggest, most ambiguous assignments that require deciding what to build.

## Takeaways
- Sol scored 56/100 on Every's Senior Engineer benchmark vs Fable's 90/100, with the gap mostly explained by Sol's tendency to overwrite — adding 12,900 lines of unnecessary code across four cooperating processes.
- Sol finished last among six models on the writing benchmark but is the team's preferred daily writing partner because it responds quickly to editorial direction and uses context (style guides, samples) better than Claude models.
- Arielle Shipper's spreadsheet test showed Sol's strength: it found an email, inspected 46 CSV files, and returned with seven useful questions with recommendations — while GPT-5.5 asked where to find the email and Fable asked the user to move files to Google Drive first.
- OpenAI merged ChatGPT and Codex desktop into one unified app, with ChatGPT Work for knowledge work and Codex for technical work, creating an ecosystem that handles both delegation and collaboration.
- The team's workflow has split into two modes: delegate (give Fable a big assignment and leave) vs. collaborate (stay close with Sol, iterating quickly on writing, coding, and analysis).

## Synthesis
Every's Vibe Check on GPT-5.6 Sol reveals a model that has become the team's default for collaborative knowledge work. The central insight is a split between delegation and collaboration as distinct work modes. Sol excels at collaboration — the kind of work where you stay close to the model, revise as you go, and make decisions that guide the outcome. Fable remains the choice for delegation — handing off a large, ambiguous assignment and returning to a finished result. Dan Shipper's analogy captures it: Sol is a Porsche, Fable is a warp drive. Most of the time you're not going to space; you're just trying to get around town.

The coding results illustrate Sol's profile precisely. It traced a bug through an unfamiliar production codebase that GPT-5.5 had failed to fix, and rebuilt a collaborative document editor from a single prompt in one-third the time Fable needed. But it overbuilt: the Senior Engineer benchmark revealed a model that understands architecture but doesn't know when to stop. Sol added thousands of lines of unnecessary machinery, recreating complexity where a senior engineer would have simplified. This is the delegation weakness — when deciding what NOT to build is a main part of the task, Fable's judgment is still needed.

The writing results are counterintuitive but instructive. Sol finished last in the formal benchmark (one-shot article introductions, editorial anticipation) but is the team's preferred daily writing partner. The explanation: Sol thrives on context. Give it style guides, source materials, and editorial rules, and the quality rises dramatically. Ask it to determine the argument and standards from scratch, and the weaknesses return. Katie Parrott used Sol to speed-run 24 drafts of the Vibe Check article in six to eight hours, something no other model could sustain at that pace while remaining responsive to direction.

The knowledge work examples are perhaps the most telling. Sol's default behavior is to read available context before asking for help — it searches files, reads standing instructions, and uses connected tools rather than turning source retrieval into another assignment for the user. This contrasts sharply with GPT-5.5, which asked where to find an email even when the sender was named. The improvement in persistence and resourcefulness is the clearest upgrade over previous GPT models.

The product context matters. OpenAI merged ChatGPT and Codex into a single desktop app, creating a unified surface for both knowledge work and technical work. The team finds this app a place they want to stay, which is significant for OpenAI's competitive positioning. However, Codex's opacity remains a weakness — engineers like Andrey Galko note they often have to work backward to understand what Sol tried and decided, while Opus explains more of its process. For teams where visibility into agent reasoning matters, this is a real trade-off.

The pricing structure positions three tiers — Sol ($5/$30 per million tokens), Terra ($2.50/$15), and Luna ($1/$6) — directly against Anthropic's Opus, Sonnet, and Haiku. The competitive dynamic is intensifying, and Sol's combination of speed, context use, and steerability makes it a credible daily driver that challenges the assumption that Anthropic models are inherently better for knowledge work.