# Building an Open Agentic Internet: Readable, Discoverable, Callable, and Payable
**Source**: https://blog.cloudflare.com/the-agentic-internet/
**Date**: 2026-08-10
**Author**: Bryton Herdes, Iliana Xygkou, Mingwei Zhang
**Keywords**: cloudflare, agents, agentic-internet, x402, web-bot-auth, mcp, monetization

## Elevator pitch
Cloudflare outlines its vision for an "Agentic Internet" where AI agents interact with the web through four pillars — readable, discoverable, callable, and payable — and introduces a suite of open standards and infrastructure to make it happen.

## Takeaways
- Agents are a new kind of web visitor that don't render CSS, see hero images, or click ads, but carry a paying human on the other end — fundamentally changing how the web should be structured
- Cloudflare proposes four pillars: Readable (Markdown for Agents), Discoverable (AI Search + Agent Engine Optimization), Callable (WebMCP + Code Mode), and Payable (Wallets + Monetization Gateway using x402 protocol)
- Web Bot Auth lets bots cryptographically identify themselves, replacing guesswork about user-agent strings; PACT tokens let sites vouch for users anonymously
- The x402 protocol enables per-request micropayments from agents to content creators, replacing ad-based models that break when agents bypass page rendering
- Cloudflare positions itself as the neutral infrastructure layer — "Customer Zero" of its own rails — connecting publishers, merchants, agent builders, and end users without privileging any one

## Synthesis
Cloudflare's "Agentic Internet" manifesto is the company's most comprehensive articulation of how the web must evolve when AI agents become primary consumers of online content and services. The core insight is that agents don't behave like human browsers — they don't render CSS, click ads, or scroll through pages. Every request now carries a cost and a purpose, which means blocking agents is blocking customers.

The four-pillar framework is methodical. **Readable** means giving agents content in a format native to them — Markdown for Agents strips HTML bloat, and the new Kitesurf browser (announced simultaneously) delivers agent-first content without Chromium overhead. **Discoverable** covers both sides of search: AI Search helps agents find content, while Agent Engine Optimization (AEO) measures how visible a brand is to the models that matter. **Callable** introduces WebMCP, which lets sites expose actions directly to agents through a structured tool interface, eliminating the need for agents to parse HTML and guess at form fields. **Payable** is where Cloudflare makes its boldest bet: x402 micropayments and agent wallets let agents pay fractions of a cent per API call or content fetch, creating a sustainable model for publishers whose ad revenue disappears when no human sees the page.

The philosophical thread is that an open Agentic Internet — built on standards anyone can implement — is preferable to a closed one where a handful of platforms own discovery, identity, and payments. Cloudflare is explicit that it's building the rails, not owning the traffic. Whether the industry adopts these standards at scale remains the open question, but the vision is coherent and the tooling is shipping.