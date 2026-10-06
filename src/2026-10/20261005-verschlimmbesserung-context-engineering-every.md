# When Trying to Make AI Better Makes It Worse
**Source**: Every (hello@every.to)
**Date**: 2026-10-05
**Author**: Katie Parrott
**Keywords**: Verschlimmbesserung, context engineering, style guides, AGENTS.md, Compound Engineering, GPT-6 Astra, GPT-5.6 Sol, Codex, Zettelkasten, context bloat, AI writing, prompt engineering, Every, mise en place, context window management

## Elevator pitch
Every writer Katie Parrott recounts how she "worsen-bettered" (Verschlimmbesserung) her AI context setup — expanding a 759-word style guide to 3,855 words, linking 385 files via Zettelkasten, and logging every experiment — until her AI produced 127 drafts and over 1 million words for a single essay, all flat and committee-like. She tore everything down and rebuilt from scratch with three principles: the agent asks first, every folder stands alone, and guides stay short — now running 513 words instead of 6,109.

## Takeaways
- Katie Parrott's context engineering mistake was rooted in Verschlimmbesserung — the German word for making something better only to make it worse
- Her original system worked beautifully: each column had its own folder with a voice guide, style guide, and drafts, managed by an AGENTS.md instructions file — chefs call this mise en place
- Three "improvements" broke it: (1) saving everything (every experiment left a durable record, repeated mistakes became checklist items), (2) connecting everything via Zettelkasten (385 files cross-linked across folders), (3) codifying everything (style guide grew from 759 to 3,855 words with 8 approved openings, 6 approved endings, and 2 checklists)
- The model couldn't tell a record from a rule — every correction to one draft became law for every draft after it
- A single essay folder held 127 drafts and over 1 million words (roughly the entire Harry Potter series) for a piece you could read on your lunch break
- GPT-5.6 Sol diagnosed the problem using Every's Compound Engineering doc-review workflow: "In an agent workflow, the concrete rules are easier to verify, so they can overwhelm the subtler ones while every checklist still passes"
- The model was obeying the parts of instructions that were easiest to follow (tick-box rules like "open with one of these eight approaches") while ignoring subtler principles like "let one experience carry the piece"
- Rebuilding from scratch: archived everything in a "Historical" folder, had the model interview her about her work, proposed a new structure, and rebuilt under "Do not change anything until I approve"
- Three new principles: (1) the agent asks first — nothing enters guides without her say, (2) every folder stands alone — no cross-folder links, (3) guides stay short — principles not templates, "often (not always)"
- Old voice + style guides ran 6,109 words; new ones run 513 words
- One personal rule added: no major context decisions under pressure — including the "thrilling new-model-tilt-a-whirl" kind that triggered the original mess

## Synthesis
Katie Parrott's account is the most detailed first-person case study of context engineering gone wrong published to date. The German word Verschlimmbesserung — "worsen-bettering" — perfectly captures the failure mode: each individual improvement felt rational in isolation, but together they created a system that was actively hostile to the work it was supposed to support. The progression from a clean 759-word style guide to a 3,855-word document with eight approved openings, six approved endings, and two checklists is a precise illustration of how context accretion compounds silently.

The mechanism of failure is the most instructive part. The model couldn't distinguish a record from a rule. When Katie told the model that an outline was "UNRECOGNIZABLE," that correction went into the log. When she said something similar twice, it became a checklist item that every subsequent draft had to pass. The system she built to help her write turned her reactions to one draft into immutable law for all future drafts. Sol's diagnosis — that "concrete rules are easier to verify, so they can overwhelm the subtler ones while every checklist still passes" — is the key insight: in agent workflows, the measurable always crowds out the meaningful.

The rebuild is equally instructive. Reducing 6,109 words to 513 is not just compression — it's a philosophical shift from prescriptive rules to descriptive principles. The instruction that drafts and notes are "task material or evidence, never new instructions" is the single most important design decision in the new system. It establishes a boundary between what the model can consult and what it must obey, preventing the context drift that caused the original collapse. The rule against major context decisions under pressure — especially the "new-model-tilt-a-whirl" kind — is a meta-principle every AI-native worker should adopt. New frontier models create the illusion that your entire workflow should be rebuilt; Katie's story is proof that this impulse is often Verschlimmbesserung in disguise.