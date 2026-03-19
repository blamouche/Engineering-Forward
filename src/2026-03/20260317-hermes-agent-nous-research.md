# Hermes Agent: Self-Improving AI Agent by Nous Research
**Source**: https://github.com/nousresearch/hermes-agent
**Date**: 2026-03-17
**Author**: Nous Research
**Keywords**: Hermes, self-improving agent, procedural memory, skill creation, Nous Research, Telegram, Discord, Atropos, tool-calling

## Elevator pitch
Hermes Agent by Nous Research is a self-improving AI agent with procedural memory that learns from use—autonomously creating new skills during conversations and maintaining them across sessions through persistent FTS5-indexed memory.

## Takeaways
- Self-improvement through use: the agent autonomously creates and stores skills during conversations, building capability over time without manual programming.
- Procedural memory: FTS5 session search enables the agent to recall past tasks and successful approaches across sessions.
- Multi-platform deployment: Telegram, Discord, Slack, WhatsApp, Signal, and terminal interfaces.
- Six execution backends: local, Docker, SSH, Daytona, Singularity, and Modal—enabling deployment across development and production environments.
- Atropos integration: connects to Nous Research's training pipeline for tool-calling model improvement, bridging deployment and research.
- Model-agnostic: supports OpenRouter, OpenAI, Anthropic, local endpoints.
- 40+ built-in tools with cron scheduler for autonomous task automation.

## Synthesis
Hermes Agent's self-improvement loop is architecturally interesting because it closes the gap between deployment and training. Most AI agents use a fixed model that doesn't learn from use; improvements require explicit fine-tuning cycles by the model developer. Hermes creates a pathway from deployment interactions to skill creation to model improvement via Atropos—making individual use potentially contribute to broader capability development.

The skill self-documentation feature addresses a real problem in personal agent deployment: the agent that works well for one set of tasks needs to be taught new ones explicitly. When Hermes observes a successful task completion and automatically documents it as a reusable skill, it reduces the maintenance burden on users who would otherwise need to manually maintain prompt libraries and workflow documentation.

The procedural memory implementation using FTS5 (SQLite full-text search) makes the memory system lightweight and local, rather than requiring an external vector database or cloud service. This design choice reflects a philosophy about where personal agents should run: on infrastructure the user controls, without data leaving their environment. FTS5 provides good semantic search over human-readable text without the operational complexity of embedding models and vector stores.

The Nous Research origin is significant context. Nous is known for releasing capable open models (Hermes series) and for research on model capabilities and training methods. Hermes Agent's integration with Atropos for training tool-calling models suggests the deployment platform is partly a research instrument—a way to gather real-world agent interaction data that can improve the next generation of tool-calling models.
