# MCP is Not the Problem, It's your Server: Best Practices for Building MCP Servers

**Source**: https://www.philschmid.de/mcp-best-practices

**Date**: January 21, 2026

**Author**: Philipp Schmid

**Keywords**: MCP, Model Context Protocol, AI agents, server design, tool design, agent UX, API design

## Elevator pitch

The Model Context Protocol functions adequately, but developers fail by treating MCP as a REST API wrapper rather than recognizing it as a user interface for AI agents that requires product thinking rather than infrastructure development.

## Takeaways

- MCP servers should be designed as user interfaces for agents, not REST API wrappers, because agents operate under different constraints than human developers
- Design single high-level tools around agent goals rather than exposing granular composable endpoints, as multi-step tool calls increase error risk
- Limit servers to 5-15 focused tools because context windows create competition between tool descriptions and actual response content
- Use service-prefixed naming patterns like `slack_send_message` to prevent confusion when agents work with multiple MCP servers
- Return helpful strings and guidance through docstrings and error messages rather than throwing exceptions that agents cannot interpret

## Synthesis

Philipp Schmid addresses a common failure mode in Model Context Protocol implementations. The core thesis is that MCP itself functions adequately—the problems developers experience stem from applying REST API design principles to a fundamentally different context. MCP servers serve AI agents, not human developers, and this distinction requires reconsidering established API design patterns.

The design philosophy mismatch manifests in several ways. REST APIs prioritize composability, flexibility, and discoverability because human developers can explore endpoints, read documentation, and mentally compose sequences of calls. AI agents operate under different constraints. Discovery becomes expensive because schemas must be included in every request. Composability necessitates multi-step tool calls that increase error probability and token consumption. Flexibility expands the space of possible outputs, increasing hallucination risks.

Six best practices structure the guidance. First, design for outcomes over operations: provide a single `track_order(email)` tool rather than separate tools for user lookup, order retrieval, and shipment tracking. Second, flatten arguments by using primitives and constrained types rather than nested dictionaries that confuse agents. Third, treat instructions as context through docstrings and error messages that guide agent behavior rather than throwing exceptions. Fourth, curate ruthlessly by limiting servers to 5-15 focused tools, recognizing that tool descriptions compete with responses for context window space. Fifth, name for discovery using service-prefixed patterns like `slack_send_message` to distinguish tools across multiple servers. Sixth, implement pagination with metadata rather than returning hundreds of records that overwhelm context.

A practical example contrasts poor and better Gmail MCP design. The poor version requires agents to construct base64-encoded MIME messages and parse nested response structures. The better version provides simple flat tools like `gmail_search()` and `gmail_read()` with pre-formatted returns that agents can directly use.

The article clarifies the relationship between MCP and Skills. These approaches are complementary rather than competing. MCP provides structured interfaces with type validation. Skills teach agents when and how to combine tools for workflows. Neither is universally superior—context determines which to use. The underlying message is that building effective MCP servers requires product thinking focused on non-human users, treating the work as product design rather than infrastructure development.
