# No Figma. No Jira. No Docs. How Gusto Built a New Product Line with Claude Code
**Source**: https://www.chatprd.ai/how-i-ai/how-gusto-built-a-new-product-line-in-10-weeks-with-claude-code-no-jira-and-no-docs
**Date**: 2026-06-29
**Author**: Claire Vo / Eddie Kim
**Keywords**: Claude Code, Gusto, AI agents, startup engineering, no-process development

## Elevator pitch
Gusto's CTO led a five-person team that shipped a tier-one product in 10 weeks by discarding all standard process and relying on Claude Code and a permanent Zoom room as the entire coordination layer.

## Takeaways
- A five-person team with no PM, no Jira, no Figma, no written specs, and no standups shipped a production AI product in 10 weeks, proving that when AI handles the engineering, coordination overhead becomes optional.
- The "trash can method" replaces written proposals with working code: engineers build features as PRs, and the team simply deletes what they don't need, making the PR itself the proposal.
- The technical stack for a production AI agent is shockingly minimal: Cloudflare Workers + Vercel AI SDK, with no proprietary orchestration framework—everything else built in-house.
- Designer Katie Chen shipped feature-flagged interfaces with canned responses that engineers replaced with real behavior, ranking in the 94th percentile for code throughput across Gusto's entire R&D organization.
- An eval-first TDD workflow for AI behavior—reproduce the failure with a test, make the smallest change, rerun the eval, then let a human approve the merge—provides the same rigor for prompts that TDD provides for code.

## Synthesis
This episode of "How I AI" with Gusto CTO Eddie Kim is a case study in what happens when a senior, empowered team treats AI as a primary contributor rather than a tool grafted onto existing processes. The product, Gusto Co-founder, is a conversational agent that automates the tedious "work before the work" of payroll preparation—exporting appointment data, calculating commissions, pooling tips—for small business owners who run their companies from phones.

The origin story is telling: Eddie prototyped the idea during a five-hour London layover, using Claude Code to build a working demo before he landed. That prototype was eventually discarded in favor of a TypeScript + Cloudflare Worker architecture, embodying the "trash can method" where code is cheap enough to throw away. PRs become proposals; the team reviews and either merges or closes on the spot.

The coordination mechanism is deliberately minimal. A persistent Zoom room replaced all scheduled meetings, standups, retros, and Slack threads. Claude Code running in a permanent loop carries shared context, making it functionally equivalent to a senior engineer who never sleeps. The team's single whiteboard photo was the only durable planning artifact across the entire 10-week build.

The agent architecture itself is refreshingly simple: an AI SDK running in the cloud with tool access. Eddie's definition is pointed: "An agent is an AI SDK running somewhere in the cloud, able to look up files and call tools. That's the full definition." No proprietary orchestration, no third-party framework. The simplicity extends to their bug-fixing workflow: Claude Code reads GitHub issues, writes failing evaluations, proposes fixes, reruns evals, and only opens a PR after Eddie approves.

The constraints are acknowledged. This was a team of five senior, highly engaged people explicitly given permission to break rules, and the 10-week sprint required nights and weekends. The lesson isn't "use Claude Code" but "design your process for AI as a team member." Most organizations graft AI onto human-scaled workflows—standups, tickets, three-person PR reviews. Eddie's team treated AI as a primary contributor and built coordination around that assumption, creating a workflow that gets faster as AI improves rather than one that merely offloads tasks to it.