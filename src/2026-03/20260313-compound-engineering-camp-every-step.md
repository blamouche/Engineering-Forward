# Compound Engineering Camp: Every Step, From Scratch
**Source**: https://every.to/source-code/compound-engineering-camp-every-step-from-scratch
**Date**: 2026-03-13
**Author**: Katie Parrott
**Keywords**: compound engineering, Kieran Klaassen, Claude Code, four-step loop, plan-work-review-compound, AI development methodology, Every.to

## Elevator pitch
A walkthrough of compound engineering in practice: Kieran Klaassen builds a feature-voting application in under an hour using a four-step AI loop where planning consumes 70% of effort and each cycle makes the system permanently smarter.

## Takeaways
- Four-step compound engineering loop: Plan (detailed implementation specs), Work (functional code with tests and docs), Review (multiple AI perspectives), Compound (preserve learnings as discoverable artifacts).
- Planning consumes approximately 70% of mental effort—generating detailed specifications through collaborative questioning transforms vague ideas into concrete implementation plans.
- Strategic model selection: faster models for brainstorming, Opus for architecture planning, specialized models for implementation and code review.
- Each bug fix, code review, and pattern becomes a reusable tool that strengthens future development rather than accumulating as technical debt.
- Philosophy: "ideally, we delete the whole thing someday because it's all built in"—compound engineering as a bridge to self-improving systems, not an end state.

## Synthesis
The 70% planning emphasis is the counterintuitive core of the compound engineering methodology. Standard software project management advice allocates significant time to implementation; compound engineering inverts this by treating thorough specification generation as the high-leverage activity and delegating implementation to AI agents. The reasoning is that implementation errors are cheap to fix when agents generate them; specification errors are expensive because they send implementation in the wrong direction entirely.

The compound step is the unique contribution that distinguishes this from generic AI-assisted development. Most teams using AI coding tools treat each session as independent: they start a session, accomplish a task, and discard the context. The compound step explicitly preserves successful patterns, solved problems, and discovered edge cases as persistent artifacts that future sessions can reference. This creates an accumulating knowledge base about the specific codebase that makes each subsequent session more effective.

The "delete the whole thing someday" philosophy reflects a mature view of tooling. The compound engineering plugin is scaffolding for a practice that should eventually become unnecessary as AI development tools internalize these patterns natively. Building good habits through explicit scaffolding, then removing the scaffolding when the habits are established, is a pedagogical approach applied to organizational practice.

The single-sentence-to-working-feature demonstration is the practical proof point. A vague requirement processed through the planning phase becomes a detailed specification with edge cases, design decisions, and implementation notes. This transformation—from intent to specification—is where most software projects fail; compound engineering makes it systematic.
