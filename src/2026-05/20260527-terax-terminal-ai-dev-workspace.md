# Terax: Lightweight Terminal-first AI-native dev workspace
**Source**: https://github.com/crynta/terax-ai
**Date**: May 27, 2026
**Author**: crynta
**Keywords**: terminal, AI, IDE, Tauri, Rust, React, local LLM, agentic workflow, open source, development environment

## Elevator pitch
Terax is a 7MB open-source terminal-first AI development environment built on Tauri 2 + Rust and React 19, combining a WebGL terminal, agentic AI side-panel with local model support, code editor, file explorer, git graph, and web preview — with no telemetry or account required.

## Takeaways
- Extremely lightweight: ~7-8 MB on disk, built with Tauri 2 (Rust) and React 19, supporting macOS, Linux, and Windows.
- Full agentic AI workflow: plans, sub-agents, project memory (TERAX.md), file operations, bash with approval gating, background processes, and plan mode.
- BYOK providers (OpenAI, Anthropic, Google, Groq, xAI, Cerebras, OpenRouter, DeepSeek, Mistral, custom) plus local models via LM Studio, MLX, and Ollama.
- Comprehensive developer tooling: xterm.js terminal with WebGL, CodeMirror 6 editor with Vim mode, source control with commit graph, and auto-detecting web preview.
- Privacy-first: API keys stored in OS keychain (never on disk), no telemetry, no account — open source under Apache 2.0.

## Synthesis
Terax represents a notable entry in the rapidly evolving "AI-native IDE" category, competing with tools like Cursor and Windsurf but from a fundamentally different design philosophy. At ~7MB, it's astonishingly lightweight — built on Tauri 2 (Rust backend) with a React 19 frontend — contrasting with Electron-based alternatives that routinely consume hundreds of megabytes.

The AI integration is comprehensive and vendor-neutral. Users can bring their own API keys for every major provider (OpenAI, Anthropic, Google, Groq, xAI, Cerebras, OpenRouter, DeepSeek, Mistral) or run fully local models via LM Studio, MLX, or Ollama. The agentic workflow includes plans, sub-agents, project memory via TERAX.md files (similar to Cursor rules or Claude's CLAUDE.md), file operations, bash execution with approval gating, and background process management. A composer interface supports snippets, file attachments, slash commands, and voice input.

The development tooling stack is thoughtfully assembled: xterm.js with WebGL rendering for the terminal (multi-tab with background streaming), CodeMirror 6 for the editor with Vim mode and inline AI autocomplete showing diffs that can be accepted/rejected hunk by hunk, source control with a real git commit graph (lane rendering for merges and branches), and a web preview that auto-detects local dev servers. Custom themes, background images, and Catppuccin icon themes round out the UX.

Privacy is a core differentiator: API keys are stored only in the OS keychain via keyring (never on disk), there's no telemetry, and no account is required. This local-first, privacy-respecting approach — combined with the extreme lightweight footprint and agentic capabilities — positions Terax as an intriguing alternative for developers who want AI assistance without vendor lock-in or cloud dependency.
