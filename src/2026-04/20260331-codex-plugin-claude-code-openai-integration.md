# Codex Plugin for Claude Code: OpenAI Codex Integration
**Source**: https://github.com/openai/codex-plugin-cc
**Date**: March 31, 2026
**Author**: OpenAI
**Keywords**: Codex, Claude Code, plugin, code review, adversarial review, slash commands, background jobs, AI coding

## Elevator pitch
OpenAI releases a plugin that integrates Codex directly into Claude Code via slash commands, enabling code review, adversarial critique, and background task delegation without leaving the Claude Code environment.

## Takeaways
- Five slash commands: /codex:review, /codex:adversarial-review, /codex:rescue, /codex:status, /codex:result, /codex:cancel
- Adversarial review goes beyond standard review to question design decisions and challenge assumptions
- /codex:rescue delegates bug investigation or fixes to Codex as background jobs
- Requires Node.js 18.18+ and ChatGPT subscription or OpenAI API key
- Respects existing Codex configurations; leverages local Codex CLI installation

## Synthesis
OpenAI releasing a Codex plugin for Claude Code is a notable strategic move: rather than treating Claude Code as a competitor to route users away from, OpenAI is building for Claude Code's plugin ecosystem. This acknowledges that Claude Code has achieved sufficient adoption to make it worthwhile for competitors to build integrations, and it positions Codex as a specialized capability that complements Claude rather than replacing it.

The adversarial review command is the most differentiated feature. Standard code review — checking for bugs, style issues, and obvious problems — is something Claude Code itself handles well. Adversarial review is different: it actively challenges design decisions, questions assumptions, and looks for structural weaknesses rather than implementation bugs. This mirrors the "red team" dynamic in software architecture review, where the most valuable feedback often comes from someone actively trying to find flaws rather than simply checking whether the code works.

The background job architecture for /codex:rescue reflects a practical workflow pattern. When an AI agent is delegated a debugging task, the developer shouldn't need to wait synchronously for it to complete. /codex:rescue submits the task, /codex:status polls for completion, and /codex:result retrieves the output. This async pattern is more appropriate for longer-running investigations than synchronous command execution.

The requirement for an existing local Codex CLI installation means the plugin inherits Codex's configuration — workspace settings, API credentials, permission profiles — without requiring separate setup. This reduces friction for developers already using Codex, making the Claude Code integration an additive capability rather than a replacement workflow.

For the AI coding tooling ecosystem, this plugin represents an emerging pattern of cross-provider integrations: rather than each AI coding tool being a closed ecosystem, specialized capabilities can be composed. Claude Code handles the primary development workflow; Codex contributes adversarial review and background task execution. The question is whether users will find value in managing multiple AI coding identities, or whether the cognitive overhead offsets the specialized capability gains.
