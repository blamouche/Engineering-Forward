# Introducing Vercel Connect: Scoped Credentials for Agent Authentication

**Source**: https://vercel.com/blog/introducing-vercel-connect
**Date**: 2026-06-17
**Author**: Hedi Zandi, Dima Voytenko, Kevin Corbett
**Keywords**: vercel, connect, agents, authentication, security, oauth, credentials

## Elevator pitch

Vercel Connect replaces long-lived provider tokens with runtime credential exchange, giving agents short-lived, scoped access to external services—solving the fundamental security problem of agent authentication in production.

## Takeaways

- Current agent authentication relies on long-lived provider tokens stored in environment variables, shared across all users, never expiring, and granting full access to every service—a significant security risk.
- Vercel Connect introduces runtime credential exchange: register a connector once, then agents request short-lived, scoped tokens only when they have work to do, with no provider secrets stored in the application.
- Connectors are reusable across projects and environments with project-level access controls, eliminating the need to manage scattered environment variables.
- The `@vercel/connect` SDK provides a simple `getToken()` API that returns scoped tokens for immediate use against provider APIs.
- Coding agents can set up Connect themselves using the vercel-connect skill, enabling self-service onboarding.

## Synthesis

As agents move from prototypes to production systems, authentication has emerged as a critical but underappreciated challenge. The current standard—storing long-lived API tokens in environment variables—works for human applications but is fundamentally unsuited for autonomous agents that act on behalf of different users and organizations.

Vercel Connect treats agent authentication as an infrastructure problem rather than a configuration one. Instead of vaulting tokens (which makes them harder to steal but doesn't reduce their blast radius), Connect replaces them entirely. The pattern will be familiar to anyone who has implemented OAuth: a connector is registered once as a relationship between your Vercel team and a provider. When an agent needs to act, it calls `getToken()` with a subject identifier, receives a short-lived credential scoped to the task, uses it, and moves on. No provider secret ever lives in the application.

This approach has several cascading benefits. Token rotation becomes automatic because tokens are short-lived by nature. Access scoping means a support agent connecting to Slack gets only Slack permissions, while a data analyst connecting to Snowflake gets only Snowflake permissions. Auditability improves because each token request is tied to a specific agent, project, and user. And the developer experience is dramatically simpler—no more hunting through a dozen environment variable panels to rotate a key.

The self-service onboarding for coding agents is a clever touch. Running `npx skills add vercel/vercel-plugin --skill vercel-connect` lets agents create and attach their own connectors, reducing the setup friction that often stalls infrastructure adoption.

For engineering teams building production agents, Vercel Connect represents an important shift in thinking: from "how do I protect my tokens?" to "how do I give my agents exactly the access they need, for exactly as long as they need it?" It's a pattern that will become standard as agent deployments scale.