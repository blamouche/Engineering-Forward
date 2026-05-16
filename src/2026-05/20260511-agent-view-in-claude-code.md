# Agent View in Claude Code
**Source**: https://claude.com/blog/agent-view-in-claude-code
**Date**: May 11, 2026
**Author**: Anthropic
**Keywords**: Claude Code, agent view, multi-agent, background sessions, developer tools, Anthropic

## Elevator pitch
Anthropic introduces agent view in Claude Code — a unified terminal dashboard to dispatch, monitor, and manage multiple background Claude Code sessions from a single screen, with peek-and-reply built in.

## Takeaways
- Agent view lets developers manage multiple background Claude Code sessions (dispatch, peek, reply, attach) from one terminal without tmux pane shuffling.
- Sessions run under a per-user supervisor process that survives terminal closure and auto-updates, with state persisted to disk for reconnection.
- Background sessions are isolated in automatic git worktrees, preventing parallel sessions from stepping on each other's file changes.
- Entry points include `claude agents` from the shell, left-arrow from inside any session, and `--bg` flag for new background sessions.
- Ships with keyboard shortcuts for power users (Space for peek panel, Ctrl+R rename, Ctrl+T pin) and shell commands (attach, logs, stop, respawn) for scripting.

## Synthesis
Anthropic's agent view, released May 11, 2026 in Claude Code v2.1.139, addresses a growing pain point for developers using AI coding agents at scale: context-switching fatigue. The core insight is that as developers run multiple Claude Code sessions in parallel, the bottleneck shifts from model capability to human attention management.

The feature is a full-terminal dashboard that lists every background Claude Code session across all projects and repositories on the machine, grouped by state (Needs Input, Working, Ready for Review, Completed). Each row shows the session's status, current task, and age. The interaction model is designed for flow: a developer can press ← on an empty prompt to jump from an active session to agent view, dispatch a new task, peek at its progress with Space, send a quick reply, and arrow back — all without leaving the terminal.

The architecture is notably robust. A per-user supervisor process parents all background sessions rather than the shell, so sessions survive terminal closure, shell exit, and even Claude Code auto-updates. File isolation is handled through automatic git worktrees: sessions are blocked from writing to the working directory until Claude transparently moves them into isolated worktrees under `.claude/worktrees/`, ensuring parallel sessions never collide on file edits.

Anthropic also shipped a `/goal` command alongside agent view, allowing Claude to work autonomously across turns until a specified goal is reached — complementing the agent view's background-first paradigm. The distinction between agent view, subagents (workers within one session's context window), and agent teams (coordinating sessions with inter-agent messaging) is clearly drawn: agent view is for managing independent sessions, subagents for delegating within a session, teams for collaborative multi-agent workflows.

For scripting and CI/CD integration, every session gets a short hex ID usable with `claude attach`, `claude logs`, `claude stop`, and `claude respawn` commands. The feature is available across all Claude Code plans (Pro, Max, Team, Enterprise, API) as a Research Preview, signaling Anthropic's expectation of rapid iteration based on user feedback.
