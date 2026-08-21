# Generative UI Is the New Frontend
**Source**: https://www.theunwindai.com/p/generative-ui-is-the-new-frontend
**Date**: 2026-06-03
**Author**: Shubham Saboo
**Keywords**: generative UI, AG-UI, A2UI, MCP, CopilotKit, frontend, agents

## Elevator pitch
Generative UI lets AI agents render real interface components instead of describing them in text—and three architectural patterns (Controlled, Declarative, Open-ended) determine whether your agent app scales or breaks.

## Takeaways
- The protocol stack for generative UI has three layers: MCP (tools), A2A (agent-to-agent), and AG-UI (agent-to-user), with AG-UI providing the streaming backbone over SSE.
- Controlled pattern: pre-built components registered as tool calls; simple to start but hits a token-tax wall past ~15 tools as each description consumes context every turn.
- Declarative (A2UI) pattern: the agent emits a JSON schema mapped to a component catalog; one tool definition serves unlimited UIs, keeping token cost flat as the catalog grows.
- Open-ended pattern: agents write raw HTML rendered in sandboxed iframes; great for throwaway visualizations but brand-inconsistent and security-sensitive for production use.
- The key decision framework: Controlled for pixel-perfect flows (≤10), Declarative for the long tail of card/widget types, Open-ended only for disposable one-shot queries—never as default.

## Synthesis
The article argues that 2026 marks the end of the static frontend era, where designers drew interfaces that engineers built and users consumed as-is. In the new model, AI agents render components in real time based on user intent—ask for a table, get a table rather than a paragraph describing one.

The author identifies three patterns that most teams confuse. Controlled UI is the default starting point: you register pre-built React components as tools, and the agent picks which one to invoke. This works well for up to about ten to fifteen high-value flows, but each tool definition costs ~400 tokens per turn, creating a linear token tax that becomes unsustainable. Declarative UI (A2UI, Google's spec) inverts this: the agent emits a schema and the app maps it to a catalog, so one tool definition serves an arbitrary number of UI types. This is the pattern built for scale. Open-ended UI gives agents full HTML control in sandboxed iframes, which is compelling in demos but produces inconsistent brand experiences and security risks in production.

The protocol foundation matters: MCP connects agents to tools, A2A connects agents to each other, and AG-UI connects agents to users via a streaming layer. CopilotKit implements AG-UI and ships A2UI in production. The article's practical advice is clear: default to Declarative, upgrade the top three flows to Controlled for pixel precision, and reserve Open-ended for disposable visualizations. Most teams that are struggling have unknowingly defaulted to Controlled and are hitting the wall at 25 tool definitions. The fix is not to switch to Open-ended (which looks attractive in demos), but to wire up A2UI and let the schema be the contract between agent and frontend.

The open-source reference implementation lives in the awesome-llm-apps repository on GitHub, covering all three patterns with starter projects and working examples including a financial coach agent.