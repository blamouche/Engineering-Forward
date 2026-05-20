# Vibe Check: Opus 4.7 Stopped Reading Between the Lines
**Source**: https://every.to/vibe-check/opus-4-7
**Date**: April 17, 2026
**Author**: Katie Parrott
**Keywords**: Opus 4.7, Claude, Anthropic, model tuning, vibe check, coding benchmark, precision vs intuition, prompt engineering

## Elevator pitch
Opus 4.7 is a deliberate dial-back from its predecessor's gap-filling intuition — the best coding model on well-specified tasks, but one that punishes vague prompts and refuses to fill in the gaps for you.

## Takeaways
- Opus 4.7 was the first model to nail a full e-commerce website build including a custom product designer and dependable shopping cart
- The model's defining trait is precision through literalism: it rewards tight prompts and frustrates users who rely on the model to intuit unstated requirements
- Anthropic is actively tuning Claude's "eagerness" between releases — 4.7 represents a hard dial-back from 4.6's proactive gap-filling
- Writing quality is competent but "rhythmically flat" compared to Opus 4.6; old prompts won't deliver the results users are used to
- The meta-insight: model releases are becoming opinionated design decisions about how much initiative the model should take

## Synthesis
Every's Vibe Check on Opus 4.7 captures a deliberate product decision by Anthropic that will divide users along a clear line: do you give your model precise, well-structured prompts, or do you rely on it to read between the lines? Opus 4.7 is the best model Kieran Klaassen has ever tested on their hardest coding benchmark, and it was the first to successfully build a complete e-commerce site with a custom product designer and reliable cart. But Dan Shipper found it could write a senior-engineer-quality diagnosis of a messy codebase and then refuse to execute the solution — the model is more literal, not less competent.

The most revealing finding is the pattern across multiple testers: Opus 4.7 missed a data error in a P&L analysis that its predecessor (4.6) caught unprompted. It wrote consulting copy so sharp it might be better than a human's, but produced a personal essay that was "rhythmically flat." The throughline is that Anthropic is treating Claude's eagerness — its willingness to fill in gaps, infer intent, correct errors — as a tunable parameter, not a constant. Each release is a bet on how much initiative the model should take, and 4.7 shifts that balance hard toward "do exactly what I asked."

This has practical implications that go beyond benchmark scores. Users migrating from Opus 4.6 will need to rewrite their prompts, adding specificity they previously got for free. Teams with established prompt libraries should expect regression testing between releases. What 4.7 teaches the industry is a counterintuitive lesson: stronger models may require more, not less, prompt engineering — but the prompts you do write will be executed with unprecedented precision.
