# What is "Loop Engineering"?
**Source**: https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering
**Date**: 2026-07-14
**Author**: Gergely Orosz (The Pragmatic Engineer)
**Keywords**: loop engineering, agentic loops, ralph loop, /goal command, AI coding, context engineering, agent harnesses

## Elevator pitch
Loop engineering is the practice of designing persistent, goal-driven AI agent loops rather than writing individual prompts, but it may be more evolutionary than revolutionary — overlapping heavily with triggers, cron jobs, and existing automation patterns.

## Takeaways
- Loop engineering originated from Geoffrey Huntley's "Ralph Wiggum" technique: a simple Bash loop (`while :; do cat PROMPT.md | claude-code ; done`) that restarts agents with fresh context, persisting progress via filesystem artifacts.
- By May 2026, all major AI coding harnesses (Codex, Hermes, Claude Code) shipped `/goal` commands that compress the Ralph loop into a single instruction — the agent keeps working until a completion condition is satisfied.
- Most developer "loop engineering" use cases are triggers (event-driven) and cron jobs (scheduled), which are fundamentally the same as pre-AI automation patterns, just with AI agents as the execution layer.
- Practical helpful loops include: auto-creating PRs for Sentry issues, babysitting flaky tests, triaging outages, and running long migrations autonomously via cron skills.
- Several developers report disappointment with loops due to agent drift, cost at API token prices ("tokenmaxxing"), and better results with human-in-the-loop approaches. Some argue loops may be a temporary hack while harnesses catch up to support goal-oriented prompting natively.

## Synthesis
The concept of "loop engineering" has become one of the most discussed ideas in the AI coding world in mid-2026, championed by prominent figures like Boris Cherny (Claude Code creator) and Peter Steinberger (OpenClaw creator), who both declared they no longer write prompts but instead design loops. But what does this actually mean in practice?

The origin traces to Geoffrey Huntley's "Ralph Wiggum" technique from mid-2025, which was a simple Bash loop that repeatedly prompted Claude Code with a goal document, restarting with fresh context each iteration. The key insight was that context window limitations (then ~200K tokens) made it necessary to break ambitious tasks into smaller, sequential agent runs with compressed state persisted to the filesystem. This approach went viral in December 2025 as better models became capable of handling multi-step projects.

The landscape shifted in April-May 2026 when Codex, Hermes, and Claude Code all shipped `/goal` commands within weeks of each other. These compress the Ralph loop pattern into a single command: you state a completion condition, and the agent keeps working across turns until it's satisfied. Codex's implementation uses files, logs, test runs, and lifecycle controls — essentially building infrastructure around the Ralph loop concept. Hermes explicitly credited Codex's `/goal` as inspiration. Claude Code added both `/goal` and `/loop` (scheduled agent runs).

However, when the Pragmatic Engineer surveyed ~210 developers about their loop engineering practices, most use cases fell into familiar categories: triggers (event-driven agent execution) and cron jobs (scheduled agent execution). These are automation patterns that predate LLMs by decades. The AI agent simply replaces the execution layer of what was previously a Zapier workflow, a cron script, or a webhook handler.

More substantive use cases do exist: auto-creating PRs for Sentry issues, babysitting nightly e2e test runs, building new telemetry integrations with iterative verification, and running long-running migrations via cron-triggered skills. These are genuinely new workflows where the AI's judgment and flexibility add value beyond simple automation.

The article also surfaces important pushback: some developers report that loops are expensive (especially at API pricing), that agents drift off-task, and that human-in-the-loop approaches still produce better results. Distinguished engineer Max Kanat-Alexander suggests loops may be a temporary hack — once harnesses support goal-oriented prompting natively, the explicit loop construct may become unnecessary. The broader insight is that "context engineering" (understanding how context windows work) may matter more for most developers than loop engineering specifically, except for those building AI infrastructure.