# The Ultimate Guide to /goal

**Source:** [Unwind AI](https://www.theunwindai.com/p/the-ultimate-guide-to-goal/)
**Date:** 2026-05-17
**Author:** Shubham Saboo

## Summary

A comprehensive guide to `/goal`, a new primitive for coding agents that's converging across tools (Codex CLI, Claude Code, Hermes Agent). `/goal` shifts from prompting (you driving each turn) to assigning (agent works toward a defined "done" state until it completes).

## Key Takeaways

- **/goal defines "done"**: you write what success looks like, submit once, and the agent works until it meets those criteria
- **Three-role pattern**: Orchestrator (Hermes) → Builder (Codex) → Reviewer (Claude Code) → verification loop
- **Verification is critical**: don't trust agent self-reports; the orchestrator independently runs tests, builds, and checks git state
- **Kanban board for agents**: every goal is a card with PID, repo, done criteria; handoffs leave a trail
- **Parallel goals work across boundaries**: different repos, worktrees, or packages — never multiple writers on the same file
- **The primitive matters more than the tools**: any new coding tool adopting `/goal` can join the pipeline

## Key Quote

> "/goal is not a feature. It is a primitive. HTTP is a primitive. JSON is a primitive. /goal is becoming one for coding agents."

## Tags

AI agents, coding agents, Codex, Claude Code, Hermes, goal, orchestrator, multi-agent

---

*Generated from: https://www.theunwindai.com/p/the-ultimate-guide-to-goal/*
