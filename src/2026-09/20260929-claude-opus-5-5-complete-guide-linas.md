# How to Use Claude Opus 5.5: The Complete Guide
**Source**: Linas's Newsletter (linas@substack.com)
**Date**: 2026-09-29
**Author**: Linas
**Keywords**: Claude Opus 5.5, Anthropic, effort levels, token costs, prompt habits, Claude Code, CLAUDE.md, routing, Fable 5.1, GPT-6 Sol, code review, concurrency, security

## Elevator pitch
Linas provides a comprehensive guide to Claude Opus 5.5 — covering the five effort levels and their cost/quality tradeoffs, the one-message brief template, a drop-in CLAUDE.md system prompt, eight high-value workflows with copy-ready prompts, routing rules for when to use Opus vs Fable vs GPT-6 Sol, and cost controls for Claude Code sessions.

## Takeaways
- Claude Opus 5.5 (released Sep 22, 2026) is Anthropic's new default model — matches Fable 5.1 on most work, writes 30%+ faster than Opus 5, costs ~40% less — but only at default settings with proper setup
- Token prices fell only 20% ($4/M input, $20/M output); the rest of the savings come from the model using fewer tokens per task, which only happens if configured correctly
- Opus 5.5 is the default model in Claude Code on all paid plans and ranks first on the Artificial Analysis Intelligence Index
- An early tester audited and fixed a 200,000-line codebase in under 3 hours (vs 20+ hours for Opus 5); in Anthropic's earnings-research test, 16 of 18 Opus 5.5 reports had no invented figures (Fable 5.1 and Opus 5: zero clean reports)
- Three key mistakes waste money: running at max effort (119K output tokens/task, 1.6x Opus 5 — the 40% saving disappears), keeping old prompt habits ("think carefully" lines now cause delayed starts with no quality gain, and chain-of-thought requests are blocked and billed), trusting unattended runs (Opus 5.5 sometimes ends with a progress report that agent loops interpret as "done")
- Quality gaps: Sonar found 44% more concurrency problems per line than Opus 5; Endor Labs found only 33.5% of fixes passed security checks once memorised answers were excluded
- Effort map: low→medium buys a big quality jump for ~80 cents/task; xhigh→max buys very little and costs ~70% more
- The guide includes a one-message brief template, a drop-in CLAUDE.md system-prompt block covering stop rules/task tracking/report format/prompt-injection protection, and 8 workflows: founder decision memos, board deck consistency, interview-build-verify coding loop, subagent migrations, pre-merge code review, sourced diligence memos, financial model audits, and multi-app operations with approval gates
- Routing rules: when Fable 5.1 is worth 2.5x the price, when GPT-6 Sol is cheaper, and why zero data retention can decide the matter for regulated teams

## Synthesis
The Opus 5.5 guide reveals that the gap between a model's theoretical cost savings and its real-world cost savings is entirely a function of operational discipline. Anthropic claims 40% cost reduction, but only at medium effort with modern prompting conventions — the same model at max effort with legacy prompts costs the same as its predecessor. This means the bottleneck is no longer model capability but user habits: teams carrying over "think carefully" instructions and max-effort defaults from older models are paying Opus 5 prices for Opus 5.5 compute.

The quality findings are the more important signal. 44% more concurrency bugs per line and only 33.5% of security fixes passing once memorised answers are excluded mean Opus 5.5 has specific failure modes that its predecessor didn't — likely because it generates more code faster, and more code means more surface area for subtle bugs. The implication is that evals and verification become more important as models get more capable, not less: the errors shift from obvious-and-rare to subtle-and-frequent. The routing guidance (Opus vs Fable vs GPT-6 Sol) signals the maturation of multi-model strategies — no single model is optimal for all tasks, and the cost-aware router (like FireRouter) is becoming an essential piece of infrastructure.