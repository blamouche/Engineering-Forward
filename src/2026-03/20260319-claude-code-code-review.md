# Claude Code: Code Review
**Source**: https://code.claude.com/docs/en/code-review
**Date**: Unknown
**Author**: Anthropic
**Keywords**: Claude Code, code review, PR review, GitHub, AI debugging, security vulnerabilities, multi-agent

## Elevator pitch
Claude Code's Code Review feature uses a fleet of specialized agents to analyze GitHub pull requests in the context of your full codebase, posting inline findings on logic errors, security vulnerabilities, and regressions without blocking existing workflows.

## Takeaways
- Multi-agent parallel analysis: A fleet of specialized agents examines code changes from different angles, then a verification step filters false positives before ranking by severity.
- Non-blocking workflow integration: Findings are tagged with severity levels (Normal, Nit, Pre-existing) and posted as inline comments without approving or blocking PRs.
- Flexible trigger modes: Reviews can run once after PR creation, after every push, or manually via `@claude review` comment, depending on repository needs.
- Customizable via CLAUDE.md and REVIEW.md: Teams can define what Claude flags or skips using repository-level guidance files without changing core configuration.
- Usage-based pricing at scale: Averaging $15-25 per review, costs scale with PR size and complexity; a monthly spend cap can be configured per organization.

## Synthesis
Claude Code's Code Review represents a production-grade implementation of AI-assisted code quality at the pull request stage. Rather than providing generic feedback, it employs multiple specialized agents analyzing the diff alongside the full codebase context—a meaningful technical distinction from simpler single-pass code analysis tools.

The architecture addresses the core challenge of AI code review: false positives. After specialized agents identify candidate issues, a dedicated verification step checks findings against actual code behavior before surfacing them. This multi-stage approach reflects hard lessons learned from earlier AI review tools that overwhelmed developers with noise.

The severity taxonomy is deliberately simple: Normal (bugs to fix before merge), Nit (minor, non-blocking), and Pre-existing (existing bugs not introduced by the current PR). The Pre-existing category is particularly thoughtful—surfacing existing issues creates awareness without blocking PRs for problems outside the current change's scope.

Customization through CLAUDE.md and REVIEW.md files enables teams to encode institutional knowledge without complex configuration. A REVIEW.md can specify "always check for integration tests on new API routes" or "skip generated files under /gen/"—turning tribal knowledge into automated enforcement. The hierarchical CLAUDE.md support allows different standards for different subdirectories within the same repository.

The pricing model ($15-25 average per review) positions this as a premium tool appropriate for enterprise teams where the cost of a missed vulnerability or regression far exceeds the review cost. The "after every push" trigger can multiply costs significantly for active PRs—teams need to weigh thoroughness against budget.

The manual trigger mode (`@claude review`) offers a pragmatic middle ground for high-traffic repositories: reviews happen only when explicitly requested, but subsequent pushes to the opted-in PR automatically trigger further reviews. This balances cost control with the benefit of catching issues as PRs evolve.

Overall, Claude Code's Code Review demonstrates how specialized AI tooling for software development is maturing beyond the "better autocomplete" category into serious workflow integration that works with existing processes rather than demanding their replacement.
