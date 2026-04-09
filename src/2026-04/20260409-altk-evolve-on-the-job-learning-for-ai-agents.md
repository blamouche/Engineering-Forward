# ALTK-Evolve: On-the-Job Learning for AI Agents

**Source**: https://huggingface.co/blog/ibm-research/altk-evolve
**Date**: April 9, 2026
**Author**: IBM Research and collaborators
**Keywords**: ALTK-Evolve, agent memory, long-term learning, guidelines, traces, CUGA, Claude Code, Codex

## Elevator pitch
ALTK-Evolve turns agent trajectories into reusable guidelines, aiming to help agents improve over time by retrieving distilled principles instead of reloading raw transcripts.

## Takeaways
- The system captures full execution traces, extracts candidate entities, scores them, and retrieves only the most relevant guidance later.
- Its core premise is that agents need portable principles rather than repeated exposure to full historical transcripts.
- Benchmark results on AppWorld show especially large gains on harder tasks and better consistency across variants.
- The project ships multiple integration tiers, from lightweight filesystem-based plugins to fuller low-code and MCP-style setups.
- ALTK-Evolve is explicitly designed to make long-term learning a composable subsystem rather than a one-off prompt trick.

## Synthesis
The strongest idea in ALTK-Evolve is that memory should not be confused with replay. Many current agent systems claim to “remember” by stuffing old conversations or traces back into context. That can help, but it rarely produces the kind of generalization humans mean by learning. ALTK-Evolve’s point is that useful experience should be distilled into guidelines that can transfer beyond the exact task where they were first observed. That is a much better framing for long-term improvement.

The architecture follows that logic closely. Downward flow captures full trajectories, while upward flow consolidates and scores candidate entities until a cleaner library of guidance emerges. Retrieval then injects only what appears relevant at the moment of action. This is important because raw memory systems tend to decay into clutter. Without consolidation and scoring, they become junk drawers that add cost and noise. ALTK-Evolve is trying to make memory selective, portable, and just-in-time.

The benchmark results are notable less for the absolute number than for where the gains show up. Hard tasks and consistency metrics improve the most. That fits the intuition that distilled guidance helps most when an agent needs judgment, sequencing, or adaptation rather than recall of a narrow fact. In other words, the system seems to improve not only whether an agent can solve something once, but whether it can solve similar things more reliably. That is a strong sign that it is capturing principles rather than memorized episodes.

More broadly, ALTK-Evolve reflects a shift in how people are designing agent stacks. The frontier is moving from bigger prompts toward better surrounding systems: memory, retrieval, evaluation, observability, and learning loops. Projects like this matter because they treat agent improvement as an engineering discipline, not as a mysterious property of model upgrades alone. If agentic software matures into a real category, memory systems that can turn traces into reusable judgment will likely be one of the core pieces of that stack.
