# Devin Fusion: Frontier Performance at 35% Lower Cost
**Source**: https://cognition.com/blog/devin-fusion
**Date**: 2026-06-29
**Author**: The Cognition Team
**Keywords**: devin, cognition, multi-model, model-routing, ai-agents, cost-optimization

## Elevator pitch
Cognition introduces Devin Fusion, a multi-model harness that runs a frontier "main agent" alongside a cheaper "sidekick" model, maintaining frontier-level coding performance at 35-60% lower cost through dynamic mid-session routing.

## Takeaways
- Devin Fusion uses a dual-agent architecture with a main frontier model and a cheaper sidekick, where the main agent delegates appropriate tasks while maintaining oversight on planning and final review.
- The sidekick approach retains frontier intelligence rather than "benchmark-score" intelligence because the main model stays in the loop for significant decisions, interpretation of ambiguity, and final review.
- Dynamic mid-session routing switches models during context compaction events — which would trigger cache misses anyway — getting model switching "for free" without additional cache penalties.
- Fable 5 proved exceptionally performant in multi-agent setups, achieving 41% cost reduction while maintaining Fable 5-level performance in a traditional harness.
- On the latest FrontierCode 1.1 Extended benchmark, Fusion achieves up to 60% cost reduction compared to pure frontier model usage, with largest efficiency gains on implementation-focused sessions.
- Internally at Cognition, 88% of merged PRs were driven entirely by the automated Fusion router, validating real-world usability beyond benchmarks.

## Synthesis
Cognition's Devin Fusion represents a significant architectural shift in how AI coding agents use models. Rather than pointing the most expensive model at every step of a task, Fusion runs two agents in parallel — a frontier "main agent" and a cost-effective "sidekick" — and routes work between them dynamically. The key insight is that most coding tasks contain a mix of high-judgment moments (where frontier intelligence matters) and mechanical steps (where a cheaper model suffices). By delegating the latter to the sidekick, the system maintains output quality while dramatically cutting costs.

The technical approach solves three problems that plagued earlier model-routing attempts. First, simple routers that select a single model for an entire task cannot adapt to varying difficulty within a session — the sidekick pattern keeps the frontier model available for hard moments while the sidekick handles easy ones. Second, naive model switching incurs expensive cache misses — Fusion sidesteps this by switching during context compaction events, which would trigger misses anyway. Third, the "smart friend" approach (having one model query another for advice) forces uncached context transfers — Fusion avoids this by maintaining separate persistent, cached contexts for each agent.

The results are compelling. On implementation-focused tasks like refactoring, dependency removal, and mechanical feature additions, the sidekick handles most of the work at 30-60% cost savings with no quality loss. On judgment-heavy tasks like complex multi-file features, delegating coding to the sidekick can backfire — the main agent's nuanced understanding of intent is lost. This creates a clear decision matrix: delegate when the task is mechanical, keep frontier intelligence when judgment is the deliverable.

Perhaps most notable is the finding that the sidekick pattern scales better as models get smarter — Fable 5's superior delegation and planning abilities yielded a larger cost improvement than Opus-level models. This suggests that multi-model harnesses will become more valuable, not less, as frontier models continue to improve.