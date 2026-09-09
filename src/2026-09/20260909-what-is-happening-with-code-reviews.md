# What Is Happening with Code Reviews?
**Source**: https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews
**Date**: 2026-09-08
**Author**: The Pragmatic Engineer (Gergely Orosz)
**Keywords**: code review, AI-generated code, PR volume, blast radius triage, AI code review tools, CodeRabbit, uReview, Anthropic, OpenAI, TDD, database schema review, Duckbill Group

## Elevator pitch
As AI agents generate a fivefold increase in pull requests on GitHub since 2023, engineering teams are scrambling to adapt code review — from humans reviewing AI-generated reviews, to triaging by blast radius, to reviewing plans and schemas instead of implementation — but no one-size-fits-all solution has emerged.

## Takeaways
- GitHub PR volume has increased 5x over three years, with nearly half that growth occurring since late 2025 when AI agents began generating most code at many companies
- The most popular approach: AI code review tools (CodeRabbit, GitHub Copilot Code Review, Claude Code Review) generate comments, and humans review the review itself rather than the code
- Anthropic and OpenAI both triage by "blast radius": low-risk changes ship with only AI review, high-risk changes require mandatory human review
- Weaviate's CTO uses a 4-step loop: adversarial agent reviews → human makes scope decision → agent implements feedback → repeat or break, leaving ~90% to agents
- Duckbill Group (5-person startup) dropped most code review: risk-based system with shell-script-enforced labels for API/auth/schema changes, resulting in 94% more PRs merged and median merge time dropping from 26h to 1h for non-human-reviewed PRs
- Some teams review the plan/tests/database schema instead of the implementation — Jackie Luo (Sigil CEO) argues the schema is the "hard" representation of what's been built and reveals the riskiest changes
- Uber built uReview: an agentic pipeline that grades, merges, categorizes, and filters AI-generated code review comments to reduce noise before showing important ones to devs
- There's more talk about dropping human code reviews than evidence of it actually happening — mostly AI startups with additional safety layers

## Synthesis
The Pragmatic Engineer's survey of code review practices in the age of AI-generated code reveals an industry in active transition. The fivefold increase in GitHub PR volume is the stark backdrop: AI agents don't just write code faster, they generate more PRs and larger PRs than humans ever did, and the traditional line-by-line human review model simply cannot scale to match.

The approaches fall into distinct categories, each with different tradeoffs. The most common — humans reviewing AI-generated reviews — preserves human oversight but risks creating a new bottleneck if the AI reviews are noisy. Uber's uReview pipeline, which grades and filters AI comments before showing them to devs, is the most sophisticated attempt to solve the noise problem. The blast-radius triage approach (used by Anthropic and OpenAI) is elegant in its simplicity: it accepts that not all code deserves the same scrutiny and uses risk as the sorting mechanism.

Duckbill Group's results are the most quantitatively striking: switching to risk-based review with improved guardrails (85% test coverage, stricter linting) doubled their PR throughput and cut non-reviewed merge time from 26 hours to 1 hour. The Jackie Luo perspective — that the database schema is what really matters because data (state) is the most rigid part of any system — is compelling for startups but, as the article notes, businesses with existing users need test coverage to guard business logic that customers depend on. The overarching message is clear: no single approach works for everyone, and the teams that figure out their own answer to this question will scale their AI-assisted development effectively.