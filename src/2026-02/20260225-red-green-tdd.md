# Red/green TDD - Agentic Engineering Patterns
**Source**: https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/
**Date**: 2026-02-25
**Author**: Simon Willison
**Keywords**: agentic engineering, TDD, testing, coding agents, reliability

## Elevator pitch
Tell a coding agent to work “red/green TDD” and you get a tight loop where tests fail first, then pass—reducing both broken output and pointless code.

## Takeaways
- “Red/green TDD” is a compact prompt that encodes a full test-first workflow agents understand well.
- The red step (confirm tests fail) matters: it validates the test actually exercises the missing behavior.
- Test-first constrains the solution space and makes verification cheaper than manual review of generated code.
- A growing test suite is the best long-term defense against regressions as an agent changes code over time.
- The practice mitigates two frequent agent failure modes: code that doesn’t work and code that isn’t needed.

## Synthesis
This note argues that the most effective single instruction you can give a coding agent is to apply “red/green TDD”—a shorthand for disciplined test-first development. In classic Test Driven Development, you specify desired behavior as an automated test, observe that it fails (red), then implement the minimum change that makes it pass (green). The author’s claim is that this workflow maps unusually well to the strengths and weaknesses of code-generating agents.

Agents are fast at producing plausible code, but plausibility is not correctness. They can also enthusiastically build functionality that looks useful but never gets integrated or used. Test-first development addresses both risks by forcing every change to be justified by an executable specification and by providing a concrete mechanism to validate results. The test suite becomes the arbiter: either the behavior is implemented or it isn’t.

A key nuance is the insistence on the red step. If you write a test and go straight to implementation without confirming the test fails, you can accidentally create a test that already passes. That can happen due to an incorrect assertion, a fixture that masks the missing behavior, or a misunderstanding of the API surface. For humans, “watch it fail first” is a guardrail; for agents, it’s even more critical because the agent can otherwise report success while both the test and the code are wrong.

The broader payoff is compounding. Each agent-assisted change adds not just code, but also tests that lock in the intended behavior. As the codebase grows, the probability of regressions rises, and the value of fast, automated verification increases. A robust test suite reduces the cognitive burden of reviewing large diffs and makes future agent work safer: the same tests can be rerun after refactors, dependency updates, or additional features.

Practically, the guidance is to encode this into prompts. A simple instruction like “Use red/green TDD” acts as an operational contract: generate tests first, run them, observe failure, then iterate until passing. It’s an example of how prompt design can leverage shared developer vocabulary to steer agents toward workflows that produce more reliable, maintainable output.