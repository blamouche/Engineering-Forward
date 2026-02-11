# OpenSpec — A lightweight spec‑driven framework
**Source**: https://openspec.dev/
**Date**: Unknown
**Author**: Unknown
**Keywords**: specifications, requirements, testing, review, diff, SDLC

## Elevator pitch
OpenSpec proposes treating product changes as *spec deltas*—diffs in requirements and scenarios—so reviewers can understand what behavior is changing without spelunking through implementation details.

## Takeaways
- Every change produces a “spec delta” that captures requirement edits as a diff.
- Focus is on readable requirement/scenario language (“SHALL”, “GIVEN/WHEN/THEN”).
- The diff format is designed for review ergonomics: understand behavior changes quickly.
- Helps align dev + review on intent before debating implementation.
- Fits naturally with AI-assisted coding where code volume grows faster than human review bandwidth.

## Synthesis
OpenSpec is small in surface area but it’s aiming at a real pain point: code review is often the wrong layer for understanding product behavior changes. When requirements are implicit, reviewers must infer intent from code, which is slow, error-prone, and increasingly untenable as AI increases the volume of changes and the speed at which they can be produced.

The “spec delta” idea is essentially shifting review from *implementation diffs* to *behavior diffs*. If a PR can present, alongside code, a clear before/after diff of requirements and scenarios, the team can debate the right thing: what the system should do. It’s also more accessible to non-specialists (PMs, QA, security) who care about behavior but don’t want to read code.

The example on the homepage—session expiration rules—illustrates the point: it’s immediately obvious what changed (configurable expiration, remember-me scenario) without needing to inspect auth middleware.

This approach pairs well with agentic workflows. If agents generate code, humans need higher-level artifacts to validate correctness. A disciplined spec delta can become the contract agents implement, and later the artifact used for regression testing and audits. In a “write-only code” future, spec diffs and scenario suites may become the primary source of trust.
