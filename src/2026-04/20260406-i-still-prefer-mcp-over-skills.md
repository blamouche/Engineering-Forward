# I Still Prefer MCP Over Skills

**Source**: https://david.coffee/i-still-prefer-mcp-over-skills
**Date**: April 6, 2026
**Author**: David Caddy
**Keywords**: MCP, skills, connectors, CLIs, agent tooling, remote tools, protocols

## Elevator pitch
David Caddy argues that skills are excellent for procedural knowledge but poor as the default integration layer, and that MCP remains the better architecture for giving LLMs secure, portable access to services.

## Takeaways
- Skills work well for teaching workflows and tool usage but are awkward when they depend on dedicated CLIs.
- MCP offers better portability, remote usage, auth handling, and sandboxing for service integrations.
- CLI-based skills fragment ecosystems because they require installation, secrets handling, and environment-specific setup.
- Loading long skill documents can create unnecessary context bloat compared with exposing typed tools directly.
- The strongest pattern may be combining both: MCP for execution and skills as cheat sheets for tool-specific gotchas.

## Synthesis
This is one of the clearer arguments against treating skills as a universal integration standard. David Caddy is not saying skills are bad; he is saying they solve a different problem. Skills are a great way to teach an LLM how to behave, how to use existing local tools, or how to follow domain-specific conventions. They become much less elegant when they are used as a substitute for actual service interfaces.

That distinction matters because many “skills” are really just manuals for installing and driving a CLI. In a terminal-based environment that may be tolerable. In web clients, mobile clients, or hosted agent runtimes, it becomes brittle fast. MCP’s advantage is that it separates execution from instruction: the service exposes a connector, the client handles auth and discovery, and the model just calls tools. That is cleaner than shipping a markdown manual plus a per-service binary and hoping every environment can run it.

The essay also highlights a less glamorous but crucial issue: operational friction. Tokens in plain-text env files, broken installers, context bloat from SKILL.md, incompatible metadata between toolchains—these are all signs that the ecosystem is still duct-taped together. Protocols usually win over conventions when enough users care about portability and maintainability.

The most convincing conclusion is not MCP instead of skills, but MCP plus skills. Use connectors for execution and skills for explanation, caveats, and workflow guidance. That division of labor feels durable because it respects what each layer is actually good at.
