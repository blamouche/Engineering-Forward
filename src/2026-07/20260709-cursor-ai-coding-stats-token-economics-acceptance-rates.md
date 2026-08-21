# Interesting AI Coding Stats from Cursor
**Source**: https://newsletter.pragmaticengineer.com/p/the-pulse-interesting-ai-coding-stats
**Date**: 2026-07-09
**Author**: Gergely Orosz
**Keywords**: Cursor, AI coding, token economics, input tokens, Opus 4.7, GPT-5.5, code acceptance rates

## Elevator pitch
Cursor's two-year usage data reveals that input tokens dominate AI coding costs (90% of tokens, 70% of cost), power users generate 30-40K lines/week, and nearly 40% of developers now accept AI changes without manual review — a dramatic shift signaling fundamental changes in how code gets written.

## Takeaways
- The median Cursor user generates ~700 lines of code per week; the 90th percentile hits 9,000; the top 1% produces 30-40K lines — equivalent to 45 "median" developers
- 90% of Cursor's token usage is input tokens (reading the codebase), not output tokens (writing code) — confirming the classic 10:1 read-to-write ratio
- Input tokens account for ~70% of AI coding costs despite being priced at 1/5 of output tokens, making caching a critical efficiency layer
- Opus 4.7 is close to 10x more expensive than Composer 2.5 per agent request, but has the same cost-per-line-accepted as GPT-5.5 at half the request cost
- The share of devs letting AI agents commit without manual review jumped from ~10% to ~40% in one month, correlating with Opus 4.7 and GPT-5.5 releases

## Synthesis
Gergely Orosz highlights Cursor's data release as one of the most revealing windows into how AI is reshaping software development. The token economics are perhaps the most striking finding: the 10:1 read-to-write ratio that Uncle Bob observed in 2008 for human code review now applies to AI token usage. This has massive implications for infrastructure — context caching and reuse isn't just an optimization, it's a requirement. Cursor spends 90% of tokens on cache reads, 2.5% on cache writes, 7% on new input, and only 0.6% on output. Without caching, costs would be 10x higher.

The cost-per-line-accepted metric is more nuanced than raw cost-per-request. Opus 4.7 and GPT-5.5 have identical cost-per-line-accepted despite Opus being 2x more expensive per request, because Opus's higher acceptance rate compensates. This suggests the industry should evaluate models on value delivered (accepted code), not on raw request cost.

The most disruptive finding is the acceptance-without-review trend. Going from 10% to 40% of devs not manually checking AI-generated code in a single month is an acceleration that forces questions about code quality, security, and the changing role of the developer. If nearly half of AI changes are accepted without review, the role of the engineer shifts from writing and reviewing code to designing systems and validating outcomes — which is exactly what the "tending your loop" and "agentic OS" paradigms describe. Google's Gemini models and Grok were notably absent from Cursor's data due to minimal platform usage, suggesting the market is consolidating around a few dominant model providers for coding specifically.