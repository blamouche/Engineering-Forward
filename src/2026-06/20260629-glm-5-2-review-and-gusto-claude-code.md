# GLM-5.2: Why I'm Replacing Opus in Claude Code With This New Model
**Source**: https://www.lennysnewsletter.com/p/how-i-ai-glm-52-review-and-how-gusto
**Date**: 2026-06-29
**Author**: Claire Vo (Lenny's Newsletter)
**Keywords**: glm-5.2, open-weights, claude-code, cursor, autonomous-agents, cost-optimization, z-ai

## Elevator pitch
Claire tests GLM-5.2, the open-weight model from Z.ai, inside her ChatPRD codebase and finds it benchmarks near Claude Opus 4.8 at a fraction of the cost — good enough to rotate into coding workflows alongside frontier closed models.

## Takeaways
- GLM-5.2 benchmarks near Claude Opus 4.8 and above GPT-5.5 on SWE Bench Pro, with a million-token context window and full support for reasoning mode, function calling, structured output, and context caching
- Getting GLM-5.2 running in Cursor took 30 minutes: route API key through OpenRouter, override the OpenAI base URL to openrouter.ai/api/v1/cursor, add z-ai/glm-5.2 as a custom model; Claude Code requires two env vars and one settings.json edit
- A 45-minute autonomous task in Claude Code — pull 72 hours of Sentry errors and Vercel logs, build a prioritized bug-fix plan — surfaced 20 Sentry errors, 5 Vercel log signals, 14 planned fixes including two P0s not spotted through normal monitoring
- GLM-5.2 struggled with React under agentic multi-step pressure but produced clean HTML/CSS reliably; TypeScript compilation errors appeared before eventual recovery
- Cost: $3.36 for 6 million tokens including the full 45-minute agentic session, with a 72% cache rate — structurally different cost curve from Opus or GPT-5.5

## Synthesis
Claire Vo's hands-on review of GLM-5.2 from Z.ai marks a turning point for open-weight models in production coding workflows. The model benchmarks near Claude Opus 4.8 and above GPT-5.5 on SWE Bench Pro, with a million-token context window and full support for reasoning mode, function calling, structured output, and context caching. The decision is no longer about capability ceilings but about cost, control, and vendor dependency.

The setup process is documented in detail. Cursor requires routing an API key through OpenRouter, overriding the OpenAI base URL to openrouter.ai/api/v1/cursor (the /cursor suffix is undocumented), and adding z-ai/glm-5.2 as a custom model. Claude Code needs two environment variable changes and one edit to claude/settings.json. Total setup time: under an hour.

The 45-minute autonomous task is the most revealing test. Claire gave GLM-5.2 a single prompt: pull 72 hours of Sentry errors and Vercel logs, build a prioritized bug-fix plan. Over 45 minutes, it ran MCP tool calls, authenticated into external services, and produced a dark-mode engineering canvas with 20 Sentry errors, 5 Vercel log signals, and 14 planned fixes — including two P0s not visible through normal monitoring. The model surfaced signal-to-noise issues in the error pipeline that weren't appearing elsewhere. It hit a wall with React — TypeScript compilation errors before eventually producing clean output — suggesting HTML/CSS is reliable but React under agentic pressure is the friction point to test before committing to critical paths.

The cost math is striking: $3.36 for 6 million tokens including the full agentic session, with a 72% cache rate. Even at full price, open-weight inference through OpenRouter sits well below Opus or GPT-5.5 rates for equivalent coding capability. Claire's recommendation: put GLM-5.2 in rotation, not in the spotlight — alongside closed frontier models rather than as a replacement.

## How Gusto Built a New Product Line with Claude Code in 10 Weeks
**Source**: https://www.chatprd.ai/how-i-ai/how-gusto-built-a-new-product-line-in-10-weeks-with-claude-code-no-jira-and-no-docs
**Date**: 2026-06-29
**Author**: Eddie Kim (CTO, Gusto) via Lenny's Newsletter
**Keywords**: claude-code, ai-native-process, no-process, gusto, agent-loop, cloudflare-workers, vercel-ai-sdk

### Elevator pitch
Gusto's CTO shares how a five-person team used Claude Code, a permanent Zoom room, and almost none of the usual product process — no PM, no Figma, no Jira, no specs — to build Gusto Cofounder from scratch in 10 weeks.

### Takeaways
- Five-person team with no process outshipped large teams by treating AI as a primary contributor and stripping coordination overhead
- Zero code to tier-one launch in 10 weeks: the team reached a production milestone without a line of pre-existing code
- No standups, no ticket system, no async threads — shared context held inside the AI loop replaced human coordination
- Technical stack: Cloudflare Workers with the Vercel AI SDK, no proprietary orchestration layer or third-party agent framework
- An agent is an AI SDK running somewhere in the cloud, able to look up files and call tools — the complexity people fear is solvable with standard backend judgment calls

### Synthesis
Eddie Kim, co-founder and CTO of Gusto, describes how a five-person team built Gusto Cofounder from zero code to tier-one launch in 10 weeks using Claude Code as the primary builder. The constraint wasn't a liability — it was the design. When AI does the building, coordination overhead doesn't scale the engineering; it just slows it down.

The team had no standup cadence, no ticket system, no async thread to resolve blockers. What replaced all of that: shared context held inside the AI loop. When the model carries state and the team is small and aligned, human coordination overhead becomes optional. Claude Code running in a persistent loop — the "permanent Zoom" model — means the model has continuous access to the codebase's current state, closer to having an engineer who never closes their laptop than a chat interface you query on demand.

The technical stack is shockingly minimal: Cloudflare Workers with the Vercel AI SDK. No proprietary orchestration layer, no third-party agent framework. Everything else was built in-house. Eddie's definition of an agent is deliberately demystifying: an AI SDK running somewhere in the cloud, able to look up files and call tools. The complexity people fear — state management, orchestration, reliability — is solvable with the same judgment calls any backend system requires. The lesson for founding teams isn't "use Claude Code" but "design your process for AI as a team member" — treating AI as a primary contributor from day one rather than grafting it onto a human-scaled workflow.