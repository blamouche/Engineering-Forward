# Can coding agents relicense open source through a “clean room” implementation of code?
**Source**: https://simonwillison.net/2026/Mar/5/chardet/
**Date**: March 05, 2026
**Author**: Simon Willison
**Keywords**: open source, licensing, clean room, coding agents, chardet

## Elevator pitch
Simon Willison examines the chardet 7.0 rewrite dispute and asks whether AI‑assisted “clean room” rewrites can legitimately relicense mature open‑source code.

## Takeaways
- chardet 7.0.0 claims to be a ground‑up MIT rewrite of an LGPL project.
- The original author disputes the relicensing, arguing maintainers were too exposed to the old code.
- The maintainer argues the result is independent and shows low similarity scores via JPlag.
- AI tools (Claude Code) were central to the rewrite process, creating new legal/ethical questions.
- The case foreshadows broader conflicts over AI‑assisted reimplementation in open source and commercial IP.

## Synthesis
This essay uses the chardet 7.0.0 licensing controversy as a lens to explore whether coding agents can produce legitimate “clean room” rewrites that allow relicensing. chardet, a long‑standing LGPL Python character‑detection library, was rewritten and released under MIT with claims of faster and more accurate performance. Mark Pilgrim, the original author, objected that relicensing is not permitted under LGPL because the maintainers had extensive exposure to the original codebase, which undermines clean‑room guarantees. He argued that even a complete rewrite does not escape the derivative‑work obligations if the developers were deeply familiar with the previous implementation.

The maintainer, Dan Blanchard, acknowledged the lack of traditional clean‑room separation. However, he argued that the goal of clean‑room methodology is independence of the resulting code, not necessarily strict process separation. He offered evidence from JPlag, a code‑similarity tool, showing minimal similarity between the new 7.0.0 code and prior releases, while earlier versions had high similarity. He also described the rewrite process: generate a design document, start in a fresh repository, explicitly instruct Claude not to reference LGPL/GPL code, and iteratively review and test the generated code. The repository contains detailed artifacts of this process, including a step‑by‑step rewrite plan.

Willison highlights ambiguities that make the case difficult. First, the maintainer had more than a decade of exposure to the codebase, which traditionally invalidates a clean‑room defense. Second, the rewrite process apparently referenced a file listing charset metadata, suggesting at least one direct touchpoint with the old code. Third, the AI model itself was likely trained on the original chardet code, raising the question of whether a model can unknowingly reproduce derivative content. Fourth, the historical lineage of chardet complicates matters further: the original code was itself a port of Mozilla’s MPL‑licensed library. Finally, the decision to keep the same PyPI package name adds another layer of continuity that could be interpreted as derivative, even if the code is new.

Willison does not take a definitive stance, but leans toward the rewrite being legitimate while acknowledging strong arguments on both sides. He frames the dispute as a microcosm of a broader shift: coding agents can now generate fresh implementations quickly and cheaply, potentially enabling relicensing or rapid re‑creation of mature systems. That could reshape open source incentives and possibly threaten proprietary IP if companies can reconstruct functionality from tests or specs. The essay suggests that legal precedent is likely to emerge as these cases multiply.

Overall, the piece is less about chardet specifically and more about the implications of AI‑assisted software creation for licensing norms. Clean‑room practices were designed for human teams; AI changes the mechanics and lowers the cost, making the boundary between derivative and independent works harder to enforce. Willison’s takeaway is that the open‑source world is encountering these questions first, but the commercial world will soon face the same disputes, likely leading to significant litigation and policy adjustments.
