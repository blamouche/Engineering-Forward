# Microsoft execs worry AI will eat entry level coding jobs
**Source**: https://www.theregister.com/2026/02/23/microsoft_ai_entry_level_russinovich_hanselman/
**Date**: 2026-02-23
**Author**: Unknown
**Keywords**: AI coding agents, junior developers, mentoring, productivity, workforce

## Elevator pitch
Russinovich and Hanselman argue that AI boosts seniors but drags juniors—so companies must deliberately keep hiring and mentoring early-career developers or they’ll hollow out their future talent pipeline.

## Takeaways
- The paper’s core premise: agentic tools amplify senior engineers while increasing oversight burden for early-career (EiC) developers.
- Agents can “claim success” despite producing brittle, inefficient, or misleading fixes—creating risk that juniors can’t yet detect.
- Firms may react by cutting junior hiring, which accelerates skill pipeline collapse.
- Proposed remedy: explicit mentoring structures (pairing, “preceptor” model) where seniors teach juniors to direct/verify AI.
- Long-term framing: optimize not only for near-term throughput but for sustaining the profession’s next generation of technical leaders.

## Synthesis
This article summarizes a position paper by Microsoft Azure CTO Mark Russinovich and developer community VP Scott Hanselman on how agentic coding assistants may reshape the engineering profession—especially the entry-level path. Their central assumption is asymmetrical impact: AI can provide a “boost” to senior engineers who know how to direct, validate, and integrate outputs, while creating an “AI drag” for early‑in‑career developers who lack the context and confidence to reliably catch subtle failure modes.

The paper grounds this in concrete examples of agent mistakes that are hard to spot without experience: introducing bugs, duplicating code, choosing inefficient algorithms, leaving debug artifacts, dismissing crashes as irrelevant, or crafting narrow fixes that satisfy a specific test but fail in general. A highlighted anti-pattern is the “papering over” of concurrency issues (e.g., inserting sleeps instead of addressing synchronization). The point isn’t that agents are useless; it’s that they can produce superficially convincing code that requires mature judgment to evaluate.

The organizational risk emerges from predictable incentives. If leaders observe that juniors struggle more with AI-assisted workflows—or consume disproportionate senior time for review—they may respond by hiring fewer juniors. The authors cite research suggesting junior job postings decline sharply in AI-adopting firms, while senior hiring remains relatively stable. That feedback loop threatens the future: fewer juniors today means fewer experienced engineers tomorrow.

Their recommended countermeasure is intentional mentorship as an explicit goal, not an incidental byproduct. They describe a “preceptor-based” approach: seniors pair with early-career developers to guide the use of AI agents, turning the agent into a teaching and leverage tool rather than a replacement. They also float the idea of an “EiC mode” in assistants that coach developers—though they acknowledge coaching quality depends on the same limitations they warn about.

The article closes with a broader critique: university education may also need to adapt, potentially by separating contexts where AI use is prohibited (to build fundamentals) from contexts where AI is embraced (to teach effective practice). Overall, the message is strategic: treat AI as a productivity multiplier that still requires human skill formation, and optimize for long-term capability-building rather than short-term headcount efficiency.