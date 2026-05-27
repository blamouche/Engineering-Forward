# Rowboat: Open-source AI coworker with memory
**Source**: https://github.com/rowboatlabs/rowboat
**Date**: May 27, 2026
**Author**: Rowboat Labs (YC-backed)
**Keywords**: AI coworker, knowledge graph, memory, local-first, open source, productivity, Gmail, calendar, Markdown, MCP, Obsidian

## Elevator pitch
Rowboat is a YC-backed open-source AI coworker that builds a persistent knowledge graph from your email and meetings, lives entirely on your machine as plain Markdown, and helps you prep for meetings, draft emails, build decks, and track topics — with memory that compounds rather than retrieval that starts cold.

## Takeaways
- Local-first design: all data stored as plain Markdown in an Obsidian-compatible vault with backlinks — fully inspectable, editable, and portable.
- Builds persistent knowledge from Gmail, Google Calendar, and meeting notes (Fireflies or built-in), maintaining long-lived context that accumulates over time.
- Practical capabilities: meeting prep from past decisions, email drafting grounded in history, PDF deck generation, follow-up tracking, and voice memo capture.
- "Live notes" feature: automatically updated notes that track competitors, market topics, people, projects, or deals — with content written back to your local vault.
- Extensible via MCP (Model Context Protocol): connects to search, databases, CRMs, and automations. BYOK for models — local via Ollama/LM Studio or hosted APIs.

## Synthesis
Rowboat, developed by YC-backed Rowboat Labs, approaches the AI assistant problem from a fundamentally different angle than most tools. Rather than focusing on real-time assistance or code generation, it builds what amounts to an external, persistent working memory — a knowledge graph that accumulates context from your actual work activity (email, calendar, meetings) over time.

The key architectural insight is that most AI tools "reconstruct context on demand by searching transcripts or documents" — meaning every interaction starts cold. Rowboat instead maintains long-lived knowledge where "relationships are explicit and inspectable." Everything lives on your machine as plain Markdown in an Obsidian-compatible vault, meaning you can inspect, edit, back up, or delete everything at any time. This transparency eliminates the black-box problem that plagues many AI assistants.

Practical use cases span the knowledge worker's daily workflow: meeting preparation that pulls past decisions and open questions into a brief or voice note, email drafting grounded in actual commitments and history, PDF deck generation using accumulated context, and follow-up tracking that captures decisions and action items. The "live notes" feature is particularly interesting — you can create auto-updating notes by typing '@rowboat' on any note, setting up persistent monitoring of competitors, topics, people, or deals across web sources and your communications.

Rowboat supports both local models (Ollama, LM Studio) and hosted APIs, is extensible via MCP for connecting to external tools, and works on Mac, Windows, and Linux. With 14.6k GitHub stars and active community, it represents a compelling vision of what a truly personal, privacy-respecting AI assistant could look like — one where memory is a first-class primitive, not an afterthought.
