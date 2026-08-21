# Xiaomi MiMo Code: Open-Source Agentic Coding Harness Beats Claude Code at Ultra-Long Tasks
**Source**: https://venturebeat.com/technology/xiaomis-new-open-source-agentic-ai-coding-harness-mimo-code-beats-claude-code-at-ultra-long-200-step-tasks
**Date**: June 11, 2026
**Author**: Carl Franzen
**Keywords**: Xiaomi, MiMo Code, open source, agentic coding, Claude Code, cross-session memory, checkpoint-writer subagent, SQLite FTS5, long-horizon tasks

## Elevator pitch
Xiaomi's open-source MiMo Code terminal coding assistant outperforms Claude Code on long-horizon, 200+ step tasks by deploying an independent checkpoint-writer subagent that maintains persistent memory across sessions, solving the context degradation problem that plagues AI coding agents.

## Takeaways
- MiMo Code V0.1.0 is a terminal-native AI coding assistant from Xiaomi, open-sourced under an MIT license on GitHub.
- It outperforms Claude Code on key agentic coding benchmarks, particularly on ultra-long, multi-step tasks of 200+ steps, according to Xiaomi's internal beta and survey of 576 developers.
- The key innovation is a cross-session memory system powered by SQLite FTS5 full-text search, spanning four layers: project memory, session checkpoints, scratch notes, and per-task progress logs.
- Rather than forcing the primary agent to pause and take notes, the system deploys an independent checkpoint-writer subagent — like a dedicated architect updating blueprints while the main agent builds.
- The release bundles limited-time free access to MiMo-V2.5, Xiaomi's multimodal flagship with a million-token context window, requiring no registration.

## Synthesis
VentureBeat reports on Xiaomi's MiMo AI team open-sourcing MiMo Code V0.1.0, a terminal-native AI coding assistant that the company claims outperforms Anthropic's Claude Code on key agentic coding benchmarks — especially on long-horizon, multi-step tasks exceeding 200 steps. The claims are based on Xiaomi's internal beta release and a survey of 576 developers. The tool is available on GitHub under an MIT license and installs with a single terminal command on macOS and Linux, or via npm on Windows. The project is a fork of the open-source OpenCode agent, which Xiaomi has extended with its own memory architecture, workflow modes, and model harness.

The article identifies the core problem MiMo Code addresses: AI coding agents degrade over long working sessions as the context window fills, causing earlier decisions, conventions, and task state to be compacted away or lost. Xiaomi argues that better compression is not the answer — what is needed is an explicit storage-and-retrieval mechanism that decides what information should be written into persistent structures and when it should be recalled. MiMo Code attacks this with a cross-session memory system powered by SQLite FTS5 full-text search, spanning four layers: project memory (a persistent MEMORY.md file), session checkpoints, scratch notes, and per-task progress logs.

The architectural innovation is the checkpoint-writer subagent. Rather than forcing the primary coding agent to interrupt its work to take notes, the system deploys an independent subagent whose sole job is to update the blueprints in real time. VentureBeat uses the analogy of a construction contractor working alongside a dedicated architect: while the main agent focuses on building, the subagent notes decisions, issues, and the actual state of the project as it progresses. When the context window approaches its limits, the primary agent can consult the subagent's records and find its place again. The system also bundles limited-time free access to MiMo-V2.5, Xiaomi's multimodal flagship with a million-token context window, with no registration required. The release signals that the open-source ecosystem is producing agentic coding tools that compete with proprietary offerings on the hardest problem in the space: maintaining coherence over long, complex tasks.