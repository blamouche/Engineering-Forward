# Anthropic tests new Bugcrawl tool for Claude Code
**Source**: https://www.testingcatalog.com/anthropic-tests-new-bugcrawl-tool-for-claude-code-bug-detection
**Date**: 2026-04-25T21:04:02.000Z
**Author**: Unknown
**Keywords**: anthropic, tests, new, bugcrawl, tool

## Elevator pitch
Anthropic is testing a Bug Crawl feature in Claude Code, letting users scan repositories for bugs and get fix suggestions.

## Takeaways
- Anthropic is testing a Bug Crawl feature in Claude Code, letting users scan repositories for bugs and get fix suggestions.
- Anthropic appears to be building a tool within Claude Code called Bugcrawl, which surfaces as a dedicated entry in the side navigation.
- The most plausible read is that Bugcrawl will set Claude loose across an entire codebase to hunt for general bugs and propose fixes, while…
- For Anthropic, the move slots cleanly into the Claude Code expansion of recent months, which has already produced Claude Code Security in February and…
- The likely audience is engineering teams on Team and Enterprise tiers, where the token burn warning is easier to absorb.

## Synthesis
Anthropic is testing a Bug Crawl feature in Claude Code, letting users scan repositories for bugs and get fix suggestions. No release date yet.

Anthropic appears to be building a tool within Claude Code called Bugcrawl, which surfaces as a dedicated entry in the side navigation. Once opened, the screen presents a repository selection UI alongside a warning that the feature consumes tokens at a high rate, so it's suggested to start with a small repository before pointing it at anything substantial. That caveat alone hints at the scale of work the agent would be carrying out in the background.

The most plausible read is that Bugcrawl will set Claude loose across an entire codebase to hunt for general bugs and propose fixes, while the Security tab already shipping in Claude Code for Enterprises targets vulnerabilities specifically. If Anthropic pushes the concept further, the same loop could extend into end-to-end product testing, where Claude spins up a local instance of the app, walks through user flows, and reports regressions. How feature specifications or test criteria would be passed into a run is still an open question, since the only screen visible so far is the repository picker.

For Anthropic, the move slots cleanly into the Claude Code expansion of recent months, which has already produced Claude Code Security in February and Claude Code Review in March, both built around multi-agent investigation of code. Bugcrawl would round out that lineup by tackling general correctness and quality, the broader, fuzzier category that sits between security scanning and PR-level review. It also fits the wider competitive picture, with OpenAI's Codex, xAI's Grok Build, and Google's Jules each pushing toward agents that reason across full repositories rather than single files.

The likely audience is engineering teams on Team and Enterprise tiers, where the token burn warning is easier to absorb. No release window has surfaced, and the feature does not appear in production builds. Given the cadence of Code Security and Code Review landing within weeks of each other, a research preview on the same web surface looks like the most likely path.

Google Pomelli expands to Europe and tests new Catalog and Websites features, aiming to simplify marketing for SMBs ahead of Google I/O.

What's new? GitHub now uses billing based on AI credits and tokens for all Copilot plans starting June 1 2026; admins can set spending limits and preview bills in May;

Reporting AI updates. A future news media, driven by virtual assistants 🤖
