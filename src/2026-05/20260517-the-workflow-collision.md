# The Workflow Collision

**Source:** Webframp
**Author:** Sean Escriva
**Date:** May 17, 2026
**URL:** https://webframp.com/posts/the-workflow-collision

## Summary

A practical engineering analysis of the fundamental tension between human team workflows (Kanban, pull-based, minimal states) and AI agent lifecycles (state machines, enforced transitions, adversarial review gates). The author argues teams should not merge these systems but compose them — letting the human workflow govern what matters and why, while the agent lifecycle governs how specific work gets executed.

## Key Points

- **Two incompatible systems:** Team workflows are pull-based and trust workers to self-organize; agent lifecycles are operator-initiated with enforced transitions because agents can't be trusted to choose
- **Planning conflict:** Team design sessions explore problems collaboratively; agents generate complete plans upfront that must pass adversarial review before implementation
- **State count mismatch:** Kanban uses ~6 states (more is anti-pattern); agent lifecycles need 10+ granular states for resumability and auditability
- **Failure semantics differ:** Teams treat failed work as learning; agents treat failure as process failure to prevent
- **Hierarchy gap:** Team workflows connect daily work to strategic goals; agent lifecycles are flat — each issue is independent
- **Recommended approach:** Composition, not merge. Agent lifecycle runs as a sub-process inside "In Progress" — the human workflow governs what matters, the agent lifecycle governs execution
- **Frameworks referenced:** Swamp and similar agentic frameworks
- **Quote:** "The answer is not to pick one. It is to figure out where one ends and the other begins."

## Why It Matters

As teams move from one-off agent tasks to multi-step agent work spanning hours or days, the workflow collision becomes unavoidable. This article provides one of the clearest frameworks for resolving it: recognize they're different systems optimized for different actors, and design the integration boundary deliberately rather than forcing either side to conform.
