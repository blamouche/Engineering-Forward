# Backpressure Is All You Need
**Source**: https://lucasfcosta.com/blog/backpressure-is-all-you-need
**Date**: 2026-05-23
**Author**: Lucas F. Costa
**Keywords**: backpressure, AI-agents, coding-agents, verification, automated-checks, review-agents, Claude-goal, agent-loops, PR-quality

## Elevator pitch
A systems-engineering concept — backpressure, where downstream components signal upstream to slow down — is the missing piece for safe AI coding agents: by building automated quality gates (tests, types, benchmarks, review agents) into the agent loop, longer unattended sessions become safe without fully removing humans.

## Takeaways
- Two obvious approaches to AI coding agents are both bad: letting LLMs run unattended (fast but produces bugs and unreviewable PR floods) or treating agents as glorified autocomplete (safe but defeats the purpose)
- Backpressure — a downstream component refusing work the producer hasn't cleaned up — is already familiar through tests, types, and CI; the insight is applying it to AI agent loops
- Six backpressure mechanisms: linting/testing, manual testing (cURL/browser), benchmarking, review agents, planning-phase review, and visual design reviews
- The packaged skill `@lucasfcosta/backpressured` (npm) implements this loop with Claude's `/goal` command, running checks in each iteration
- Core maxim: any system that relies on a human to catch the machine's mistakes will be limited by the human, not the machine

## Synthesis
Lucas Costa proposes backpressure as the key concept for making AI coding agents safe enough for unattended use. The two obvious approaches — letting LLMs run wild (fast, exciting, stupid) or forcing human review of every step (safe but slow) — both fail. The third approach: build ways for agents to validate their own work before humans have to step in.

Backpressure is a systems-engineering concept where a downstream component signals upstream that it can't accept more work, forcing the producer to slow down, buffer, or shed load. In software development, automated tests are the simplest form: you don't submit a PR with failing tests. TypeScript types add another layer, refusing work at the boundary where a type mismatch occurs. CI pipelines bundle these guardrails. The insight is recognizing that when the producer is an LLM writing code faster than anyone can read it, the human reviewer becomes the default backpressure — an expensive clipboard doing mechanical work between two machines.

Costa details six backpressure mechanisms built incrementally into Claude's `/goal` loop. First, linting and testing with explicit instructions to run checks in each iteration, not just at the end. Second, manual testing with cURL and browser tools (Playwright MCP), requiring the agent to run local dependencies and test real behavior. Third, benchmarking for performance-sensitive applications, with a dedicated skill for running and interpreting results. Fourth, review agents — the most effective mechanism — checking readability, complexity, testing, and types. Fifth, planning-phase review, where a reviewer subagent checks the fundamental approach before any code is written. Sixth, visual design reviews for front-end work.

The packaged skill `@lucasfcosta/backpressured` (available via npm) implements this loop. Running `/backpressured <goal description>` in Claude kicks off the automated iteration with backpressure checks. A `BACKPRESSURE.md` file allows project-specific customization. The full loop spans planning (create plan, review), iteration (write patch, run all checks until green), post-iteration (manual testing, benchmarks, final review), and PR monitoring.

The piece closes with a reflection on packaging: whether `SKILL.md` is the right vehicle for enforcing this workflow, and a desire to experiment with breaking the review agent into multiple specialized agents (readability, complexity, testing, types). Regardless of implementation, Costa argues this is the direction software engineering is headed: "We've spent decades moving the 'no' off humans. Now we have to do it again, for code that writes itself."