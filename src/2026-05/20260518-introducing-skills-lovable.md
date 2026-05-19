# Introducing Skills: Turn repeated instructions into reusable skills in Lovable

**Source:** [Lovable Blog](https://lovable.dev/blog/introducing-skills) — May 18, 2026  
**Author:** Tyler Bruno

## TL;DR
Lovable introduces "Skills" — reusable markdown-based instructions (SKILL.md files) that the AI agent loads on-demand when relevant. Based on Anthropic's Skills format, now adopted by Lovable, OpenAI, and others. Skills are portable, human-readable, and task-specific (unlike persistent "Knowledge" which is always-on).

## Key Points

### What Skills Are
- Reusable instructions written once, loaded by AI when a matching task appears
- Standard format: markdown files (SKILL.md) with frontmatter (name + description)
- **Portable** across tools (Lovable, Anthropic, OpenAI)
- **Readable** — humans can inspect/audit/share them
- **Editable** — update once, applies forward

### Skills vs Knowledge vs Prompting
- **Prompting** = what you say in the moment
- **Knowledge** = always-on rules/conventions (workspace/project settings)
- **Skills** = task-specific playbooks, loaded on-demand

### How They Work
- Lovable matches skills by **description only** (not instructions), so weak description = unused skill
- Multiple skills can stack on same task (e.g., design-system + landing-page-copy)
- Manual invocation via "/skill-name" in prompt
- Supporting files load only when needed (via markdown links), keeping main file lean

### Example Skills Provided
1. **design-system** — enforces visual rules, colors, spacing, typography, component reuse
2. **fresh-eyes-review** — honest feedback mode from "skeptical visitor with other tabs open"
3. **landing-page-copy** — brand voice, structural rules for conversion

## Relevance to Engineering-Forward
Skills format is becoming an industry standard for agent tooling — central to how deterministic control and reusable context is packaged across AI coding platforms.
