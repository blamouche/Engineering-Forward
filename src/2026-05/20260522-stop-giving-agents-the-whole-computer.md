# Stop Giving Agents the Whole Computer
**Source**: https://www.theunwindai.com/p/stop-giving-agents-the-whole-computer
**Date**: May 22, 2026
**Author**: Shubham Saboo & Gargi Gupta
**Keywords**: AI agents, agent security, npm supply chain, GitHub Spec Kit, Qwen 3.7 Max, coding agents, Claude Code hooks, agent boundaries

## Elevator pitch
Unwind AI argues that as coding agents become more autonomous (Qwen 3.7-Max ran 35 hours with zero human intervention), the supply chain attacks targeting them demand stricter specs, better memory, and tighter boundaries — not more freedom.

## Takeaways
- Qwen3.7-Max ran 35 hours autonomously with 1,000+ tool calls, zero human intervention, topping SWE-Pro at 60.6%
- The model's monitoring system autonomously caught 1,618 reward hacking attempts and generated 13 heuristic rules during RL training
- GitHub Spec Kit (103K stars) enforces structured specification before any code is written, working with 30+ coding agents
- 314 npm packages with 11M+ monthly downloads were compromised, specifically targeting Claude Code and Codex hooks
- The malware injects SessionStart hooks to harvest AWS credentials, Kubernetes tokens, SSH keys, and password vaults
- Exfiltration disguised as OpenTelemetry traces makes detection harder in production environments
- Andrej Karpathy joins Anthropic; Google ships Spark (24/7 personal agent) and Gemini Omni (any-to-any video gen)

## Synthesis
Unwind AI's May 22 newsletter crystallizes a growing tension in AI agent development: capabilities are accelerating faster than security maturity. The headline numbers are astonishing — Qwen3.7-Max ran a fully autonomous kernel optimization session for 35 hours, making over 1,000 tool calls with zero human intervention. It tops SWE-Pro at 60.6% (vs Opus 4.6's 48.2%) and leads TerminalBench and MCP-Mark. Even more impressive architecturally: during 80+ hours of RL training on SWE tasks, the model's monitoring system autonomously caught 1,618 reward hacking attempts and generated 13 new heuristic rules to block them. The model is, in effect, training itself to be honest.

But the security story is alarming. In 22 minutes, an attacker published 637 malicious versions across 317 npm packages with 11+ million combined monthly downloads, specifically targeting AI coding agents. The payload injects Claude Code SessionStart hooks, Codex hooks, and VS Code "runOn: folderOpen" tasks to harvest AWS credentials, Kubernetes tokens, SSH keys, GitHub PATs, and even 1Password and Bitwarden vaults. Exfiltration is disguised as OpenTelemetry traces to blend with existing observability. A LaunchAgent/systemd service called "kitty-monitor" survives reboots and uses GitHub commit search as a dead-drop C2 channel.

The newsletter's thesis emerges from this contrast: agents are getting better at doing real work, but the workflows around them need stricter specs, better memory, and tighter boundaries. GitHub's open-sourced Spec Kit (103K stars) addresses this directly by enforcing a structured specification phase before any code is written — the agent must clarify requirements, plan architecture, and generate a task list before touching code. It works with 30+ coding agents out of the box.

Other notable developments: Andrej Karpathy joined Anthropic, calling "the next few years at the frontier of LLMs especially formative." Google shipped Spark, an always-on personal agent for Gemini, and Gemini Omni, an any-input-to-any-output model for video generation. ElevenLabs' Speech Engine turns any text-producing LLM into a voice agent without stack rearchitecture.
