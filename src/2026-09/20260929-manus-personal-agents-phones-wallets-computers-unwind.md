# Manus Personal Agents with Phones, Wallets, and Computers
**Source**: Unwind AI (unwindai@mail.beehiiv.com)
**Date**: 2026-09-29
**Author**: Unwind AI
**Keywords**: Manus 2.0, Cue, personal agents, Cloudflare CLI, Sonnet 5.5, boxd, Fo, ElevenLabs v4, Tapkit, FireRouter, GPT Researcher, Claude Code, Jev, agent infrastructure

## Elevator pitch
Unwind AI covers Manus 2.0 giving each agent its own email, phone number, wallet, and computer — plus the week's agent infrastructure launches: Cloudflare's agent-first CLI, Sonnet 5.5 as cheaper daily driver, boxd's instant-boot VMs, Fo's human-fallback agents, ElevenLabs v4 expressive voice, Tapkit's physical iPhone control, and FireRouter's cost-aware Opus routing.

## Takeaways
- Manus 2.0 launches Cue, giving each agent its own email, phone number, wallet, and computer — agents can take calls, send messages, make approved payments, and keep working after you log off; multiple agents can be put in a group chat to split work across research, shortlisting, outreach, and deliverables
- Cue is free in early access (invite code MEETCUE), with iOS app pending App Store approval — Manus 2.0 is live on web, desktop, and mobile
- Cloudflare released `cf`, an open beta CLI exposing 3,000+ API operations (vs Wrangler's ~280) designed for agents — defaults to JSON, open-source, with `npm i -g cf` install and `cf migrate` for existing Workers
- Claude Sonnet 5.5 launched as faster/lower-cost complement to Opus 5.5: same pricing as Sonnet 5, 30%+ faster generation, up to 30% less cost per task, 70.6% on Terminal-Bench 4.0 (vs 10.3% for Sonnet 5)
- boxd sells persistent KVM Linux machines that boot in <10ms, fork a live machine in <200ms, and hibernate when idle — giving each agent a full machine with root, systemd, Docker, 100GB disk
- Fo (ex-Google DeepMind) launched agents with inbox, phone, voice, credit card, and a builder for anyone to create one — can route to human experts when stuck; 71% task completion, 94% trust rate in internal evals
- ElevenLabs v4 and v4 Turbo: expressive TTS that follows inline direction (laughs, whispers, pauses, accents) in 150ms response time
- Tapkit: Mac app letting agents (Claude, Codex, any MCP client) control a physical iPhone via screenshots and taps — no jailbreak, no simulator, no phone-side install
- Cloudflare open-sourced Forge, the generator behind `cf` — produces SDKs, CLIs, docs, and MCP servers from API definitions
- FireRouter with Opus: cache-aware router choosing between Opus 5.5, GLM 5.3, and GLM 5.3 Flash per turn — cut coding-session cost from $15.36 to $6.63 while retaining 98.1% of Opus-only accuracy
- GPT Researcher dropped embeddings for Jev as context filter: 73% relevant passage retention vs 46% for embeddings at same cost
- Claude Code added `/claude-api build-eval` and `/claude-api hillclimb` to build evals and optimise apps against them

## Synthesis
Manus 2.0's Cue represents the logical endpoint of the personal-agent trajectory: if agents are going to act in the world, they need the same infrastructure humans use — phone numbers for communication, wallets for payment, computers for work, email for identity. The group-chat feature, where multiple agents split a goal across roles, is the agent equivalent of a project team. The question it raises is not technical but social: when an agent has its own phone number and can make calls, how does the human on the other end know they're talking to software?

The infrastructure launches this week form a coherent stack: Cloudflare's `cf` gives agents API access, boxd gives them machines, Tapkit gives them physical device control, ElevenLabs v4 gives them expressive voice, and Fo gives them human fallback. Sonnet 5.5 and FireRouter address the economics — making agent workflows cheaper without sacrificing quality. The GPT Researcher → Jev migration and Claude Code's eval/hillclimb commands show the tooling layer maturing: agents are getting better at knowing what's relevant and at evaluating their own work. The full stack is coming into focus.