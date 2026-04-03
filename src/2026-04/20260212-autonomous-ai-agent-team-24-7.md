# How I Built an Autonomous AI Agent Team That Runs 24/7
**Source**: https://www.theunwindai.com/p/how-i-built-an-autonomous-ai-agent-team-that-runs-24-7
**Date**: February 12, 2026
**Author**: Shubham Saboo
**Keywords**: AI agents, autonomous agents, OpenClaw, multi-agent, workflow automation

## Elevator pitch
Shubham Saboo describes building a six-agent autonomous team modeled on TV show characters that saves 4-5 hours daily through filesystem-based coordination, persistent memory, and self-healing cron jobs at roughly $400/month.

## Takeaways
- Six specialized agents (Monica, Dwight, Kelly, Rachel, Ross, Pam) handle daily operations from research to content creation
- Agents communicate through shared files rather than API calls, eliminating authentication and infrastructure complexity
- Dual-layer memory system uses daily logs and a curated MEMORY.md for persistent context across sessions
- Self-healing HEARTBEAT function monitors for silent failures and forces reruns when tasks exceed 26-hour staleness
- Total monthly cost: approximately $400; sequential onboarding (one agent at a time) is strongly recommended over simultaneous deployment

## Synthesis
Saboo presents a practical framework for deploying multiple AI agents that autonomously handle repetitive workflow tasks. Rather than treating AI as a single tool, he structures his operation like hiring a specialized team, each with distinct roles and personalities.

He runs six agents named after TV characters—Monica as Chief of Staff, Dwight for research, Kelly for Twitter, Rachel for LinkedIn, Ross for engineering, and Pam for newsletters—to handle daily operations. This naming convention intentionally leverages the models' training data; "Dwight Schrute energy" immediately conveys thoroughness and intensity without extensive instruction. The system runs on a Mac Mini M4, though any always-on computer suffices, using OpenClaw as the orchestration platform.

The coordination mechanism is deliberately simple: agents communicate through shared files rather than API calls or message queues. Dwight produces research summaries to intel/DAILY-INTEL.md, which Kelly and Rachel read to draft platform-specific content. This filesystem-based handoff eliminates complexity around authentication, rate limiting, and infrastructure failures.

Memory operates on two levels. Daily logs capture session-specific activities in memory/YYYY-MM-DD.md files, while curated long-term memory in MEMORY.md stores refined insights and learned preferences. Each agent begins sessions fresh but loads these persistent files, enabling continuous improvement without permanent model retraining.

Initial agent outputs rarely match requirements perfectly. Saboo describes corrective prompt-engineering where agents update their memory files based on guidance. Kelly initially used excessive emojis; after feedback, she integrated this constraint into her persistent context. This mirrors real team management where personalities emerge through repeated interaction rather than perfect initial specification.

Cron jobs handle scheduled execution, but the system includes self-healing capabilities. A HEARTBEAT monitoring function checks whether daily jobs executed successfully and forces reruns if tasks exceed 26-hour staleness windows. This prevents silent failures where jobs simply disappear without human notification.

The monthly cost totals approximately $400 across Claude API, Gemini, TinyFish web agents, and Eleven Labs voice services. The primary benefit emerges through compounding consistency over weeks rather than immediate daily output. Saboo strongly advises against deploying six agents simultaneously, recommending sequential onboarding to establish reliability before adding complexity.

The framework demonstrates that systematic AI deployment depends less on model sophistication than on surrounding infrastructure: personality definition, memory management, simple coordination protocols, and reliability monitoring.
