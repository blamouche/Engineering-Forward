# GET SHIT DONE: Meta-Prompting System for AI-Assisted Development
**Source**: https://github.com/gsd-build/get-shit-done
**Date**: 2026-03-20
**Author**: TÂCHES (gsd-build)
**Keywords**: meta-prompting, context engineering, Claude Code, multi-agent, agentic development, workflow automation, AI coding

## Elevator pitch
GET SHIT DONE is a lightweight meta-prompting and context engineering system for Claude Code and compatible runtimes that fights "context rot" through structured five-phase workflows and wave-based parallel execution with fresh context windows per agent.

## Takeaways
- Addresses "context rot"—quality degradation as LLMs fill their context windows—through fresh 200K-token context windows per executor
- Five-phase workflow: Initialize, Discuss, Plan, Execute, Verify—each with research, iteration, and verification gates
- Wave-based parallel execution groups dependent tasks intelligently, with atomic git commits per wave for precise history
- XML-formatted task specifications optimize Claude's instruction comprehension and enable multi-agent orchestration
- Supports Claude Code, OpenCode, Gemini CLI, Codex, Copilot, and Antigravity; installable via `npx get-shit-done-cc@latest`

## Synthesis
GET SHIT DONE addresses a problem that becomes apparent only when working with AI agents on non-trivial projects: as conversations grow longer, output quality degrades. The system calls this "context rot," and its entire architecture is organized around preventing it.

The five-phase workflow begins with thorough initialization—comprehensive questioning, domain research, and roadmap generation before any code is written. This front-loaded investment pays for itself by reducing mid-execution ambiguity. The Discuss phase captures implementation preferences before planning begins, avoiding the common failure mode where an agent produces a technically correct but organizationally inappropriate implementation. The Plan phase creates atomic task specifications in XML format and iterates until a verification pass confirms the plan's completeness.

The Execute phase is where the architecture's most interesting decisions manifest. Rather than processing tasks sequentially in a single context window, the system groups tasks into "waves" based on dependency analysis. Each wave spawns fresh executor instances with full 200K-token context windows, preventing any single agent from accumulating irrelevant conversation history that degrades later performance. Each completed task generates an atomic git commit, creating a reversible, inspectable history that makes debugging failed waves tractable.

The XML task specification format is a deliberate engineering choice. Claude processes structured XML-formatted instructions more reliably than natural language task descriptions, particularly for multi-step operations with clear sequencing requirements. By investing in this structured representation upfront, the system trades human readability of intermediate artifacts for execution reliability.

Quick mode allows bypassing the full planning cycle for ad-hoc tasks, preserving the option for lighter-weight usage. The multi-runtime support—spanning Claude Code, Gemini CLI, OpenCode, and others—reflects an awareness that tool ecosystems are still evolving and that lock-in to a single runtime is a liability. For solo developers and small teams that want reliable AI-assisted development without enterprise overhead, GET SHIT DONE offers a practical scaffolding system built on hard-won experience with agentic context management.
