# Vibe Check: Opus 5.5 Is Pulling Our Codex Converts Back to Claude
**Source**: Every (hello@every.to)
**Date**: 2026-09-22
**Author**: Katie Parrott (Every)
**Keywords**: Claude Opus 5.5, Fable 5.1, Codex, GPT-6 Astra, model comparison, coding, price-performance, token cost, Anthropic

## Elevator pitch
Anthropic's Claude Opus 5.5 delivers most of Fable 5.1's performance at roughly 60% less per token, pulling Every's builders back to Claude from Codex — but it remains an unreliable finisher when precision and deadlines matter.

## Takeaways
- **Opus 5.5 offers Fable-level power at ~60% less token cost**: The price-performance claim is "surprisingly credible" after testing across coding, design, writing, and consulting work, making it the key economic argument for switching.
- **Builders are switching back to Claude**: Kieran Klaassen replaced Fable 5.1 with Opus as his daily driver, while former Claude power users Mike Taylor and Tyler Nishida are reconsidering their moves to Codex.
- **Opus beat GPT-6 Astra on latency budgets**: Ruby code handled 427 requests per second and met 17 of 20 latency budgets, beating Astra on the latter measure — a meaningful result for performance-sensitive workloads.
- **A 251-line Rails patch passed 4 of 5 automated checks**: Mike Taylor's reviewable patch was a strong result, but another app burned 5.9 million tokens before its core screens threw errors, showing Opus's inconsistency.
- **Most readable prose measured, but ideas got buried**: Opus produced the most readable prose the team measured, yet it buried ideas that GPT-6 Astra reliably surfaced first — a tradeoff between style and substance.
- **Set Opus a budget and a stopping point**: The recommendation is to use Opus for visual products and creative collaboration, keep Fable for problems too large to inspect, and keep Astra/Sol when the deliverable has a clock.

## Synthesis
This Vibe Check is the most detailed public assessment of Opus 5.5's positioning in the frontier model landscape. The core finding — Fable-level performance at 60% less token cost — is an economic earthquake if it holds at scale. The frontier model market has been dominated by a price-performance arms race where each new model either raises capability or lowers cost, but rarely both. Opus 5.5 appears to do both, which explains why builders are actively switching.

The nuance in the review is what makes it credible. Opus isn't uniformly better — it "occasionally loses the assignment while doing extra credit," a pattern familiar to anyone who has watched a capable model produce impressive but off-target output. The 5.9 million token burn before core screens threw errors is a cautionary tale: Opus's creativity and verbosity, assets in open-ended work, become liabilities when the task requires convergence. Dan Shipper's continued preference for Codex in knowledge work underscores this — different models genuinely excel at different cognitive tasks.

The practical guidance — "set Opus a budget and a stopping point" — is the kind of operational wisdom that emerges only from hands-on testing. It reflects a mature understanding of model selection in 2026: you don't pick a model, you configure one. Budgets, stopping criteria, fallback models, and task-specific routing are now part of the practitioner's toolkit, and publications that test these dimensions (as Every does) provide more actionable guidance than benchmark leaderboards.