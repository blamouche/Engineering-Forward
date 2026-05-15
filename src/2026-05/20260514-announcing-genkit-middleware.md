# Announcing Genkit Middleware: Intercept, extend, and harden your agentic apps
**Source**: https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/
**Date**: May 14, 2026
**Author**: Chris Gill
**Keywords**: Genkit, middleware, agentic apps, Google, observability, retry, fallback, tool approval, skills, TypeScript, Go

## Elevator pitch
Google's Genkit framework introduces middleware — composable hooks that intercept generation calls at three layers (generate, model, tool) — enabling retries, fallbacks, human-in-the-loop approval, and custom enforcement logic for production agentic applications.

## Takeaways
- Middleware hooks attach at three layers: Generate (per iteration), Model (per API call), and Tool (per execution)
- Pre-built middleware includes Retry (exponential backoff), Fallback (switch providers on errors), ToolApproval (human-in-the-loop), Skills (SKILL.md injection), and Filesystem (scoped file access)
- Custom middleware follows a simple contract: provide a name and factory function returning hooks — ~20 lines for a content filter
- Middleware stacks left-to-right with explicit ordering: first listed is outermost wrapper
- Available in TypeScript, Go, and Dart, with Python support coming soon

## Synthesis
Google's Genkit middleware system brings a mature software engineering pattern — middleware/interceptor chains — to AI agent development. The core problem it solves is that production agentic applications need cross-cutting concerns (reliability, safety, observability) that shouldn't be baked into every prompt or tool definition.

The three-layer hook architecture is well-designed for the agent loop. The Generate hook runs once per tool-loop iteration and handles conversation-level logic like context injection. The Model hook runs per API call and handles infrastructure concerns like retry, fallback, and caching. The Tool hook runs per tool execution and handles safety concerns like human approval and sandboxing.

The pre-built middleware covers common needs competently. Retry with exponential backoff and jitter only retries the model call (not the surrounding tool loop), avoiding duplicate side effects. Fallback enables provider switching on quota exhaustion — practical for cost management. ToolApproval enables human-in-the-loop for destructive operations via Genkit's interrupt/resume mechanism.

The custom middleware story is particularly strong: a ~20-line Go struct implementing a content filter demonstrates how teams can enforce organization-specific policies deterministically, rather than relying on prompt engineering alone. The composability model — left-to-right stacking with explicit ordering — makes middleware chains predictable and debuggable.

This positions Genkit as a serious contender in the agent framework space, competing with LangChain and CrewAI by focusing on production concerns that matter at scale: reliability, safety, and observability.
