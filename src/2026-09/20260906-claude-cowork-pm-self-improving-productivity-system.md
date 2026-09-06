# Claude Cowork for PMs: How Daniel Blum Built a Self-Improving AI Productivity System
**Source**: https://www.chatprd.ai/how-i-ai/claude-cowork-for-pms-my-self-improving-productivity-system
**Date**: 2026-08-31
**Author**: Daniel Blum (interviewed by Claire Vo on How I AI)
**Keywords**: Claude Cowork, PM productivity, self-improving AI, Notion dashboard, morning brief, context management, AI onboarding, persistence, AI workflows

## Elevator pitch
Melio PM Daniel Blum built a self-improving AI system on Claude Cowork that now handles 70-80% of his workday — managing his Notion board, preparing weekly plans, scanning Slack and email for context gaps, and learning from his edits without explicit feedback — demonstrating how a personal AI system compounds in value over months of investment.

## Takeaways
- The system architecture matters more than the AI tool choice: once a system can update its own core files and connect to tools the user already has, it becomes self-improving regardless of whether it's built on Cowork, Codex, or ChatGPT
- Context is not a one-time setup but an ongoing system: Daniel spent months feeding Claude voice memos, links, decks, and brain dumps to build detailed context files, then created recurring updates that refresh them every few weeks
- The morning brief's most impressive feature is identifying what it doesn't know — Claude reviews Slack, email, and notes for unfamiliar terms or projects, then asks targeted questions to fill those gaps
- A self-improvement loop compares Claude's original drafts with Daniel's final versions, learning from the differences without requiring explicit feedback — it observes actual behavior rather than waiting for ratings
- The Workstation plugin addresses the personalization barrier: a 15-minute onboarding flow connects each employee's tools, maps colleagues, and learns their voice, giving every Melio employee a personalized starting point
- The biggest remaining limitation is persistence, not intelligence: Claude handles 70-80% of Daniel's workday but cannot reliably continue working in the cloud while his computer is off

## Synthesis
Daniel Blum's self-improving PM assistant, built on Claude Cowork, is one of the most detailed examples of a personal AI system that compounds in value over time. The system manages his Notion board as a read-only dashboard, runs a Weekly Prep workflow to kick off each week, generates a Morning Brief that reviews Slack and email for action items, and includes a self-healing context loop that keeps Claude's understanding of the company current.

The architecture is built around several interconnected workflows. The Notion dashboard serves as the front-end UI, organized into "top of mind," "this week," and "inbox" sections — but Daniel almost never touches it directly. His Cowork system built and manages the board entirely on his behalf, migrating him from a messy Google Doc to a structured view that updates automatically from the workflows feeding into it.

The Weekly Prep workflow kicks off each week with a plan, reviewing the previous week's outcomes and setting tactical priorities. The Morning Brief is more sophisticated: Claude reviews Slack, email, and notes for action items, but its most impressive feature is gap detection. When it encounters unfamiliar terms (like "settlement cap"), it has already read the relevant thread and understood the general idea — it only needs Daniel to confirm the meaning before saving it to its context files. This creates a system that actively identifies and fills its own knowledge gaps.

The self-improvement loop is perhaps the most innovative component. Rather than asking Daniel for explicit feedback on every output, the system runs a weekly skill that compares Claude's original drafts with the final versions Daniel actually sent. It learns from the small edits he makes instinctively — the difference between what the AI proposed and what the human chose to change. This resembles Alex Lieberman's "write like me" loop but relies on observed behavior rather than explicit corrections.

The Workstation plugin extends the system beyond a single user. Daniel watched other PMs struggle with his spec-writing tool because it was designed around his own working style. He built an onboarding flow that connects each employee's tools, maps their colleagues, and learns their voice in about 15 minutes, giving every Melio employee a personalized starting point with a strong shared foundation. This addresses one of the biggest barriers to AI adoption inside companies: the cold-start problem of personalization.

The biggest remaining limitation is persistence: Claude cannot reliably continue working in the cloud when Daniel's computer is off. He is already preparing for that future by teaching Claude to recognize the "closed state" of different tasks — if a drafted Slack message is no longer saved, the system can infer it was probably sent. When truly autonomous operation becomes available, his system will already understand what completion looks like.