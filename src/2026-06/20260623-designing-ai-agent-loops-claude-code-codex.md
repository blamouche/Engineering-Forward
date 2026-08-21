# Designing AI Agent Loops in Claude Code and Codex
**Source**: https://www.chatprd.ai/how-i-ai/how-i-ai-designing-ai-agent-loops-in-claude-code-and-codex
**Date**: 2026-06-17
**Author**: Claire Vo
**Keywords**: agent loops, Claude Code, Codex, goal loops, heartbeat, cron, hook, subagents, automation

## Elevator pitch
AI agent loops—scheduled or goal-driven systems that keep prompting themselves until a job is done—are the next evolution from manual prompting, and this hands-on guide builds two real automations: a daily PR-review loop and a weekly skill-discovery loop with delegated subagents.

## Takeaways
- A loop is just a prompt that fires itself; the four trigger patterns are Heartbeat (recurring check), Cron (scheduled time), Hook (event-driven), and Goal (runs until a stated outcome is validated).
- Design loops like onboarding an employee: define the job, tools, permissions, workspace, reusable skills, state tracking, and sometimes subagents—prompts become operating procedures, not one-off requests.
- The PR-review loop in Claude Code inspects stale PRs older than 12 hours, babysits merge checks autonomously via delegated threads, and escalates to Slack only when human attention is needed.
- The skills-discovery loop in Codex scans recent PRs every Friday, identifies missing engineering skills, then spawns validation subagents that run goal loops against the base branch to confirm each proposed skill actually works.
- Goal-based loops are the most powerful but most dangerous pattern—fuzzy success criteria cause agents to loop forever burning tokens, so precise validation rules and runtime monitoring are essential design constraints.

## Synthesis
Claire Vo's episode of "How I AI" demystifies the emerging concept of "loop engineering" by showing that a loop is simply a prompt that re-triggers itself based on a schedule, event, or goal condition. The terminology sounds exotic but maps directly to existing automation primitives: heartbeats (polling), crons (scheduled jobs), hooks (webhooks), and goals (convergence loops). What's new is pointing these at AI agents instead of batch jobs.

The first demo builds a daily PR-review routine in Claude Code. The routine checks for open PRs older than 12 hours, evaluates merge-readiness, and either babysits the PR through automated checks via a delegated thread or sends a Slack summary to the product team. The key operational lesson is that loops depend on their surrounding environment—connectors must be configured, permissions granted, and the machine must be awake at the scheduled time.

The second demo is more ambitious: a weekly Codex automation that scans recent engineering activity to discover missing agent skills. This loop doesn't just identify gaps—it spawns validation subagents that each run their own goal loop to confirm a proposed skill produces high-quality output against the base branch. The system becomes a manager supervising other agents, creating a layered orchestration pattern.

The author is candid about costs and limitations. Goal-based loops can burn through tokens rapidly, especially when they fan out into multiple delegated threads. Monitoring runtime, cost, and concurrency limits is part of workflow design, not an afterthought. The prompts shown are rough working versions, not production-grade systems. Goal loops require precise success criteria; without them, agents either loop indefinitely or approve low-quality work.

The strongest practical takeaway is that loops work best for tasks that are repetitive, inspectable, and easy to validate. PR triage, test monitoring, and skill discovery are good candidates because inputs and outputs are clear. Human judgment remains essential for evaluation—agents reduce repetitive supervision but don't eliminate the need for supervision entirely.