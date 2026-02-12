# Teach Your AI to Think Like a Senior Engineer

**Source**: https://every.to/source-code/teach-your-ai-to-think-like-a-senior-engineer-789ba7ca-ca7c-45a1-91fa-4178f59f226f

**Date**: January 29, 2026

**Author**: Kieran Klaassen

**Keywords**: AI, planning, senior engineer, agents, code review, software development, institutional knowledge, CLAUDE.md

## Elevator pitch

AI development works best when it mirrors senior engineer practices: structured research and planning before coding, with preferences and patterns progressively captured to make future AI interactions more intelligent.

## Takeaways

- Jumping directly to coding with AI leads to building incorrect solutions; structured planning prevents wasted effort
- Eight planning strategies scale with task complexity, from reproducing bugs to synthesizing multi-option approaches
- Running five research agents in parallel beats sequential human planning while preserving human judgment for decisions
- Each learning captured in CLAUDE.md or codified as specialized agents makes future AI interactions progressively smarter
- Developer choices during planning reveal preferences that get codified, creating compound knowledge over time

## Synthesis

Kieran Klaassen continues his exploration of AI-assisted development practices with a detailed framework for teaching AI systems to think like senior engineers. The core argument extends his previous work on planning: rather than treating AI as a code generation tool, developers should use it as a research and planning partner that absorbs institutional knowledge through structured interaction.

The article opens with a concrete example from Cora's email bankruptcy feature, which involved archiving 53,000 emails without data loss. Initial assumptions about the implementation proved incorrect when planning revealed constraints: Gmail rate limits would fail at 2,000 emails, and the system would timeout on long operations. What seemed like a quick implementation actually required three days of architectural work. This discovery emerged only because the team invested in planning rather than jumping directly into code.

Klaassen presents eight planning strategies organized by task complexity. For simpler Fidelity One and Two tasks, the strategies include reproducing and documenting bugs without immediately fixing them, grounding solutions in industry best practices through web research, finding existing patterns in the codebase to avoid duplication, and reading source code of installed libraries for undocumented capabilities. For more complex Fidelity Two and Three work, developers should study git history to understand past decisions, build rapid throwaway prototypes to clarify requirements, synthesize findings into multi-option plans with honest tradeoffs, and run specialized review agents checking for preferences around simplicity, security, and coding style.

The parallel execution capability of AI agents provides significant leverage. Running five agents to research simultaneously outperforms sequential human planning, but the framework preserves human judgment for decision-making. When developers choose between presented options, those choices reveal preferences that get codified for future use. The compound effect becomes substantial: documented learnings in CLAUDE.md files and specialized agents accumulate into institutional knowledge that makes every subsequent AI interaction more aligned with team standards.

For practical adoption, Klaassen recommends starting with one medium-complexity feature. Spend 15-20 minutes having AI research best practices, existing codebase patterns, and library capabilities. Have the AI synthesize findings into a multi-option plan, review it carefully, capture any learnings, then proceed with implementation. The author has open-sourced planning system components including slash commands and research agents through Every's GitHub marketplace. This framework represents a shift from viewing AI as a productivity tool to treating it as a knowledge accumulator that progressively learns how a team thinks about software development.
