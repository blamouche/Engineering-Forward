# Writing code is cheap now - Agentic Engineering Patterns
**Source**: https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/
**Date**: 2026-02-25
**Author**: Simon Willison
**Keywords**: coding agents, engineering habits, software quality, trade-offs, cost of change

## Elevator pitch
When code generation becomes near-free, the bottleneck shifts from writing code to ensuring it’s good—so teams need new habits that default to trying things, then paying the real cost in verification and integration.

## Takeaways
- Agents collapse the cost of producing code, invalidating many planning and trade-off instincts built around expensive human typing.
- “Good code” remains costly: correctness, confidence, minimality, error handling, tests, docs, and non-functional requirements.
- The developer’s role shifts toward steering, evaluation, and raising quality, not merely implementation.
- Parallel agents increase the temptation (and ability) to do more at once, raising coordination and review demands.
- A practical heuristic: when your instinct says “not worth the time,” run an async agent attempt anyway—then decide based on results.

## Synthesis
This essay frames agentic coding as an economic shock to long-held engineering intuition: writing code has historically been expensive, and that fact shaped how developers and organizations plan, estimate, and choose trade-offs. Coding agents dramatically lower the marginal cost of producing lines of code, and parallel agent workflows lower it further by letting one engineer spawn multiple implementation attempts at once.

The author’s main warning is that the falling cost of writing code does not imply the falling cost of shipping good software. In practice, “good code” is a bundle of properties that still require time, judgment, and verification. Good code works; is known to work; solves the right problem; handles unhappy paths predictably; remains simple and maintainable; is protected by tests; is documented in a way that stays synchronized with behavior; and meets the relevant “ilities” such as security, reliability, observability, accessibility, and scalability.

Agents can help generate many of these artifacts—tests, docs, refactors, instrumentation—but they don’t eliminate the need for someone to ensure the artifacts are correct and appropriate. That shifts the developer’s job from producing code to producing confidence: assessing whether the problem is well-defined, whether the solution is minimal, and whether the system remains understandable and evolvable.

At the macro level, this challenges traditional planning. If implementation is no longer the scarce resource, then extensive upfront design and estimation can become miscalibrated. At the micro level, it challenges daily decisions like whether to add tests, refactor, or build debugging tools—because the “time cost” of doing the work has changed, but the downstream costs (maintenance, incidents, regressions, and complexity) have not.

The essay proposes a transitional habit: second-guess the old instincts that were optimized for expensive code writing. If the gut reaction says “don’t build that, it’s not worth an hour,” it may now be worth spending tokens instead—especially if the attempt can run asynchronously while you work on something else. The risk becomes less about wasted typing time and more about managing the review, integration, and quality overhead of the additional code. In that world, teams need explicit practices to keep output aligned with product value and to keep quality costs visible and controlled.