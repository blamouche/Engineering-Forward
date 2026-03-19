# claude-replay: Interactive HTML replays for AI coding sessions
**Source**: https://github.com/es617/claude-replay
**Date**: Unknown
**Author**: es617
**Keywords**: AI coding sessions, interactive replay, HTML export, Claude Code, Cursor, Codex CLI, session transcripts, self-contained

## Elevator pitch
A developer tool that transforms AI coding agent session logs into self-contained, interactive HTML replays for sharing and documentation—eliminating bulky screen recordings and unnavigable transcripts.

## Takeaways
- Zero-dependency output: Generated replays are single HTML files with embedded compressed data, requiring no external resources or frameworks.
- Multi-source compatibility: Automatically detects and converts session formats from Claude Code, Cursor, and Codex CLI into a unified playback experience.
- Integrated redaction system: Pattern-based secret scanning removes API keys, tokens, and credentials before export, protecting sensitive data in shared replays.
- Browser-native player: Vanilla JavaScript with built-in decompression enables smooth playback, keyboard controls, and speed adjustment without dependencies.
- Flexible customization: Supports custom themes via JSON, bookmarks for chapters, turn filtering, timing modes, and embedded iframe integration for blogs and documentation.

## Synthesis
Claude-replay addresses a practical pain point in AI-assisted development: sharing and documenting agent sessions effectively. Traditional approaches—screen recordings or raw transcript files—are either bulky or difficult to navigate. This tool reimagines session sharing as interactive, self-contained HTML files.

The architecture emphasizes simplicity and portability. The parser handles JSONL transcripts from three major sources (Claude Code, Cursor, Codex), normalizing their formats into a unified turn-based structure. A renderer compresses this data using deflate and base64 encoding, reducing output size by 60-70%, then injects it into a minified HTML template. The resulting file contains everything needed for playback: parser logic, player controls, themes, and compressed session data—no external requests or frameworks required.

The player interface mimics media controls familiar to users: play/pause, step navigation, progress bars, and adjustable speed (0.5x to 5x). Users can toggle thinking blocks and tool calls, navigate via keyboard shortcuts, and jump to bookmarked chapters. Multiple timing modes accommodate different sources—real timestamps for Claude Code sessions, synthetic paced timing for Cursor transcripts without timestamps.

Security considerations are built into the workflow. Automatic redaction scans for common secret patterns (API keys, tokens, connection strings, private keys, environment variables) and replaces them with [REDACTED] before writing to disk. This prevents accidental leaks when exporting sessions for public sharing, though the documentation appropriately notes this is a best-effort safety net rather than a guarantee.

Customization is extensive. Built-in themes include Tokyo Night, Monokai, Solarized, and others; users can create custom themes via JSON with color overrides and arbitrary CSS rules. The web-based editor provides visual session browsing, turn-by-turn editing, live preview, and export—running locally without exposing data externally.

The tool serves multiple use cases: embedding demos in blog posts via iframes, attaching reproducible replays to bug reports, creating teaching walkthroughs, and documenting debugging sessions. Technical polish includes minification, compression, Docker support, and zero production dependencies—the entire tool runs on Node.js 18+ with only esbuild as a dev dependency.

As a community tool unaffiliated with Anthropic, claude-replay demonstrates how open-source tooling can enhance proprietary platforms. By focusing on portability, accessibility, and user control, it transforms ephemeral agent sessions into shareable, durable artifacts suitable for collaboration, learning, and documentation.
