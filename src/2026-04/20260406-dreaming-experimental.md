# Dreaming (experimental)

**Source**: https://docs.openclaw.ai/concepts/dreaming
**Date**: April 6, 2026
**Author**: OpenClaw Docs
**Keywords**: OpenClaw, dreaming, memory consolidation, MEMORY.md, recall, background learning, agents

## Elevator pitch
OpenClaw’s new “Dreaming” system formalizes background memory consolidation: short-term recall traces are staged, ranked, and only promoted into long-term memory when they clear explicit thresholds, keeping the process reviewable instead of magical.

## Takeaways
- Dreaming is opt-in and disabled by default.
- The system separates light, REM, and deep phases, with only deep promotion writing to MEMORY.md.
- Promotion decisions depend on explicit scoring thresholds like recall frequency, diversity, and recency.
- Human-readable outputs go to DREAMS.md while machine state lives in memory/.dreams/.
- The design emphasizes explainability and review over opaque always-on memory.

## Synthesis
Dreaming is interesting because it turns “memory” from a vague assistant promise into a concrete background workflow. Instead of pretending an agent just remembers things, OpenClaw defines a multi-phase consolidation system that stages recent material, reflects on recurring themes, and only promotes durable items into long-term memory when they clear explicit gates. That is a far healthier abstraction than black-box persistence.

The phase split matters. Light and REM phases are exploratory and reflective; deep phase is conservative and durable. That gives the system room to notice patterns without immediately polluting MEMORY.md. In practical terms, it mirrors a good human habit: jot things down freely, notice what keeps resurfacing, and only then promote what is actually worth keeping.

The strongest part of the design is explainability. Promotion depends on legible signals like frequency, retrieval relevance, query diversity, recency, and consolidation across days. That makes the memory system auditable. Users can understand why something stuck instead of treating memory as an occult side effect of chatting more.

The broader lesson is that useful agent memory probably looks less like giant context windows and more like disciplined curation. Systems that can stage, score, and selectively promote knowledge will age better than systems that just keep stuffing more text into the prompt.
