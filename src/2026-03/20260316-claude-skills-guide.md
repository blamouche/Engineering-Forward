# The Ultimate Guide to Claude Skills
**Source**: https://linas.substack.com/p/claudeskills
**Date**: 2026-03-16
**Author**: Linas Beliūnas
**Keywords**: Claude Skills, Claude Code, SKILL.md, YAML, productivity, automation, Skills 2.0, prompt engineering

## Elevator pitch
Linas Beliūnas's definitive guide to Claude Skills explains how to create, structure, and deploy SKILL.md files that automate recurring tasks—with Skills 2.0 adding evaluations, A/B benchmarking, and description optimization for reliable triggering.

## Takeaways
- Skills are reusable instruction files stored in `~/.claude/skills/` that automate recurring Claude tasks, distinct from Projects (knowledge bases) and MCP (connection layers)
- YAML frontmatter with precise trigger descriptions determines when Skills activate; third-person writing with 5-7 trigger phrases and explicit negative boundaries improves reliability
- Five-step process: define job specs precisely, write YAML triggers, structure instructions sequentially under 500 lines, handle reference documents one-level deep, deploy
- Skills 2.0 introduces evaluations (testing outputs against instructions), A/B benchmarking, and description optimization
- Multiple Skills require non-overlapping territories, explicit exclusions, and distinctive trigger phrases to prevent conflicts

## Synthesis
Claude Skills occupy a specific position in the Claude productivity ecosystem that Linas Beliūnas's guide clarifies from the outset: they are instruction automation files, distinct from Projects (which manage knowledge and context) and MCP (which provides connections to external tools). This categorical clarity is itself useful—many power users have these concepts conflated, leading to solutions that work but aren't optimally constructed.

The core mechanism is straightforward. A Skill is a folder containing a SKILL.md file with YAML frontmatter that tells Claude when to activate and structured instructions that tell it what to do. When Claude recognizes a trigger condition matching the Skill's description, it applies the Skill's instructions automatically—transforming a task that would require typing the same multi-paragraph prompt repeatedly into a single recognized phrase.

The YAML description field is the critical component. Beliūnas emphasizes "third-person writing" with explicit trigger phrases and negative boundaries because Claude uses this description to make activation decisions. Vague descriptions produce unreliable triggering; precise descriptions with specific trigger phrases and clear exclusions produce consistent behavior. The recommendation to include 5-7 trigger phrases reflects empirical learning about the pattern diversity needed for robust matching.

The 500-line instruction limit is a practical constraint that forces discipline. Skills longer than 500 lines tend to be doing too many things, which both reduces execution reliability and makes the Skill harder to maintain. The "one-level deep" reference document rule similarly prevents complexity sprawl—Skills that include included files that include other files become difficult to debug when something goes wrong.

Skills 2.0's evaluation and A/B benchmarking capabilities elevate Skill development from craft to engineering practice. The ability to test Skill outputs against defined criteria and compare Skill performance against raw Claude provides the feedback loops necessary for systematic improvement. Description optimization—iteratively improving trigger descriptions based on activation accuracy measurements—turns what was an art into a measurable engineering process.
