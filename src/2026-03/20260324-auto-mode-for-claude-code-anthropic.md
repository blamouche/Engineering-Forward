# Auto mode for Claude Code
**Source**: https://claude.com/blog/auto-mode
**Date**: March 24, 2026
**Author**: Unknown
**Keywords**: permissions, safety, Claude Code, tooling, governance

## Elevator pitch
Anthropic introduces “auto mode” for Claude Code, a middle‑ground permission setting that reduces approval prompts while using a safety classifier to block destructive or risky actions.

## Takeaways
- Auto mode is positioned as a safer alternative to --dangerously-skip-permissions for long‑running tasks.
- A classifier reviews each tool call before execution and blocks destructive or sensitive operations.
- If Claude repeatedly proposes blocked actions, it escalates to a user permission prompt.
- Auto mode reduces friction but can still allow risky actions or block benign ones.
- Rollout begins on Team, with Enterprise and API users to follow; admins can disable it via settings.

## Synthesis
Anthropic’s announcement of auto mode for Claude Code aims to solve a familiar tension in agentic development: the safest default is constant human approvals, but that makes long‑running tasks impractical. Auto mode is introduced as a compromise between strict manual gating and the highly permissive `--dangerously-skip-permissions` flag. Instead of removing checks entirely, the system inserts a safety classifier that screens each tool call before it runs.

Operationally, auto mode works by having a separate model review intended actions for potentially destructive behavior—mass deletions, sensitive data exfiltration, or malicious code execution—then automatically allow or block the action. If Claude keeps proposing actions that the classifier refuses, the system escalates to a direct permission prompt. The intent is to allow routine operations (file edits, safe commands) to proceed without human intervention while preserving guardrails for higher‑risk operations.

Anthropic is careful to position this as a risk‑reduction measure, not a risk elimination. The announcement explicitly notes that the classifier can misjudge: it might allow a risky action because the user’s intent is ambiguous or because Claude lacks enough context to understand environmental constraints, and it might block benign actions. Auto mode also adds some overhead in token use, cost, and latency for tool calls. The guidance remains to use auto mode in isolated environments, reinforcing that the feature is a convenience with guardrails rather than a comprehensive security solution.

From a product perspective, the rollout targets Claude Team users first, with Enterprise and API users next. Administrators can disable auto mode via managed settings, and the feature is off by default in the desktop app. For developers, enabling auto mode in the CLI requires a flag, with UI toggles for desktop and the VS Code extension.

The announcement reflects a broader shift in AI tooling: teams want autonomous execution but are wary of invisible, high‑impact actions. Auto mode signals a direction where permission systems become more adaptive and automated, trading absolute control for reduced friction. It also underscores that even with classifiers, trustworthy autonomy depends on environment isolation, clear intent, and continued human oversight for high‑risk steps.
