# Welcome to Gas Town
**Source**: https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04
**Date**: January 1, 2026
**Author**: Steve Yegge
**Keywords**: Gas Town, AI agents, agent orchestrator, Claude Code, vibe coding, multi-agent engineering, Beads, Kubernetes for agents

## Elevator pitch
Steve Yegge introduces Gas Town, an opinionated multi-agent orchestrator that coordinates 20-30 parallel Claude Code instances like a "Kubernetes for agents," built entirely through vibe coding over three weeks and designed for developers who have already mastered running multiple AI coding agents simultaneously.

## Takeaways
- Gas Town is a Go-based orchestrator that manages 20-30 Claude Code instances in parallel, treating coding agents like workers in an "industrialized coding factory."
- Yegge built it entirely through vibe coding — he's never read the code — yet it solves complex problems (including the MAKER benchmark's 20-disc Hanoi towers) that single LLMs fail at.
- Gas Town's architecture mirrors Kubernetes and Temporal: a mayor (supervisor), polecats (disposable workers), witnesses (observers), and refineries (processing steps), all coordinated through Beads (Yegge's universal git-backed data plane).
- Only developers at "Stage 7+" (managing 10+ agents by hand) are ready for Gas Town; it requires significant elbow grease, tmux proficiency, and acceptance of chaotic, high-throughput vibecoding workflows.
- Cost is extreme — Yegge needed multiple Claude Code accounts just to keep it running, and it burns through massive token budgets.
- Gas Town represents Yegge's fourth complete orchestrator built in 2025, following three failed iterations, each teaching lessons about what multi-agent coordination requires.
- The tool degrades gracefully: workers can operate independently or in groups, and it even works without tmux, just slower.

## Synthesis
Published on New Year's Day 2026, Steve Yegge's "Welcome to Gas Town" is a manifesto for a new era of AI-assisted software development. Yegge, a legendary engineer known for his tenure at Amazon and Google, has built an orchestrator that turns Claude Code (and its clones) from individual coding assistants into a coordinated workforce of 20-30 agents working simultaneously on the same codebase.

Gas Town is the culmination of a year-long obsession. After his March 2025 post "Revenge of the Junior Developer" predicted the rise of agent orchestrators, Yegge spent months evangelizing the concept to companies like Temporal and Anthropic, only to find nobody interested in building it. So he built it himself — four times. Gas Town (v4, written in Go) is his first functioning orchestrator to achieve liftoff, and like its predecessor Beads (225k lines of Go), it was built entirely through vibe coding — Yegge proudly states he's never read the code.

The architecture is deliberately reminiscent of Kubernetes and Temporal. A "Town" serves as headquarters, "Rigs" represent individual git repositories under management, and seven distinct worker roles collaborate to keep the system running: a Mayor that orchestrates, Polecats that execute disposable tasks, Witnesses that observe, and Refineries that process work. The entire system runs on Beads, Yegge's universal git-backed data plane, which serves as both the data and control plane.

Yegge is brutally honest about who should use Gas Town (almost nobody) and what it costs (a fortune). He outlines an eight-stage evolution of AI-assisted programmers, with Gas Town reserved for Stage 7+ developers already comfortable managing 10+ parallel Claude Code instances. The tool requires tmux proficiency, acceptance of chaotic workflows (some bugs get fixed multiple times, designs go missing), and comfort with vibe coding's "throughput over perfection" philosophy. Cost-wise, Yegge had already burned through one Claude Code account and was projecting the need for a third by week's end.

Despite these barriers, Gas Town represents a genuine advance. It solves the MAKER benchmark's 20-disc Hanoi towers problem — something single LLMs fail at after a few hundred steps — by distributing the million-step solution across agents. Yegge frames Gas Town as the next logical step beyond individual coding agents: an Idea Compiler where the developer becomes a product manager, creating features and implementation plans that the agent workforce executes. As he puts it, "This is how work should be done. It's the best way already, and it will get better."
