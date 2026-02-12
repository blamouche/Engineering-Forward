# MCP, Skills, and Agents

**Source**: https://cra.mr/mcp-skills-and-agents/

**Date**: January 20, 2026

**Author**: David Cramer

**Keywords**: MCP, skills, agents, tools, prompts, AI architecture, sub-agents

## Elevator pitch

A practical breakdown of MCP, skills, tools, and agents that cuts through the hype to explain when each approach actually makes sense.

## Takeaways

- Skills are reusable prompts with optional bundled artifacts that load content on-demand, minimizing context overhead
- Tools function as simple RPC calls exposed to agent grammar through JSON schema
- MCP is a protocol for exposing remote procedure calls as tools, particularly useful for network services and permissions management
- Agents and sub-agents operate as isolated contexts with their own model and tool configurations
- The "X is all you need" mentality causes confusion; each technology serves specific purposes

## Synthesis

David Cramer opens with a provocative statement—"RIP MCP. Long live skills!"—before quickly pivoting to address the widespread misconceptions surrounding these technologies in the AI development space. Rather than declaring any single approach superior, Cramer methodically defines each concept and explains its appropriate use case.

Skills emerge as lightweight, reusable prompts that can optionally bundle artifacts like scripts. Their key advantage lies in minimal context consumption: only metadata (name and description) is exposed initially, with full content loaded on demand. This makes them ideal for routine tasks and standardized workflows where the same prompt patterns recur frequently.

Tools take a different approach, functioning as straightforward RPC calls that integrate into agent grammar. While they consume slightly more context than skills due to JSON schema exposure, they provide direct functionality that agents can invoke programmatically. The distinction matters for developers optimizing context windows and token usage.

MCP (Model Context Protocol) occupies a specific niche as a protocol layer that exposes remote procedure calls as tools. Cramer notes that many MCP implementations suffer from poor design rather than fundamental protocol limitations. The protocol proves particularly valuable for network services where organizational benefits like permissions management, OAuth authentication, and context steering matter. It provides a standardized way to connect AI systems to external services without reinventing integration patterns.

Agents and sub-agents represent the highest level of abstraction, operating as encapsulated units with their own isolated contexts, model configurations, and tool access. This isolation enables complex multi-step workflows where different components can specialize in specific tasks without polluting each other's context.

Cramer dismisses commands as primarily a UX concern—they either represent skills or trigger sub-agents, but the underlying mechanism matters more than the surface-level interface.

The central argument challenges the tech community's tendency toward singular solutions. Rather than adopting whatever approach gains current attention, Cramer advocates for thoughtful evaluation of each technology's actual value proposition. Skills excel for routine tasks, tools provide direct functionality, MCP offers organizational and integration benefits, and agents enable complex orchestration. The practical path forward involves understanding these distinctions and selecting the right tool for each specific problem rather than forcing every use case into a single paradigm.
