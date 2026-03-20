# The Future of Software Engineering with Anthropic
**Source**: https://www.akashbajwa.co/p/the-future-of-software-engineering
**Date**: 2026-03-16
**Author**: Akash Bajwa
**Keywords**: software engineering, AI, Anthropic, Stripe, NVIDIA, Microsoft, Google DeepMind, hiring, agents, context management

## Elevator pitch
A roundtable with engineering leaders from Anthropic, Stripe, NVIDIA, Microsoft, Google DeepMind, and others reveals that long-horizon autonomous tasks remain unsolved, that forced AI tool adoption backfires, and that internal tooling is being replaced faster than business-facing software.

## Takeaways
- Test-first methodology is becoming standard—write tests, then let AI implement against them
- Organizations use competitions and hackathons for organic AI adoption; forced usage breeds resentment
- Long-horizon autonomous tasks (multi-hour agent runs) remain the primary unsolved bottleneck in agentic engineering
- Developer tooling is being replaced by AI faster than business-facing software; internal tools are built rather than bought
- Companies now prioritize willingness to experiment with AI over raw coding ability in hiring decisions

## Synthesis
Akash Bajwa's synthesis of a roundtable discussion featuring engineering leaders from Anthropic, Stripe, NVIDIA, Microsoft, Apple, Google DeepMind, xAI, Scale AI, and OpenAI provides a rare multi-perspective view of where AI is actually changing software engineering practice and where hype exceeds reality.

The workflow evolution section reveals an important shift in development methodology. Test-first approaches are becoming the dominant paradigm for AI-assisted coding: engineers write tests that define desired behavior, then let AI implement against those tests. This inversion of the traditional write-code-then-test pattern forces clarity about requirements before implementation begins and provides an objective evaluation signal the AI can use without human intervention. It also ensures human judgment is applied at the specification layer—where it matters most—rather than the implementation layer, where AI is increasingly competent.

The adoption dynamics discussion challenges the common assumption that organizations should mandate AI tool usage. Multiple leaders reported that competitive demonstrations and internal hackathons drove faster adoption than top-down requirements. Engineers who see peers doing 3x their output with AI tools adopt them voluntarily; engineers required to use unfamiliar tools resent the imposition and find workarounds. The lesson is that AI adoption is a social and competitive phenomenon as much as a technical one.

The honest acknowledgment of unsolved problems is the most valuable content in the summary. Long-horizon autonomous tasks—multi-hour agent runs that must maintain coherent behavior across hundreds of steps without human checkpoints—remain genuinely unsolved. Context management at scale lacks standardized solutions. Human-authored documentation consistently outperforms agent-generated alternatives for providing context to subsequent agents.

The displacement pattern is striking: developer tooling (incident management, auth systems, project management) is being replaced by AI-built alternatives faster than externally-facing products. The combination of internal users with high tolerance for rough edges and clear requirements that teams understand deeply makes internal tooling the ideal first target for AI-assisted software. The purchasing implication is significant—budgets that previously went to developer tooling vendors are increasingly being absorbed by internal engineering time and AI API costs.
