# Anthropic Acquires Stainless
**Source**: https://www.anthropic.com/news/anthropic-acquires-stainless
**Date**: May 18, 2026
**Author**: Anthropic
**Keywords**: Anthropic, Stainless, acquisition, SDK, MCP, API tooling, developer experience, agent connectivity

## Elevator pitch
Anthropic has acquired Stainless, the SDK-generation startup whose tools power API clients for OpenAI, Google, Cloudflare, and Anthropic itself — taking a key piece of AI developer infrastructure off the market and strengthening Claude's agent connectivity via MCP.

## Takeaways
- Stainless automates SDK generation across TypeScript, Python, Go, Java, and more from API specs — it has powered every official Anthropic SDK since the API's earliest days
- The acquisition strengthens Anthropic's MCP (Model Context Protocol) ecosystem by bringing SDK and server tooling expertise in-house for agent connectivity
- Stainless founder Alex Rattray (ex-Stripe engineer) joins Anthropic with his team; the deal is reportedly valued at over $300 million
- Hosted Stainless products will wind down; existing customers retain ownership of generated SDKs but lose the automated maintenance service
- This takes a key infrastructure supplier away from competitors OpenAI, Google, and Cloudflare, who used Stainless for their own SDKs

## Synthesis
Anthropic's acquisition of Stainless represents a strategic move that reshapes the AI developer tooling landscape. Stainless, founded in 2022 by former Stripe engineer Alex Rattray, built a platform that automates SDK creation from API specifications — turning API specs into production-ready SDKs across TypeScript, Python, Kotlin, Go, and Java, with automatic updates as APIs evolve.

The significance extends beyond the technology. Stainless had become the go-to SDK generator for the AI industry: OpenAI, Google, Replicate, Runway, and Cloudflare all relied on it. By acquiring Stainless, Anthropic is simultaneously deepening its own developer platform and removing a shared infrastructure supplier from competitors' toolchains.

The deal makes strategic sense in the context of Anthropic's MCP (Model Context Protocol), which enables Claude to connect to external tools and data sources. Stainless's expertise in generating SDKs and MCP servers directly enhances Claude's ability to act as an agent — connecting to APIs, databases, and services programmatically. As Anthropic's Head of Platform Engineering Katelyn Lesse put it: "Agents are only as useful as what they can connect to."

The reported price tag (over $300 million per The Information) reflects the strategic premium of controlling the SDK layer in an ecosystem where developer experience increasingly determines platform adoption. Anthropic is betting that owning the tools developers use to integrate with Claude — rather than relying on third-party infrastructure shared with competitors — provides a durable competitive advantage.

For existing Stainless customers outside Anthropic, the wind-down of hosted products creates a gap. They retain their generated SDKs and can modify them, but lose the automated update pipeline. This may accelerate in-house SDK development at companies like OpenAI and Cloudflare, or create opportunities for new entrants in the API tooling space — a market that now appears to be consolidating around platform-specific solutions rather than neutral infrastructure providers.
