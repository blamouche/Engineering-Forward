# Many SWE-bench-Passing PRs Would Not Be Merged into Main
**Source**: https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
**Date**: March 10, 2026
**Author**: METR
**Keywords**: SWE-bench, code review, AI benchmarks, maintainers, software engineering

## Elevator pitch
METR finds that about half of AI-generated PRs that pass SWE-bench Verified would still be rejected by real maintainers, highlighting a large gap between benchmark scores and real-world usefulness.

## Takeaways
- Maintainer acceptance rates are ~24 percentage points lower than automated SWE-bench scores.
- The analysis uses real maintainers from scikit‑learn, Sphinx, and pytest reviewing 296 AI PRs.
- Results are normalized against “golden” human PRs to account for reviewer noise.
- The study does not claim a fundamental limitation—agents lacked iterative feedback loops.
- Benchmarks remain useful but can overstate deployable performance without human review context.

## Synthesis
METR’s analysis probes how well SWE-bench Verified scores translate into real‑world acceptance by open‑source maintainers. The core finding is a sizable gap: patches that pass the automated grader still face substantial rejection when reviewed by maintainers, with acceptance rates roughly 24 percentage points lower than benchmark pass rates. The authors emphasize that this is not a declaration that AI systems are fundamentally incapable; rather, it signals that benchmark scores alone can mislead if interpreted as “mergeable in production.”

To test this gap, METR recruited four maintainers from three SWE‑bench Verified repositories (scikit‑learn, Sphinx, and pytest). They reviewed 296 AI‑generated PRs that had already passed the SWE‑bench automated grader. Reviews mirrored real GitHub code review practices, with maintainers asked to accept or request changes and to classify reasons for rejection such as core functionality issues, code quality, or unintended side effects. The key distinction is that the benchmark’s automated grader checks for test pass/fail, while maintainers judge broader criteria like code clarity, adherence to repository standards, and potential regressions.

The study also controls for noise in human review by re‑submitting “golden” PRs—real human contributions that were previously merged. Even these golden patches were not always re‑accepted, revealing the subjectivity and context dependence of maintainer decisions. METR therefore normalizes AI pass rates against this golden baseline. This allows them to say, for example, that if maintainers re‑accept 68% of golden patches, then an AI system’s acceptance rate should be understood as a fraction of that baseline rather than an absolute measure.

Results show that the gap persists even after normalization. Maintainers reject a significant fraction of test‑passing AI PRs, and the rate of improvement in maintainer acceptance appears slower than the rate of improvement in automated benchmark scores. The authors caution that the latter trend is more tentative, but it strengthens the argument that benchmark improvements do not translate one‑to‑one into production readiness.

Crucially, METR is careful about interpretation. The study does not claim that agents cannot reach human‑level acceptance; it notes that the AI patches were “one‑shot” submissions without the iterative feedback loop that human developers typically receive. Many rejections reflect issues that could plausibly be fixed with follow‑up iterations, better prompts, or tighter adherence to repository conventions. Thus, the gap may reflect elicitation and workflow limitations rather than intrinsic capability ceilings.

The practical implication is that SWE‑bench remains valuable for comparing systems, but teams should be cautious when mapping benchmark scores to operational readiness. For real‑world automation, adding human review, iterative loops, and repo‑specific standards is likely essential. Benchmarks are best viewed as one signal among many, not a direct proxy for mergeable code.
