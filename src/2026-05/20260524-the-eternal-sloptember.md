# The Eternal Sloptember
**Source**: https://geohot.github.io/blog/jekyll/update/2026/05/24/the-eternal-sloptember.html
**Date**: May 24, 2026
**Author**: George Hotz (geohot)
**Keywords**: AI agents, code quality, software engineering, LLM limitations, slop, programming automation, statistical models

## Elevator pitch
George Hotz argues that AI agents cannot truly program — they produce increasingly plausible but subtly broken code that will constitute "one of the most costly mistakes" in software engineering history, especially for large organizations where bottom performers lack the error-correction instincts to detect AI-generated slop.

## Takeaways
- AI agents are "highly sophisticated statistical models designed to mimic the distribution of programming" — their output is broken in ways that get harder to detect as models become more accurate
- Hotz tried using agents for real work (tinygrad, USB firmware reverse engineering) for 6 months and concluded he could have done it better and faster manually: "the agent frontloads all the progress, then gives you a slot machine lever"
- High-performing engineers have developed the ability to detect "slop" through careful line-by-line review; they use AI selectively in confined domains
- Large organizations face asymmetric risk: bottom performers without self-check produce 10x output, but it's low-quality — "a golden era for buckets of slop, and a dark age for gems of quality"
- AI-produced artifacts are broken in ways that weren't previously possible because the process differs from human creation — old quality proxies like syntax and grammar are useless
- Hotz aligns with LeCun/Marcus: LLMs will never truly program without world models; RLVR that comments out failing tests doesn't count
- He predicts the real story will be "who manages to avoid harming themselves in their AI psychosis"

## Synthesis
George Hotz delivers one of the most pointed critiques of AI coding agents from someone who actually tried to make them work at a high level. His framing is deliberately provocative — "Eternal Sloptember" — but the argument is substantive. Over six months of earnest experimentation with agents on non-trivial projects (GPU emulation, USB firmware reverse engineering), he found a consistent pattern: agents generate plausible-looking progress rapidly, then stall on the last 10% that requires real understanding. The result is a slot machine where each pull might fix the issue or introduce new subtle bugs.

The most original insight concerns organizational dynamics. Hotz observes that high-performing engineers have developed effective outer loops around AI tools: they use them selectively, review every line, and know when to trust output. But this calibration is hard-won and individual. Large organizations, with slower feedback loops and uneven talent, face a different dynamic. Bottom performers — those who can't or won't carefully review AI output — become 10x producers of subtle garbage. The organization's average output degrades while appearing more productive.

This connects to a deeper epistemological problem. AI-produced code looks syntactically correct and passes superficial review, but the underlying process that created it is fundamentally different from human reasoning. The artifacts are "broken in ways that weren't previously possible" because old quality proxies — clean syntax, good grammar, passing tests — no longer correlate with actual correctness.

Hotz's conclusion is bleak but nuanced. He doesn't reject AI tools outright — he acknowledges they're useful for prototyping and as "better Google" — but he draws a hard line at calling them engineers. He predicts that the organizations that will suffer most are those that force AI adoption universally (he singles out Apple), mistaking tool deployment for productivity improvement. The winners will be those who maintain the discipline to distinguish between plausible output and correct output.
