# He's Building the Plumbing for AI to Use the Internet
**Source**: https://every.to/podcast/he-s-building-the-plumbing-for-ai-to-use-the-internet
**Date**: October 1, 2025
**Author**: Rhea Purohit
**Keywords**: MCP, Stainless, Alex Rattray, APIs, SDKs, LLM tool use, model context protocol, AI plumbing, agent infrastructure

## Elevator pitch
Stainless founder Alex Rattray explains why making APIs legible to LLMs is the critical unsolved plumbing problem of the agentic internet, and shares design principles for building MCP servers that language models can actually use reliably.

## Takeaways
- MCP servers are to LLMs what websites are to humans: the native interface through which AI agents interact with software and services
- Building usable MCP servers is harder than building good SDKs because we don't yet understand how LLMs "think" about tool selection
- Rattray's design rules for MCP: keep tool counts small, use clear/precise names, minimize required parameters, and filter outputs to only relevant fields
- Stainless uses MCP internally to connect Notion, HubSpot, and databases, allowing natural language queries across business systems
- APIs are the invisible dendrites of the internet, and MCP is the new layer that makes those connections accessible to AI agents

## Synthesis
In this episode of AI & I, Alex Rattray, founder of Stainless, articulates a problem that sits at the foundation of the agentic internet: APIs are the hidden wiring that lets programs talk to each other, but they were designed for developers, not for language models. MCP (Model Context Protocol) is the attempt to build a native interface layer for LLMs — the equivalent of what websites are to humans. Just as a website presents buttons for humans to click, an MCP server presents a set of tools for an LLM to invoke. But making those tools usable by models is harder than it looks.

Rattray points out that humanity spent decades figuring out how to make good SDKs for human developers, and we still haven't cracked the equivalent for LLMs. The reason is simple: we understand how Python developers think, but we don't yet have the same intuition for how a language model approaches tool selection. Through trial and error, Stainless has arrived at several design principles: keep the number of available tools small to avoid overwhelming the model, give tools names and descriptions that are clear enough for the model to know when to use them, minimize the number of required parameters (a refund tool might only need customer name and order number, not a dozen fields), and filter outputs to return only what's relevant rather than dumping entire transaction histories.

The practical payoff is already visible inside Stainless itself. Rattray has built MCP servers for Notion, HubSpot, and internal databases, allowing him to ask natural language questions like "Which interesting customers signed up last week?" The system queries databases, cross-references HubSpot, pulls Notion notes, and delivers a summary — not perfectly yet, but the trajectory is clear. The episode serves as a window into why Anthropic would later acquire Stainless for $300M: the API-to-agent translation layer is becoming strategic infrastructure, and getting it right determines whether agents can actually do useful work.
