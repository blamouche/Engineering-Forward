# Agents can now create Cloudflare accounts, buy domains, and deploy

**Source**: https://blog.cloudflare.com/agents-stripe-projects
**Date**: April 30, 2026
**Author**: Sid Chatterjee and Brendan Irvine-Broque
**Keywords**: cloudflare, agents, stripe, deployment, commerce

## Elevator pitch
Cloudflare and Stripe are wiring account creation, payments, and credential issuance into an agent-friendly flow so coding agents can ship real apps to production without manual setup.

## Takeaways
- Agents can now create Cloudflare accounts, purchase domains, obtain API tokens, and deploy apps with minimal human intervention.
- Stripe Projects acts as the orchestrator for discovery, authorization, and payment across providers.
- The integration is designed so users approve when needed, but do not have to copy tokens or enter card details manually.
- Cloudflare positions service catalogs, API-based provisioning, and delegated credentials as core agent infrastructure primitives.
- The post points toward a future where cloud onboarding is optimized for agents rather than dashboards.

## Synthesis
Cloudflare's announcement is important because it shifts agent deployment from a demo-friendly coding loop into a real production workflow. The company says agents can now create Cloudflare accounts, start subscriptions, register domains, obtain API tokens, and deploy code, all through a Stripe Projects integration that handles discovery, authorization, and payment. In practical terms, that means an agent building an application no longer has to stop at the familiar boundary where a human opens a dashboard, pastes keys, and enters billing details. Stripe provides the signed-in identity and the payment rails, while Cloudflare provisions accounts and returns credentials the agent can use on the user's behalf. Humans still approve key actions, but the friction is substantially reduced. This matters because one of the biggest blockers to agent usefulness has been the handoff from software generation to real-world operations. Cloudflare is effectively saying that hosting providers need to expose machine-readable catalogs, delegated provisioning APIs, and safe billing hooks if they want to become default infrastructure for software agents. The larger signal is that cloud vendors are beginning to redesign onboarding and credential flows around autonomous software as a first-class customer.
