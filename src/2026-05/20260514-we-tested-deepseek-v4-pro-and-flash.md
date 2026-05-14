# We Tested DeepSeek V4 Pro and Flash Against Claude Opus 4.7 and Kimi K2.6
**Source**: https://blog.kilo.ai/p/we-tested-deepseek-v4-pro-and-flash
**Date**: May 13, 2026
**Author**: Darko (Kilo Code)
**Keywords**: DeepSeek V4, Claude Opus 4.7, Kimi K2.6, LLM benchmarking, open-weight models, AI coding, FlowGraph, cost-performance analysis, MIT license

## Elevator pitch
DeepSeek V4 Pro scored 77/100 for $2.25, landing between Claude Opus 4.7 (91) and Kimi K2.6 (68), while DeepSeek V4 Flash scored 60/100 for $0.02 — a previously nonexistent price point that changes the economics of AI-first development.

## Takeaways
- DeepSeek V4 Pro slots between Opus 4.7 and Kimi K2.6 on quality, with failures concentrated in the same areas as Kimi: lease expiry handling, scheduling, validation, and build integrity
- DeepSeek V4 Flash is in a new category: $0.02 for an entire backend build attempt, roughly 100x cheaper per quality point than Opus 4.7, making multiple cheap attempts economically viable
- Both DeepSeek models share a critical bug: timed-out workers with expired leases can still complete steps, despite documentation claiming otherwise
- Tool calling reliability on DeepSeek V4 Flash held up surprisingly well — the model read files before editing, ran tests at sensible points, and avoided retry loops, defying expectations for its price tier
- Claude Opus 4.7 still leads with only one reproducible bug, while the gap on surface coverage between open-weight and proprietary continues to narrow

## Synthesis
Darko's benchmark at Kilo Code, published May 13, 2026, puts DeepSeek's new V4 lineup through the same FlowGraph spec previously used to compare Claude Opus 4.7 and Kimi K2.6. The test is a workflow orchestration backend with 20 endpoints, persistent state, lease management, retries, and event streaming — deliberately heavier than typical coding benchmarks to push models to their limits.

DeepSeek V4 Pro and V4 Flash launched together on April 24, 2026 under MIT license, marking DeepSeek's first new architecture since V3 and their first open-weight lineup with two tiers. V4 Pro scored 77/100 for $2.25, placing it between Opus 4.7 at 91 and Kimi K2.6 at 68. With DeepSeek's 75% promotional discount through May 31, the same run would cost approximately $0.55, putting it below Kimi K2.6 on cost while scoring 9 points higher.

The bugs reveal where open-weight models still lag. Both DeepSeek models share an expired-lease completion bug: a worker whose lease has timed out can still mark a step as completed, reaching past its expired ownership. This was documented as not-allowed in the model's own README but not enforced in code. V4 Pro's claim logic also blocks unrelated work: when the first candidate run on a queue is at its parallel cap, the function gives up entirely rather than checking the next candidate, causing idle workers despite available work. The TypeScript build failed because the config was set to not emit compiled output while package.json expected compiled output.

DeepSeek V4 Flash is the more interesting result. At $0.02 total run cost, it occupies territory no prior benchmark has tested. Its score of 60/100 reflects real gaps: the workflow-run creation endpoint was mounted under the wrong route prefix, rendering the system's entry point unusable from an HTTP client perspective; failed workflows still handed out work to remaining steps; and validation only accepted JSON objects when the spec allowed arbitrary JSON. But the model's tool-calling behavior was unexpectedly solid — reading files before editing, installing dependencies at sensible points, running tests, and avoiding the retry loops that typically plague cheaper models.

The cost-per-point analysis is striking: DeepSeek V4 Flash delivers roughly 100x cheaper per quality point than Opus 4.7 and 30x cheaper than Kimi K2.6. This creates a new development strategy: run the same task three or four times with Flash and compare results, for less than a single Kimi K2.6 attempt. For workflows where a human review step is acceptable, the math changes the economics of AI-assisted development.

The broader pattern from this and previous Kilo benchmarks is consistent: the surface coverage gap between open-weight and frontier proprietary models is narrowing rapidly, while the correctness gap in hard code paths — lease recovery, cross-run scheduling, expired-state rejection — remains but is also narrowing. Claude Opus 4.7 had one reproducible bug; the other three models had multiple.
