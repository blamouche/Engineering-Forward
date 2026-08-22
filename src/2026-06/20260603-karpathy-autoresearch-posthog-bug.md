# Karpathy's Autoresearch Found a 3-Year-Old Bug in PostHog's Query Engine
**Source**: https://posthog.com/blog/karpathy-autoresearch-query-engine-bug
**Date**: 2026-06-03
**Author**: PostHog team
**Keywords**: Karpathy, autoresearch, PostHog, ClickHouse, query optimization, AI agent, bug finding, performance, primary key, timestamp filter

## Elevator pitch
PostHog pointed an AI agent at its own query engine, fed it slow queries from production, and let it run overnight—the next morning it discovered a three-year-old bug where every query with a timestamp filter had not been using ClickHouse's primary key correctly, improving performance by 11-37%.

## Takeaways
- A three-year-old bug in PostHog's ClickHouse query engine caused every timestamp-filtered query to skip primary key pruning, scanning 62% more granules than necessary
- The autoresearch loop (pi + pi-autoresearch) found the bug by running EXPLAIN, noticing "Partition: Condition='true'" (no pruning), and trying two fixes: adding indexHint() and rewriting the timestamp comparison
- The fix improved the best run by 22% (2,824ms → 2,192ms) and the trimmed mean by 37% (4,694ms → 2,954ms), while reducing skip-index granules by 62%
- The agent had no priors—it treated a three-year-old expression with the same suspicion as a line written yesterday, seeing what humans had stopped seeing
- PostHog is now building a pipeline to automatically detect slow queries from production, spin up sandboxed ClickHouse clusters, and run autoresearch campaigns without human intervention

## Synthesis
PostHog ran an autoresearch hackathon using Karpathy's autoresearch concept: give an AI agent a system, a benchmark, and a budget, and let it loop—propose a change, run the benchmark, keep what helps, throw away what doesn't. The setup used pi (a small terminal coding agent) with pi-autoresearch (a community extension wiring Karpathy's loop into pi), running against a throwaway ClickHouse test cluster with anonymized production data.

The investigation was structured into campaigns, hypotheses, and experiments. Each campaign targeted one slow query on one git branch. The agent had to do an explicit reflection pass after every experiment instead of just hill-climbing. Range-narrowing helped: when a target query timed out, the agent halved the date range until it completed in 1-10 seconds, then optimized against that narrowed version.

The bug was silently broken primary key usage. For almost three years, every PostHog query with a timestamp filter wrapped the timestamp field in a toTimeZone() function call, which prevented ClickHouse from using the primary key for pruning. The autoresearch loop ran EXPLAIN, noticed the partition condition was "true" (meaning no pruning at all), and tried two approaches: adding indexHint() with bare-timestamp bounds, and rewriting the comparison so the field side was bare and the constant carried the timezone. The second approach worked.

The most interesting insight is the second-order effect: the agent doesn't carry the bias that comes from living in a codebase. To the PostHog team, the toTimeZone() wrap had always been there—the kind of code you stop seeing. The agent has no priors. It runs every diagnostic, reads the surrounding source for context, and treats a three-year-old expression with the same suspicion as a line written yesterday. PostHog is now building a pipeline to automate this: detect slow queries from production, spin up sandboxes, run autoresearch campaigns, and ship fixes without the hackathon.