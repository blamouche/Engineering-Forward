# Agents, Meet the Figma Canvas
**Source**: https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents
**Date**: May 2026
**Author**: Figma
**Keywords**: Figma, MCP, agentic design, use_figma, skills, Claude Code, Codex, design systems, AI agents, canvas

## Elevator pitch
Figma opened its canvas to third-party AI agents through the use_figma MCP tool and introduced skills — markdown-based instructions that teach agents how to produce brand-aligned, design-system-aware output directly in Figma files.

## Takeaways
- The use_figma MCP tool lets Claude Code, Codex, and other agents create and modify Figma files while respecting existing design systems and components
- Skills are markdown files that encode team conventions, workflows, and design standards so agents know "what good looks like" for a given brand
- The generate_figma_design tool (for converting HTML/live apps into Figma layers) and use_figma (for editing within Figma) are complementary: one brings code to the canvas, the other keeps designs in sync
- OpenAI's Codex design lead confirmed the team uses Figma as the shared decision-making space, with Codex now able to find and use design context from Figma files
- This is currently a free beta but will become a usage-based paid feature — Figma is building the commercial model for agent access

## Synthesis
Figma's decision to open its canvas to external AI agents through MCP is an infrastructure play that positions Figma as the central coordination layer for AI-driven product design. The use_figma tool doesn't just let agents generate generic design mockups — it lets them operate within an existing design system, using real components, variables, and conventions. The strategic difference from other AI design tools is that Figma isn't trying to replace designers with prompt-to-mockup generation; it's making the existing design system and canvas the substrate on which agents operate.

The skills system is the key innovation. By encoding team-specific conventions in markdown files, Figma is creating a format for "agent configuration" that's both human-readable and machine-interpretable. Skills define which steps an agent should take, in what sequence, and what conventions to follow — they bridge the gap between an agent that can technically use Figma's API and one that produces work that actually fits a team's standards.

The partnership with OpenAI is notable: Codex uses Figma as the decision-making and refinement space, and now Codex agents can read and write to that same space. Combined with the generate_figma_design tool that converts live HTML/CSS into editable Figma layers, Figma is pursuing a bidirectional bridge between code and design that could make the traditional design-to-code handoff obsolete. The canvas becomes the shared language for both humans and agents.
