# Claude Code + MCP Just Made SaaS Dashboards Disposable
**Source**: https://linas.substack.com/p/fintechpulse1101
**Date**: 2026-07-16
**Author**: Linas Beliūnas
**Keywords**: Anthropic, Claude Code, MCP connectors, SaaS, permissions, row-level security, AI-generated apps, agentic AI

## Elevator pitch
Anthropic's latest Claude Code update enables AI-generated pages to call MCP connectors at view time with each call running through the viewer's own enterprise permissions — eliminating the permissions moat that protected SaaS dashboards and making throwaway apps with row-level security a reality.

## Takeaways
- Previous attempts to let AI generate business software hit a wall: connecting generated dashboards to live data with proper per-viewer access controls required wiring OAuth, managing credentials, and recreating authorization logic
- Claude Code artifacts can now call MCP connectors at view time, with each call executing through the viewer's enterprise permissions — two people opening the same dashboard see different Stripe transactions, GitHub repos, and Jira queues
- Row-level security for throwaway apps eliminates the technical moat that protected reporting tools, admin consoles, BI layers, and status pages from being replaced by a prompt
- Gartner projects up to $234 billion in SaaS spending exposed to agentic AI by 2030, making the permissions problem economically significant
- The "barbell model" predicts this will simultaneously grow software consumption (more apps created) and crush SaaS margins (fewer paid surfaces needed), creating both opportunity and disruption

## Synthesis
Anthropic's update to Claude Code and MCP connectors solves what has been the single biggest blocker for AI-generated business software: permissions. Until now, you could spin up a dashboard in seconds with AI, but connecting it to live data with the right access controls for every individual viewer meant recreating the authorization logic that SaaS vendors spent years building. Each user's view had to respect their specific permissions — which Stripe transactions they could see, which GitHub repos they had access to, which Jira tickets were in their queue.

The breakthrough is deceptively simple: instead of the AI page owning the permissions logic, the MCP connector call runs at view time through the viewer's own enterprise credentials. This means the same generated artifact renders differently for each person who opens it, with row-level security enforced by the underlying data source. It's the architectural shift from "the app has permissions" to "the viewer has permissions, and the app is just a lens."

For SaaS companies, this is seismic. The long tail of paid surfaces — reporting tools, admin consoles, BI layers, status pages — just lost the one technical justification for their existence: that only they could connect to live data with proper access controls. When a prompt can generate the same surface in minutes with the same permissions enforcement, the margin compression is structural, not cyclical. The barbell model suggests the outcome won't be less software but cheaper software: more apps will be created (growing consumption) while fewer will need to be purchased as SaaS subscriptions (crushing margins). Engineering teams should evaluate which of their internal dashboards and reporting surfaces could already be replaced by AI-generated MCP-connected artifacts, and SaaS companies should assess whether their moat is really permissions — or something deeper.