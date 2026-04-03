# Awesome LLM Apps: A Collection of RAG, AI Agents, Multi-agent Teams, MCP, and Voice Agents
**Source**: https://github.com/Shubhamsaboo/awesome-llm-apps
**Date**: Unknown
**Author**: Shubhamsaboo
**Keywords**: LLM apps, RAG, AI agents, multi-agent, MCP, voice agents, open-source, examples

## Elevator pitch
A curated open-source collection of practical LLM applications covering RAG, AI agents, multi-agent teams, MCP integrations, and voice agents built with models from OpenAI, Anthropic, Google, xAI, and open-source alternatives.

## Takeaways
- Organizes projects across starter agents, advanced agents, multi-agent teams, voice AI agents, MCP agents, RAG tutorials, and optimization guides
- Covers models from OpenAI, Anthropic, Google, xAI, and open-source alternatives like Llama and Qwen
- Includes practical domains: travel, data analysis, music generation, web scraping, research, consulting, financial coaching
- Provides framework crash courses for Google ADK and OpenAI SDKs
- 963+ commits; emphasizes educational value with well-documented projects

## Synthesis
The Awesome LLM Apps repository occupies a specific and valuable niche in the AI development ecosystem: it is a curated collection of working, documented examples rather than a framework or library. Where most repositories ask developers to adopt new patterns or dependencies, this one demonstrates what is already possible with existing tools across a wide range of application domains.

The categorization is deliberately layered. Starter agents provide low-complexity entry points for developers new to LLM application development — travel planning and data analysis agents are concrete enough to be useful while simple enough to understand. Advanced agents in domains like fraud investigation and financial coaching demonstrate how the same patterns scale to production-relevant use cases. Multi-agent teams showing sales intelligence, legal services, and recruitment pipelines address the next step: systems where multiple specialized agents collaborate rather than a single agent handling everything.

The inclusion of MCP (Model Context Protocol) agents is timely. As MCP has emerged as a standard protocol for AI models to interact with external tools and data sources, having documented examples of MCP integration with GitHub, Notion, and browser automation provides practical reference material that is difficult to find elsewhere.

Voice AI agents represent a distinct capability set — the latency, streaming, and speech processing requirements differ substantially from text-based agents. Including them alongside text-based examples in a single collection allows developers to compare architectural patterns across modalities.

The framework crash courses for Google ADK and OpenAI SDKs address a common friction point: new frameworks often lack sufficient examples to make getting started tractable. Including guided courses within an application collection creates a pathway from "learning the framework" to "building something real" within a single resource.

For engineering teams evaluating what to build, the collection functions as a map of the current state of practical LLM applications — useful both for identifying what has already been built and for finding implementation patterns to adapt.
