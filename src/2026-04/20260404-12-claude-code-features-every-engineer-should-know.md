# EP209: 12 Claude Code Features Every Engineer Should Know

**Source**: https://blog.bytebytego.com/p/ep209-12-claude-code-features-every
**Date**: April 4, 2026
**Author**: ByteByteGo
**Keywords**: Claude Code, developer tools, CLAUDE.md, permissions, plan mode, checkpoints, hooks, MCP, subagents

## Elevator pitch
ByteByteGo offers a compact field guide to the parts of Claude Code that matter in practice, from project memory and permissions to checkpoints, hooks, MCP, and subagents.

## Takeaways
- CLAUDE.md acts as persistent project memory for rules, conventions, and context.
- Permissions and plan mode are governance tools as much as convenience features.
- Checkpoints reduce fear by making it easier to revert agent actions.
- Hooks, MCP, plugins, and slash commands turn the base coding agent into an extensible platform.
- Subagents and context management matter when work exceeds a single prompt-response loop.

## Synthesis
This ByteByteGo issue is not a deep essay, but it is a useful checklist of how coding-agent workflows are professionalizing. The 12 features it highlights show that Claude Code is no longer just a chat shell wrapped around a model. It is becoming a programmable environment with memory, permissions, orchestration, extensibility, and recovery mechanisms. That matters because the difference between a toy coding assistant and a dependable engineering tool increasingly lies in the scaffolding around model calls.

The most important items on the list are not glamorous. CLAUDE.md, permissions, plan mode, and checkpoints all address predictability and control. They let teams encode conventions, restrict risky behavior, review intent before action, and recover when things go wrong. Those capabilities are what make delegation usable in real repositories. They reduce the cost of trust. If an agent can remember local rules, operate within boundaries, and leave behind reversible changes, it becomes much easier to integrate into daily engineering work.

The rest of the list points to a platform model. Hooks let teams attach scripts to lifecycle events. MCP and plugins connect the agent to external tools and services. Slash commands package repeated workflows. Subagents distribute cognitive load across parallel workstreams. Each of these features turns the coding agent into something closer to an operating system for software tasks than a single assistant persona.

The practical takeaway is that coding-agent adoption is shifting from “which model is best?” to “which environment best supports disciplined delegation?” Teams that learn how to use memory files, permissions, recovery points, and extensibility will get more reliable leverage than teams that focus only on prompting tricks. That is the real story behind this feature roundup.
