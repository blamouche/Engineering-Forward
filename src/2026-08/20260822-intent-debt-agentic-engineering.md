# The Intent Debt: Why Agentic Engineering Makes Unwritten Knowledge Expensive
**Source**: https://tldrnewsletter.com (TLDR, 2026-06-08)
**Date**: 2026-06-08
**Author**: TLDR
**Keywords**: intent-debt, agentic-engineering, documentation, technical-debt, knowledge-management

## Elevator pitch
Intent debt — the unwritten goals, constraints, and rationale for why a system is the way it is — becomes dramatically more expensive in agentic engineering because intent can only come from humans, and models don't know why decisions were made.

## Takeaways
- Intent debt comprises the artifacts that were never written down: goals, constraints, and rationale for system design decisions, often scattered in team documents or discussions but unorganized and incomplete
- Agentic engineering makes intent debt more expensive because models don't know why decisions were made — they can only work from what's explicitly documented
- Unlike technical debt which can be measured and refactored, intent debt is invisible: it only surfaces when an agent makes a decision that contradicts an unstated constraint
- The economics of not writing things down change fundamentally when AI agents are the ones reading the documentation — missing context leads to wrong decisions at scale
- Writing down intent becomes a form of infrastructure investment, not documentation overhead

## Synthesis
The concept of "intent debt" articulated in this TLDR piece identifies a class of technical liability that is distinct from traditional technical debt. While technical debt refers to code-level compromises — duplicated logic, outdated patterns, missing tests — intent debt comprises the artifacts that were never written down: the goals, constraints, and rationale for why a system is the way it is. This knowledge often exists only in team members' heads, scattered across chat threads and meetings, but is never formalized.

The argument is that agentic engineering makes this debt dramatically more expensive. When a human developer works on a system, they can ask a colleague why a decision was made, or infer rationale from context. An AI agent cannot do this — it can only work from what is explicitly documented. If the rationale for a design constraint was never written down, the agent has no way to know it exists, and will make decisions that contradict it. The result is wrong decisions at scale, because agents operate faster than humans and touch more of the codebase.

The economics of documentation change fundamentally in this model. Writing down intent is no longer an overhead activity that can be deferred — it becomes a form of infrastructure investment. Without it, agents will repeatedly make decisions that look correct in isolation but violate unstated system-level constraints. The cost of this is not just rework but also subtle architectural erosion, as agents optimize for locally correct solutions that are globally wrong.

The article positions intent debt as a new category that engineering teams need to manage deliberately, especially as they integrate AI agents into their development workflows.