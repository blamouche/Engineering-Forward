# Running an AI-Native Engineering Org
**Source**: https://claude.com/blog/running-an-ai-native-engineering-org
**Date**: 2026-06-03
**Author**: Fiona Fung (Anthropic)
**Keywords**: ai-native, engineering-org, claude-code, agile, code-review, just-in-time-planning, team-structure, dogfooding

## Elevator pitch
Anthropic's Director of Engineering for Claude Code details how the team rewrote planning, code review, context gathering, and team composition processes when agentic coding became the default — replacing six-month roadmaps with just-in-time planning, shifting code review to expertise-only, and blurring traditional engineering roles.

## Takeaways
- Writing code, tests, and refactoring rarely slows the Claude Code team down anymore — the bottlenecks moved to verification, code review, and security
- Planning shifted from six-month roadmaps to "just-in-time" (JIT) planning: prototype first, get internal users on it, act on feedback, skip heavy design docs
- Context gathering changed from "ask the author" to "ask Claude": since all PRs are Claude-assisted, "who made this change?" is no longer sufficient — go deeper into what you actually need to know
- Code review now focuses on human expertise only: legal review, trust boundaries, security-sensitive code, product sense — Claude handles style, linting, bug-catching, and test generation
- Team roles are blurring: PMs code with Claude, engineers take on design and content work; hiring indexes on creative builders with product sense and deep systems expertise rather than raw throughput
- Every commit is Claude-assisted by default; onboarding ramp time and PR cycle time are the key metrics to track

## Synthesis
At Code w/ Claude SF 2026, Fiona Fung, Director of Engineering for Claude Code and Claude Cowork, walked through how the team's processes and structure changed once agentic coding became the default way of working. The presentation offers one of the most detailed first-person accounts of operating an AI-native engineering organization from inside a frontier AI lab.

The core observation is that engineering bandwidth was historically the expensive part of building applications — every process from waterfall to agile was built around that cost. On the Claude Code team, writing code, writing tests, and refactoring rarely slow things down anymore. But the bottlenecks didn't disappear; they moved to verification, code review, and security.

Planning underwent the most visible transformation. The old norm was extensive pre-planning because coding time was expensive. A six-month roadmap was written, but Claude Code changed things so fast it was outdated by month three. The new approach is just-in-time (JIT) planning, analogous to JIT compiling: do the right amount of planning at the right time. Planning shifted from design docs to discussions in PRs or prototypes. The team prototypes, gets internal users on it, and acts on feedback rather than conducting formal product reviews.

Context gathering flipped from asking the code author to asking Claude. When all PRs are Claude-assisted, "who made this change?" is no longer the right question. The new norm is to identify what you actually need to know — whether you're looking for the cause of a regression, an expert to answer a customer question, or context on a decision — and ask Claude directly. The team's process is to also ask "is there a way to automate this?" for every recurring question.

Code review evolved to trust-but-verify. Claude handles all style, linting, PR feedback, bug-catching, and test generation. Human review is reserved for where it matters: legal review for risk tolerance, domain experts for trust boundaries and security-sensitive code, and PMs/designers for product sense and taste. Team composition shifted to index on two profiles: creative builders with product sense, and engineers with deep systems expertise. Raw throughput is de-prioritized because the models handle that.

Three non-negotiable team principles govern the transition: relentlessly dogfood your product, keep the team as flat as possible (managers start as ICs), and don't hesitate to kill processes that no longer work. Key metrics to track: onboarding ramp time (should decrease), PR cycle time (should decrease), and Claude-assisted commit percentage (should increase). Fung warns against confusing throughput with success — the real metric is whether you're solving the problem you set out to solve.