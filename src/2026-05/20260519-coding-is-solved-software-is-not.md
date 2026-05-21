# Coding is solved? Software is not.
**Source**: https://arcplane.ai/journal/software-is-not-solved
**Date**: May 19, 2026
**Author**: Gao
**Keywords**: AI coding agents, software development workflow, code review, entropy reduction, agent trust, software engineering

## Elevator pitch
AI agents make coding dramatically faster, but this exposes the real bottleneck: the surrounding workflow of specs, context, verification, and human judgment hasn't kept up, so software development as a whole does not feel solved.

## Takeaways
- "Coding is solved" is incomplete: writing code is no longer the slowest part of software development, but problem understanding, scoping, review, and trust-building remain hard.
- AI agents can add entropy: generated code and tests can look complete while failing to actually reduce ambiguity or prove the right behavior.
- Review shifts from code correctness to archaeology: reviewers must reconstruct agent intent from noisy transcripts instead of reading deliberate code.
- Four workflow problems emerge: context selection, specs that stay with the work, verifiable evidence, and human checkpoints at the right moments.
- The bottleneck has moved from implementation speed to workflow integrity — teams need a "spec-in-the-loop" approach where intent, evidence, and judgment travel with the task.

## Synthesis
The article, written by Gao from Arcplane (an auth platform managing millions of identities), pushes back against the claim that "coding is solved" by reframing the problem. Citing Boris Cherny of Claude Code, it acknowledges that AI can now write 100% of the code for certain kinds of programming. But the author argues that software development is fundamentally about reducing entropy: turning ambiguous intent into a verified, reliable system — and coding is only one step in that chain.

The core insight is that fast AI-generated code exposes structural weaknesses in the development workflow. When implementation took hours or days, teams tolerated friction in specs, context sharing, and review. Now that code arrives in minutes, those surrounding processes become the bottleneck — and in some cases, AI makes them worse by producing output that looks complete but doesn't reduce the actual mess. Agents can write large test suites that mostly confirm their own implementation, leaving reviewers to dig through chat transcripts to understand whether the right thing was built.

Gao identifies four recurring problems: purposeful context selection (not just throwing data into a large context window), specs that stay alive and evolve with the work, evidence reviewers can actually inspect rather than a wall of green checks, and human checkpoints placed where judgment truly matters — before implementation to validate scope, and after to assess fit. The author advocates for a "spec-in-the-loop" approach where the spec changes as edge cases are discovered, and the implementation is continually judged against it.

The article is also a product pitch for Arcplane, which aims to provide a workflow layer above GitHub for managing agent-authored work with proper lifecycle, but the analysis stands on its own. The team's conservative stance on auth and permissions changes provides credibility: they cannot afford to trust agents blindly. The conclusion is that code is getting easier to produce, and the real work now is making it hold up — through better workflows, not just better models.
