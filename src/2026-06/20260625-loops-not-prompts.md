# Writing Loops, Not Prompts, Explained
**Source**: https://rico.codes/loops-not-prompts
**Date**: 2026-06-24
**Author**: Rico
**Keywords**: agent loops, prompt engineering, loop engineering, execution horizon, agent automation, Codex goals

## Elevator pitch
The "write loops, not prompts" movement isn't about abandoning prompts — it's about automating the parts of prompting you keep repeating, moving your attention from manual steering to judgment, taste, and prioritization.

## Takeaways
- A loop is defined as: intent + context + action + evaluation + memory + a stop condition — the scarce resource is not model intelligence but your attention inside the loop
- The "execution horizon" is the point where your supported execution rate exceeds the rate at which you can generate, prioritize, and review good ideas — past it, the bottleneck changes from "could I do this?" to "which of these moves is worth doing?"
- The break-even equation for building a loop: P × N × (S + R) > F, where F is build cost, N is future tasks, S is attention saved per task, R is risk avoided per task, and P is the probability the loop works
- Loops don't have to be code: a Codex goal with a done condition, an AGENTS.md file, a CI check, a PR template, or a scheduled agent run are all loops
- The compounding move is that when an agent makes a mistake and you add a test, CI check, or better stop condition, you change the future — "you planted the saplings by the base"

## Synthesis
Rico's explanation of the "loops, not prompts" philosophy is the clearest articulation of a concept that has been circulating among the most active users of agentic coding tools. Peter Steinberger, Boris Cherny (Claude Code lead), Addy Osmani, and NeetCode have all been saying versions of the same thing: stop prompting coding agents and start designing loops that prompt them. Rico's contribution is to make the idea precise and actionable.

The core reframe is about where your attention goes. A prompt says "do this." A loop says "keep doing this class of work until this condition is true, remember what happened, and stop or ask me when judgment is required." The distinction matters because the scarce resource is not model intelligence — it's your attention inside the loop. If you have to inspect every step, re-explain the repo, paste the same constraints, and ask the same follow-up questions every time, the model may be doing the typing but you're still carrying the process in your nervous system.

The "execution horizon" concept is the essay's most original contribution. It's the point where your supported execution rate exceeds the rate at which you can generate, prioritize, and review good ideas. Before that horizon, your bottleneck is execution — you have more ideas than hands. Past it, the bottleneck changes — you're no longer asking "could I do this if I had more hands?" but "which of these possible moves is actually worth doing?" That is a fundamentally different kind of problem to have.

The break-even math is practical and grounded. Building a loop is worth it when the expected future savings exceed the upfront cost. A shipping skill that takes 90 minutes to write, saves 10 minutes per PR, avoids 5 minutes of CI thrash, and has an 80% probability of working, breaks even after 8 PRs. A daily triage automation that takes 4 hours, saves 25 minutes per workday, and has a 70% chance of working, breaks even after 10 workdays. Loops decay — tools change, repos change, models change — which is why the equation includes maintenance cost and a decaying probability of the loop still working.

The Minecraft metaphor is perfect: you stop treating wood as a wandering-around problem. You plant saplings near your base, making the resource renewable and local. You still have to cut the trees down — the work didn't disappear, the loop got shorter. The same is true for agent loops: a lot of useful loops don't eliminate the task, they make the next execution obvious, local, renewable, and less dependent on you remembering the whole ritual. The compounding move is when an agent's mistake leads to a test, a CI check, or a better stop condition — you changed the future, not just the current output.