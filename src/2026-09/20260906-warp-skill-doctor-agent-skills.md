# Warp Skill Doctor: Score and Improve Your Agent Skills From Past Sessions
**Source**: https://warp.dev/skill-doctor
**Date**: 2026-08-31
**Author**: Warp
**Keywords**: Warp, Skill Doctor, agent skills, self-improving agents, Claude Code, Codex, code review, agent evaluation, skill improvement

## Elevator pitch
Warp's Skill Doctor reads past agent conversation transcripts from Claude Code, Codex, and Warp, scores them against rubrics for efficiency and code quality, then proposes merge-ready diffs to your skill files — turning session feedback into actionable skill improvements.

## Takeaways
- Skill Doctor supports transcripts from Claude Code, Codex, and Warp, making it tool-agnostic for developers using any of the major coding agents
- The tool runs a three-step loop: aggregate past transcripts, score them against tested rubrics (efficiency, code quality, skill coverage), and propose concrete improvements to skill files
- It's the productized version of the self-improvement system behind Warp Factories, which runs the same loop automatically across an entire team's agent conversations
- Warp Factories extends the concept to team scale: configurable scoring metrics, benchmarking against real tasks from team repositories, and dashboards tracking velocity, cost-per-PR, and quality scores
- A Series C infrastructure company reports that Warp Factories drove their cost per agent PR down by 30%, suggesting the self-improvement loop delivers measurable economic impact

## Synthesis
Warp's Skill Doctor productizes a pattern that has emerged organically in the agentic coding ecosystem: the idea that agent skill files should be treated as living artifacts that improve from real usage data rather than static prompts written once and forgotten. The tool reads past conversation transcripts from Claude Code, Codex, and Warp — the three most widely used agentic coding environments — and applies a structured three-step loop to turn session history into skill improvements.

The loop is straightforward in concept but powerful in practice. First, Skill Doctor aggregates past transcripts from the developer's agent sessions. Second, subagents score these conversations against tested rubrics covering efficiency, code quality, and skill coverage — metrics that go beyond simple "did the task get done" to evaluate how well the agent performed. Third, the tool reviews these scores and proposes concrete, merge-ready diffs to the developer's skill files. The output is not a vague suggestion but an actual code change that can flow through normal review workflows.

Warp Factories extends this from individual developer use to team scale. It runs the self-improvement loop automatically across an entire team's agent conversations, with configurable scoring metrics that teams can tailor to their priorities — test coverage, verbosity, task compliance, and more. It also benchmarks agent setups against real tasks from the team's repositories and provides dashboards tracking velocity, cost-per-PR, and quality scores. The reported 30% reduction in cost per agent PR at a Series C infrastructure company suggests the compounding effect of continuous skill improvement delivers tangible economic returns.

The broader significance is that Skill Doctor represents a shift from "write a better prompt" to "learn from the mess your agent already made." Instead of trying to anticipate every failure mode when authoring a skill, developers can ship a reasonable first version and let the tool identify weaknesses from actual sessions. This is the same philosophy that Warp applies internally — their code review, spec-writing, and triage agents each carry their own self-improvement loop, with human feedback captured where work happens and an observer agent proposing skill edits on a schedule.