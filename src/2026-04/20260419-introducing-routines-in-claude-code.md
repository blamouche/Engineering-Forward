# Introducing routines in Claude Code

**Source**: https://claude.com/blog/introducing-routines-in-claude-code
**Date**: April 19, 2026
**Author**: Unknown
**Keywords**: claude, introducing, routines, code

## Elevator pitch
Define repeatable routines that work your backlog, review your PRs, and respond to events in the cloud

## Takeaways
- Introducing routines in Claude Code Define repeatable routines that work your backlog, review your PRs, and respond to events in the cloud.
- Category Product announcements Product Claude Code Date April 14, 2026 Reading time 5 min Share Copy link https://claude.com/blog/introducing-routines-in-claude-code Today, we're introducing routines in Claude Code in research preview.
- A routine is a Claude Code automation you configure once — including a prompt, repo, and connectors — and then run on a schedule, from an API call, or in response to an event.
- Routines run on Claude Code’s web infrastructure , so nothing depends on your laptop being open.
- Developers already use Claude Code to automate the software development cycle, but until now, they've managed cron jobs, infrastructure, and additional tooling like MCP servers themselves.

## Synthesis
Introducing routines in Claude Code Define repeatable routines that work your backlog, review your PRs, and respond to events in the cloud. Category Product announcements Product Claude Code Date April 14, 2026 Reading time 5 min Share Copy link https://claude.com/blog/introducing-routines-in-claude-code Today, we're introducing routines in Claude Code in research preview. A routine is a Claude Code automation you configure once — including a prompt, repo, and connectors — and then run on a schedule, from an API call, or in response to an event. Routines run on Claude Code’s web infrastructure , so nothing depends on your laptop being open. Developers already use Claude Code to automate the software development cycle, but until now, they've managed cron jobs, infrastructure, and additional tooling like MCP servers themselves. Routines ship with access to your repos and your connectors , so you can package up automations and set them to run on a schedule or trigger. How it works Scheduled routines Give Claude Code a prompt and a cadence (hourly, nightly, or weekly) and it runs on that schedule: Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR. If you're using /schedule in the CLI, those tasks are now scheduled routines. API routines You can also configure routines to be triggered by API calls. Every routine gets its own endpoint and auth token.
