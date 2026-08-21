# Engineering Management After the Cost of Code Collapsed
**Source**: https://karimjedda.com/engineering-management-after-cost-of-code-collapse/
**Date**: 2026-07-20
**Author**: Karim Jedda
**Keywords**: engineering management, AI, LLMs, code generation, verification, junior engineers, org design

## Elevator pitch
A director of engineering systematically evaluates which management practices rest on assumptions that broke when LLMs made code cheap, and which remain valid—concluding that verification, not generation, is now the binding constraint.

## Takeaways
- About half of traditional engineering management practices rest on assumptions that have broken (code is expensive), while the other half remain valid because they rest on human coordination and verification needs.
- Velocity, PR counts, and ticket closures are now actively misleading metrics—volume is cheap, so optimizing for it rewards the wrong behavior.
- The "right thing still takes time" rule splits in two: plumbing time collapsed (scaffolding, first drafts), but correctness time splits further into mechanical verification (collapsing) and semantic verification (unchanged).
- The junior engineer pipeline is an unsolved problem: AI absorbs the practice work that historically built judgment, creating a 3–5 year delay before the impact becomes visible.
- In the agentic limit, org charts stop recording who produces and start recording who signs—headcount becomes a measure of accountability capacity, not output capacity.

## Synthesis
Jedda's essay is one of the most clear-eyed assessments of how AI actually changes engineering management, precisely because it refuses the two common extremes of either dismissing AI's impact or declaring management obsolete. Instead, it systematically examines what each management practice assumes and whether that assumption still holds.

The most actionable insight is the splitting of verification into mechanical and semantic layers. Mechanical verification—anything expressible as types, tests, contracts, lint rules, invariants—is collapsing because agents can run the loop faster than humans. But semantic verification—does the code implement what the business actually needs?—depends on human judgment and institutional knowledge that AI checking AI structurally cannot validate, because checker and generator share the same blind spots.

This leads to a critical strategic implication: the fraction of your correctness that is machine-checkable is not fixed. It's a function of your specifications, contracts, and invariants. "Teams with strong specs get the full benefit of cheap checking. Teams with weak specs get generated code reviewed by the same machine that generated it." Investing in machine-checkable correctness is now among the highest-leverage infrastructure work an organization can fund.

The junior pipeline argument is perhaps the essay's most sobering point. The judgment we want in senior engineers was historically built through precisely the work that AI now absorbs. If the practice disappears, the pipeline that produces seniors breaks—with a 3–5 year delay before we notice. Jedda's honest position—"I cannot tell you these solutions work, because the outcome variable is the quality of a senior engineer half a decade from now"—is a refreshing alternative to the vendor-driven certainty that dominates AI discourse.

The concluding vision is stark: in the agentic limit, org charts record who signs, not who produces. Headcount measures how much accountability you can afford. This reframes the role of engineering management from output coordination to specification and ownership—the exact same shift that individual contributors are experiencing, just one level up.