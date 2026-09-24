# How to Get the Most Out of Jev
**Source**: Every (hello@every.to)
**Date**: 2026-09-24
**Author**: Laura Entis (Every)
**Keywords**: Jev, TypeSafe, classification model, Mike Taylor, Jack Cheng, Douglas Brundage, intent-based software, Codex, Claude Code, tldraw, decision model, probability, email filtering, AI writing detection

## Elevator pitch
Every's deep dive into Jev — TypeSafe's classification model that outputs probabilities instead of text — reveals why it's blowing up timelines: at 4.2 cents per million input tokens, it can make high-volume judgment calls (is this email urgent, does this sound like AI, should I escalate this ticket) at 600x lower cost than LLMs, and the newsletter walks through practical workflows for turning fuzzy questions into discrete Jev checks.

## Takeaways
- **Jev is a decision model, not a chatbot**: Frame a task as yes/no, multiple-choice, or a rating, and Jev returns a probability. It outputs probabilities rather than generating tokens, enabling massive parallel batch processing at a fraction of LLM cost.
- **The 10-second rule**: If a task would take a human less than 10 seconds (email classification, content moderation), Jev is a good fit. For tasks requiring more reasoning, use an LLM.
- **Subjective questions need decomposition**: "Is this email urgent?" must be broken into discrete checks — was it sent by a human, do you know the sender, will ignoring it cost something — which Jev evaluates separately and you combine in code.
- **Jev as a tool for coding agents**: You can draft an article in Codex and send the draft to Jev at every phase to check for AI writing tells. When Jev flags a phrase, Codex revises it on the spot — real-time feedback loops between generator and judge.
- **Intent-based software is emerging**: Jack Cheng's viral demo (1M+ views) uses Jev with voice and hand gestures on a tldraw canvas. The browser transcribes speech, records fingertip coordinates, and describes the canvas state. Jev answers "which shape, what color, where" in real-time — interactions that would take LLMs 1-2 seconds, breaking the feeling of responsiveness.
- **4.2 cents per million input tokens**: Output is free. Compare: Gemini 3.7 Flash at $0.75/$3.75, Haiku 4.5 at $1/$5, Sol at $4/$20, Astra at $10/$50.
- **Mining X for demos works**: Douglas Brundage gave his Grok bot a Jev demo from Elvis Sun (384 news stories → 15 brand recommendations) and asked "can you just do this?" The bot asked for an API key and built it. Morning pulse now reviews 500+ posts vs. fewer than 20 before.

## Synthesis
Jev represents a category shift that's easy to underestimate because it doesn't generate text. The model's value proposition — probabilistic decisions at near-zero cost — fills a gap that LLMs were never optimized for. Most AI workflows today force a choice: either pay LLM prices for simple judgment calls, or skip them entirely. Jev makes those calls economically viable at scale, which changes what's possible to check.

The Every newsletter's practical framing is what makes this piece valuable. The workflow decomposition — break fuzzy questions into discrete checks, define yes/no for each, identify context needed, combine scores in code — is the translation layer that makes Jev useful beyond toy demos. Mike Taylor's email board experiment and Jack Cheng's intent-based canvas demo both follow the same pattern: human defines the decision structure, Jev executes it at scale and speed.

The intent-based software concept is the most forward-looking signal. When Jev can interpret "make a blue square here" from voice + gesture + canvas state in real-time, it suggests a new interaction paradigm where the model's role isn't to converse but to decide. The implications for UI design — interfaces that respond to intent rather than commands — are significant, especially as the latency gap between Jev (milliseconds) and LLMs (seconds) makes the difference between feeling responsive and feeling broken.