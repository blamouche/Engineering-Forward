# mb · mini-browser — An Agent-First Browser CLI
**Source**: https://github.com/runablehq/mini-browser
**Date**: April 2026 (based on repository activity)
**Author**: Runable (runablehq)
**Keywords**: agent-tools, browser-automation, cli, puppeteer, chrome-devtools-protocol, AI-agents

## Elevator pitch
mini-browser is a Unix-style CLI that turns Chrome into a composable tool for AI agents, letting them navigate, observe, interact with, and record web pages through simple pipable commands.

## Takeaways
- Each command is a small, single-purpose Unix tool reading args and writing stdout, composable with pipes and `&&` — fitting naturally into agent workflows
- Installs as an agent skill via `npx skills add` or globally via npm, with no-code online access at runable.com
- Covers navigation (go, back, forward), observation (text, snap, shot), interaction (click, type, fill, scroll, drag, key), recording, tab management, JS execution, and design audits
- `snap` uses the Accessibility Tree to return interactive elements with roles, coordinates, and state flags, making it ideal for agents to discover clickable elements
- Ships with Chrome lifecycle management scripts (`mb-start-chrome`, `mb-restart-chrome`) that auto-detect browser binaries and use fresh profiles

## Synthesis
mini-browser addresses a concrete gap in the agent ecosystem: how do you give an LLM-powered agent reliable, programmatic control over a web browser without building fragile Selenium scripts or wrestling with complex Playwright setups? The answer is refreshingly Unix-philosophical — a collection of small, focused CLI tools that do one thing well.

The project is built by Runable, a company that also provides a browser-based agent playground. The CLI wraps Chrome's DevTools Protocol and exposes it through commands like `mb go`, `mb snap`, `mb click`, and `mb fill`. What makes this particularly elegant for agent use is the `snap` command, which uses the Accessibility Tree rather than DOM scraping to return a clean list of interactive elements with their roles (button, textbox, link), accessible names, center coordinates, and state flags (disabled, checked, expanded). This structured output is machine-readable and ideal for agent decision loops.

The tool also supports recording via Chrome's screencast API, tab management with stable CDP targetIds, JavaScript evaluation with stdin piping, and design audits covering colors, fonts, contrast, accessibility, and SEO metadata — all in a single pass. The JSON output mode on several commands makes integration with agent reasoning pipelines straightforward.

With 132 stars, 18 forks, and a growing skills.sh ecosystem integration, mini-browser represents a pattern we're likely to see more of: specialized CLI tools designed not for human developers but as primitives for autonomous AI agents to compose and orchestrate. The fact that it's written in TypeScript and distributed as both an npm package and a skills.sh skill suggests the Runable team understands that agent tools need multiple distribution channels to reach different agent frameworks and runtimes.
