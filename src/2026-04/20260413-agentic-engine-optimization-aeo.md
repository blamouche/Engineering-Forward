# Agentic Engine Optimization (AEO)

**Source**: https://addyosmani.com/blog/agentic-engine-optimization
**Date**: April 13, 2026
**Author**: Addy Osmani
**Keywords**: documentation, AI coding agents, developer tools, llms.txt, skills, MCP

## Elevator pitch
Addy Osmani argues that documentation now needs a second optimization layer for AI coding agents, where discoverability, parseability, and token efficiency determine whether agents can use a product correctly at all.

## Takeaways
- The article introduces Agentic Engine Optimization as an SEO-like discipline for AI agents that fetch and consume docs autonomously.
- It highlights that agent traffic often bypasses traditional client-side analytics, making current documentation funnels incomplete.
- Token budgets, raw Markdown access, and robots.txt settings are framed as operationally important documentation concerns.
- The piece recommends machine-readable indexes such as llms.txt and capability descriptors such as skill.md to help agents find and use the right material.
- Its broader point is that developer experience now includes optimizing for non-human consumers of technical content.

## Synthesis
Addy Osmani’s piece makes a simple but important point: AI coding agents do not experience documentation the way humans do, so teams that optimize only for human readers are increasingly shipping a broken developer experience. Instead of browsing, clicking, and gradually building context, agents typically fetch a page or two as raw text, strip the layout, and make hard decisions based on token cost and structural clarity. If the page is noisy, hidden behind JavaScript, or too long, the agent may ignore it or hallucinate around it.

The AEO framing is useful because it gives this shift a practical design vocabulary. Discoverability, parseability, token efficiency, capability signaling, and access control are all things platform teams can actually improve. That moves the discussion away from vague “AI readiness” talk and into concrete publishing mechanics: serve Markdown, expose raw docs, avoid bloated navigation chrome, maintain llms.txt, and make robots.txt rules intentional instead of accidental.

One of the sharper observations is that agents break existing analytics. If most of the interaction collapses into one or two server-side fetches, then time-on-page, scroll depth, and click funnels stop reflecting the real quality of the docs. That means teams may already be failing AI-driven integrations without seeing the failure in dashboards. In other words, the documentation product can be deteriorating for an important new class of users while appearing healthy by legacy metrics.

The article also implies that documentation is becoming part of an agent interface layer. Files like llms.txt and skill.md are not just nice-to-have metadata; they are emerging affordances that help agents discover both where relevant information lives and what a product can do. If this pattern sticks, developer docs will increasingly resemble an API surface for models as much as a learning resource for humans.
