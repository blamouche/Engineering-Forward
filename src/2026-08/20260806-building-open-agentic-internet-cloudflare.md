# Building an Open Agentic Internet
**Source**: https://blog.cloudflare.com/the-agentic-internet/
**Date**: August 6, 2026
**Author**: Jack Galilee, Will Papper, and Andrew Galloni
**Keywords**: agents, web, MCP, payments, bot-authentication

## Elevator pitch
Cloudflare argues that agent traffic needs open primitives for identity, machine-readable content, actions, and payment if the web is to remain economically viable.

## Takeaways
- Agent requests need authenticated identity rather than a spoofable user-agent string.
- Machine-readable pages can reduce token and bandwidth waste.
- Explicit browser tools are more reliable than agents scraping changing interfaces.
- Payment and receipts could give publishers a business model beyond human page views.
- Open standards matter because discovery, identity, and payments otherwise consolidate into a few platforms.

## Synthesis
Cloudflare frames the agentic web as an infrastructure transition, rather than a new category of bot. Agents are already fetching pages built for visual rendering, repeatedly retrieving unchanged material and then paying to discard much of the resulting HTML. That is inefficient for both the site owner and the agent operator. The proposed response is a set of interoperable layers: Web Bot Auth and PACT for trustworthy identity, Markdown for Agents for readable content, WebMCP for callable actions, and x402-style mechanisms for payment.

The useful distinction is between access and cooperation. A site should be able to admit a known, well-behaved agent without giving the same treatment to indiscriminate scraping. Likewise, an agent should not need to infer a button's semantics from a DOM when a site can expose a typed action. This moves interactions from brittle UI automation to explicit contracts while keeping the user's existing session and authorization context.

The commercial claim is equally important. If an agent answers questions without rendering ads or creating referral visits, publishers need a way to charge for the resource being consumed. Micropayments, usage receipts, and explicit attribution are presented as a replacement for the old exchange of free content for search traffic. Whether those mechanisms gain broad adoption is unresolved, but the article makes clear that technical protocols and content economics are now the same problem.
