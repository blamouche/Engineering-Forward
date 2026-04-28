# Building agents that reach production systems with MCP | Claude
**Source**: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
**Date**: Unknown
**Author**: Unknown
**Keywords**: building, agents, reach, production, systems

## Elevator pitch
Meet Claude Products Claude Claude Code Claude Cowork Features Claude for Chrome Claude for Slack Claude for Excel Claude for PowerPoint Claude for Word Skills Models Opus Sonnet Haiku

## Takeaways
- Meet Claude Products Claude Claude Code Claude Cowork Features Claude for Chrome Claude for Slack Claude for Excel Claude for PowerPoint Claude for Word…
- Solutions Use cases AI agents Coding Departments Security Industries Customer support Education Financial services Government Healthcare Life sciences Nonprofits
- Resources Insights Blog Customer stories Anthropic news Learn Anthropic Academy Courses Tutorials Use cases Tools Connectors Plugins Connect Events Community
- Share Copy link https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
- Agents are only as useful as the systems they can reach.

## Synthesis
Meet Claude Products Claude Claude Code Claude Cowork Features Claude for Chrome Claude for Slack Claude for Excel Claude for PowerPoint Claude for Word Skills Models Opus Sonnet Haiku

Solutions Use cases AI agents Coding Departments Security Industries Customer support Education Financial services Government Healthcare Life sciences Nonprofits

Resources Insights Blog Customer stories Anthropic news Learn Anthropic Academy Courses Tutorials Use cases Tools Connectors Plugins Connect Events Community

Share Copy link https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp

Agents are only as useful as the systems they can reach. Teams tend to converge on three approaches for connecting them to external systems—direct API calls, CLIs, and MCP. This post lays out where each fits, why production agents tend to land on MCP, and the patterns for building those integrations effectively.

We generally see three paths for connecting agents to external systems: direct API calls, CLIs, and MCP. Each makes sense somewhere, depending on what you're building. The key distinction is whether there's a common layer between agents and services, and how far that layer reaches.

The agent calls your API directly—either by writing code that issues HTTP requests inside a code-execution sandbox, or through a generic function-calling tool. This is where most teams start, and it works fine for one agent talking to one service, or a small number of integrations that don't need to be reused across agent platforms. The challenges start to hit at scale. With no common layer between agents and services, each agent–service pair becomes a bespoke integration with its own auth handling, tool descriptions, and edge cases—the M×N integration problem.

The agent runs your command-line tool in a shell. This is fast, lightweight, and leans on pre-existing tooling. It works great for local environments and sandboxed containers—anywhere there's a filesystem and a shell. This provides a common layer, but it’s thin. CLIs hit hard limits reaching mobile, web, or cloud-hosted platforms that don't expose a container, and auth is handled by the CLI's own mechanism—usually a credential file on disk. This is best suited to quick, permissive integrations in local environments.
