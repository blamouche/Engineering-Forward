# VS Code Agent Kanban
**Source**: https://marketplace.visualstudio.com/items?itemName=AppSoftwareLtd.vscode-agent-kanban
**Date**: 2026-03-08
**Author**: App Software Ltd
**Keywords**: Kanban board, GitHub Copilot Chat, markdown tasks, git worktrees, agent workflow, VS Code extension

## Elevator pitch
A VS Code extension that integrates a Kanban board with markdown-based task files, enabling structured "plan/todo/implement" workflows alongside GitHub Copilot Chat while maintaining version-controllable conversation history and optional isolated git worktree environments.

## Takeaways
- Dual Workflow Support: Users can work directly in the main workspace or isolate agent work in git worktrees, providing flexibility for different task scales and risk tolerances.
- Context Persistence: The extension uses layered mechanisms (AGENTS.md sentinel markers, per-thread references, and `/refresh` commands) to prevent context decay in long conversations by re-injecting instructions at the system-prompt level.
- Version-Control Friendly Design: Task files use markdown with YAML frontmatter and conversation markers, making them naturally diff/merge-compatible for team collaboration.
- Minimal Agent Customization: Rather than embedding custom LLM logic, the extension leverages Copilot's native agent mode and tool-calling capabilities, positioning itself as a workflow orchestrator.
- Automated Worktree Management: Creating a worktree auto-commits task data, generates task-specific AGENTS.md, and uses `--skip-worktree` to keep modifications independent from the repository.

## Synthesis
Agent Kanban addresses a critical pain point in AI-assisted development: maintaining instruction coherence across long conversations. The extension's central thesis is that "a plan / todo / implement workflow with markdown files that form a permanent record of design choices" strengthens human-in-the-loop development quality. Rather than treating agent interactions as ephemeral chat sessions, tasks become persistent, editable artifacts that capture both decisions and implementation history.

The extension employs a three-layer context injection strategy. At the foundation, it writes a sentinel-delimited section into AGENTS.md that VS Code re-injects at the system-prompt level on every agent turn—a mechanism stronger than one-shot instruction injection because it resists context decay. Complementary approaches include per-thread task file references and an on-demand `/refresh` command for manual context realignment. This redundancy reflects the recognition that no single mechanism fully solves context retention in extended conversations.

The extension provides two operational models. The main-workspace workflow suits small-to-medium tasks where direct editing is acceptable. Users select a task, begin work with commands like "plan," "todo," or "implement," and refresh context as needed. For larger or riskier work, the worktree flow isolates agent operations on a separate branch in a distinct directory—the extension automates setup including branch creation and AGENTS.md configuration.

Tasks live as flat markdown files in `.agentkanban/tasks/`, with lane assignment stored in YAML frontmatter rather than directory structure. This design philosophy prioritizes text-based, diff-friendly storage, enabling teams to version-control and merge task boards as code.

The extension is explicitly designed not to implement custom LLM logic, instead delegating all work to Copilot's native agent mode. This simplifies development and avoids vendor lock-in but ties functionality to GitHub Copilot's capabilities. Overall, Agent Kanban represents a pragmatic engineering approach to the context-decay problem in agent-assisted development, trading sophisticated prompt engineering for transparent, version-controllable artifacts and structural redundancy in context delivery.
