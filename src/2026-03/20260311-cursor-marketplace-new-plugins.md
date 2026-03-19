# Over 30 new plugins join the Cursor Marketplace
**Source**: https://cursor.com/blog/new-plugins
**Date**: 2026-03-11
**Author**: Kevin Niparko
**Keywords**: Cursor, Marketplace, plugins, MCP, Atlassian, Datadog, GitLab, Glean, AI agents, developer tools

## Elevator pitch
Cursor's Marketplace expansion with 30+ plugins from Atlassian, Datadog, GitLab, and others enables AI agents to read, write, and act across the entire development stack—combining MCPs with instructional skills for capabilities greater than MCPs alone.

## Takeaways
- 30+ new plugins from major partners including Atlassian, Datadog, GitLab, Glean, Hugging Face, monday.com, and PlanetScale.
- Plugins bundle Model Context Protocols (MCPs) with instructional skills, delivering significantly greater capability than MCPs alone.
- Infrastructure plugins: query logs/metrics/dashboards (Datadog), manage repositories/pipelines (GitLab), optimize database performance (PlanetScale).
- Productivity plugins: issue management/reporting (Atlassian), knowledge retrieval/stakeholder identification (Glean), project task management (monday.com).
- Team-level distribution and custom plugin development support enables organizational standardization of agent tool access.
- Cursor Automations enables scheduled or event-triggered agent workflows without manual intervention.

## Synthesis
The plugin marketplace represents Cursor's move from a coding assistant to a developer platform. The distinction matters: a coding assistant improves individual productivity within the IDE; a platform enables organizations to embed their entire operational context—monitoring data, project tracking, knowledge bases, database schemas—into the agent's working environment.

The plugins-exceed-MCPs observation is interesting and reflects a real limitation of raw MCP integrations. MCPs provide tool access—the ability to call an API and get data back. They don't provide the instructional context about how and when to use that data effectively. A Datadog MCP can return metrics; a Datadog plugin adds instructions about what metrics matter, how to interpret them in context, and what actions to take when thresholds are exceeded. The difference between tool access and effective tool use is what the instructional layer addresses.

Team-level distribution is the organizational adoption unlock. Individual developers adopting plugins is interesting but doesn't create team-wide capability. When teams can standardize which plugins are available—ensuring everyone working on a codebase has access to the same Jira, Datadog, and GitLab context—the agent becomes a team-level capability rather than an individual one. This is the same dynamic that made IDE plugins valuable organizationally: consistent tooling across the team reduces friction and creates shared context.

Cursor Automations for scheduled and event-triggered workflows extends the IDE from a place where developers interact with AI to a place where AI acts without developer involvement. This is a significant expansion of scope that creates new questions about permissions, audit trails, and organizational governance of automated agent actions.
