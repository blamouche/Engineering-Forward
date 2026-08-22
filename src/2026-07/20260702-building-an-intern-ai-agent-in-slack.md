# Building an Intern: A Slack-Based AI Agent at Sentry
**Source**: https://cra.mr/building-an-intern/
**Date**: 2026-07-02
**Author**: David Cramer (Sentry)
**Keywords**: AI agents, Slack integration, agent architecture, serverless compute, agent harness, open source, Junior, Sentry

## Elevator pitch
Sentry built "Junior," an open-source AI intern living in Slack that handles GitHub issues, visual QA, and code exploration — revealing that building a production-grade agent harness requires 100,000 lines of TypeScript and far more complexity than the "receive webhook, call model, post reply" mental model suggests.

## Takeaways
- Junior is described as an "intern" because the interaction model is literal: you give it information, review its work, and steer it in the right direction — not a fully autonomous agent that works without supervision.
- The project grew to ~100,000 lines of TypeScript over four months, far exceeding initial expectations, because turning an agent idea into a good product requires substantial ongoing engineering.
- Junior's architecture uses a task broker pattern on Vercel Queues: Slack webhook → inbox → enqueue → worker claims conversation → agent continues from session log → interrupt timer avoids serverless timeouts → reply posted to Slack.
- Serverless compute is "hostile to agents" — function timeouts, statelessness, and platform constraints force significant architectural complexity that wouldn't exist in a traditional server environment.
- Junior is deliberately not trying to win the agent race; it's a harness/framework for Sentry's specific needs, and is open source purely because Sentry does open source, not as a product strategy.

## Synthesis
David Cramer's account of building "Junior" — Sentry's AI intern in Slack — is a refreshing dose of engineering reality in a space dominated by demo-driven hype. The project started as a joke ("it's my junior") but evolved into a substantial engineering effort that reveals how much complexity hides behind the simple mental model of "receive webhook, call model, post reply."

The most valuable insight is about scope and complexity. Junior grew to 100,000 lines of TypeScript across four months, and Cramer is explicit that this isn't excess — it's the minimum viable product for a useful agent in a real workplace. The complexity comes from multiple sources: serverless function timeouts require interrupt-and-resume patterns, authentication needs careful handling, conversation state must persist across worker claims, and the plugin system evolved from simple YAML to full packages as plugins absorbed responsibility for credentials, OAuth, MCP endpoints, hooks, routes, and skills.

The architecture is instructive for anyone building agents on serverless platforms. The core pattern — save messages to an inbox, enqueue a conversation task, have a worker claim the conversation with a lease, run the agent with an interrupt timer to avoid timeouts, and requeue if incomplete — is a standard task broker approach, but the implementation has many edge cases. The lease mechanism prevents concurrent workers from stepping on each other, and the interrupt timer ensures progress is saved before a serverless timeout kills the process.

Junior's practical value at Sentry comes from filling gaps that vendor-specific agents can't. Cramer explicitly doesn't want another constrained agent that only knows one product. Junior can search the repo, trace code paths, open GitHub issues with gap analysis and RCA, and perform visual QA using Vercel's agent-browser. The collaborative dimension was almost accidental — once it worked for Cramer, the whole team started using it, and the cultural shift ("waste the robots' time instead of humans, please") happened organically.

The honesty about limitations is notable. Junior is "absolutely garbage" at coding tasks by default, partly because it uses Sonnet for speed rather than Opus for quality, and partly because the general-purpose skill loading creates noise. Cramer frames this as acceptable — Junior is a framework, and purpose-built instances can be tuned for specific domains. The plan to experiment with a coding-tuned instance shows the framework's extensibility.

The "stateless compute is hostile to agents" section is a valuable contribution to the agent infrastructure discourse. Vercel and Cloudflare provide great primitives, but the fundamental mismatch between stateless compute and stateful agent conversations creates significant overhead. Cramer notes that providers are working to increase function runtimes, but the architectural patterns required to work around current limitations add real complexity.

The closing reflection — "this is the most fun I've had building something in recent history, but it's also routinely the most frustrating" — captures the agent builder's experience. The behavior of LLMs means you're constantly making judgment calls about whether to solve something or treat it as a steering concern. The admission that much of the pain is self-inflicted (YAML plugins that should have been packages from the start, half-baked libraries that needed patching) is candid and useful for others on the same path.