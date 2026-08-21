# How building software is changing at Anthropic
**Source**: https://newsletter.pragmaticengineer.com/p/inside-anthropic
**Date**: 2026-07-28
**Author**: Gergely Orosz
**Keywords**: Anthropic, AI-native engineering, Claude Managed Agents, Bun, Rust rewrite, code review, AI tooling, software engineering practices

## Elevator pitch
The Pragmatic Engineer visits Anthropic's SF headquarters and finds that AI-generated code, AI-driven code review, and agent-managed workflows are reshaping how one of the world's leading AI labs builds software—offering a preview of what's coming for the rest of the industry.

## Takeaways
- Claude Managed Agents was one of Anthropic's most complex infrastructure projects, taking six months to ship and creating a new primitive at the agent-infra level; infra projects still require mid-flight re-architecture.
- Bun's creator Jarred Sumner (now at Anthropic) rewrote the 500K+ line Bun runtime to Rust in just 11 days using Fable and $165K of tokens—a project that would have taken a small team a year traditionally.
- Inside Anthropic, prototyping is more fluid, but verification is now more time-consuming than implementation; code review and testing are increasingly done by AI.
- Teams work on more projects with a maximum of two engineers per project; design is more ongoing and less upfront; "two-pizza teams" remain the norm even at 3,500+ employees.
- The article previews a follow-up comparing Anthropic and OpenAI's approaches, suggesting the two leading labs have convergent but distinct views on how AI reshapes software engineering.

## Synthesis
Gergely Orosz visited Anthropic's San Francisco headquarters and spoke with four insiders—Katelyn Lesse (head of engineering for Claude Platform), Jarred Sumner (creator of Bun, now at Anthropic), Thariq Shihipar (Claude Code engineering and education), and David Hershey (Applied AI, working with Cursor, Cognition, and Perplexity). The resulting deep dive reveals how one of the world's most AI-forward companies is actually using its own tools to build software.

The most striking finding is the inversion of traditional engineering effort: verification now consumes more time than implementation. When AI agents generate most of the code, the bottleneck shifts from "writing it" to "checking that it's correct." Anthropic has responded by putting AI in charge of code review and testing—creating a loop where AI writes, AI reviews, and humans supervise. The Bun-to-Rust rewrite is a dramatic proof point: 500K+ lines migrated in 11 days with Fable assistance, a task that would have taken a small team a full year under traditional methods.

Claude Managed Agents represents the infrastructure challenge of the new era. It took the Claude Platform team six months to ship, required mid-project re-architecture, and created a new primitive for agent-level coordination. This isn't a side project—it's foundational infrastructure that every other product at Anthropic depends on.

Team structure has also evolved. Despite growing past 3,500 employees, Anthropic maintains small "two-pizza" teams, caps projects at two engineers, and treats design as an ongoing process rather than a phase that precedes implementation. This is a deliberate choice: smaller teams can iterate faster with AI assistance, and the cost of coordination grows faster than the benefit of added headcount when AI handles the bulk of implementation.

The article sets up a follow-up comparing Anthropic and OpenAI, which will be essential reading for anyone tracking how the frontier labs diverge or converge in their engineering practices. For engineering leaders outside the labs, the key takeaway is clear: the practices that work at Anthropic today—AI-assisted code review, small teams, fluid prototyping, heavy verification—are a preview of what will be standard across the industry within 18 months.