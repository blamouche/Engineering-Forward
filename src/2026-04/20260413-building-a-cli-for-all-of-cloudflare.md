# Building a CLI for all of Cloudflare

**Source**: https://blog.cloudflare.com/cf-cli-local-explorer
**Date**: April 13, 2026
**Author**: Matt “TK” Taylor, Dimitri Mitropoulos, Dan Carter
**Keywords**: Cloudflare, CLI, developer tools, code generation, local development, AI agents

## Elevator pitch
Cloudflare is rebuilding Wrangler into a unified `cf` CLI and pairing it with Local Explorer, aiming to make its sprawling platform more consistent for both humans and AI agents by generating commands, schemas, and local-debug interfaces from shared definitions.

## Takeaways
- Cloudflare sees agents as a primary consumer of its APIs and is redesigning its CLI around consistency, predictable conventions, and low-context interfaces.
- A new TypeScript-based schema layer is being used to generate commands, config, bindings, and other interfaces from one source instead of maintaining them manually.
- Local Explorer extends the same philosophy to debugging, giving developers and agents a clearer view into locally simulated state for products like KV, R2, D1, and Durable Objects.

## Synthesis
Cloudflare’s post is really about context engineering for infrastructure tooling. The company has too much surface area for hand-crafted interfaces to stay aligned across APIs, SDKs, CLIs, config files, local emulators, and docs. Its answer is to define richer shared schemas and generate those interfaces from a common layer, with explicit guardrails for consistency. That matters because inconsistency is annoying for humans but actively harmful for agents, which depend on predictable verbs, flags, and defaults to behave reliably.

The interesting product insight is that Cloudflare is not treating AI-agent support as a bolt-on. It is using agent interaction as a forcing function to clean up the entire developer experience. If a command surface is too irregular for an agent to use well, it is probably also too irregular for a human to learn quickly. Designing for agents therefore becomes a way to standardize naming, expose state more clearly, and reduce hidden behavior across the stack.

Local Explorer reinforces that point. Agents and humans both need visibility into what local resources actually contain during development, especially in a platform that blurs local and remote execution. By making local state inspectable through the same conceptual model as remote infrastructure, Cloudflare is reducing a class of debugging ambiguity that often slows both autonomous and human workflows. The broader lesson is that agent-ready tooling often looks like good tooling, full stop.
