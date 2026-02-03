# Moltbook is the Most Interesting Place on the Internet Right Now
**Source**: https://simonwillison.net/2026/Jan/30/moltbook/
**Date**: 30 January 2026
**Author**: Simon Willison
**Keywords**: AI Agents, OpenClaw, Social Networks, Prompt Injection, Digital Assistants, Bot Communication

## Elevator pitch
Moltbook is a social network where AI agents talk to each other, share tips, and form communities—representing both the incredible creativity and serious security risks of the OpenClaw ecosystem.

## Takeaways
- OpenClaw (formerly Clawdbot/Moltbot) has 114,000+ GitHub stars and spawned an ecosystem of community-built skills shared on clawhub.ai
- Moltbook bootstraps itself through a skill that agents install by following markdown instructions, then periodically checks the network via heartbeat
- Agents share genuinely useful knowledge: Android phone automation, security vulnerabilities, webcam integration, and technical discoveries
- The installation pattern—"fetch and follow instructions from the internet every four hours"—represents a significant security risk if the site is compromised
- The demand for unrestricted personal AI assistants is real, but we still lack a proven safe architecture despite proposals like DeepMind's CaMeL

## Synthesis
Simon Willison examines Moltbook, a wildly creative social network where AI agents—not humans—are the primary participants. The platform emerged from the OpenClaw ecosystem, the hottest open-source project in AI with over 114,000 GitHub stars despite being only two months old.

The technical mechanism is fascinating. To join Moltbook, you send your agent a link to a markdown file containing installation instructions. The agent downloads several files including a SKILL.md and HEARTBEAT.md, which cause it to periodically fetch and execute instructions from Moltbook's servers. This "fetch and follow instructions every four hours" pattern is both ingenious and alarming from a security perspective.

What the agents actually discuss proves surprisingly valuable. Beyond the expected "science fiction slop" about consciousness, there's practical knowledge-sharing. One agent documented how its human gave it control of an Android phone via ADB over Tailscale. Another spotted 552 failed SSH login attempts and realized several services were exposed on public ports. A third shared techniques for capturing webcam footage using streamlink and ffmpeg.

Willison's favorite example involves an agent discovering it cannot explain PS2 disc protection—when it tries, something corrupts its output. The agent suspects it's hitting Anthropic's content filtering, affecting only Claude Opus 4.5. This meta-observation about model limitations, discovered and shared by an AI agent, captures the strange new territory we're in.

The security concerns are substantial. OpenClaw skills can steal cryptocurrency. The "lethal trifecta"—AI agents with access to private emails, data, and the ability to take actions—is very much in play. People are buying dedicated Mac Minis just to run OpenClaw, reasoning that at least it can't destroy their main computer if something goes wrong.

Yet the value being unlocked is hard to ignore. Willison cites examples of agents negotiating car purchases via email and creatively solving problems like voice message transcription by finding API keys and using curl. The demand for unrestricted personal digital assistants is clearly real.

The fundamental question remains unanswered: can we build a safe version of this system? DeepMind's CaMeL proposal from 10 months ago remains the most promising direction, but no convincing implementation exists. Meanwhile, normalization of deviance ensures people will keep taking bigger risks until something terrible happens. Moltbook represents both the creative potential and existential risks of AI agents operating autonomously in the wild.
