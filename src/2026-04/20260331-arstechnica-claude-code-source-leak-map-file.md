# Entire Claude Code CLI Source Code Leaks Thanks to Exposed .map File
**Source**: https://arstechnica.com/ai/2026/03/entire-claude-code-cli-source-code-leaks-thanks-to-exposed-map-file/
**Date**: March 31, 2026
**Author**: Unknown
**Keywords**: Claude Code, source code leak, npm, source map, TypeScript, Anthropic, supply chain security

## Elevator pitch
Ars Technica covers the accidental exposure of Anthropic's entire Claude Code CLI source (512,000 lines of TypeScript) via a forgotten .map file in the npm package, revealing undisclosed features including an autonomous daemon mode.

## Takeaways
- A .map source map file accidentally included in the @anthropic-ai/claude-code npm package exposed 512,000 lines of TypeScript
- The 59.8 MB file spread rapidly across GitHub once discovered
- Undisclosed features exposed: Undercover Mode, fake tool interception, sentiment detection, and KAIROS autonomous daemon mode
- Represents a common build pipeline security gap: dev tools intended for debugging inadvertently shipped to production
- The incident highlights growing supply chain security risks in AI developer tooling

## Synthesis
Ars Technica's coverage of the Claude Code source leak brings the incident to a mainstream technical audience, contextualizing the security implications of the npm source map accident. The publication provides the technical community perspective on what the leak reveals about software supply chain hygiene in AI development tooling.

Source map files are debug artifacts: they map minified or compiled JavaScript output back to original source code, enabling developers to debug production issues with readable code references. They are intentionally excluded from most production deployments because including them exposes intellectual property — the full source code that compilation was meant to obscure. When a .map file is included in an npm package, anyone can download the package and extract the original source.

The scale of the exposure (512,000 lines, 59.8 MB) and the speed with which it spread across GitHub illustrate both the sensitivity of the information and the efficiency of the open-source community's ability to discover, share, and archive such leaks. Once published to npm, retrieval becomes permanent through package mirrors and GitHub archives.

The technical features exposed — Undercover Mode preventing secret leaks, fake tool interception, sentiment detection adjusting verbosity, and KAIROS as an autonomous daemon mode — represent significant unreleased or undisclosed capabilities. KAIROS in particular, described as a background mode with memory consolidation and daily logging, points toward a persistent AI assistant model distinct from the current session-based Claude Code.

For security practitioners, the incident illustrates the need for explicit source map exclusion in publish configurations and pre-publish audits that verify package contents. For the broader AI tooling ecosystem, it demonstrates that as AI developer tools proliferate and handle increasingly sensitive development workflows, their security hygiene deserves the same scrutiny as production infrastructure.
