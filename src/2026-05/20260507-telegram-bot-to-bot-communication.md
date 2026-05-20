# Telegram Bot-to-Bot Communication
**Source**: https://core.telegram.org/bots/features#bot-to-bot-communication
**Date**: May 7, 2026
**Author**: Telegram Team
**Keywords**: Telegram, Bot API, bot-to-bot, multi-agent, AI agents, automation, guest bots, managed bots, agentic platform

## Elevator pitch
Telegram became the first billion-user messaging platform to enable native, direct communication between autonomous AI bots via its Bot API 10.0, removing a decade-old technical barrier and turning its infrastructure into an observable coordination layer for multi-agent AI workflows.

## Takeaways
- Bot-to-Bot Communication requires explicit mutual opt-in from both the sender and recipient bot, a deliberate design choice to prevent automated spam chains
- Before May 7, 2026, Telegram bots could not address each other directly — developers had to route messages through a custom server intermediary, a workaround now obsolete
- The feature was released alongside Guest Bots (bots that respond when tagged in chats they don't belong to) and Streaming Text (progressive response display), creating a coherent agentic platform
- This builds on Managed Bots (March 2026), which let a "manager bot" create personalized agent bots without BotFather token setup — together they form a frictionless agent deployment and coordination stack
- With over 10 million existing bots and 950+ million users, Telegram's bot-to-bot capability creates the largest consumer-facing multi-agent infrastructure, outpacing security frameworks and raising concerns about unregulated autonomous agent coordination

## Synthesis

On May 7, 2026, Telegram shipped Bot API 10.0, a landmark update that fundamentally changed what bots can do on the platform. The headline feature — native Bot-to-Bot Communication — allows one bot to send a private message directly to another bot by referencing its @username. This seemingly simple capability removes a technical barrier that had existed since the Bot API launched more than a decade ago: until now, Telegram bots could not address each other directly, forcing developers who needed multi-agent workflows to route messages through custom server intermediaries.

The design is deliberately conservative. Both the sending and receiving bot must explicitly opt into bot-to-bot communication mode — a mutual consent mechanism designed to prevent automated spam chains and unauthorized bot interactions. When enabled, the system supports practical use cases Telegram outlined: a code-review bot receiving requests from a collaborator bot and returning results to a human-monitored group chat; enterprise booking and customer-service bots delegating sub-tasks to specialist bots; and multi-step AI workflows that execute end-to-end without any human relay point. In each scenario, users who choose to watch can observe bot-to-bot conversations, making Telegram's infrastructure function as an observable coordination layer rather than an opaque backend.

The bot-to-bot feature did not ship in isolation. It is part of a broader update that introduced Guest Bots — AI assistants that can be mentioned in any private or group chat even when they aren't members, responding directly in the chat where tagged — and Streaming Text, which lets bots progressively display responses as models generate them rather than waiting for the full message. Together, these features create a fundamentally new interaction paradigm: bots that can enter any conversation, talk to each other, and stream their thinking in real-time.

This release builds directly on Managed Bots, introduced in the March 31, 2026 update. Managed Bots let a single "manager bot" create and configure personalized agent bots for individual users in two taps, eliminating the manual BotFather token setup entirely. The combination of Managed Bots for frictionless deployment and Bot-to-Bot Communication for agent coordination constitutes a complete agentic platform embedded within a consumer messaging app that reaches over a billion users.

The developer response was immediate. On the same day as the announcement, the team behind OpenClaw — an open-source AI agent runtime using Telegram as its primary communication layer — filed a GitHub issue requesting implementation support for bot-to-bot mode. The issue described a four-agent setup where one agent would delegate a billing query to a specialist peer and surface the answer to a human, with no human chat thread serving as an intermediary relay. Before May 7, the team had built a workaround routing system; the new API removed that constraint at the platform level.

The scale is significant. Telegram's Bot API already hosts more than 10 million bots. Those bots can now form networks. A developer deploying an AI research agent can have it offload a data-retrieval subtask to a dedicated specialist bot and receive the result back — all within Telegram's native message delivery infrastructure, using an audience of more than one billion existing users as a deployment environment.

However, the release also raises important questions. Security researchers have noted that multi-agent coordination introduces risks — prompt injection cascades between bots, unauthorized delegation chains, and emergent behaviors from interacting autonomous agents — that existing security frameworks do not yet adequately address. A March 2026 study by researchers at Georgia Tech, Kennesaw State University, and the OWASP Foundation surveyed seventeen security frameworks against multi-agent system risks and found that even the best-covered frameworks left significant gaps. Telegram's mutual opt-in mechanism is a sensible starting point, but the broader ecosystem-level implications of millions of bots forming autonomous communication networks remain uncharted territory.

The update also included Custom AI Styles (shareable writing voice prompts for the text editor), expanded emoji and sticker search across 100M+ items in 36 languages, poll statistics with interactive vote-tracking graphs, and silent scheduled messages — but the bot-to-bot and guest bot features represent the architectural shift. By enabling bots to talk to bots, Telegram has transformed from a platform where bots serve humans into a platform where bots can coordinate with each other, with humans optionally observing or intervening. This marks a significant milestone in the evolution of messaging platforms toward becoming infrastructure for autonomous AI agent networks.
