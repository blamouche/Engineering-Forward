# Google Adds llms.txt Check to Chrome Lighthouse
**Source**: https://searchengineland.com/google-llms-txt-chrome-lighthouse-478246
**Date**: 2026-05-20
**Author**: Danny Goodwin
**Keywords**: Google, Lighthouse, llms.txt, AI agents, LLM, web standards, agentic browsing, Chrome

## Elevator pitch
Google has integrated an llms.txt audit into Chrome Lighthouse's new "Agentic browsing" category, signaling that the emerging llms.txt convention — a machine-readable site summary for LLMs and AI agents — is becoming a first-class web standard alongside traditional SEO and performance audits.

## Takeaways
- Lighthouse now audits for llms.txt presence, flagging server errors but treating 404 (file absent) as Not Applicable since providing the file is currently optional
- llms.txt is an emerging convention (llmstxt.org) that provides a concise Markdown summary of a website's purpose and key links for AI agents
- The audit is part of Lighthouse's new "Agentic browsing" category, which also includes WebMCP integration, accessibility for agents, and layout stability
- Google's Chrome and Search teams appear to have different guidance on llms.txt, with Search focusing on visibility and Chrome focusing on agentic browser readiness
- This represents a significant step in formalizing how websites communicate with AI agents rather than just human visitors and traditional search crawlers

## Synthesis
Google's addition of an llms.txt audit to Chrome Lighthouse marks an inflection point for how the web serves non-human visitors. The llms.txt file — a simple Markdown file placed at a website's root — provides AI agents and LLMs with a structured summary of what a site contains and its key links, reducing the need for agents to crawl entire sites to understand their structure.

This is part of a broader "Agentic browsing" category in Lighthouse that includes WebMCP (Model Context Protocol for the web), accessibility considerations for agents, and layout stability. The implication is clear: Google sees a future where a significant portion of web traffic comes from AI agents rather than human browsers, and websites need to be optimized for both audiences.

The timing is notable alongside Google's broader push into agent infrastructure — including Agent Executor and Agent Substrate announced the same week. The Chrome team's approach (optional, agent-focused) differs from the Search team's (stronger recommendation for visibility), reflecting an internal tension between treating llms.txt as a ranking signal versus a practical agent utility.

For web developers and SEO professionals, the message is that the old paradigm of optimizing for Googlebot and human visitors is expanding to include optimizing for AI agents. The llms.txt file represents the simplest entry point into this new discipline — a convention simple enough (plain Markdown, human-readable) that adoption should be frictionless, yet powerful enough to meaningfully improve how AI systems interact with websites.
