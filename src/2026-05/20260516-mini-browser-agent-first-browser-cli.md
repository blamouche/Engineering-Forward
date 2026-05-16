# mini-browser: An Agent-First Browser CLI
**Source**: https://github.com/runablehq/mini-browser
**Date**: May 16, 2026
**Author**: RunableHQ
**Keywords**: browser automation, agent tools, CLI, Chrome DevTools Protocol, web scraping, headless browsing

## Elevator pitch
mini-browser (mb) is a Unix-style CLI that turns Chrome into a composable tool for AI agents, exposing navigation, observation, interaction, recording, and tab management as pipable commands.

## Takeaways
- Designed specifically for AI agents: each command is a small Unix tool that reads args and writes to stdout, enabling composition with pipes and shell operators.
- Full browser control via Chrome DevTools Protocol: navigation (go, back, forward), DOM observation (text, snap, shot), interaction (click, type, fill, drag, scroll), and JavaScript evaluation.
- Recording capability built in: can record browser sessions as .webm, .mp4, or .gif using Chrome's screencast API.
- Accessibility-tree-based element discovery via `snap` command returns interactive elements with roles, coordinates, and states.
- Ships as both a global npm CLI and an agent skill via skills.sh for automatic agent integration.

## Synthesis
mini-browser represents a significant evolution in how AI agents interact with web browsers. Rather than requiring agents to use complex browser automation frameworks like Playwright or Puppeteer, it provides a clean Unix-philosophy interface where every browser operation is a discrete command that reads arguments and writes to standard output.

The tool is built on Chrome DevTools Protocol (CDP), connecting to a Chrome instance with remote debugging enabled on port 9222. Its command surface covers the full spectrum of browser interaction: navigation commands (`go`, `back`, `forward`, `url`), observation commands (`text` for content extraction, `snap` for accessibility tree analysis, `shot` for screenshots), interaction commands (`click`, `type`, `fill`, `drag`, `scroll`, `key`), and utility commands (`js` for script evaluation, `wait` with multiple strategies, `audit` for design analysis).

What sets mini-browser apart is its agent-first design philosophy. The `snap` command returns structured data about interactive elements from the accessibility tree — including roles, accessible names, center coordinates, and state flags — making it trivial for an agent to discover and interact with page elements without parsing HTML. The `fill` command intelligently matches form fields by accessible name, aria-label, placeholder, name attribute, id, and label text.

The recording feature is particularly noteworthy for agent debugging: agents can record their entire browsing session, providing visibility into their decision-making process. The tab management system uses stable CDP target IDs, allowing agents to coordinate across multiple tabs reliably.

For integration, mini-browser ships both as a traditional npm package and as an installable skill via skills.sh, where agents can automatically learn to use its commands without additional configuration. The tool handles common pain points like cookie banners and modal overlays with straightforward JavaScript removal patterns.

The project is actively maintained by RunableHQ with 146 stars and 21 forks on GitHub, suggesting growing community adoption. Its architecture — simple Unix tools that compose well — aligns with the broader trend of making AI agents more capable by giving them access to well-designed, composable primitives rather than monolithic frameworks.
