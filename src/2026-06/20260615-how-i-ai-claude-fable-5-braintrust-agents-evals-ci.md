# How I AI: Claude Fable 5 Review & How Braintrust Uses AI Agents, Evals, and CI to Ship Better Software
**Source**: https://www.lennysnewsletter.com/p/how-i-ai-claude-fable-5-review-and
**Date**: 2026-06-15
**Author**: Lenny Rachitsky (How I AI podcast)
**Keywords**: Claude Fable 5, Mythos, Anthropic, Braintrust, Ankur Goyal, AI agents, evals, CI, benchmarks, model review, agent engineering

## Elevator pitch
Two podcast episodes from Lenny's How I AI series: (1) Claire's hands-on review of Claude Fable 5—Anthropic's first generally available Mythos-class model—revealing it's a powerhouse for hard technical problems and vision tasks but surprisingly bad at writing, design, and one-shot MVP execution; and (2) Ankur Goyal (Braintrust CEO) on how top engineering teams use agents, evals, and CI to ship better software, arguing that evals are the modern PRD and that practical AI-assisted quality beats theoretical human quality.

## Takeaways
- **Fable 5 is "baby Mythos"**—the same underlying model as the unrestricted Mythos, but tuned for safety and general availability with cybersecurity/biology/chemistry/distillation fallbacks to Opus 4.8 (95% of sessions never hit a fallback)
- Fable 5 scored 80% on SWBench Pro, outperforming Opus 4.8, GPT-4.5, and Gemini 3.1 Pro, but excels specifically in hard technical problems, long-horizon work, and vision tasks (PDF parsing, document formatting)
- The model is expensive by design: $10/MTok input, $50/MTok output, consuming tokens at ~2x rate of other models—requires strategic deployment matching model intelligence to task complexity
- Fable 5's writing for specs/PRDs is "nearly unreadable"—produces dense, internally-referenced paragraphs that obscure the big picture; design output is "shockingly bad" for one-shot tasks
- **Ankur Goyal's key insight: evals are the modern PRD**—they define what success looks like, not how to achieve it; the #1 engineering priority for AI product teams is building a feedback loop that automatically turns real-world data into evals
- Practical quality beats theoretical quality: AI agents maintain consistent focus, run every test, and work continuously for days—humans lose context and skip tedious benchmarks, making AI-assisted engineering practically higher quality
- Run 4-6 foreground agents simultaneously (the human concurrency limit), each in isolated environments with their own ports and services
- When agents fail, don't prompt harder—close the session, improve the evals, and start fresh; the solution is always better evals, not better prompting
- Product building is now "carving, not constructing"—it's easy to create something with too many features; the hard part is removing complexity

## Synthesis
This dual-episode from How I AI captures two complementary perspectives on the current state of AI-assisted engineering: a rigorous product review of the most capable model available, and a practitioner's playbook for building with agents at scale.

Claire's Fable 5 review is valuable precisely because it's not a benchmark summary—it's a real-world stress test across product specs, agent workflows, design tasks, vision, and multi-agent orchestration. The model's profile that emerges is paradoxical: it's a "seasoned engineer" that will investigate every corner of a problem to be 120% sure, but this thoroughness is both its superpower and its Achilles' heel. For hard technical problems where detail matters, this is exactly what you want. For specs, PRDs, and design—where clarity and simplicity matter more than completeness—the thoroughness produces unreadable documents and terrible designs. The $10/$50 pricing and 2x token consumption make misdeployment expensive.

The safety architecture is notable. Rather than blocking sensitive tasks entirely, Fable 5 falls back to Opus 4.8 for cybersecurity, biology, chemistry, and distillation tasks. This graceful degradation approach means users aren't hard-blocked—they get a less capable but still functional model. The 30-day data retention policy (also seen in the export-control compliance statement) is the surveillance cost of this safety architecture.

Ankur Goyal's Braintrust episode shifts from model review to engineering practice. His core argument—that evals are the modern PRD—reframes the AI engineering workflow: instead of specifying implementation, you specify success criteria and let agents figure out the implementation. The feedback loop that converts real-world data into evals is the highest-leverage investment an AI product team can make, analogous to investing in CI for traditional software. Without it, teams are stuck in whack-a-mole mode.

The "practical quality beats theoretical quality" argument is the most contrarian and important insight. Engineers who argue AI can't handle complex problems are often comparing theoretical human quality (infinite time, perfect focus) against practical AI quality. In practice, humans lose context, skip benchmarks, and decay on tedious problems. Agents don't. This doesn't mean agents produce theoretically better code—it means the code they produce, tested against evals that encode real success criteria, is practically better than what most humans ship under real constraints.

The carving-not-constructing metaphor captures a genuine shift in how products are built with AI: the bottleneck has moved from creation to curation. It's trivially easy to generate something with too many features; the skill is in removing what doesn't serve the user.