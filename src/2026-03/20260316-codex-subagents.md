# Use Subagents and Custom Agents in Codex
**Source**: https://simonwillison.net/2026/Mar/16/codex-subagents/
**Date**: 2026-03-16
**Author**: Simon Willison
**Keywords**: Codex, subagents, OpenAI, custom agents, TOML, gpt-5.3-codex-spark, agentic coding, multi-agent

## Elevator pitch
OpenAI's general availability of Codex subagents mirrors Claude Code's approach, allowing developers to create TOML-configured custom agents with specialized instructions and model selections—a pattern now standard across all major coding agent platforms.

## Takeaways
- Codex's default subagents include "explorer," "worker," and "default"—with "worker" optimized for many small parallel tasks
- Custom agents are TOML files stored in `~/.codex/agents/` supporting custom instructions and model selection including `gpt-5.3-codex-spark` for high speed
- Agents can be referenced by name to coordinate specialized tasks (e.g., debugger + code mapper working in parallel)
- Willison notes this pattern is now "widely supported": Claude Code, Gemini CLI, Mistral Vibe, VS Code, and Cursor all implement variants
- Willison added a dedicated subagents chapter to his Agentic Engineering Patterns guide in response

## Synthesis
Simon Willison's coverage of Codex subagents is as notable for what it reveals about the industry's convergence as for the Codex-specific details. The fact that he can observe "this pattern is widely supported in coding agents now" and list five separate implementations across competing platforms indicates that multi-agent coordination has moved from experimental feature to expected capability in coding AI tooling.

The mechanics of Codex's implementation are clean. Default subagents with preset optimizations—"worker" for high-frequency parallel tasks, "explorer" for investigation tasks—provide immediately useful specialization without configuration overhead. The TOML file format for custom agents is a pragmatic choice: structured enough to be machine-parseable and editor-friendly, simple enough that non-engineers can create and modify agent configurations without learning a new DSL.

The ability to select `gpt-5.3-codex-spark` for high-speed agents reflects an important design insight: not all sub-tasks in a complex workflow need the same capability level. A code mapper tracing call paths requires speed more than reasoning depth; a debugger formulating hypotheses requires the opposite. Custom agent configurations that pair the right model to the right subtask produce better cost-efficiency and overall workflow performance than using a single model for everything.

Willison's decision to add a dedicated subagents chapter to his Agentic Engineering Patterns guide signals that this capability has reached a maturity level where documentation and best practices are warranted. The practical example he gives—having a debugger reproduce issues while a code mapper traces problematic paths in parallel—illustrates how even simple multi-agent patterns can significantly accelerate workflows that would be sequential in a single-agent system.

The cross-platform convergence is the most strategically significant signal: when Claude Code, Gemini CLI, Mistral Vibe, VS Code, and Codex all implement essentially the same subagent pattern, it suggests the pattern reflects genuine user workflow requirements rather than platform-specific design choices.
