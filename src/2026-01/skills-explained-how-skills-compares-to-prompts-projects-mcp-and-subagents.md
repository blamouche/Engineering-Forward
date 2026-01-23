# Skills Explained: How Skills Compares to Prompts, Projects, MCP, and Subagents

**Source**: https://claude.com/blog/skills-explained

**Date**: November 13, 2025 (Modified: January 6, 2026)

**Author**: Unknown

**Keywords**: AI agents, agentic workflows, Claude ecosystem, context management, task automation, Model Context Protocol, tool orchestration, enterprise AI

## Elevator pitch

Anthropic explains how Claude's five interconnected tools—Skills, Prompts, Projects, MCP, and Subagents—work together to create sophisticated agentic workflows for enterprise and personal use.

## Takeaways

- Skills are specialized instruction folders that Claude dynamically loads using progressive disclosure when relevant to a task
- Projects provide persistent 200K context windows for uploading documents and maintaining knowledge bases across conversations
- Subagents are independent AI assistants with their own context windows, useful for parallel processing and task specialization
- MCP (Model Context Protocol) connects Claude to external systems like databases and business tools for data access
- Combining these tools creates sophisticated workflows where each component handles its optimal function

## Synthesis

Anthropic's documentation provides a comprehensive breakdown of Claude's agentic architecture, distinguishing between five complementary tools that serve different purposes in AI-assisted workflows. Understanding these distinctions is essential for organizations and individuals seeking to implement effective AI augmentation strategies.

Skills represent Claude's approach to reusable procedural knowledge. Unlike simple prompts, Skills are organized folders containing instructions and resources that Claude dynamically loads when relevant to a conversation. The system employs progressive disclosure—loading metadata first, then full instructions only when needed. This architecture makes Skills ideal for encoding organizational workflows, domain expertise, and personal preferences that repeat across multiple interactions. The design reflects a broader industry trend toward persistent AI customization that survives beyond individual conversations.

Prompts occupy the simplest position in the hierarchy. They are natural language instructions provided during conversations, ephemeral by nature and suited for one-off requests or conversational refinement. While prompts remain the most accessible entry point for AI interaction, their transient nature limits their utility for complex, repeatable workflows.

Projects introduce persistence to the equation. With 200K context windows for uploading documents and setting custom instructions, Projects maintain knowledge bases accessible across all chats within that project. This makes them particularly valuable for initiatives requiring consistent background context—research projects, client accounts, or ongoing development efforts. The architecture acknowledges that effective AI assistance often requires substantial domain-specific knowledge that would be impractical to re-establish in every conversation.

Subagents represent Claude's approach to task decomposition and parallel processing. These specialized AI assistants operate with independent context windows, custom prompts, and specific tool permissions. By delegating discrete tasks to subagents, users can manage complexity without overwhelming a single conversation's context. This mirrors established software engineering patterns for managing complex systems through modularity.

MCP (Model Context Protocol) addresses the integration challenge. As an open standard for connecting Claude to external systems—databases, business tools, content repositories—MCP enables data access rather than teaching procedures. This distinction is crucial: while Skills encode how to do things, MCP provides access to what Claude needs to know.

The documentation emphasizes that these tools achieve their full potential in combination. A research workflow might use Projects for background context, MCP for data connectivity, Skills for analytical frameworks, and subagents for specialized execution. This layered approach reflects the complexity of real-world knowledge work and positions Claude as an orchestration layer for sophisticated agentic systems.
