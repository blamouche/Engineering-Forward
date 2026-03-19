# How Uber uses AI for development: inside look
**Source**: https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development
**Date**: 2026-03-10
**Author**: Gergely Orosz
**Keywords**: AI, agentic coding, software development, internal tools, developer experience, code generation, token costs, Uber

## Elevator pitch
Uber has built a sophisticated internal AI infrastructure—including specialized agents like Minion, uReview, and Shepherd—to automate repetitive engineering work, though adoption and cost management remain significant challenges.

## Takeaways
- Uber's agentic stack spans four layers: an internal AI platform, context sources (code/documentation), industry agents (Claude, Copilot), and specialized background agents for testing and code review.
- 84% of developers actively use agentic coding tools, with 65-72% of IDE-based code being AI-generated, though usage patterns differ significantly by tool type.
- Parallel agent orchestration has replaced single-threaded workflows, with engineers naturally gravitating toward running multiple concurrent background tasks while waiting for results.
- Minion provides background agent infrastructure at scale, offering monorepo access and optimized defaults—solving the challenge of coordinating many simultaneous AI-driven tasks across teams.
- Cost and adoption remain problematic: AI-related expenses increased 6x since 2024, and top-down adoption mandates proved less effective than grassroots peer-to-peer knowledge sharing.

## Synthesis
Uber's comprehensive approach to integrating AI into engineering demonstrates both the transformative potential and operational complexity of agentic systems. Rather than replacing developers, the company strategically deploys AI to eliminate "toil"—upgrades, migrations, trivial fixes—freeing engineers for creative, high-value work.

The infrastructure itself is sophisticated. Uber constructed an MCP (Model Context Protocol) gateway that unifies internal and third-party data sources, an Agent Builder for no-code workflow composition, and the AIFX CLI to ensure consistent client provisioning and configuration across thousands of developers. This platform-first approach reflects lessons learned during the company's hypergrowth phase.

Developer workflows have fundamentally shifted from single-threaded IDE work to orchestrating multiple parallel agents. Engineers intuitively spawn background tasks while awaiting results, creating operational challenges around resource allocation and monitoring that Uber addressed through Minion—a background agent platform with optimized defaults and monorepo integration.

However, the narrative also reveals friction. Despite Uber's engineering maturity, AI adoption proved slower than anticipated. The company discovered that top-down mandates proved ineffective compared to peer-driven adoption, where engineers organically share wins with colleagues. Additionally, 11% of pull requests originating from agents represents substantial volume, necessitating new tooling like Code Inbox for smart PR routing and uReview for high-signal code review comments.

Most pressing is cost. Token expenses have ballooned sixfold since 2024, making cost optimization a priority—a pattern likely repeated across the industry. This tension between capability expansion and operational economics suggests that mature AI integration requires not just sophisticated tooling but also disciplined financial stewardship.

Uber's experience indicates that AI-powered engineering is feasible at scale but demands substantial platform investment, thoughtful change management, and continuous cost monitoring to remain sustainable. The company's journey from ad-hoc tool adoption to a structured agentic platform represents a template other large organizations can study, though the scale of investment required may limit replication to organizations with similar engineering resources.
