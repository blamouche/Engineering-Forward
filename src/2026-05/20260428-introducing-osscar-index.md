# Introducing the OSSCAR Index
**Source**: https://supabase.com/blog/introducing-osscar-index
**Date**: 2026-04-28
**Author**: prashant
**Keywords**: open-source, ranking, community, github-stars, contributors, package-downloads, growth-metrics

## Elevator pitch
The OSSCAR Index is a quarterly ranking of the fastest-growing open source organizations, measured with a transparent, reproducible methodology that focuses on growth rate rather than absolute size, with the site, data, and scoring code all open source.

## Takeaways
- OSSCAR ranks GitHub organizations by growth rate across three signals: net new stars, unique contributors, and package downloads (npm, PyPI, Cargo)
- Projects are split into two divisions — Emerging (<1,000 stars at quarter-start) and Scaling (1,000+ stars) — to ensure fair peer comparison
- The L² norm scoring method rewards standout growth on a single signal rather than penalizing projects without all three signal types (e.g., a library without a published package)
- Openclaw was the breakout story of Q1 2026, crossing 365K stars, going from 29 to 1,383 contributors, and hitting 16.7 million package downloads in a single quarter
- AI agents dominated the Emerging division, but non-AI projects like Craft Docs, npmx, Mantine, and the Free Ebook Foundation also showed strong momentum

## Synthesis
Supabase, in collaboration with >commit, launched the OSSCAR Index (Open Source Supabase Commit Analytical Ranking) to address what they see as a fundamental problem in open source visibility: most ranking lists measure size (stars, total downloads, total contributors), which tells you who was big yesterday, not who is growing today. OSSCAR flips the lens to growth rate.

The methodology is transparent by design. Three signals are tracked per quarter: net new GitHub stars, unique contributors, and package downloads from npm, PyPI, and Cargo. Each is normalized within its division (Emerging or Scaling), then combined using an L² norm (square root of sum of squares). This approach deliberately rewards breakout performance on a single signal — a project can top the rankings on star growth alone even without package downloads. Missing signals don't hurt; only growth counts. Small bases don't get a free ride thanks to minimum thresholds that prevent tiny numbers from producing absurd growth rates.

Q1 2026's results revealed several interesting patterns. Openclaw was the quarter's breakout story, crossing the Scaling threshold with 365K stars, exploding from 29 to 1,383 contributors, and reaching 16.7 million package downloads — all compounding simultaneously. AI agents dominated the Emerging division's top 10, with Paperclip taking #1. But the methodology also surfaced non-AI momentum: Craft Docs picked up 768K npm downloads for #3 Emerging, npmx gained 237 new contributors for #7, and both the Mantine UI library and Free Ebook Foundation cracked the Scaling top 100 on contributor growth alone. A "Claw" ecosystem cluster emerged: Openclaw at #1 Scaling, ZeroClaw Labs at #2 Emerging, NullClaw at #15 Emerging, and a GoClaw fork already active.

The index is quarterly, with Q2 2026 data collection already underway. The roadmap includes more package managers (Go modules, expanded crate coverage, container images), a public RFC process for methodology changes, and historical rankings to track which projects sustain growth versus flash and fade.
