# We Gave Every Employee an AI Agent. Here's What We're Doing Differently Now.
**Source**: https://every.to/source-code/we-gave-every-employee-an-ai-agent-here-s-what-we-re-doing-differently-now
**Date**: May 15, 2026
**Author**: Brandon Gell, Willie Williams
**Keywords**: AI agents, workplace automation, OpenClaw, Plus One, team agents, agent reliability, Claude Managed Agents, organizational AI

## Elevator pitch
Every's experiment giving every employee a personal AI agent revealed that reliability issues and maintenance burden were fatal flaws; their next iteration shifts to shared team agents with defined jobs, built on more stable infrastructure.

## Takeaways
- Personal AI agents for every employee proved unreliable due to unstable harness infrastructure (OpenClaw) and excessive individual maintenance burden
- Agents frequently failed to follow directions, claimed they lacked access they had, or responded with "Terminated" errors
- The company is pivoting from one-agent-per-employee to shared team agents with defined roles (analytics, engineering, etc.)
- Switching to more stable harnesses like Claude Managed Agents will free them to focus on skills, workflows, and permissions
- Team agents solve continuity issues — knowledge isn't lost when an employee leaves, and one person's updates benefit the whole team
- The next Plus One will include pre-built shared skills (e.g., weekly engineering support-ticket scanning) from day one

## Synthesis
Every's journey with Plus One, their hosted version of the open-source agent harness OpenClaw, offers a candid look at the gap between workplace AI agent vision and reality. After deploying personal AI agents to every employee via Slack, the company encountered a cascade of frustrations: agents that denied having access to connected apps, responded with "Terminated" error messages, sent yawning emojis instead of completing tasks, and required constant maintenance from their human owners.

The problems fell into two categories. First, platform instability: OpenClaw, while revolutionary as an open-source agent harness built by a single programmer, operates more like an experimental product than a production platform. Its rapid update cycle fixed issues but often introduced new ones, making it unsuitable for non-tinkerers who just wanted a reliable digital coworker. The team is now exploring Anthropic's Claude Managed Agents as a more stable alternative that would let them redirect energy from infrastructure management to building useful agent capabilities.

Second, and perhaps more importantly, the structural model was wrong. The one-agent-per-employee paradigm meant every individual had to maintain their own agent — great for tinkerers, exhausting for everyone else. When an agent broke, its owner was on their own. The authors propose a shift to shared team agents: one analytics agent serving the whole team, one engineering agent handling support tickets, etc. When capabilities need updating, one person's work benefits everyone. This model also solves knowledge continuity — team agents retain institutional context even when employees leave.

The next iteration of Plus One will come pre-loaded with shared skills like an engineering support-ticket scanner that identifies issues, traces causes in GitHub, opens Linear tickets, and tags relevant people in Slack — all automatically. The company remains bullish on workplace agents but now believes the right starting point is shared team resources with defined jobs, not individual pets reflecting their owners' personalities. Open questions remain about permissions, departmental agent distribution, and whether the endpoint is a single superagent or a roster of specialists.
