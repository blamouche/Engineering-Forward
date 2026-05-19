# Using Claude Code: The Unreasonable Effectiveness of HTML
**Source**: https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/
**Date**: May 8, 2026
**Author**: Simon Willison
**Keywords**: HTML, Claude Code, AI output, Markdown, prompt engineering, web tools

## Elevator pitch
Simon Willison, a longtime Markdown advocate, changes his mind about HTML as an AI output format after reading Thariq Shihipar's viral post, and demonstrates with a practical example using GPT-5.5 to create an interactive HTML explanation of a Linux security exploit.

## Takeaways
- Willison has been defaulting to Markdown since GPT-4's 8K token days, when Markdown's token efficiency was essential.
- Shihipar's post convinced him that for output (not input), HTML's interactive capabilities outweigh the token cost — SVG diagrams, collapsible sections, in-page navigation.
- He demonstrates the approach by having GPT-5.5 explain the copy.fail Linux security exploit in rich HTML, producing an interactive explainer page.
- Marks a shift from Willison's December 2025 HTML tools patterns (which focused on interactive utilities) to using HTML for ad-hoc explanations and research.
- Practical prompt engineering tip: ask the model to "use capabilities of HTML and CSS and JavaScript to make the explanation rich and interactive."

## Synthesis
Simon Willison, one of the most respected voices in the AI tools community and author of the popular `llm` CLI tool, publicly changed his stance on HTML vs. Markdown for AI output. For years, he had defaulted to requesting Markdown — a habit formed during the GPT-4 era when 8,192-token context windows made Markdown's efficiency a practical necessity.

Thariq Shihipar's "The Unreasonable Effectiveness of HTML" post caused Willison to reconsider. The key shift in his thinking: Markdown is still the right choice for input (prompts, system instructions, files the AI needs to parse), but HTML is far superior for output that a human will consume. HTML lets the model drop in SVG diagrams, interactive widgets, in-page navigation, and collapsible sections — features that make complex information more pleasant to navigate and understand.

To test the approach, Willison used his `llm` tool with GPT-5.5 to generate an interactive HTML explanation of a recently discovered Linux security exploit (copy.fail). His prompt asked the model to "explain this code in detail... output HTML, neatly styled and using capabilities of HTML and CSS and JavaScript to make the explanation rich and interactive." The result was an interactive page that expanded obfuscated Python, added annotations, and made the exploit mechanics navigable — far more effective than a wall of Markdown text.

This represents an evolution from Willison's previous work on HTML tools (his tools.simonwillison.net site of interactive utilities), broadening the pattern from purpose-built tools to general-purpose explanations. His endorsement carries weight: when one of Markdown's strongest advocates in the AI community changes his mind, it signals a genuine paradigm shift.
