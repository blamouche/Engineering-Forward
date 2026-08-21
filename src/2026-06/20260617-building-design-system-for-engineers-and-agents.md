# Building a Design System Specced for Engineers and Agents

**Source**: https://evilmartians.com/chronicles/building-a-design-system-specced-for-engineers-and-agents
**Date**: 2026-06-17
**Author**: Evil Martians
**Keywords**: design-systems, ai-coding, engineering-practices, oklch, figma, storybook

## Elevator pitch

Evil Martians demonstrates how to build an AI-readable design system in seven weeks—one that both engineers and coding agents can use without a designer in the room—by making every design decision explicit, machine-parseable, and obvious.

## Takeaways

- AI-assisted coding amplifies design divergence: without a design foundation, every AI-generated PR risks adding new inconsistent components, making design systems more urgent than ever.
- An AI-assisted audit of 791 files with design information was completed in one-third the time a manual audit would take, revealing 236 unique colors with 1,413 uses across five competing color systems.
- The typography system uses Innovator Grotesk (metrics-matched to Inter) with six sizes and five token groups, each with a dedicated job—so there's exactly one correct token for each use case.
- Colors are defined in OKLCH, making them AI-readable: an agent can extend the palette by holding hue and lightness constant while stepping chroma, producing values that belong to the system rather than drifting one-offs.
- The 1,413 color usages were collapsed into four groups (elevation, content, UI, border), and AI mapped ~90% of the 191 legacy icons to the new Figura One set automatically.

## Synthesis

Evil Martians' work with Currents—a test observability platform for Cypress and Playwright—illustrates a problem that's becoming acute as AI coding tools proliferate: without a design system, AI-generated code introduces inconsistencies at the same velocity it produces features. Currents' CEO Andrew Goldis articulated the tension: his team was using Cursor and Claude for code generation, but every AI-assisted PR risked adding new, inconsistent components. The business case was clear—improve the UI to enable confident go-to-market—but the technical solution needed to work for engineers and agents alike.

The process began with an AI-assisted audit of 791 files containing design decisions. In a third of the time a manual audit would take, the team cataloged two competing icon libraries, two font systems, 236 unique colors, and inconsistent button and filter components. This audit became the foundation for a design system built on a critical principle: every decision should have exactly one correct answer, obvious to both humans and machines.

Typography uses Innovator Grotesk, chosen because its metrics match the team's existing Inter font—enabling an immediate switch with no layout reflow. The type scale has six sizes and five token groups, each with a single job. When an engineer or agent needs a button label, there's exactly one correct token: `ui.default`. No judgment calls, no design debates.

Colors follow the same principle, but with an additional trick: OKLCH encoding. Because OKLCH expresses colors as human-readable lightness, chroma, and hue, an AI agent can extend the palette programmatically. "Give me a border one step softer than `border.default`, same hue" produces a value that belongs to the system rather than a one-off hex that drifts. This is genuinely novel—making a design system legible not just to humans but to LLMs.

The migration story is equally pragmatic. AI mapped ~90% of 191 legacy icons to the new Figura One set, generating a lookup table that an engineer or agent can follow icon by icon with no judgment calls. The 1,413 color usages were collapsed into four groups with clear jobs. The design system lives in Figma, Storybook, and GitHub—accessible from wherever the team works.

The broader lesson is clear: the cost of building without a design foundation has become exponentially higher as AI coding tools amplify both productivity and inconsistency. A design system that's AI-readable isn't a luxury—it's a prerequisite for teams shipping AI-generated code at scale. If at least two of these signals apply—your product is technical but the UI doesn't inspire confidence, your team uses LLMs for coding without a designer, or you can name three places where the same components follow different rules—it's time to invest.