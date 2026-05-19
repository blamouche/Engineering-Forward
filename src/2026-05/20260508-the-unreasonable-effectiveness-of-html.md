# The Unreasonable Effectiveness of HTML
**Source**: https://thariqs.github.io/html-effectiveness/
**Date**: May 8, 2026
**Author**: Thariq Shihipar (Anthropic, Claude Code team)
**Keywords**: HTML, Markdown, AI agents, Claude Code, agent output format, SVG, interactive documents

## Elevator pitch
Thariq Shihipar argues that AI agents should produce single-file HTML instead of Markdown, demonstrating 20 compelling examples across exploration, code review, design, prototyping, research, and custom editing interfaces that make documents interactive and visually rich.

## Takeaways
- Markdown was the right choice when context windows were small (GPT-4's 8,192 tokens); now that windows are large enough, HTML's rich capabilities outweigh token efficiency.
- HTML enables capabilities Markdown simply can't: styled tables, collapsible sections, embedded SVG diagrams, inline charts, light JavaScript, and interactive widgets.
- The article provides 20 concrete examples grouped by use case: exploration/planning, code review, design systems, prototyping, diagrams, slide decks, research explainers, reports, and custom editing interfaces.
- Key insight: HTML trades a document you'd skim for one you'd actually read — interactive code reviews with margin annotations, animated prototypes, drag-and-drop triage boards.
- Each example is a self-contained .html file, demonstrating that agents can produce fully functional output with no build step.
- Custom editing interfaces close the loop: drag tickets, tune prompts, or toggle feature flags in a throwaway UI, then export back to markdown for the agent.

## Synthesis
Thariq Shihipar, a member of the Claude Code team at Anthropic, published what became one of the most influential AI engineering posts of 2026. "The Unreasonable Effectiveness of HTML" argues that the era of Markdown as the default output format for AI agents is ending, replaced by single-file HTML documents that can include SVG diagrams, collapsible sections, embedded charts, and lightweight JavaScript.

The post's companion website showcases 20 self-contained HTML files across nine categories. For exploration and planning, agents can produce side-by-side comparisons of code approaches or implementation plans with timelines and data-flow diagrams. For code review, they generate annotated diffs with margin notes and severity tags. For design, they render living design systems with color swatches and component variant sheets. For prototypes, they create animation sandboxes and clickable flows. The list extends to SVG illustrations, arrow-key slide decks, research explainers with tabbed code samples, and custom editing interfaces where users can drag tickets through a triage board and export the result as markdown.

The argument hinges on a fundamental shift in who consumes agent output. When context windows were small (GPT-4's 8,192 tokens), Markdown's token efficiency was essential. Now that windows can hold full HTML documents, the question becomes: is a human going to edit this file? If yes, Markdown is still more legible in raw form. If no — if the output is consumed once and discarded, or if it benefits from visual structure — HTML produces dramatically better results.

The post went viral (4.4 million views in 16 hours), earning endorsements from Andrej Karpathy and prompting Simon Willison, a longtime Markdown advocate, to change his mind. The implication for AI tooling is significant: as agents become the primary producers of documentation, our tools (Slack, GitHub, Google Docs) will need to adapt to handle HTML as a first-class format rather than treating it as an attachment to download.
