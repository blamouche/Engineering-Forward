# Build agents that run automatically
**Source**: https://cursor.com/blog/automations
**Date**: March 08, 2026
**Author**: Unknown
**Keywords**: Cursor, automations, agents, DevOps, workflow

## Elevator pitch
Cursor introduces Automations—scheduled or event‑driven cloud agents that run in sandboxes, integrate with tools via MCPs, and automate review, monitoring, and operational chores across the software lifecycle.

## Takeaways
- Automations can be triggered by schedules, webhooks, or events like PRs, Slack messages, or incidents.
- Each automation runs a cloud agent in a sandbox with configured tools and self‑verification.
- Cursor uses automations for security review, risk‑based codeowners, and incident response.
- Chore automations handle weekly change summaries, test coverage checks, and bug triage.
- Customers like Rippling use automations to consolidate updates and generate dashboards.

## Synthesis
Cursor’s announcement positions Automations as the next step in agentic software development: always‑on agents that execute tasks in response to schedules or events. Instead of invoking an assistant manually, teams can wire agents into their workflow so that they run when a PR is opened, a Slack message is posted, a PagerDuty incident fires, or a webhook arrives. The system supports built‑in integrations and custom events, allowing agents to operate across the tools that already govern engineering work.

The post describes how each automation spins up a cloud sandbox, follows user‑defined instructions, and leverages configured MCPs and models to complete work. It also highlights a memory tool that allows agents to learn from past runs and improve, implying that automations can become more reliable over time. The core value proposition is scale: as coding agents increase the volume of code shipped, the bottlenecks move to review, monitoring, and maintenance. Automations are presented as the mechanism to scale those downstream processes.

Cursor’s own examples emphasize review and monitoring. A security review automation runs on every push to main, auditing diffs for vulnerabilities and posting high‑risk findings to Slack. An “agentic codeowners” automation classifies PR risk and either auto‑approves low‑risk changes or assigns reviewers based on contribution history, with decisions logged for audit. An incident response automation triggered by PagerDuty uses monitoring data to analyze logs, reviews recent code changes, and produces a proposed fix in a PR, shortening on‑call response times.

The article also stresses “chores”—routine tasks that are easy to automate but consume time. A weekly digest automation summarizes meaningful changes, highlighting bug fixes, technical debt, and security updates. Another automation checks for missing test coverage in newly merged code, adds tests following established conventions, and runs relevant test targets before opening a PR. Bug report triage automations parse Slack reports, deduplicate, create Linear issues, and attempt fixes, replying with a summary in the original thread.

Customer examples reinforce the broad applicability. At Rippling, a personal assistant automation aggregates meeting notes, action items, and links from Slack, then cross‑references GitHub PRs, Jira issues, and mentions to produce a consolidated dashboard every two hours. Other automations handle incident triage, weekly status reports, and on‑call handoffs. The narrative is that automations are not just about code quality but also about operational coordination and knowledge management.

The announcement frames automations as part of a “software factory” vision where agent fleets continuously monitor and improve a codebase. Under this model, agents don’t just generate code; they enforce standards, manage risk, and carry out routine maintenance. Cursor positions its automation system as the infrastructure layer for that factory—configurable, tool‑integrated, and designed for continuous operation. The implied strategic shift is from one‑off agent usage to persistent, workflow‑integrated agents that materially change how engineering teams scale.
