# Agent Hooks: Deterministic Control for Agent Workflows

**Source:** [Nader's Thoughts (Substack)](https://nader.substack.com/p/agent-hooks-deterministic-control) — May 15, 2026  
**Author:** Nader Dabit  
**Code:** [GitHub](https://github.com/dabit3/agent-hooks-in-depth)

## TL;DR
Hooks attach user-defined handlers to specific lifecycle points in an agent session, enabling deterministic control over agent behavior. Use prompts for guidance, hooks for behavior that should run every time. Covers six lifecycle points with a companion demo implementing protected paths, command policies, quality gates, and audit logging.

## Key Points

### The Operating Model
```
event → optional matcher/filter → handler → outcome
```

### Six Lifecycle Hooks
1. **SessionStart** — load project conventions, constraints, environment facts
2. **UserPromptSubmit** — inspect prompt, add context, route, or block
3. **PreToolUse** — inspect tool call before execution; block/approve/modify
4. **PostToolUse** — run validation, tests, formatting, logging after tool call
5. **Stop** — prevent agent from finishing if quality gate failed
6. **SessionEnd** — write logs, flush metrics, export summary

### Why Hooks Are Underutilized
- Teams default to adding more prompt instructions (easier to see than lifecycle automation)
- Hooks require setup: picking events, writing scripts, testing payloads
- Their best outputs are avoided mistakes, shorter recovery loops, durable logs — invisible wins

### When to Use Hooks vs Prompts
- **Hooks**: when requirements say "always," "never," "block," "record," "run," "verify"
- **Prompts**: for guidance and judgment

### Concrete Demo Examples
- Protected files (generated/, .env, .git) blocked at PreToolUse
- Dangerous shell commands (rm -rf, cat .env) blocked before execution
- Tests run automatically after code edits via PostToolUse
- Stop hook prevents completion when last quality gate failed
- Audit log written at SessionEnd

### Supported Platforms
- Claude Code, Codex, Cursor, Devin (terminal mode)

## Relevance to Engineering-Forward
Hooks represent the maturation of agent infrastructure — moving from pure LLM-based control to deterministic guardrails. Essential pattern for production-grade agent deployments and CI/CD integration.
