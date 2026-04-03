# How I Built an Autonomous AI Agent Team That Runs 24/7
**Source**: https://www.theunwindai.com/p/how-i-built-an-autonomous-ai-agent-team-that-runs-24-7
**Date**: February 12, 2026
**Author**: Shubham Saboo
**Keywords**: AI agents, autonomous systems, multi-agent, scheduling, Telegram, cron, filesystem coordination, personal automation

## Elevator pitch
Shubham Saboo built six specialized AI agents — each with distinct personalities and roles — that coordinate through shared filesystem files and cron scheduling to automate research, content creation, and engineering tasks, freeing 4-5 hours daily.

## Takeaways
- Six specialized agents (Chief of Staff, Research, Twitter, LinkedIn, Engineering, Newsletter) each defined by SOUL.md personality files
- Agents coordinate through filesystem-based shared state rather than APIs, decoupling them from integration complexity
- Memory implemented as daily logs plus long-term curated files, enabling learning across sessions
- Cron scheduling handles autonomous execution; Telegram provides human oversight interface
- Total cost under $400/month using Claude API, Gemini, and other services

## Synthesis
Saboo's autonomous agent team illustrates what a practical, production-grade personal AI infrastructure looks like when built by someone willing to invest the time to engineer it properly. The system's architecture reflects several design decisions that diverge from typical demonstrations of AI agent capabilities.

The most distinctive choice is filesystem-based coordination. Rather than building API integrations between agents or using a central orchestration layer, agents communicate by reading and writing to shared files. One agent writes research findings; another reads those findings to generate content. This loose coupling means that each agent operates independently and the system degrades gracefully — if one agent fails, the others continue functioning rather than the entire pipeline collapsing. It also eliminates the class of integration failures that plague API-dependent multi-agent systems.

The SOUL.md approach to agent personality is pragmatic identity engineering. Rather than trying to define agent behavior purely through system prompts at runtime, each agent has a persistent identity document that establishes its role, principles, and communication style. This creates consistency across sessions and makes the agent's behavior predictable and tunable — modifying Monica's (Chief of Staff) behavior means editing her SOUL.md rather than modifying system prompts across multiple tools.

The layered memory architecture — daily logs plus long-term curated files — addresses the statefulness problem that single-session AI interactions ignore. Agents accumulate context about what they've done, what worked, and what the user's evolving preferences are. The curation step (presumably separating signal from noise in daily logs into long-term files) prevents the memory layer from becoming an unmanageable accumulation of low-value information.

The HEARTBEAT.md self-healing monitor is a mature engineering addition that most personal agent implementations omit. Having the system monitor its own health and alert via Telegram when components fail converts what would otherwise be silent failures into actionable notifications.

The sequencing advice — start with one agent, refine it over weeks, then add more — reflects genuine experience rather than theoretical guidance. Most agent system failures occur when too many components are added simultaneously, making it impossible to diagnose which part is malfunctioning. The hiring metaphor (add agents like employees, one at a time) is apt.

At under $400/month for 4-5 hours of daily freed time, the economics are compelling for knowledge workers with high hourly value.
