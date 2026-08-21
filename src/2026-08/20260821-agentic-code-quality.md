# Agentic Code Quality
**Source**: https://addyo.substack.com/p/agentic-code-quality
**Date**: 2026-08-10
**Author**: Addy Osmani
**Keywords**: ai-agents, code-quality, quality-gates, constraints, testing

## Elevator pitch
As AI agents generate more code, quality depends less on reviewing the output and more on designing the constraints around the agents — the harness, the environment, and the operating system that gates what proposals actually ship.

## Takeaways
- Traditional code review doesn't scale to agents generating hundreds of thousands of changes daily; the quality check must move from human review to system-level constraints
- Quality gates take many forms: unit tests, property tests, mutation testing, cyclomatic complexity limits, and architectural linting rules — all must be automated and enforced programmatically
- The concept of "back-pressure" is key: when verification can't keep up with the volume of agent-generated changes, you can either scale verification, slow down generation, or lower quality — the first option is the only sustainable one
- An agent can propose anything, but your constraints decide whether the proposal is safe enough, correct, scoped, and useful to ship
- The article introduces a framework for thinking about agentic quality: correctness, maintainability, performance, security, efficiency, and comprehensibility are independent dimensions that each require their own automated checks

## Synthesis
Addy Osmani's article on agentic code quality reframes a growing problem in AI-assisted software development. As coding agents become more prolific — generating changes at a volume that no human review process can keep up with — the traditional approach of "someone reads what you wrote" breaks down entirely. The alternative is to design the system around the agent such that quality is enforced by the environment rather than by post-hoc review.

The key insight is that quality gates need to exist throughout the loop, not as a single review at the end. This means compilers rejecting invalid code, tests failing, security policies blocking bad practices, and CI declining to deploy — all of these are forms of back-pressure that slow or block the agent's output until it meets the standard. The article argues that this back-pressure is actually a feature, not a bug: it gives the agent reliable feedback about what the system considers acceptable, which makes the next iteration more likely to produce a correct result.

The article also highlights the tension between speed and quality at scale. When verification can't keep up with generation volume, organizations face three choices: scale verification (invest in faster CI, more mutation testing, broader property testing), slow down generation (rate-limit agent proposals), or lower the quality bar (accept more risk). Osmani's position is that scaling verification is the only viable long-term strategy, and that organizations should be investing in their constraint infrastructure with the same intensity they invest in their AI coding tools.