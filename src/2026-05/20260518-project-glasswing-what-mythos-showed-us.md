# Project Glasswing: what Mythos showed us
**Source**: https://blog.cloudflare.com/cyber-frontier-models/
**Date**: 2026-05-18
**Author**: Grant Bourzikas
**Keywords**: Mythos Preview, Anthropic, Project Glasswing, vulnerability research, exploit chain, LLM security, Cloudflare, harness, agent orchestration, proof of concept

## Elevator pitch
Cloudflare tested Anthropic's Mythos Preview against 50+ of their own repositories and found it represents a paradigm shift in AI-assisted vulnerability discovery — able to chain exploit primitives into working proofs of concept — but the models still need careful harness architecture, not chat interfaces, to produce actionable results at scale.

## Takeaways
- Mythos Preview can chain multiple low-severity bugs into a single high-severity exploit proof, something previous models couldn't do — and its reasoning resembles a senior researcher's, not an automated scanner's
- The model generates and iteratively compiles/runs proof-of-concept code; if it fails, it reads the output, adjusts its hypothesis, and tries again — closing the gap between "suspects a bug" and "proves it's exploitable"
- Despite lacking standard safeguards, Mythos organically refuses certain requests — but inconsistently. The same task framed differently can flip from refusal to compliance, making emergent guardrails unreliable as a sole safety boundary
- Pointing a generic coding agent at a repo doesn't scale: single-agent sessions cover ~0.1% of surface before context fills up; vulnerability research needs many narrow, parallel tasks, not one broad agent
- Cloudflare's harness uses 8 stages (Recon → Hunt → Validate → Gapfill → Dedupe → Trace → Feedback → Report) with ~50 concurrent hunters and adversarial review agents to cut noise and produce queryable, actionable findings

## Synthesis
Cloudflare's blog post delivers a field report from the frontier of AI-assisted security research, built around their access to Anthropic's Mythos Preview through Project Glasswing. The core message is nuanced: Mythos Preview is genuinely impressive — a step change, not an iteration — but it's not magic, and the engineering *around* the model matters as much as the model itself.

The two capabilities that define Mythos Preview's leap forward are exploit chain construction and proof generation. Previous models could find individual bugs and reason about them, but they stopped short of stitching findings together. Mythos Preview takes a use-after-free bug, chains it to a memory corruption primitive, hijacks control flow with ROP chains, and produces working code that demonstrates the full attack. Grant Bourzikas describes the reasoning as "the work of a senior researcher rather than the output of an automated scanner." The proof generation loop — write code, compile it, run it, observe failure, adjust, retry — transforms the model from a bug-finder into an exploit-builder.

But there's a tension. Even without standard production safeguards, Mythos Preview shows emergent refusal behavior, pushing back on some legitimate research requests. The problem is inconsistency: semantically identical tasks produce opposite outcomes depending on framing. Cloudflare's team found cases where the model refused to analyze a project, then agreed after an unrelated environment change. These organic guardrails are "real" but "aren't consistent enough to serve as a complete safety boundary" — which is precisely the argument for why generally available models need additional safeguards.

The post's most practical contribution is its detailed description of Cloudflare's vulnerability discovery harness. This is where the real lessons lie for security teams considering AI-assisted research. The key insight: vulnerability research is narrow and parallel by nature, while coding agents are broad and sequential. Cloudflare learned through painful iteration that asking Mythos to "find vulnerabilities in this repository" produces wandering, noisy results that fill the triage queue with speculative hedged findings.

The harness they built solves this structurally. Stage 1 (Recon) maps the codebase and generates architecture documents. Stage 2 (Hunt) runs ~50 concurrent agents, each targeting one attack class against a specific scope. Each hunter has compiler and execution tools. Stage 3 (Validate) introduces an adversarial review agent — different prompt, different model, no ability to generate new findings — which catches noise the hunter would miss self-reviewing. Stage 4 (Gapfill) counteracts model drift toward successful attack classes. Stage 5 (Dedupe) collapses variant findings sharing root causes. Stage 6 (Trace) checks whether attacker input actually reaches the bug from outside the system — the critical step that distinguishes "there is a flaw" from "there is a reachable vulnerability." Stage 7 (Feedback) re-queues reachable traces as new hunt tasks, and Stage 8 (Report) outputs structured, queryable data.

Four architectural principles emerge: narrow scope produces better findings; adversarial review between disagreeing agents reduces noise; splitting analysis questions across agents improves reasoning; and parallel narrow tasks beat one exhaustive agent. Together they describe something that is no longer a chat interface — it's a pipeline.

The post ends with implications for security teams: the models are advancing faster than the processes around them, and building the harness is as important as having access to the model. There's a subtle warning too — if Cloudflare can do this with Mythos, attackers will find ways to do it too, which makes the defensive side's speed of adoption a matter of competitive urgency rather than optional modernization.
