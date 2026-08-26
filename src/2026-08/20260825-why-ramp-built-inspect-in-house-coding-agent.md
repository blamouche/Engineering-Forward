# Why Ramp Built Its Own In-House Coding Agent, Inspect
**Source**: https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect
**Date**: 2026-08-25
**Author**: Gergely Orosz, Jessica Salmon, and Ivan Klaric
**Keywords**: coding agents, in-house tooling, Ramp, Inspect, AI infrastructure, developer tools

## Elevator pitch
Ramp, a fintech company, rejected off-the-shelf AI coding agents and built Inspect, an in-house coding agent running on remote sandboxes that has become a step ahead of what frontier AI labs offer, demonstrating why select companies choose to build rather than buy.

## Takeaways
- Ramp built Inspect because engineers and designers were dissatisfied with third-party coding harnesses: they wanted to run more than a few agents in parallel (local machines don't support this), needed better frontend tooling, and faced demand for remote development environments
- Inspect runs on remote sandboxes with access to most internal data sources and verifies all backend and frontend changes on the remote machine before presenting results
- The tech stack includes React/Vite, Cloudflare Durable Objects, SQLite, the Cloudflare Agents SDK, and Modal sandboxes, with services like Postgres, Redis, RabbitMQ, and Temporal available inside each sandbox
- Smart tricks enable sandbox spin-up in five seconds or less, including pre-warming and snapshot restoration
- All Inspect sessions are public and open to collaboration with no opt-outs allowed, and more than 150 people at Ramp have contributed to the project
- The "buy, don't build" tooling convention is being challenged by companies like Ramp (Inspect), Block (Goose, open source), Stripe (Minions), and Shopify (River) that find custom tooling more efficient than what frontier labs offer

## Synthesis
At a select few tech companies, engineers write most of their code with custom-built, internal AI coding agents rather than commercial tools like Codex, Claude Code, Cursor, or GitHub Copilot. Ramp's version is called Inspect, and it represents a deliberate choice to build rather than buy—rejecting the convenience of off-the-shelf agents in favor of tighter integration with internal systems and workflows.

The motivation came from practical frustration. Engineers and designers at Ramp found third-party coding harnesses limiting: they wanted to run many agents in parallel, which local machines cannot support, and they needed better frontend tooling. They also faced growing demand for remote development environments that could be accessed from anywhere.

Inspect runs on remote sandboxes that serve as full developer machines in the cloud, with access to numerous internal integrations via API and MCP. Each sandbox includes OpenCode, development services (Postgres, Redis, RabbitMQ, Temporal), Chromium, and VS Code Server. The team engineered sandbox spin-up to complete in five seconds or less through pre-warming and snapshot restoration techniques.

The architecture is built on React/Vite for the frontend, Cloudflare Durable Objects for coordination, SQLite for state, the Cloudflare Agents SDK for orchestration, and Modal for sandbox provisioning. Beyond coding, Inspect is used for bugfixing in Slack, debugging, and as a platform for building internal agents like code review and incident management tools.

A defining cultural choice is that all Inspect sessions are public and open to collaboration, with no opt-outs. This radical transparency has driven adoption: more than 150 people at Ramp have contributed to the project. The article suggests this pattern—companies building custom coding agents—is not isolated to Ramp. Block built Goose (open source), Stripe built Minions, and Shopify built River. The common thread is that non-AI-frontier companies can build more efficient tooling than what frontier AI labs offer when the tooling is tightly integrated with their specific internal systems, data sources, and workflows.