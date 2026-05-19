# How I AI: Thariq Shihipar on Replacing Markdown with HTML for AI-Powered Development

**Source:** [ChatPRD / How I AI](https://www.chatprd.ai/how-i-ai/claude-code-anthropic-thariq-shihipar-on-replacing-markdown-with-html)
**Date:** 2026-05-18
**Author:** Claire Vo
**Guest:** Thariq Shihipar, engineer on the Claude Code team at Anthropic

## Summary

Thariq Shihipar (Claude Code, Anthropic) makes the case that "HTML is the new markdown." While Markdown was the lingua franca for LLM interaction, it hits limits when plans grow to thousands of lines — humans stop reading. HTML enables richer, interactive, visual communication that keeps humans engaged as collaborators rather than passive reviewers.

## Key Workflows

### 1. Brainstorming and Planning with Interactive HTML
Instead of asking Claude for a text list, ask for an HTML file. Thariq's prompt: "Can you brainstorm some ideas in HTML file?" → produces visual, scrollable pages with mockups, descriptions, and risk assessments. Follow-up: "Create an HTML file as a plan that helps me visualize what the implementation plan is. Include excerpts, mockups, code, whatever is needed to give me maximum context."

### 2. Building Micro-Apps to Edit Plans
When an HTML plan contains complex sections (e.g. decision rules tables) that are tedious to edit, ask Claude to build a temporary custom UI just for editing that section. Prompt: "Make this a custom UI that helps me with structure but gives me flexibility. Design the ideal interface for this problem." Use the throwaway app, then copy the output back.

### 3. Living Design System in HTML
Point Claude at project folders/GitHub repos to extract the design system (CSS, components, styling). Generate a `design_system.html` file that visually displays color palette, typography, spacing, and interactive component examples. This becomes a portable source of truth — provide it as context for any new feature to ensure on-brand output.

## Key Insight: "Compute Allocator"

"Only about 1% of the tokens I generate end up in production code. The other 99% are spent on rich scaffolding: plans, custom interfaces, status updates, design systems." Engineers are becoming compute allocators — investing in alignment and communication to ensure the 1% that ships is exactly right.

## Why It Matters

- **Human engagement:** HTML plans are actually readable and explorable vs. giant Markdown files you skim or ignore
- **Richer communication:** Interactive elements, visual mockups, better information density
- **Better prompts:** Give Claude direction but leave room: "whatever is needed" signals trust and produces better results
- **Abundance mindset:** When tokens are cheap, make every interface you interact with beautiful and tailored
