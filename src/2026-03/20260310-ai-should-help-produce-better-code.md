# AI should help us produce better code
**Source**: https://simonwillison.net/guides/agentic-engineering-patterns/better-code/
**Date**: 2026-03-10
**Author**: Simon Willison
**Keywords**: AI coding, code quality, technical debt, refactoring, agentic engineering, compound engineering, quality tradeoffs

## Elevator pitch
Shipping worse code with AI agents is a deliberate choice, not an inevitable outcome—the same economics that enable velocity also make continuous quality investment feasible for the first time.

## Takeaways
- Refactoring is an ideal use case for coding agents: tasks that are conceptually simple but time-consuming (API redesigns, naming updates, code consolidation) were previously hard to justify; agents make them low-cost.
- Reduced refactoring costs mean teams can now address minor code smells without needing to clear a justification hurdle—the break-even point shifts significantly.
- Rapid prototyping with agents helps identify overlooked approaches early, before architectural decisions become expensive to reverse.
- Following Every's compound engineering methodology: document successful agent-assisted patterns in retrospectives to create a compounding feedback loop.
- The central thesis: velocity and quality are not opposed when using agents—both improve simultaneously when teams deliberately choose quality.

## Synthesis
The prevailing concern about "vibe coding" and AI-assisted development focuses on quality degradation: code generated quickly by agents accumulates technical debt, lacks proper test coverage, and creates maintenance nightmares. Willison's reframe is important: the economics that enable faster shipping also enable faster quality improvement. The question isn't whether AI makes shipping fast—it's what teams choose to ship.

The refactoring argument is the strongest part of this reframe. Refactoring has always had a difficult organizational economics problem: it benefits the codebase but doesn't ship features, making it hard to justify in sprint planning. The cost-benefit calculation changed significantly when agents can perform many refactoring tasks at dramatically lower cost. A migration that would have taken a developer a week now takes hours of agent work with developer review—a threshold change that makes continuous improvement viable without reorganizing sprint priorities.

The compound engineering feedback loop concept—systematically documenting and reusing successful agent-assisted patterns—addresses the individual-to-organizational knowledge transfer problem. Most teams currently treat AI-assisted work as individual productivity enhancement; the patterns that work for one developer on one project don't automatically become organizational capability. Deliberate retrospectives that extract and share these patterns create the kind of compounding improvement that Willison describes.

The rapid prototyping point has a specific implication for architecture decisions: if exploring an alternative approach costs hours rather than days, teams can afford to validate assumptions earlier. The cost of "let's try both approaches" drops enough that "let's commit to an approach before fully understanding it" becomes less necessary.
