# How I AI: 8 Jev Use Cases, ChatGPT Sites at OpenAI, and Claire's DevDay Recap
**Source**: Lenny's Newsletter (lenny+how-i-ai@substack.com)
**Date**: 2026-10-05
**Author**: Lenny / John Lindquist / Kath Korevec / Claire
**Keywords**: Jev, decision engine, TypeSafe, John Lindquist, ChatGPT Sites, Kath Korevec, OpenAI DevDay 2026, Dots, Spaces, Decisions API, GPT-6.1 Sol, Astra Ultrafast, plugin insights, layered classification, efficient inefficiency, agent routing, temporary software, community skills, Lenny's Podcast Network

## Elevator pitch
Lenny's How I AI podcast network released three episodes: John Lindquist demonstrating 8 real Jev use cases (treating it as an if/else decision engine, not a chatbot, at 73 cents for 23 runs), Kath Korevec showing how OpenAI uses ChatGPT Sites internally for incident dashboards and automated music discovery with Plugin Insights personalization, and Claire's DevDay 2026 recap covering Dots, Spaces, Sites with bundled plugins, the Decisions API with vision, and Astra Ultrafast.

## Takeaways
**John Lindquist — 8 Jev Use Cases:**
- Jev outputs decisions instead of text — scores, classifications, probabilities, function calls — and that constraint is its defining feature
- The right mental model for Jev is an if/else statement, not prompt engineering: use it wherever a traditional program would contain a condition, switch, or branching decision
- Jev's speed and cost unlock a different class of applications: John spent 73 cents across 23 development runs; Claire processed 5 GB of JSON for 40 cents
- Routing is Jev's most immediately useful pattern: a single natural-language input identifies the right tool, infers the action, and triggers the function
- Layered classification (one classification fed into another) often works better than one perfect decision, and at Jev's cost, adding passes is cheap
- Chess benchmark: Jev analyzed a full game in under a second, 10x faster and 4x cheaper than a low-reasoning LLM without sacrificing accuracy
- "Efficient inefficiency" becomes viable: brute-force analysis (every chess move, every Wikipedia route) can be simpler and more effective than narrowing the search space when each decision is fast and cheap
- Jev works best when the action space is defined; creative reasoning, brainstorming, and image interpretation still belong to LLMs

**Kath Korevec — ChatGPT Sites at OpenAI:**
- Plugin Insights lets a site personalize itself for every visitor: an incident command site inferred team membership from Slack channel access and displayed only relevant incidents
- Codex can infer appropriate plugins from prompt context — mentioning Notion, calendars, or collaboration triggers the right connectors without explicit instruction
- Sites is infrastructure, not just hosting: includes D1 storage, R2 bucket, MCP plugin hosting, co-editor support — Kath's team used it for the DevDay keynote slides
- Software can be temporary and still worth building: Kath creates personalized sites for single business trips, uses them for a week, discards them
- Kath's automated music discovery: computer control finds Reddit playlists every Monday, creates a Spotify playlist, plays it — surfacing songs she'd never heard
- Skills let a community extend an application without codebase access: a dungeon-building skill lets anyone create themed rooms with Astra and add them to a shared game
- Faster models make builders more creative: slow generation breaks the creative thread; immediate results encourage continued experimentation
- Kath draws a clear boundary: AI can help prepare communication, but the send button remains hers

**Claire — DevDay 2026 Recap:**
- Dots are more capable than they look (shopped, wrote code, noticed a swim schedule conflict) but the relationship between Dot threads, ChatGPT conversations, and Codex remains confusing
- ChatGPT Spaces may be the most underrated DevDay announcement — shared workspace for humans and agents with proper permissions and data controls
- Sites with bundled plugins: enterprise answer to AI-generated internal tools — package connectors like Snowflake while preserving per-user data permissions
- GPT-6.1 Sol: $2/M input, $10/M output vs Astra's $10/M and $50/M — compelling workhorse for cost-conscious teams
- Decisions API with vision: Claire scanned 100 video frames and identified usable thumbnails in ~10 seconds — a previously tedious production task largely solved
- Astra Ultrafast: ~$97 for an interactive session with her kids, but real-time SVG sketchpad and 3D game showed what near-instant code generation feels like
- Platform primitives may matter more than demos: computer use in Agents API, Codex developer tools, plugin monetization, Pro 500 plan
- Claire is still using Grok Bots for daily work and not rushing to switch — prefers narrow agents for specific jobs over one agent for everything

## Synthesis
The three episodes together form a comprehensive picture of where agentic AI stands in October 2026. John Lindquist's Jev demos crystallize a paradigm shift that's been building since the model's launch: decision engines are not smaller LLMs, they're a different category of tool. The if/else mental model is the key insight — developers who stop treating Jev like a chatbot and start treating it like a conditional statement unlock use cases that were previously impractical. The economics are staggering: 73 cents for 23 runs, 40 cents for 5 GB of JSON processing. When decisions cost nearly nothing and return nearly instantly, brute-force approaches ("efficient inefficiency") become the rational strategy rather than the wasteful one. The chess benchmark — 10x faster, 4x cheaper, no accuracy loss — is the concrete proof.

Kath Korevec's ChatGPT Sites walkthrough reveals how far OpenAI has moved from a chatbot company to a platform company. Plugin Insights — where a site personalizes itself based on a user's channel access and data permissions — is the kind of feature that makes agent-built software feel native rather than bolted on. The observation that Sites is infrastructure (D1 storage, R2 buckets, MCP hosting) rather than a prototyping layer positions it as a competitor to traditional web infrastructure, not just a toy. The "temporary software" concept — building a tool for a one-week business trip and discarding it — represents a fundamental shift in the economics of software creation. When development overhead falls far enough, even seven-day-lifespan tools deliver value.

Claire's DevDay recap provides the strategic synthesis. The platform primitives (computer use, Codex tools, plugin monetization, Pro 500) are more significant than any single demo because they create the foundation developers build on over time. The Decisions API with vision — scanning 100 video frames for thumbnails in 10 seconds — shows how OpenAI is integrating Jev-like decision capabilities into its platform. But Claire's decision to stick with Grok Bots and narrow agents rather than consolidating on one mega-agent is the most telling signal: the market is fragmenting into specialized tools rather than consolidating on a single platform, and users who already have working systems are not rushing to switch.