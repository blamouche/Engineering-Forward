# The Pulse: New Trend — Concern About Massive Increase in Code Review Load

**Source**: https://newsletter.pragmaticengineer.com/p/the-pulse-new-trend-concern-about
**Date**: 2026-07-23
**Author**: Gergely Orosz
**Keywords**: code review, AI code, engineering productivity, code review tools, AI slop, software engineering

## Elevator pitch

Engineering leaders are increasingly concerned about the growing bottleneck of code review as AI-generated code floods PR pipelines, prompting a boom in AI code review tools and in-house solutions, but with few proven answers for the core problem of review quality degrading under volume pressure.

## Takeaways

- The bottleneck of building software is shifting from writing code to reviewing it, driven by Opus 4.5 and GPT 5.4 generating more and better code
- A boom in AI code review tools has emerged: CodeRabbit, Greptile, Qodo, SonarQube (now Gitar), plus built-in tools from Claude Code, Cursor, GitHub Copilot
- Observability and project management tools are entering the review space: Sentry's Seer AI reviews, Linear code reviews
- Large companies are building in-house tools: Uber's Code Inbox (with smart assignments and risk profiles), Cloudflare's AI Code Reviewer, Faire's Fairey, HubSpot's Sidekick
- In-house implementations often work better than vendor integrations for code review
- An alternative approach — verifying code instead of reviewing it — raises hard questions about what "thorough testing" actually means
- Too much code review is burning out engineers, and many devs now rubber-stamp AI-generated PRs when AI reviewers have no real comments
- Engineers who still put effort into reviews feel overloaded by AI slop PRs
- The current solutions feel more like experiments than proven answers

## Synthesis

Gergely Orosz identifies a structural shift in software engineering that's been accelerating since early 2026: the bottleneck of shipping software has moved from writing code to reviewing it. This isn't a marginal concern — it's becoming the top-of-mind issue for Director-level engineering leaders at companies of all sizes.

The root cause is clear. As models like Opus 4.5 and GPT 5.4 have become capable of generating substantial volumes of working code, the volume of pull requests has exploded. But code still needs to be reviewed before it ships, and the review process hasn't scaled proportionally. The result is a growing queue of PRs and engineers who are increasingly treating reviews as perfunctory approvals rather than substantive quality gates.

The market response has been a Cambrian explosion of AI code review tools. Dedicated platforms like CodeRabbit and Greptile have emerged alongside review features in coding assistants (Claude Code, Cursor, GitHub Copilot) and even tools from adjacent domains — Sentry adding AI code review, Linear adding review capabilities. At the same time, large tech companies are building bespoke solutions. Uber's Code Inbox adds smart assignment and risk profiling. Cloudflare, Faire, and HubSpot have all concluded that in-house implementations outperform vendor integrations for their specific review workflows.

The more interesting philosophical question Orosz raises is whether "reviewing" is even the right frame. An alternative approach would be "verifying" — using comprehensive testing, fuzz testing, or even formal methods to confirm code correctness rather than relying on human judgment. But this raises thorny questions about what level of testing constitutes "thorough," how to verify that the tests themselves are meaningful, and how to connect verification with observability.

The most concerning finding is behavioral: developers are increasingly treating AI code review as a rubber stamp. When the AI reviewer has no substantive comments, humans tend to approve without careful examination. Meanwhile, engineers who still engage deeply with reviews feel overwhelmed by the volume of AI-generated PRs. The solutions available today — both commercial and in-house — feel more like experiments than proven answers. The fundamental tension between speed and quality in code review has been amplified, not resolved, by the current generation of AI tools.

For engineering leaders, this is a strategic problem that requires strategic thinking — not just adopting another AI tool, but reconsidering what code review is for and how it should work in an AI-augmented workflow.