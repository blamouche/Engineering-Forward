# Agent SDK overview

**Source**: https://code.claude.com/docs/en/agent-sdk
**Date**: Unknown
**Author**: Anthropic
**Keywords**: Claude Agent SDK, agent tooling, built-in tools, hooks, subagents, sessions

## Elevator pitch
Anthropic’s Agent SDK turns Claude Code into a programmable agent runtime with built-in file, shell, web, hook, session, MCP, and subagent capabilities for production use.

## Takeaways
- The Agent SDK packages the same tool loop and context management that power Claude Code as a Python and TypeScript library.
- Developers get built-in tools for reading files, running commands, editing code, and fetching web content without implementing execution themselves.
- The platform supports hooks, MCP servers, and custom agents so teams can shape behavior and integrate external systems.
- Permissions and session controls are first-class, which matters for deploying agents safely in real workflows.
- The documentation positions the SDK as a higher-level alternative to raw API usage when teams want autonomous tool use out of the box.

## Synthesis
The main point of this documentation page is not a single feature but a product positioning move. Anthropic is reframing Claude Code from an interactive coding tool into a reusable runtime for agents. The Agent SDK packages the same loop, tools, and context handling as a library, which means teams can embed Claude-style autonomous behavior directly into Python or TypeScript systems instead of rebuilding orchestration from scratch. That lowers the barrier for shipping agents that can inspect files, run commands, search codebases, and use web resources with relatively little custom scaffolding.

The built-in tool layer is the most consequential part. In many agent stacks, the hard part is not model access but safe, reliable tool execution and state management. By bundling tools like read, write, edit, bash, grep, glob, web fetch, and web search, Anthropic is trying to standardize the default operating environment. That gives developers a much shorter path from prototype to useful agent because they no longer need to build an entire execution harness just to get basic autonomy.

The surrounding features show where the product is heading. Hooks let developers audit, block, or transform behavior at specific lifecycle events. Subagents create a structured way to delegate focused work. MCP support extends the runtime to external systems. Sessions preserve context across interactions. Permissions narrow what an agent can do. Taken together, that stack looks less like a chatbot SDK and more like an operating system for controlled agent workflows. The emphasis on governance is notable because it reflects where real adoption pressure now sits: enterprises want autonomy, but only inside inspectable and governable boundaries.

There is a useful strategic implication here for engineering teams. If you expect agents to become part of application workflows, then the winning platform will not just provide a model but a reliable execution environment with policy controls, integrations, and memory. This documentation signals that Anthropic understands that shift. The SDK is not only for coding assistants. It is a bid to become infrastructure for production agents more broadly, where tool access, permissions, and lifecycle control matter as much as raw model quality.
