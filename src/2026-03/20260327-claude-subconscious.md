# Claude Subconscious
**Source**: https://github.com/letta-ai/claude-subconscious
**Date**: Unknown
**Author**: Letta AI
**Keywords**: Claude Code, memory, agents, plugins, tooling

## Elevator pitch
Claude Subconscious is a Letta‑powered background agent that watches Claude Code sessions, builds persistent memory, and injects contextual “whispers” before each prompt.

## Takeaways
- Runs as a plugin that pairs Claude Code with a persistent Letta agent.
- Watches transcripts and reads files to build memory across sessions and projects.
- Injects guidance via stdout (whisper/full/off modes) without editing CLAUDE.md.
- Supports read‑only or full tool access for the background agent.
- Includes hooks for session start, prompt submit, pre‑tool use, and stop.

## Synthesis
Claude Subconscious is an experimental plugin from Letta AI that adds a persistent, background “sub‑agent” to Claude Code. While Claude Code itself resets context between sessions, Subconscious maintains long‑term memory by ingesting transcripts, scanning project files, and tracking preferences. It then injects guidance back into Claude’s context before each prompt, effectively acting as a continuous memory layer and advisor.

The system runs through a set of hooks: on session start it initializes conversation state; before each user prompt it syncs memory and “whispers” messages; before tool use it can inject updates; and on session stop it asynchronously processes the transcript. Everything is injected via stdout—nothing is written to CLAUDE.md—so the guidance is dynamic and non‑intrusive. Modes allow lightweight message‑only hints (whisper), full memory block injection, or complete disablement.

A key feature is tool access. By default the background agent can read files, grep, glob, and search the web, allowing it to build project context while Claude Code is working. Users can toggle to full autonomy or disable tools entirely. Memory is organized into structured blocks (preferences, project context, pending items, etc.) shared across projects, with the option to separate agents per repo.

In short, Claude Subconscious aims to close the continuity gap in Claude Code by adding a persistent observer with its own memory system and tool access. The design reflects a broader trend: pairing fast, interactive coding agents with slower, context‑building background agents to improve consistency and reduce repeated onboarding.
