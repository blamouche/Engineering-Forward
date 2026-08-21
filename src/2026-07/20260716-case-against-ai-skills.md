# The Case Against Skills
**Source**: https://every.to/context-window/the-case-against-skills
**Date**: 2026-07-16
**Author**: Laura Entis
**Keywords**: AI skills, agent skills, prompt engineering, SWE-Skills-Bench, Fable 5, Claude, model performance

## Elevator pitch
The elaborate skill libraries popular in AI agent workflows may actually be making your AI worse — SWE-Skills-Bench shows that 39 out of 49 tested skills had no impact, three made things worse, and only seven improved outcomes.

## Takeaways
- Skills are reusable instruction packages that load when relevant to a task, but frontier models like Fable 5 and GPT-5.6 have absorbed most of what popular skills teach, making extra instructions create confusion rather than clarity
- SWE-Skills-Bench tested 49 public software-engineering skills and found that 39 had no measurable impact, 3 actively harmed performance, and only 7 improved outcomes — all 7 provided specialized knowledge the model couldn't have known (financial-risk formulas, traffic-management instructions)
- Skills that compensated for Opus 4.8's weaknesses actually harmed Fable 5's performance, echoing the GPT-3→GPT-4 transition where "hacks and magic words" became unnecessary
- The worst skill tested increased token use by 451% without improving results, making skills an inflationary cost that may not pay off
- Skills have a shelf life: instructions patching a model's blind spot become redundant or counterproductive the moment a new version absorbs that capability

## Synthesis
Every from Every's newsletter argues that the sprawling custom skill libraries treated as status symbols on social media may be actively counterproductive. Mike Taylor, Every's head of tech consulting, advocates that every skill should earn its place with measurable proof of improvement. The argument rests on a simple observation: frontier models are now smart enough that they've internalized most of the patterns that skills encode. When you force a model to follow your specific instructions instead of relying on its trained weights, you're "fighting the model" — and the model is more likely to make mistakes.

The data from SWE-Skills-Bench reinforces this: of 49 tested skills, the vast majority were neutral or harmful. Only skills providing genuinely private context — personal writing preferences, company-specific templates, internal data, exact workflow sequences — consistently improved outcomes. This aligns with a broader pattern in AI development: techniques that patch model weaknesses (like GPT-3-era prompt engineering tricks) become technical debt when models improve.

The practical recommendation is a skills audit: keep skills that provide private context or custom tool access, retest skills compensating for general model weaknesses (which may have a shelf life), and retire skills that don't demonstrably improve results. The autoreview skill from OpenClaw — which sends code changes to a separate model for review — is cited as one that genuinely earns its place by providing a workflow the model can't replicate alone. For engineering teams, the takeaway is clear: invest in evaluation infrastructure to measure skill impact, and treat your skill library as a living system that requires regular pruning, not a trophy case.