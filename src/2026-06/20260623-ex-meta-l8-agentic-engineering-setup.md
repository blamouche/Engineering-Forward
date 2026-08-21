# An Ex-Meta L8's Agentic Engineering Setup
**Source**: https://blog.bytebytego.com/p/an-ex-meta-l8s-agentic-engineering-setup
**Date**: 2026-06-23
**Author**: Kun Chen
**Keywords**: agentic engineering, Claude Code, Codex, workflow, voice input, planning, code review, parallel agents

## Elevator pitch
Former Meta L8 principal engineer Kun Chen shares his complete agentic engineering setup—from terminal and Neovim configuration to voice input, interactive planning with Lavish Editor, the "good night, have fun" orchestrator for overnight tasks, and a validation pipeline called no-mistakes that catches 68% of bugs before they reach human review.

## Takeaways
- The author acts as an engineering manager directing agents rather than writing code himself; his workflow is agent-agnostic, switching between Claude Code and OpenCode to avoid vendor lock-in
- Voice input (OpenSuperWhisper with Whisper turbo v3 large, running locally) is one of the biggest productivity levers—you talk much faster than you type, and it works for prompting agents, writing articles, and anything else requiring text
- Delegation like a manager means asking for outcomes not actions, explaining the "why," and never taking back control—writing feedback into CLAUDE.md or AGENTS.md so the agent self-corrects instead of reverting to manual work
- Complex work benefits from upfront planning: the author built Lavish Editor (open-source) for interactive HTML-based planning with agents, replacing markdown proposals with clickable, annotatable visual plans
- The "good night, have fun" (gnhf) orchestrator breaks big tasks into steps with fresh context windows, automatic rollback on failure, and token budgets—enabling overnight implementation of massive plans, metric improvement, and batch experiments

## Synthesis
Kun Chen's setup is built around a terminal-first philosophy: WezTerm as the only terminal emulator, Neovim with oil.nvim/neogit/snacks.nvim plugins for quick file operations and git review, tmux for session/window/pane management, and a left-right split with an agent on the left and Neovim on the right. He explicitly avoids agent-specific "fancy" features like auto-managed memory to maintain vendor independence.

The biggest productivity insight is the delegation mindset. Instead of "rename this variable" (action), you say "audit this codebase to follow this convention" (outcome). This lets the agent run longer, produce better-aligned work, and learn conventions for future sessions. When agents make mistakes, Chen writes feedback directly into memory files rather than doing the work manually.

For complex features, Chen built Lavish Editor, an open-source tool that renders agent plans as interactive HTML pages. Instead of editing a markdown file, you click elements in the browser to annotate them. The agent iterates based on your visual feedback, making planning collaborative and concrete rather than abstract.

Validation is handled by no-mistakes, another open-source tool: it reviews code in a fresh context window (to avoid confirmation bias), escalates ambiguous product decisions to the human, forces end-to-end evidence over just unit tests, and runs the full pipeline from branch creation through CI automatically. Chen reports that 68% of changes pushed through no-mistakes had bugs caught before reaching him.

For parallel work, Chen built treehouse, which manages a pool of git worktrees—dropping you into a ready worktree with dependencies, build artifacts, and env files already in place, so you don't think about where to work, just what to work on. He typically runs 5-10 tasks simultaneously.

Remote access is handled via Tailscale and mosh (for resilient SSH over flaky networks), letting him SSH from his phone into his Mac, attach to the tmux session, and pick up exactly where he left off.