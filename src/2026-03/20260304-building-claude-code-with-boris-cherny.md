# Building Claude Code with Boris Cherny
**Source**: https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
**Date**: 2026-03-04
**Author**: Gergely Orosz
**Keywords**: Claude Code, Boris Cherny, Anthropic, AI coding tools, parallel agents, prototyping, clean code, developer productivity, Meta

## Elevator pitch
Boris Cherny, Head of Claude Code at Anthropic, ships 20-30 PRs daily using five parallel Claude instances—and argues that clean codebases, simple search strategies, and prototypes-over-specs are what make AI-assisted development actually work.

## Takeaways
- 20-30 PRs daily by running five parallel Claude instances: once a solid plan exists, "it will one-shot the implementation almost every time."
- Clean codebase research from Meta showed double-digit productivity gains—the same principle applies to AI-generated code, as partially-migrated codebases confuse both humans and models.
- Claude Code's search uses basic glob and grep—outperformed local vector databases and recursive model-based indexing despite being simpler.
- Anthropic has a flat title structure: everyone is "Member of Technical Staff," removing hierarchy from cross-functional collaboration.
- The Claude Code team abandoned PRDs and built dozens of working prototypes before shipping features—PRDs don't capture the novel nature of AI-assisted development.

## Synthesis
The 20-30 PRs per day number is striking, but the mechanism behind it is more interesting than the headline. Cherny's approach involves planning first—developing a solid implementation plan—and then parallelizing execution across multiple Claude instances. This is a different workflow than sequential AI-assisted coding, and it requires a different set of engineering skills: decomposing work into parallel-runnable tasks, writing plans that are clear enough for one-shot implementation, and managing the review and integration of multiple concurrent outputs.

The clean codebase finding from Cherny's Meta research connects to something important about AI coding tools: they amplify existing code quality in both directions. In a clean, well-organized codebase, AI tools can make precise changes with low risk of unintended effects. In a tangled codebase, the same tools make changes that create new tangles. The teams getting the most value from AI coding assistance are often the ones who invested in code quality before these tools existed.

The simple search finding cuts against a common assumption that AI coding tools should use sophisticated retrieval methods. Claude Code's glob/grep approach outperforms more complex alternatives, probably because simplicity creates predictability. When engineers understand exactly what context the tool has, they can communicate more precisely. Complex retrieval mechanisms introduce uncertainty about what the model knows, which makes accurate prompting harder.

Prototypes over PRDs reflects a real limitation of written specifications for AI-native products. PRDs describe functionality by analogy to existing products or abstract user needs; AI coding tools create genuinely novel interaction patterns that don't have good analogues. Building and discarding dozens of prototypes is more expensive in traditional development but becomes feasible when prototypes take hours rather than weeks.
