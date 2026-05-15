# We Tested DeepSeek V4 Pro and Flash Against Claude Opus 4.7 and Kimi K2.6
**Source**: https://blog.kilo.ai/p/we-tested-deepseek-v4-pro-and-flash
**Date**: 2026-05-13
**Author**: Darko (Kilo Blog)
**Keywords**: DeepSeek V4, Claude Opus 4.7, Kimi K2.6, AI benchmarking, open-weight models, coding agents, FlowGraph, model pricing, code generation

## Elevator pitch
DeepSeek V4 Pro scored 77/100 for $2.25 (slotting between Claude Opus 4.7 at 91 and Kimi K2.6 at 68), while DeepSeek V4 Flash scored 60/100 for an unprecedented $0.02, establishing open-weight models as serious contenders on cost-adjusted quality for complex backend builds.

## Takeaways
- DeepSeek V4 Pro lands between Claude Opus 4.7 (91/100) and Kimi K2.6 (68/100) at 77/100, getting the broad system shape right but failing on lease expiry enforcement, cross-run scheduling, and build integrity.
- DeepSeek V4 Flash scored 60/100 for $0.02 total—a price point that didn't exist before—with a critical bug: the workflow start endpoint was mounted under the wrong route prefix, making the system unusable from a client perspective.
- Both DeepSeek models share the same expired-lease completion bug: a worker can still mark work as done after its lease expires, violating the ownership model.
- Claude Opus 4.7 had only one reproducible bug; every other model lost points on timing, recovery, and coordination between moving parts.
- With DeepSeek's 75% promotional discount (through May 31, 2026), V4 Pro would cost ~$0.55, making it cheaper than Kimi K2.6 while scoring 9 points higher.

## Synthesis
DeepSeek launched V4 Pro and V4 Flash on April 24, 2026 under MIT license—their first new architecture since V3 and their first open-weight lineup with two tiers. The Kilo team ran both through the same FlowGraph spec used in their previous Claude Opus 4.7 vs Kimi K2.6 comparison: a workflow orchestration backend with 20 endpoints, persistent state, lease management, retries, and event streaming.

DeepSeek V4 Pro achieved 77/100, getting the broad system architecture right. Endpoints are wired, the test suite passes, and the project layout is reasonable. But the same failure patterns as Kimi K2.6 surfaced: lease expiry handling, scheduling, validation, and build integrity. Specifically, timed-out workers can still complete steps (enforced on heartbeats but not completions), a full workflow blocks unrelated work when its parallel cap is reached, and the TypeScript build fails—even after fixes, the project isn't runnable through npm start because the TS config doesn't emit compiled output.

DeepSeek V4 Flash's score of 60/100 comes with a $0.02 price tag that changes the cost conversation entirely. The internal logic is plausible, but the public API is fatally flawed: the workflow creation endpoint is mounted under the wrong route prefix (/runs/key/:key/runs instead of /workflows/key/:key/runs), making the system's entry point inaccessible. The test suite calls internal functions directly, so tests passed while the API was broken. Flash also shares the expired-lease completion bug and rejects valid JSON arrays as workflow input, accepting only objects.

On tool calling reliability, Flash surprised: it read files before editing, installed dependencies and ran tests at sensible points, and avoided retry loops—unexpected performance at this price tier where cheap models typically break down on malformed arguments and hallucinated paths.

The cost-per-point analysis is revealing: DeepSeek V4 Flash's cost per point is roughly 30x cheaper than Kimi K2.6 and 100x cheaper than Opus 4.7. A 60/100 score isn't a reason to use Flash alone, but at $0.02 per attempt, running the task multiple times for comparison is still cheaper than a single Kimi K2.6 run. The pattern holds: surface coverage gaps between open-weight and proprietary models are narrowing, while correctness gaps on hard code paths (lease recovery, cross-run scheduling) persist but are also shrinking.
