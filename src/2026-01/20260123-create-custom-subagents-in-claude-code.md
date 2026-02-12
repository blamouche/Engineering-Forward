# Create Custom Subagents in Claude Code

**Source**: https://code.claude.com/docs/en/sub-agents

**Date**: Unknown

**Author**: Anthropic

**Keywords**: subagents, task delegation, context isolation, Claude Code, tool access control, permission modes, hooks, agentic workflows

## Elevator pitch

Anthropic's documentation explains how to create specialized AI subagents within Claude Code, enabling isolated context windows, custom permissions, and task-specific configurations for sophisticated agentic workflows.

## Takeaways

- Subagents are specialized AI assistants with isolated context windows, custom system prompts, and independent permissions
- Three built-in subagents exist: Explore (fast, read-only), Plan (research agent), and general-purpose (complex multi-step tasks)
- Configuration supports allowlist and denylist approaches for tool access control
- Subagents can run in foreground (blocking) or background (concurrent) execution modes
- Hook-based validation enables conditional rules for advanced security use cases

## Synthesis

Anthropic's Claude Code documentation provides comprehensive guidance on creating and managing specialized AI subagents, a feature that represents a significant step toward sophisticated agentic workflows. The system addresses fundamental challenges in AI-assisted development: context preservation, task specialization, and security enforcement.

Subagents function as independent AI assistants with their own context windows, system prompts, and tool permissions. This architecture solves the context window limitation problem by allowing developers to delegate specific tasks to focused agents without polluting the main conversation's context. Each subagent invocation starts fresh, though a resume capability allows continuing previous work with full history intact.

The configuration system offers multiple creation methods. Interactive setup through the `/agents` command provides guided creation for less technical users. Manual creation involves writing Markdown files with YAML frontmatter specifying parameters like name, description, available tools, and permission modes. CLI-based configuration enables programmatic agent definition, while the plugin ecosystem facilitates sharing subagent configurations across teams.

Tool access control represents a critical security feature. Developers can use an allowlist approach, explicitly specifying which tools a subagent can access, or a denylist approach that restricts specific tools while allowing others. Permission modes range from default interactive prompting to `bypassPermissions` for trusted automated workflows. Hook validation adds another security layer, enabling conditional rules that can inspect and reject specific operations before execution.

The documentation distinguishes between foreground and background execution modes. Foreground execution blocks the main conversation and handles permission requests interactively—suitable for complex tasks requiring user oversight. Background execution runs concurrently, inheriting parent permissions and auto-denying unknown requests, making it appropriate for parallel processing of routine tasks.

Built-in subagents demonstrate the system's design philosophy. The Explore agent prioritizes speed with read-only access for codebase navigation. The Plan agent focuses on research and architecture without write capabilities. The general-purpose agent handles complex multi-step tasks requiring full tool access.

The documentation provides practical examples including a Code Reviewer (read-only analysis), Debugger (analysis and fixes), Data Scientist (SQL/BigQuery specialized), and Database Query Validator (enforces read-only SQL through hooks). These templates illustrate how task-specific constraints improve reliability and security.

Context management features include auto-compaction at approximately 95% capacity and separate transcript storage from the main conversation. This isolation ensures subagent activities remain contained while still being accessible for review or continuation.

For organizations implementing agentic AI systems, the subagent architecture provides granular control without sacrificing capability. The emphasis on focused agents, detailed descriptions, and limited tool access reflects emerging best practices for production AI deployment.
