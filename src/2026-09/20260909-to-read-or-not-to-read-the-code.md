# To Read — Or Not to Read the Code?
**Source**: https://every.to/emails/click/09c24c7a4dd0698c6700616530f966228bcd55b2042584e4395d015976ea692d
**Date**: 2026-09-08
**Author**: Kieran Klaassen (Every / Cora GM)
**Keywords**: compound engineering, code reading, discernment, AI agents, skill erosion, irony of automation, dark factory, /ce-explain, learning loops, human oversight

## Elevator pitch
As AI agents handle more coding work, the risk isn't just bugs — it's the erosion of the developer's own judgment. The solution isn't to read every line of code for verification, but to read code to learn: building a daily practice of understanding the system well enough to distinguish a plausible-sounding fix from a correct one.

## Takeaways
- The "dark factory" metaphor from manufacturing applies to AI-assisted coding: lights off, machines running, but the risk is turning out the light in your own head — losing the understanding that lets you judge the system's output
- Reading code is no longer for verification (planning, testing, and review agents handle that better) — it's for learning: building the mental model that lets you recognize when a plausible-sounding answer is actually wrong
- A real-world example: a Cora bug where a speedup exposed a latent cleanup issue that deleted already-sent emails — the first proposed fixes (wait 30 seconds, skip if Cora sent it) sounded reasonable but were both wrong; the correct fix was asking Gmail directly whether a message was still a draft before deleting
- Four practices to compound human understanding: (1) open merged PRs and keep a list of gaps, (2) ask for the mechanics not the diff, (3) recover the reason behind design choices (incidents buried behind safeguards), (4) let the model quiz you without making it a gate
- Research confirms the "irony of automation" (identified 1983): extended AI agent use measurably erodes vigilance, critical thinking, and domain skill — the very capabilities human oversight depends on
- Experienced engineers are most at risk: "I know this" is always available as an excuse, while junior engineers constantly encounter unfamiliar things they must learn

## Synthesis
Kieran Klaassen's essay is one of the most thoughtful contributions to the debate about AI's impact on developer skill. While most discussions focus on whether AI-generated code is correct, Klaassen focuses on whether the developer using AI remains capable of judging correctness — and the evidence is that this capability erodes measurably with extended agent use.

The Cora email-deletion bug is a perfect case study. When a speedup exposed a latent bug where Gmail drafts that had been sent by the user were still being cleaned up by Cora's process, the first proposed fixes were both reasonable-sounding and both wrong. The correct fix — asking Gmail directly whether a message was still a draft before deleting — required understanding the system well enough to know that the plausible fixes were guessing about timing and ownership, when the real issue was that Cora had no way to know the draft's state had changed externally. This is discernment, not code verification, and it's what humans contribute to agentic workflows.

The four practices are practical and tool-agnostic. The most distinctive is "recover the reason the code can't show you" — understanding that design choices that look needlessly complicated in isolation usually have an incident buried behind them. Until you know why a safeguard exists, you can't tell whether removing it is a simplification or a regression. This connects directly to the broader theme: the value of experienced engineers in an AI-assisted world isn't writing code, it's knowing where to point the machine, when to stop it, and which of two reasonable-sounding plans will hurt you six months from now.