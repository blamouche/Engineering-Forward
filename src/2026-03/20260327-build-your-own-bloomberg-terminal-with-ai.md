# Build Your Own Bloomberg Terminal With AI
**Source**: https://every.to/p/build-your-own-bloomberg-terminal-with-ai
**Date**: March 27, 2026
**Author**: Brooker Belcourt
**Keywords**: finance, analyst workflows, dashboards, Claude Code, automation

## Elevator pitch
A finance workflow playbook shows four escalating AI setups—from custom GPTs to Claude Code—that automate earnings previews and culminate in a personalized Bloomberg‑style dashboard.

## Takeaways
- Level 1: Custom GPTs can automate earnings previews but hit instruction limits and formatting constraints.
- Level 2: Claude Skills + data connectors (MCP) enable richer, reusable workflows with live financial data.
- Level 3: Claude Cowork adds local file access to leverage proprietary models and notes.
- Level 4: Claude Code orchestrates multi‑task pipelines into a unified custom dashboard.
- The trade‑off is complexity: higher levels require more setup but deliver deeper automation.

## Synthesis
Brooker Belcourt outlines a practical, four‑level ladder for financial analysts who want to automate earnings previews and build a personalized research workstation. The framing is simple: start with the easiest AI tooling and progress toward a full Bloomberg‑like dashboard as your needs and appetite for setup grow.

Level one uses a custom GPT in ChatGPT Projects. With detailed instructions and SEC filings uploaded, a single prompt can generate a reasonable earnings preview, complete with beat/miss analysis and citations. But the workflow is constrained by instruction limits, fixed formatting, and a chat‑only output. It works for single tasks, not end‑to‑end workflows.

Level two shifts to Claude Skills and data connectors. Skills let you split instructions into reusable prompt files—earnings templates, dashboard formatting, and investment philosophy—avoiding the character limit. Using MCP, the model can pull structured financial data (e.g., via Daloopa) rather than scraping the web. This enables richer dashboards with the analyst’s preferred metrics and layouts, but it still lacks access to proprietary internal data.

Level three introduces Claude Cowork, which runs locally and can read private files—Excel models, call notes, and historical analyses. This unlocks deeper analysis by comparing projections to consensus estimates, linking transcripts to model assumptions, and extracting nuanced deltas across internal datasets. The limitation is fragmentation: each task still generates a separate output rather than a unified workspace.

Level four is the most advanced: Claude Code orchestrates multiple tasks into a single, persistent dashboard. A single command runs a full workflow—previews, reviews, meeting prep, news scans—and assembles everything into a custom website. This compresses weeks of quarterly research work into a background process plus human review, approximating what large firms build with dedicated engineering teams.

The piece emphasizes that value exists at every level. Not every team needs a custom terminal, but even basic automation can save dozens of hours per quarter. The core idea is to match tooling complexity to workflow demands: start simple, and only climb the ladder when your needs outgrow the previous tier.
