# The 2nd Phase of Agentic Development
**Source**: https://www.dbreunig.com/2026/04/01/the-2nd-phase-of-agentic-development.html
**Date**: April 1, 2026
**Author**: Drew Breunig
**Keywords**: agentic development, software reimagining, Cloudflare, Pretext, legacy software, cost reduction, AI coding

## Elevator pitch
Agentic development is shifting from Phase 1 (cloning and porting existing software) to Phase 2 (reimagining practical because the cost of rebuilding is so much lower) — targeting software people rely on but dislike.

## Takeaways
- Phase 1: Use existing test suites to guide AI agents in replicating established software (Rust compiler, TypeScript emulator)
- Phase 2: Rethink solutions to longstanding problems using contemporary approaches — Pretext reimagines text layout, EmDash reimagines WordPress
- Drastically reduced development costs make previously impractical challenges to established software economically viable
- AI enables synthetic testing to rapidly validate new approaches before committing to full implementation
- "Software tools that people rely on but don't like" are prime targets for Phase 2 reimagining

## Synthesis
Breunig's two-phase framing provides a useful lens on the trajectory of AI-assisted software development. Phase 1 — replicating existing software — was the natural first application of agentic coding because existing test suites provided automatic verification infrastructure. An agent could implement a Rust compiler, run the existing test suite, and the test results would verify correctness without requiring new evaluation methodology. This is technically conservative but practically useful: it produces reliable implementations with automatic quality validation.

Phase 2 is more ambitious and economically significant. The premise is that the cost reduction AI enables makes it rational to challenge established software products that would have been impractical to compete with before. Building a competitor to WordPress requires substantial engineering investment; if AI coding reduces the implementation cost by 10x, projects that couldn't justify the investment become viable. Cloudflare's EmDash (a modern serverless CMS) and Cheng Lou's Pretext (accurate text layout without CSS overhead) illustrate this with concrete examples from April 2026.

The synthetic testing capability is what makes Phase 2 tractable. Without AI-generated tests and rapid iteration, building a new approach to a solved problem requires either accepting lower quality than the incumbent or investing heavily in test infrastructure before writing any product code. AI agents can generate comprehensive test coverage during development rather than as a post-implementation effort, making early-stage exploration of new approaches less risky.

The targeting of software "people rely on but don't like" is a specific strategic insight. These products have captured users through network effects, lock-in, or the absence of adequate alternatives — not because users prefer them. They represent markets where an adequately capable new entrant with better UX, modern architecture, or lower operational overhead could attract switching despite high incumbent deployment. The calculus changes when building the challenger costs a fraction of what it did before.

For engineering teams, this suggests evaluating incumbents in their vendor stack through a Phase 2 lens: which tools are they using despite not liking them, and how has AI changed the cost of alternatives?
