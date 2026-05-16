# Agent View in Claude Code
**Source**: https://claude.com/blog/agent-view-in-claude-code
**Date**: May 11, 2026
**Author**: Anthropic
**Keywords**: Claude Code, agent view, multi-agent, dashboard, background sessions, developer tools, AI coding

## Elevator pitch
Anthropic introduces Agent View in Claude Code, a terminal dashboard that lets developers dispatch, monitor, and manage multiple parallel AI coding sessions from one screen, eliminating tmux-based context switching.

## Takeaways
- Agent View is a full-terminal dashboard listing every background Claude Code session, grouped by state (Needs input, Working, Ready for review, Completed) with real-time status indicators.
- Sessions can be dispatched from the shell (claude --bg), from inside a session (/background), or directly from Agent View, with each session running independently in its own isolated git worktree.
- The peek-and-reply system lets developers check on a session's progress without leaving the dashboard — press Space to see recent output and type a reply to unblock it.
- Agent View is part of a three-tier multi-agent architecture: subagents (workers within one session), agent teams (coordinating sessions), and Agent View (independent parallel sessions supervised by the developer).
- Sessions survive terminal closure because they're parented to a per-user supervisor process, not the shell — they auto-restart after Claude Code updates and persist state on disk.

## Synthesis
Anthropic launched Agent View in Claude Code on May 11, 2026, addressing a pain point familiar to heavy users: managing multiple concurrent AI coding sessions without drowning in tmux panes and mental context-switching overhead. The feature is a Research Preview available to Pro, Max, Team, Enterprise, and API plan users running Claude Code v2.1.139 or later.

Agent View presents a full-terminal dashboard where every background Claude Code session appears as a row, regardless of which project or repository it belongs to. Sessions are grouped by state: "Needs input" (blocked on permission or questions) sits at the top, followed by "Working," "Ready for review" (sessions with open PRs), and "Completed." Each row shows a one-line AI-generated summary of current activity, refreshed every 15 seconds during active work.

The entry points are designed for minimal friction. From the shell: `claude agents`. From inside any session: press the left arrow key on an empty prompt. This second path is where the feature's workflow value crystallizes — a developer mid-implementation can arrow out, dispatch an unrelated investigation, peek at its progress, and arrow back, all within seconds and without leaving the terminal.

The underlying architecture is a per-user supervisor process that parents all background sessions independently of the shell. This means sessions survive terminal closure, shell exit, and even Claude Code auto-updates. When a session finishes and sits unattached for about an hour, the supervisor stops its process to free RAM, preserving state on disk for transparent restart on next access.

File isolation is handled through automatic git worktrees. Every background session starts in the working directory but is blocked from writing to it. When file edits are needed, Claude moves the session into an isolated worktree under `.claude/worktrees/`, allowing parallel sessions to read the same checkout while writing to their own copies. Worktrees are deleted with the session, so developers must merge or push before deletion.

The launch positions Agent View within a three-tier multi-agent architecture. Subagents are workers inside a single session that return summaries to the parent agent. Agent teams are coordinated sessions that message each other and share task lists (experimental, off by default). Agent View is for fully independent parallel sessions supervised directly by the developer — no inter-agent communication, no shared state, with PRs as deliverables.

Practical workflows include the "PR shotgun" (dispatching five small bug fixes in parallel and reviewing five PRs 20 minutes later), long-running /loop watchers (periodic evaluation runs), and instant cross-repo investigations without context-switching tax. The feature acknowledges real constraints: each session burns quota independently, sessions stop when the laptop sleeps, and organizations can disable it entirely. But for developers already running multiple Claude Code sessions, it transforms the experience from managing infrastructure to managing work.
