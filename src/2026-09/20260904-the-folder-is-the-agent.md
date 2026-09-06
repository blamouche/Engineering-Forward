# The Folder Is the Agent
**Source**: https://every.to/emails/the-folder-is-the-agent
**Date**: 2026-09-04
**Author**: Kieran Klaassen (Every)
**Keywords**: AI agents, Claude Code, compound engineering, folder-as-agent, orchestration, dispatch layer, multi-agent systems, CLAUDE.md

## Elevator pitch
After three months of failing to make agent swarms work, Every's Kieran Klaassen discovered that the real agent architecture was already on his hard drive: a project folder with a CLAUDE.md, skill definitions, and accumulated context — and he now runs 44 such folder-as-agents across multiple projects with a file-based dispatch layer.

## Takeaways
- An agent is fundamentally "a model with enough context so you don't have to re-explain everything each time" — a project folder with CLAUDE.md and .claude/ files is already an agent
- The author runs 44 folder-as-agents across projects like ~/cora/ (Rails engineer) and ~/cora-agent/ (ops engineer), each with different context but running on the same model (Opus 4.6, GPT 5.4, Gemini Pro 3.1)
- A custom Ruby daemon acts as the dispatch layer: it watches a directory for spawn requests, creates lead agents that break tasks into subtasks, and spawns workers in the right folders — file-based messaging, no custom networking
- Two slash commands replace 20 terminal tabs: /hey (morning briefing across all projects) and /orchestrate (kick off a task that gets decomposed and routed to specialized workers)
- Anthropic's own research supports the pattern: an Opus lead with Sonnet sub-agents outperformed a single Opus by 90% on research tasks, but multi-agent systems burn 15x more tokens

## Synthesis
Kieran Klaassen, general manager of Every's email product Cora, spent three months trying to build agent swarms — fleets of coordinating AI agents that would multiply his productivity. The experiment failed: when 10 agents finished simultaneously, he had 10 results to evaluate without enough context to know which to trust. The bottleneck was never the agents' speed but the human manager's evaluation capacity.

The breakthrough came from realizing that the real agent architecture was already embedded in his project folders. A folder containing a CLAUDE.md file (project conventions, deploy workflows, database patterns), accumulated documentation (architecture reports, runbooks, postmortems), and specialized agent definitions (.claude/agents/) gives a model enough context to act as a specialist. Point Opus at ~/cora/ and it's a Rails engineer; point it at ~/cora-agent/ and it's an ops engineer who knows the incident history and service topology. The model doesn't change — the folder does.

To manage 44 agents across these folders, Klaassen built a dispatch layer: a Ruby daemon that watches a directory for spawn requests, creates lead agents that decompose tasks into subtask files, and spawns workers in the appropriate folders. Workers report back by writing files. The daemon checks status every 60 seconds. There's no agent-to-agent protocol or custom networking — just file-based messaging on top of folders that already contain the sophistication.

The biggest lesson is that "you can't vibe orchestrate." Before handing a flow to the dispatch layer, Klaassen builds the folder, establishes the flows, and uses them manually until they're predictable. Only when he trusts a flow does he hand it off. Skipping this step leads to agents opening duplicate pull requests and filing issues for work already done. The order is: build it, use it, trust it, then orchestrate it. Anthropic's launch of Claude Managed Agents — a hosted service for sandboxing, state management, and tool execution — suggests this pattern is about to become infrastructure rather than DIY.