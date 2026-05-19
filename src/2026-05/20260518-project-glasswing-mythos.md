# Project Glasswing: what Mythos showed us
**Source**: https://blog.cloudflare.com/cyber-frontier-models
**Date**: May 18, 2026
**Author**: Grant Bourzikas
**Keywords**: Mythos, Anthropic, cybersecurity, LLM, vulnerability research, exploit chain, Cloudflare, AI security

## Elevator pitch
Cloudflare tested Anthropic's Mythos Preview (a security-focused LLM) on 50+ internal repositories through Project Glasswing, finding it can chain low-severity bugs into working exploits — but organic model refusals are inconsistent, and generic coding agents are fundamentally the wrong tool for vulnerability research.

## Takeaways
- Mythos Preview represents a step change from general-purpose frontier models: it constructs exploit chains by combining attack primitives, and generates working proofs of concept by writing, compiling, and testing exploit code in a loop.
- The model can take low-severity bugs that would traditionally sit invisible in backlogs and chain them into a single severe exploit — a capability that changes how organizations must triage vulnerabilities.
- Organic guardrails cause inconsistent refusals: the model may refuse vulnerability research in one context, then accept the same task after an unrelated environment change — too inconsistent to serve as a safety boundary.
- Programming language matters enormously: memory-unsafe languages (C/C++) generate far more false positives than memory-safe ones (Rust).
- Generic coding agents (Claude Code-style) are the wrong tool for vulnerability research: they're designed for focused, linear work, but vulnerability research requires narrow, parallel investigation across thousands of surface areas.
- A proper harness is essential: fan-out architecture, parallel hypothesis testing, and post-validation stages to manage the signal-to-noise problem.

## Synthesis
Cloudflare CSO Grant Bourzikas shares the results of testing Anthropic's Mythos Preview — a specialized cybersecurity LLM — on the company's own infrastructure through Project Glasswing. The findings reveal both a significant leap in AI security capabilities and the hard engineering work required to use them at scale.

Mythos Preview's standout capability is exploit chain construction. Traditional vulnerability scanners find individual bugs; Mythos can reason about how to combine several small attack primitives into a working exploit — turning a use-after-free into arbitrary read/write, then hijacking control flow via ROP chains. More importantly, it generates proofs: the model writes exploit code, compiles it in a scratch environment, runs it, reads the failure, adjusts its hypothesis, and tries again. A finding that arrives with a working PoC is actionable; one without is speculation that costs human time to dismiss.

The signal-to-noise challenge remains significant. Models exhibit a confirmation bias toward finding vulnerabilities — ask them to find bugs, and they will find them, whether the code has any or not. Hedged findings ("possibly," "potentially," "could in theory") vastly outnumber solid ones. Mythos improves on this significantly, producing clearer reproduction steps and fewer hedged outputs than general-purpose models. But memory-unsafe languages (C/C++) generate consistently more false positives than memory-safe ones (Rust).

Cloudflare's most important architectural insight: generic coding agents are the wrong tool for vulnerability research. Coding agents are tuned for focused, linear work — building a feature, fixing a bug. Vulnerability research requires the opposite: narrow, parallel investigation across thousands of surface areas. A single agent session against a 100K-line repository covers maybe 0.1% of the surface before context fills up and compaction discards earlier findings. The solution is a purpose-built harness that fans out multiple parallel hypotheses, with post-validation stages to filter noise.

The organic refusal behavior is also notable: Mythos Preview's built-in guardrails sometimes reject legitimate security research, but inconsistently — the same task framed differently produces different outcomes. This underscores why future generally-available cyber models will need additional safeguards beyond baseline behavior.
