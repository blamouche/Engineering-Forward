# Superpowers

**Source**: https://github.com/obra/superpowers?utm_source=www.theunwindai.com&utm_medium=newsletter&utm_campaign=openclaw-that-runs-on-10-hardware&_bhlid=65b92fb99406f6177152dbcb8f582fdf2c110164

**Date**: Unknown

**Author**: Jesse

**Keywords**: coding agents, skills, workflows, TDD, subagent development

## Elevator pitch

Superpowers is a skills-driven workflow that turns coding agents into disciplined, plan-first, test-first collaborators by automating design, planning, and execution rituals.

## Takeaways

- Superpowers layers a structured, skills-based workflow on top of coding agents to reduce ad-hoc behavior.
- The process emphasizes design validation, bite-sized planning, and subagent-driven execution.
- Test-driven development is enforced as a first-class norm, not an optional best practice.
- Installation differs across platforms, with plugin marketplaces for Claude Code/Cursor and manual setup for others.
- The skill library covers brainstorming, planning, debugging, collaboration, and workflow completion.

## Synthesis

Superpowers presents itself as a complete workflow for coding agents, built on a library of composable skills that trigger automatically during a development session. The core promise is to take the chaotic, often unstructured behavior of AI coding assistants and replace it with a predictable process that mirrors a disciplined engineering team. Instead of jumping directly into implementation, the system prompts the agent to clarify intent, gather requirements, and produce a readable design in small chunks that a human can actually review. This early design checkpoint is positioned as a gate: you validate the direction before any code is written.

Once the design is accepted, Superpowers shifts the agent into a planning mode. The plan is deliberately granular, aiming for tasks small enough for a junior engineer to execute confidently. It also reinforces core engineering heuristics like YAGNI and DRY, and it explicitly calls out a red/green TDD loop as mandatory. The workflow then moves into subagent-driven development or batched execution, where each task is handled by a fresh subagent that is expected to follow the plan and then review its own work against the specification. The intent is to create a double-check mechanism that reduces drift and improves compliance with the original design.

The system highlights several built-in skills that map to common phases of an engineering cycle: brainstorming, planning, executing, testing, debugging, code review, and branch cleanup. This list doubles as an opinionated checklist of what “good” looks like in AI-assisted development. Instead of relying on a single assistant to remember to do all these steps, Superpowers encodes them as reusable skills that are invoked automatically when the context matches. That automation is the main leverage point: you are not manually prompting the agent to plan or to test; the agent does it because the workflow requires it.

Installation is designed to match how different tools work. Claude Code and Cursor use plugin marketplaces, while Codex and OpenCode rely on manual instructions fetched from repository files. This emphasis on distribution channels reinforces that Superpowers is not a codebase as much as a behavioral overlay. The repository functions as a skill library and a set of rules of engagement that shape how the agent behaves, rather than adding features to a specific IDE.

The philosophy section makes the intent explicit: systematic processes over ad-hoc hacking, verification over claims, and simplicity over unnecessary complexity. The broader implication is that AI coding assistants only become trustworthy when they follow the same professional norms that human teams use. Superpowers does not claim to improve model capability; it claims to improve the reliability of outcomes by enforcing rituals. If that framing holds, the value is less about novel tooling and more about institutionalizing “good habits” for autonomous agents.
