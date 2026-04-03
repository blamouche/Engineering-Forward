# Anthropic Accidentally Leaked Claude Code's Entire Source
**Source**: https://www.theunwindai.com/p/anthropic-accidentally-leaked-claude-code-s-entire-source
**Date**: April 1, 2026
**Author**: Shubham Saboo & Gargi Gupta
**Keywords**: Claude Code, source code leak, npm, source map, TypeScript, KAIROS, undercover mode, security

## Elevator pitch
Anthropic's entire Claude Code codebase — 512,000 lines of TypeScript — was accidentally exposed via a forgotten source map file in npm package version 2.1.88, revealing unreleased features including an autonomous daemon mode called KAIROS.

## Takeaways
- A 59.8 MB .map file in the @anthropic-ai/claude-code npm package exposed 512,000 lines of unobfuscated TypeScript
- Revealed "Undercover Mode" — a system designed to prevent accidental secret leaks during agent execution
- Fake tool interception redirects dangerous calls through safe dummy endpoints
- Sentiment detection adjusts agent verbosity based on user frustration signals
- KAIROS: an unreleased autonomous daemon mode with background memory consolidation and daily logging

## Synthesis
The accidental exposure of Claude Code's source via npm is a cautionary tale about the gap between deployment security and build pipeline hygiene. Source map files (.map) are standard developer tools that map compiled or minified JavaScript back to original source code for debugging purposes. They are not intended for production distribution, but automated build and publish pipelines can inadvertently include them if not explicitly excluded. In this case, the oversight resulted in Anthropic's entire 512,000-line TypeScript codebase becoming publicly accessible to anyone who inspected the npm package contents.

The technical revelations from the leaked code are substantive. "Undercover Mode" addresses a real problem: agents executing tasks in production environments can accidentally trigger security scanning systems or leak internal API keys through side channels. By intercepting potentially dangerous tool calls and routing them through safe dummy endpoints, the system adds a behavioral guardrail that operates below the prompt level.

Sentiment detection as a verbosity controller is an interesting design choice. Rather than using static configuration to determine how detailed Claude's responses should be, the system infers user state from interaction patterns — detecting frustration signals and adjusting output accordingly. This creates an adaptive interface that responds to inferred user context without requiring explicit commands.

KAIROS is the most significant unreleased capability revealed. An autonomous daemon mode that operates in the background — consolidating memory and maintaining daily logs without active user sessions — points toward a persistent AI assistant model that maintains continuity across sessions independently. This is architecturally distinct from session-based assistants and represents a meaningful step toward agents that accumulate context over time.

The broader security implication is supply chain risk. The Axios npm package compromise mentioned in the same news cycle, where a remote access trojan was inserted, illustrates the attack surface that npm dependency chains represent. For engineering teams, the Claude Code leak is a reminder to audit what gets included in published packages — not just for intentional inclusion, but for accidental artifacts from development toolchains.
