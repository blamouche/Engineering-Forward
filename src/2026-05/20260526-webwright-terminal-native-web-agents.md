# Webwright: A terminal is all you need for web agents
**Source**: https://microsoft.github.io/Webwright/
**Date**: May 26, 2026
**Author**: Yadong Lu, Lingrui Xu, Chao Huang, Ahmed Awadallah (Microsoft Research & HKU)
**Keywords**: web agents, terminal-native, browser automation, Playwright, agent architecture, code generation, web browsing

## Elevator pitch
Microsoft Research's Webwright reimagines web agents: instead of clicking through pages, the model writes bash scripts in a terminal — launching disposable browsers, composing actions as code, and producing reusable programs rather than ephemeral sessions.

## Takeaways
- Webwright separates the agent from the browser session: browsers are launched, inspected, and discarded while code, logs, and artifacts persist in the workspace
- Achieves 86.7% on Online-Mind2Web (300 live tasks, 136 sites) and 60.8% on Odysseys long-horizon browsing, a 35.1% improvement over previous SOTA
- The harness is deliberately small — ~1K lines across three modules (Runner, Model Endpoint, Environment) with no multi-agent orchestration
- The "premature done gate" requires agents to generate a final script, rerun it in a fresh folder, and pass self-reflection before the task is accepted
- Solved tasks become reusable CLI tools and Codex skills, eliminating the need to rediscover solutions from scratch

## Synthesis
Microsoft Research, in collaboration with HKU, has released Webwright, a fundamentally different approach to building web agents. Where traditional web agents maintain a single browser session and predict sequences of clicks, types, and scrolls, Webwright gives the model a terminal, a local workspace, and the freedom to write code that launches, inspects, and discards browser sessions.

The paradigm shift is threefold. First, browsers become disposable: the agent spawns fresh sessions, captures screenshots only when useful, inspects failures, and reruns scripts without being trapped in a single stateful page. Second, actions become code: date selection, form filling, filtering, comparison, and extraction can be expressed as loops and functions instead of long chains of primitive browser actions. Third, artifacts survive: the durable output is a workspace containing exploratory scripts, action logs, screenshots, final outputs, and eventually a reusable task program.

The architecture is deliberately minimal — roughly 1,000 lines of harness code across three modules: a Runner that sends context to the model, a Model Endpoint, and a terminal Environment that executes commands and returns observations. The loop works in four steps: send context (task, workspace state, observations), emit bash (the model returns a thinking block and a shell command, often writing Playwright-backed scripts), return observations (terminal output, logs, screenshots, files), and refine until the agent produces a final script that passes self-reflection.

Results are competitive. On Online-Mind2Web, GPT-5.4 with Webwright achieves 86.7% accuracy on 300 live tasks across 136 sites with a 100-step budget. On the harder Odysseys long-horizon browsing benchmark, Webwright scores 60.8% — a 35.1% relative improvement over the previous reported state-of-the-art. Notably, even small models benefit: Qwen3.5-9B augmented with Webwright-crafted tools reaches 66.2% on the hard split of Online-Mind2Web.

The project introduces several practical safeguards. The "premature done gate" requires agents to generate a final script, rerun it in a fresh folder, save logs and screenshots, and pass a self-reflection judgement. Context compaction periodically summarizes long coding trajectories while keeping workspace artifacts concrete. And solved tasks can be parameterized, exported as CLI tools, and shared with coding agents — transforming one-time browsing sessions into permanent, reusable infrastructure.
