# Developer's Guide to Building ADK Agents with Skills
**Source**: https://developers.googleblog.com/en/developers-guide-to-building-adk-agents-with-skills/
**Date**: April 1, 2026
**Author**: Lavi Nigam and Shubham Saboo (Google)
**Keywords**: Google ADK, Agent Development Kit, skills, progressive disclosure, token efficiency, L1/L2/L3 knowledge

## Elevator pitch
Google's ADK uses progressive disclosure of skills (L1 metadata ~100 tokens, L2 full instructions <5,000 tokens, L3 resources as needed) to reduce token usage by up to 90% compared to monolithic system prompts.

## Takeaways
- Three knowledge levels: L1 (~100 tokens, skill names for decision-making), L2 (<5,000 tokens, full skill body when activated), L3 (external resources loaded conditionally)
- Four skill patterns: Inline (hardcoded, simple), File-Based (SKILL.md directory structure), External (downloaded from agentskills.io), Skill Factory (meta-skills that generate new skills)
- 90% token reduction vs. monolithic system prompts through progressive disclosure
- Best practice: maintain human oversight for Skill Factory-generated skills before deployment
- Start simple with inline implementations; graduate to file-based to prevent over-engineering

## Synthesis
Google's ADK progressive disclosure architecture addresses one of the fundamental inefficiencies in current agent design: monolithic system prompts that include all domain knowledge regardless of whether it is relevant to the current task. An agent that handles both customer support and code review queries doesn't need both sets of expertise in its context simultaneously — it needs the relevant expertise loaded when each type of query arrives.

The three-level knowledge hierarchy is elegantly simple. L1 metadata (skill names and short descriptions, ~100 tokens per skill) gives the agent enough information to decide which skill is relevant without loading the full skill body. Once a skill is selected, L2 instructions (the full skill body, under 5,000 tokens) are loaded into context. L3 resources — detailed reference materials, examples, and external data — are loaded only when the skill's instructions explicitly call for them. The 90% token reduction claim reflects the difference between loading 10+ full skill bodies at session start vs. loading only the 1-2 skills actually needed for a given interaction.

The Skill Factory pattern is the most sophisticated element. A meta-skill that can generate new skill definitions at runtime enables agents to create specialized capabilities for novel task types without requiring developer intervention. This is analogous to code generation — the agent can author new expertise modules in response to requirements — but it introduces the risk that generated skills may behave unexpectedly. The recommendation to treat Skill Factory outputs like code dependencies requiring human review before deployment is appropriately cautious.

The agentskills.io specification mentioned in the External Skills pattern suggests Google is positioning skill repositories as a shareable infrastructure layer — analogous to npm for JavaScript packages. If skill definitions become standardized and shareable across organizations, the collective investment in skill quality compounds across the ecosystem rather than requiring each organization to develop their own skills from scratch.

For teams currently using monolithic system prompts, the progressive disclosure pattern offers a straightforward refactoring path: identify distinct domains of expertise in the current prompt, extract them into separate skill definitions, and implement L1 routing logic to load them on demand.
