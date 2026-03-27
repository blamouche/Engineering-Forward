# Control Claude Code from your Phone using Telegram
**Source**: https://www.theunwindai.com/p/control-claude-code-from-your-phone-using-telegram
**Date**: Unknown
**Author**: Unwind AI
**Keywords**: Claude Code, Telegram, MCP, channels, agent workflows

## Elevator pitch
Unwind AI details Claude Code Channels, a new MCP‑based bridge that lets you control a running Claude Code session from Telegram or Discord with two‑way messaging and access controls.

## Takeaways
- Claude Code Channels lets users send instructions from Telegram/Discord into an active local Claude Code session.
- The bridge is built on MCP and supports two‑way messaging, reactions, and message edits.
- Setup relies on bot tokens and a pairing flow with an allowlist for access control.
- The newsletter contextualizes Channels alongside Open SWE and other agent tooling releases.
- It frames the feature as a practical way to operate coding agents from a phone.

## Synthesis
This Unwind AI issue centers on the release of Claude Code Channels, a feature that turns chat apps into remote control surfaces for a running Claude Code session. The core idea is a two‑way MCP bridge: a user sends a message in Telegram or Discord, the MCP server injects that message into the active Claude Code session, and Claude replies back in the same chat. This effectively lets a developer steer their local agent from a phone without being at the terminal.

The article highlights several technical characteristics of the Channels system. It is currently in research preview and requires a recent Claude Code version. Official plugins for Telegram and Discord are available, and the plugin architecture is open for community‑built connectors to other platforms. Unlike notification‑only integrations, Channels supports bi‑directional interaction—Claude can reply, react with emojis, edit messages, and on Discord even fetch channel history and attachments. This design is meant to preserve the richness of collaboration tools rather than reduce them to a one‑way alert stream.

Setup is framed as lightweight but secure. Users create a bot via BotFather (Telegram) or the Discord Developer Portal, install the plugin, configure the token, and launch Claude Code with the channels flag. Pairing involves a code exchange, and each plugin maintains an allowlist of approved sender IDs so that only authorized users can push messages into the active session. Unapproved senders are dropped silently, emphasizing a “default deny” posture for remote access.

The broader context in the newsletter is a roundup of recent agent‑related developments, including LangChain’s Open SWE framework and techniques for improving Claude skills through iterative evaluation loops. But the Channels item stands out for its operational impact: it turns a running agent into something you can direct asynchronously from anywhere. The article suggests that this is especially useful for long‑running tasks—developers can check in, send updates, or unblock an agent without needing to open a laptop.

Overall, the piece presents Channels as a practical step toward agent‑native workflows: less time tethered to a terminal, more ability to orchestrate tasks through familiar chat platforms. The combination of MCP interoperability, real‑time two‑way messaging, and explicit access control makes it a credible pattern for remote agent control rather than a simple notification integration.
