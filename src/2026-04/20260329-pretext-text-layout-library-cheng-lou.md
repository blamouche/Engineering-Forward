# Pretext: A Browser Library for Accurate Text Height Calculation
**Source**: https://simonwillison.net/2026/Mar/29/pretext/
**Date**: March 29, 2026
**Author**: Simon Willison
**Keywords**: JavaScript, browser, text layout, typography, multilingual, canvas, Claude Code, Codex

## Elevator pitch
Pretext is a tiny browser library by former React core developer Cheng Lou that accurately calculates wrapped text height without touching the DOM, built with extensive multilingual testing aided by Claude Code and Codex.

## Takeaways
- Calculates text height across wrapped lines using an off-screen canvas without DOM manipulation
- Handles words, soft hyphens, non-Latin characters (Thai, Chinese, Korean, Japanese, Arabic, emoji)
- Tested by rendering the Great Gatsby and public domain texts across multiple browsers and languages
- Built by Cheng Lou (react-motion creator) using Claude Code and Codex for multilingual browser quirk measurement
- Simon Willison created an interactive artifact demonstrating the library

## Synthesis
Pretext addresses a browser layout problem that sounds simple but is genuinely difficult: determining how tall a block of text will be when wrapped across multiple lines at a given width. Browsers calculate this internally during rendering, but accessing that calculation without forcing a layout reflow — which would require DOM manipulation and trigger performance-expensive browser recalculations — requires reproducing the browser's word-wrapping algorithm outside the rendering engine.

The two-function architecture reflects the technical constraints. `prepare()` segments text and measures segments using an off-screen canvas, which provides font metric information without triggering a layout reflow. `layout()` then applies a word-wrapping algorithm that emulates the browser's behavior, using the pre-measured segment widths to determine where line breaks will occur. The combination produces accurate height calculations without interacting with the live DOM.

The multilingual support is the technically hard part. Latin text word-wrapping follows relatively predictable rules: break at word boundaries, handle hyphens, manage whitespace. Non-Latin scripts introduce different challenges. Chinese and Japanese lack word spaces, requiring character-based rather than space-based segmentation. Arabic and Hebrew text flows right-to-left with different line-breaking rules. Thai requires linguistic word boundary detection. Getting each of these right, and getting them right consistently across different browsers that implement the layout engine with slight variations, requires systematic testing at scale.

The development process — using Claude Code and Codex to measure browser ground truth and iterate — illustrates a pattern that Willison highlighted: AI-assisted development of low-level, correctness-critical code through iterative comparison against known-correct outputs. Cheng Lou wasn't using AI to generate the algorithm; he was using it to run thousands of measurements across browsers and languages, generating the empirical data needed to validate correctness.

The tiny footprint (few kilobytes, described as "aware of browser quirks") reflects the engineering discipline appropriate for a library that might be embedded in any browser application.
