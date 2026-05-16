# mb · mini-browser: An agent-first browser CLI
**Source**: https://github.com/runablehq/mini-browser
**Date**: May 2026
**Author**: runablehq
**Keywords**: browser automation, CLI, AI agents, Chrome DevTools Protocol, web scraping, agent tooling

## Elevator pitch
Mini-browser is a Unix-philosophy browser CLI designed specifically for AI agents, exposing every browser operation as a composable command-line tool—navigate, click, type, screenshot, audit—with stdout output that pipes naturally into grep, jq, and other standard Unix tools.

## Takeaways
- Each command is a focused Unix tool: `mb go`, `mb click`, `mb text`, `mb shot`, `mb fill`, `mb audit`—all writing to stdout with composable flags like `--json` for structured output.
- The `snap` command returns an accessibility-tree view of interactive elements with exact coordinates, enabling agents to discover page structure without visual reasoning.
- Built-in recording captures browser sessions as .webm, .mp4, or .gif via Chrome's screencast API, with configurable FPS and scale—useful for debugging agent interactions.
- The `audit` command collects design, typography, contrast, accessibility, and SEO data in a single pass, turning visual audits into programmable checks.
- Ships with `skills.sh` integration (`npx skills add runablehq/mini-browser`), making it installable as a skill for any agent framework without manual configuration.

## Synthesis
The rise of AI coding agents has created a new category of infrastructure: tools designed not for humans typing commands, but for machines composing workflows. Mini-browser, from runablehq, is a clear example of this shift. It's a browser CLI where every operation is a small, composable Unix tool—reading arguments, writing to stdout—designed for agents to chain with pipes and `&&`.

The design philosophy is explicitly agent-first. Where traditional browser automation tools like Selenium or Puppeteer require programming in a specific language with complex APIs, mini-browser reduces every interaction to a single command. `mb go "https://example.com" && mb snap` navigates to a page and returns interactive elements. `mb click 512 380` clicks at coordinates. `mb text "main"` extracts visible text. Each command is independently testable, chainable, and debuggable—exactly what an LLM-based agent needs when reasoning about web interactions.

The `snap` command is particularly clever for the agent use case. Instead of requiring visual reasoning (which remains challenging even for frontier models), it returns structured accessibility-tree data: each interactive element's role, accessible name, center coordinates, and state flags. An agent can reason about `button "Submit" (512, 380)` much more reliably than about a screenshot. The `--json` flag across multiple commands ensures structured output that's parseable without fragile regex.

The recording feature addresses a pain point in agent debugging. By capturing browser interactions as .webm, .mp4, or .gif via Chrome's screencast API, it creates replayable artifacts that help developers understand what an agent actually did—essential when debugging failed interactions or demonstrating capabilities.

The audit command is another agent-native design choice. It bundles color palette extraction, typography analysis, contrast checking (via CDP), accessibility evaluation, and SEO metadata into a single pass. For a human, this saves opening DevTools and clicking through panels. For an agent, it means one deterministic command produces structured data that can feed into code review, design systems validation, or accessibility compliance checks.

The `skills.sh` integration (`npx skills add runablehq/mini-browser --all --global`) is forward-looking. It treats the browser CLI not just as a tool to install but as a skill for agent frameworks to discover and use. This aligns with the emerging pattern where agents consume tools through standardized manifests rather than ad-hoc installation.

Several design decisions reflect hard-won lessons about web automation. `mb go` waits for `networkidle0` before returning, acknowledging that SPAs need time to render. The overlay-handling advice (dismiss cookie banners, remove blocking elements via JS) addresses a common failure mode. The clear documentation around selectors, coordinate systems, and wait strategies reduces the ambiguity that causes agents to fail.

The main limitation is Chrome dependency—it requires a running Chrome instance with remote debugging enabled on port 9222. But the included `mb-start-chrome` and `mb-restart-chrome` scripts manage this, creating fresh profiles that respect viewport settings. At 144 stars and 19 forks, the project has traction but remains early-stage.

Mini-browser matters because it crystallizes a pattern that's likely to become standard: tools designed for agents need to be composable, predictable, and output-oriented. The Unix philosophy—do one thing well, write to stdout, compose with pipes—turns out to be as applicable to agent infrastructure as it was to human command-line workflows. As more tools adopt this agent-first design pattern, the line between "CLI tool" and "agent capability" will increasingly blur.
