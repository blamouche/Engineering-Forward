# Printing Press: Agent-Native CLIs from a Single Prompt
**Source**: https://printingpress.dev/
**Date**: 2026-06-09
**Author**: Matt Van Horn and Trevin Chow
**Keywords**: agent-cli, printing-press, api-wrapper, local-sqlite, mcp-server, token-efficiency

## Elevator pitch
Printing Press generates purpose-built Go CLIs with local SQLite mirrors, compound commands, and token-efficient output from any API spec, website URL, or service — all from a single prompt, producing agent-native CLIs, Claude Code skills, OpenClaw skills, and MCP servers simultaneously.

## Takeaways
- Point Printing Press at an API spec, website URL, or service with no public API, and it generates a Go CLI, a Claude Code skill, an OpenClaw skill, and an MCP server from one prompt
- For services without a public API, it launches a browser, captures traffic, reverse-engineers endpoints, and generates the spec automatically
- High-gravity resources get domain-specific SQLite tables with FTS5 full-text search and incremental sync — queries run in milliseconds offline
- 237+ community CLIs in the Public Library across 19 categories, from flight search to restaurant reservations to eBay auctions
- Token-efficient by default: --compact mode cuts 60-80% of tokens, auto-JSON when piped, typed exit codes for agent self-correction
- The CLI is built for agents first, humans second — install via Go, add the Claude Code or OpenClaw skills, and run /printing-press inside your agent

## Synthesis
Printing Press by Matt Van Horn and Trevin Chow introduces a fundamentally different approach to how AI agents interact with external services. Instead of agents making raw HTTP API calls — which are token-expensive, rate-limited, and require round-trips for every query — Printing Press generates purpose-built Go CLIs that cache data locally in SQLite and expose compound commands that return exactly what an agent needs in one call.

The concept is elegant: point Printing Press at an API spec, a website URL, or even a service with no public API. It generates a Go CLI, a Claude Code skill, an OpenClaw skill, and an MCP server — all from a single prompt. For services without a public API, it launches a browser, captures traffic, reverse-engineers the endpoints, and generates the spec automatically. If you can click through a service, Printing Press can build a CLI for it.

The local-first data layer is the key architectural innovation. High-gravity resources get domain-specific SQLite tables with FTS5 full-text search and incremental sync. Queries run in milliseconds offline, and agents never wait for 429 rate-limit responses. When you "print" an ESPN CLI, you don't get a thin REST wrapper — you get live scores, series state, leading scorers, and injury news in one call, all queried from a local database that syncs incrementally. The same pattern applies to Linear, Slack, Notion, or any of the 237+ CLIs in their Public Library.

The design is explicitly agent-first. The --compact mode cuts 60-80% of tokens. Auto-JSON activates when piped. Typed exit codes enable agent self-correction. The CLI is built for agents first, humans second, which inverts the typical API design philosophy where human readability is the primary concern.