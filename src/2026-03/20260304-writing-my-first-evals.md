# Writing my first evals
**Source**: https://workos.com/blog/writing-my-first-evals
**Date**: 2026-03-04
**Author**: Nick Nisi
**Keywords**: AI evaluation systems, LLM testing, evals, agent reliability, quality scoring, pass rates, A/B testing

## Elevator pitch
A developer documents building practical evaluation systems for two AI tools, discovering that statistical measurement of non-deterministic outputs replaces traditional testing and reveals uncomfortable truths about tool effectiveness.

## Takeaways
- Evals measure statistical quality, not deterministic correctness: Unlike traditional tests, evaluation systems accept variable outcomes and measure success through pass rates rather than binary assertions.
- Pass/fail judgments aggregate into meaningful signal: Setting thresholds (80% first-attempt, 90% with correction, 95% with retries) reveals trends and prevents chasing perfection on trivial edge cases.
- Negative eval results expose hidden problems: A context-augmented skill that scored -12% revealed that added information could actively harm output quality, something intuition alone wouldn't have caught.
- Transcripts and qualitative grading matter more than scores: Saving full LLM outputs, diffs, and tool call logs enables root cause analysis when results disappoint.
- Domain-specific metrics beat generic scoring: Measuring what actually matters—correct API methods, hallucination-free outputs, framework-specific patterns—proves more valuable than abstract helpfulness ratings.

## Synthesis
Nisi confronts the core problem of evaluating non-deterministic AI systems: traditional testing's "given X, expect Y" framework collapses when Y varies meaningfully with each run. His solution involves two architecturally different eval systems unified by shared principles.

For the CLI agent, he builds fixture-based testing across 16 frameworks. Real projects copied to temp directories, actual agent invocations, git diffs as ground truth. The agent installs authentication into applications, and success means the code compiles, middleware integrates correctly, and hallucinated API methods don't appear. Quality scoring through Claude Haiku adds subjective dimensions—does the code match project conventions? Is error handling appropriate?—before numerical thresholds gate deployment.

The skills evaluation uses A/B testing: identical prompts run twice, once with contextual knowledge and once without. A/B deltas reveal whether added context helps or hurts. This approach uncovered that several skills actively degraded output quality despite seeming valuable. The scoring mechanism penalizes hallucinations while rewarding correct method signatures and proper parameter usage.

Both systems share crucial implementation details. Multiple grading stages separate functional correctness from quality. Pass rates measured across many trials replace singular success metrics. Saved transcripts enable investigation when results surprise. Automated thresholds prevent regressions but never demand perfection.

Nisi acknowledges uncertainty about whether evals truly predict real-world success, admits to using Claude to build the evaluation system itself (creating circular trust), and ultimately settles on a pragmatic stance: imperfect measurement beats intuition-based shipping, and trends matter more than absolute accuracy.

The deeper insight emerges in his reflection on "trust is a measurement"—quantifying confidence transforms shipping from faith to informed decision-making. When data contradicts intuition, data wins. For teams building AI-powered products, this represents a critical operational shift: replacing subjective assessment with systematic measurement, even when the measurement remains imperfect.
