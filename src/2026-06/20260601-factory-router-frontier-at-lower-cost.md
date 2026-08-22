# Factory Router: Frontier Performance at 20-25% Lower Cost
**Source**: https://factory.ai/news/factory-router
**Date**: 2026-06-01
**Author**: Factory.ai
**Keywords**: Factory Router, model routing, cost optimization, coding agent, Terminal-Bench, Legacy-Bench, Pareto frontier, enterprise AI, token spend

## Elevator pitch
Factory Router automatically selects the right model for each coding session and escalates to a more capable one only if the first choice struggles—achieving 99% of Claude Opus 4.7's pass rate at 20% lower cost on Terminal-Bench 2.

## Takeaways
- Factory Router cuts token spend by 20-25% while maintaining frontier performance by automatically selecting the right model for each coding session
- On Terminal-Bench 2: 99% of Claude Opus 4.7's pass rate at 20% lower cost per session; on Legacy-Bench: 96% at 25% lower cost
- If the selected model struggles to complete the task, Router automatically escalates to a more capable model to ensure high-quality outcomes
- Provider failover keeps sessions running through alternative paths when providers degrade, rate limits hit, or capacity gets constrained, providing 99.9%+ request reliability
- Enterprise admins can provide routing guidance—workflow patterns, codebase areas, toolchains, and model preferences—that shape automatic model selection

## Synthesis
Factory Router addresses a growing problem in enterprise AI coding: engineers default to the most performant models for fear of losing on performance, but simple questions, mechanical refactors, documentation updates, and small bug fixes don't need frontier capability. The result is rapidly exhausted AI budgets without clear increases in organization-level output. A higher token bill does not mean more engineering work is getting done.

The solution is automatic model selection per session. Factory Router chooses the optimal model from a diverse pool of frontier and efficient models. If the selected model struggles to complete the task, Router moves the session to a more capable model. The Pareto frontier analysis shows that near the top of the cost/performance curve, cost drops sharply while performance barely moves, because the first work to leave the frontier model is work that cheaper models handle just as well. Factory Router operates on this flat stretch, just before the curve bends.

The reliability angle is equally important. Provider failover keeps Droid sessions running through provider issues, capacity limits, and model availability changes. Enterprise customers get reserved throughput for critical work instead of depending only on shared public capacity. US-hosted open-source models are available for teams that need cost-efficient or controlled model options.

The enterprise controls let organizations shape routing to their actual work patterns. Admins can describe workflow patterns, codebase areas, toolchains, and model preferences that should shape automatic selection. The same policy surfaces that govern other Factory models apply to Factory Router, so admins can manage access, compliance, and automatic-routing eligibility without creating a separate control plane. The key insight: any fixed model is one point on the cost/performance curve—either too expensive for easy work or too weak for hard work. Staying on the frontier means choosing per session.