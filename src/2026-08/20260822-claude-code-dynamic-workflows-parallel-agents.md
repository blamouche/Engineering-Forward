# Claude Code Dynamic Workflows: Orchestrating 100s of Parallel Agents
**Source**: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
**Date**: 2026-06-09
**Author**: Anthropic
**Keywords**: claude-code, multi-agent, orchestration, parallel-agents, dynamic-workflows

## Elevator pitch
Anthropic's Dynamic Workflows lets Claude Code write custom JavaScript orchestration scripts on the fly, fanning work across hundreds of parallel subagents that independently verify and refute each other's results until answers converge.

## Takeaways
- Claude generates a bespoke JS orchestration script per task — no pre-built templates — then runs it to coordinate hundreds of parallel subagents
- Independent verification is built in: agents tackle problems from different angles while other agents try to refute findings, iterating until convergence
- Workflows are resumable and saveable: progress is checkpointed, interrupted jobs resume where they left off, and workflows can be saved as reusable /commands
- The proof of concept is striking: Jarred Sumner ported Bun from Zig to Rust — 750K lines, 99.8% test suite passing, 11 days first commit to merge
- Token consumption is significantly higher than typical sessions; users should start with scoped tasks to calibrate usage before applying to entire codebases
- Available as research preview on Max, Team, Enterprise plans, plus Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry; requires Claude Code v2.1.154+

## Synthesis
Anthropic's Dynamic Workflows for Claude Code represents a shift from single-agent coding to orchestrated multi-agent engineering at scale. The core idea is that some problems — bug hunts across entire services, migrations touching hundreds of files, stress-testing plans from every angle — are too large for one agent in one pass. Rather than manually decomposing the work, the developer asks Claude to "create a workflow," and Claude writes a custom JavaScript orchestration script tailored to the specific task.

The orchestration script fans work across hundreds of parallel subagents, each working on a piece of the problem. What distinguishes this from simple fan-out is the verification loop: independent agents try to break what other agents produced. The system iterates until results converge, catching issues that a single-pass approach would miss. This is closer to adversarial peer review than to parallel execution.

The Bun-to-Rust port is the headline proof point. Jarred Sumner used Dynamic Workflows to port 750,000 lines of Rust, achieving 99.8% test suite passing in eleven days from first commit to merge. Hundreds of agents worked in parallel with two reviewers on each file. This is a scale of work that would be infeasible with a single agent or a manual multi-agent setup.

The system is resumable — progress checkpoints mean interrupted jobs pick up where they left off — and workflows can be saved as reusable /commands with structured input parameters. This makes complex orchestration patterns shareable across teams. However, Anthropic warns that token consumption is meaningfully higher than typical sessions, and recommends starting with scoped tasks before applying workflows to entire codebases. The feature is available as a research preview on Max, Team, and Enterprise plans, as well as the Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry, requiring Claude Code v2.1.154+ with ultracode effort level enabled.