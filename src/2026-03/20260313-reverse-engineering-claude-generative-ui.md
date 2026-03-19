# Reverse-engineering Claude's generative UI — then building it for the terminal
**Source**: https://michaellivs.com/blog/reverse-engineering-claude-generative-ui
**Date**: 2026-03-13
**Author**: Michael Livshits
**Keywords**: Claude, generative UI, reverse engineering, terminal, WKWebView, morphdom, streaming, DOM diffing, Glimpse, pi coding agent

## Elevator pitch
By extracting Anthropic's actual design guidelines from browser network requests, Livshits reverse-engineered Claude's generative UI system and rebuilt it for terminal using native macOS WKWebView windows with streaming-smooth DOM diffing.

## Takeaways
- Claude's generative UI uses a `show_widget` tool call returning HTML parameters—not markdown embeds—and requires calling `visualize_read_me` first to load design guidelines progressively.
- HTML is injected directly into the DOM with Content Security Policy restricting CDN sources.
- Anthropic's actual design guidelines: 10 modular sections covering core design, color palettes, SVG setup, and diagram types; available from browser network requests.
- Streaming-friendly HTML: styles first, scripts last; no gradients or shadows that flash during DOM updates.
- Terminal implementation uses native macOS WKWebView windows (<50ms startup) opened early via intercepted tool call streaming events.
- morphdom library for DOM diffing applies fade-in animations only to genuinely new elements, solving streaming smoothness by diffing rather than replacing innerHTML.

## Synthesis
Reverse-engineering production systems from network traffic is a time-honored technique for understanding how things actually work as opposed to how they're documented. The discovery that Claude's generative UI loads design guidelines via a `visualize_read_me` tool call rather than having them baked into the system prompt is interesting for what it reveals about the architecture: guidelines are fetched on demand, reducing the cost of including them when visualizations aren't needed.

The streaming-friendly design constraints are the most technically instructive details. "Styles first, scripts last; no gradients that flash during DOM updates" reflects the reality that streaming HTML—where the browser renders partial content as it arrives—creates visual artifacts when interactive or animated elements appear before their dependencies. Designing for streaming requires anticipating how partial renders will look, not just how final renders will look.

The WKWebView terminal approach solves a genuine problem: rendering HTML in a terminal typically requires either a full browser (heavy), a text-mode HTML renderer (poor fidelity), or server-side rendering to images (no interactivity). Native WKWebView at <50ms startup time provides full HTML rendering capability without the overhead of a full browser process, making it practical for use in terminal-based coding agents.

The morphdom DOM diffing solution is elegant. The naive approach of replacing innerHTML on each streaming update produces visible flashing and loses any state (scroll position, focus, animation progress). DOM diffing applies only the minimum set of changes needed, producing smooth progressive rendering while preserving existing state—the same technique that makes frameworks like Svelte and React efficient for incremental updates.
