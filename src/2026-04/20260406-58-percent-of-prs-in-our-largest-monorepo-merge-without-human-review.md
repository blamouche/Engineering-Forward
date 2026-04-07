# 58% of PRs in our largest monorepo merge without human review

**Source**: https://vercel.com/blog/58-percent-of-prs-in-our-largest-monorepo-merge-without-human-review
**Date**: April 6, 2026
**Author**: Vercel
**Keywords**: code review, agents, pull requests, monorepo, risk classification, automation

## Elevator pitch
Vercel explains how it built a risk-classified auto-approval workflow where an agent now merges 58% of low-risk pull requests, cutting merge time sharply without increasing reverts or rollbacks.

## Takeaways
- Vercel split PR review into alignment and verification, concluding many mature-codebase changes only need verification.
- An LLM classifier labels PRs as HIGH or LOW risk using evidence grounded in the diff.
- LOW-risk PRs can satisfy branch protection automatically; HIGH-risk changes still require human review.
- In the rollout, skipped-review PRs showed no measurable safety regression while merge times dropped substantially.
- The biggest gain was reallocating human attention toward risky changes rather than eliminating review altogether.

## Synthesis
This is one of the clearest production case studies so far on where code review automation actually makes sense. Vercel did not argue that human review is obsolete. It argued that mandatory human review for every change had already become procedural theater in a mature monorepo, especially for CSS tweaks, docs edits, tests, and other low-blast-radius work.

The important design choice is the risk framework. Instead of asking an agent to judge code quality in some broad, fuzzy way, Vercel constrains the task to routing: is this PR structurally high risk or low risk? That is a much better fit for automation. The system stays conservative, hard-codes path-based escapes, and fails open to human review when uncertain.

What stands out is the organizational effect. Faster merges matter, but the more strategic result is that reviewers get to the dangerous PRs sooner. Review capacity was not destroyed; it was reallocated. That is likely the pattern other teams will copy: agents handling verification-heavy work so humans can spend attention on architecture, security, and edge cases.

The compliance and adversarial-hardening sections are also unusually strong. They show the system was treated as a change-management component, not just a productivity hack. Overall, this is a strong example of using agents to narrow operational bottlenecks without pretending that all judgment can be automated.
