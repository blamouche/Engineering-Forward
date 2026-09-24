# Opus 5.5, GPT-6 Sol and Luna
**Source**: Unwind AI (unwindai@mail.beehiiv.com)
**Date**: 2026-09-24
**Author**: Unwind AI
**Keywords**: Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, Jev-Omni, OpenMuse, CopilotKit, Firecrawl Alexandria, Cloudflare Worker Previews, Unreal Agent, JevBench, TypeSafe, prompt cache, formal verification, Boris Cherny, Lean

## Elevator pitch
A packed Unwind AI issue covering Anthropic's Claude Opus 5.5 (Fable 5.1-level performance at 40% less than Opus 5), OpenAI's GPT-6 Sol and Luna (48 on Intelligence Index at $2/$10 per million tokens), plus a wave of Jev ecosystem releases including Jev-Omni for multimodal decisions, a public JevBench leaderboard, and practical tools from Cloudflare, Firecrawl, and Unreal Labs.

## Takeaways
- **Claude Opus 5.5**: First model in the Claude 5.5 family. Matches Fable 5.1-level performance at 40% less than Opus 5. 30%+ faster output. Higher five-hour limits for Pro, Max, Team, and Enterprise. Lower pricing across input, output, and especially cache reads.
- **GPT-6 Sol and Luna**: Intelligence Index score of 48, placing among leading models. $2/M input, $10/M output — 50% lower than GPT-5.6 promotional pricing. Not just a budget Astra but a scale-optimized model.
- **Jev-Omni brings multimodal decisions**: Open-weight model on Gemma 4 12B that makes bounded decisions over text, images, audio, and video — returning probabilities for fixed options instead of generating explanations.
- **JevBench leaderboard live**: 534 English decisions testing intelligence, calibration, speed, and cost. Jev leads, but open models SemIf and djev sit within a point on the combined score.
- **TypeSafe paused new Jev signups**: Immense demand surge forced temporary signup pause one day after removing the waitlist. Existing accounts still work.
- **Opus 5.5 playbook**: Anthropic says stop telling it to "think carefully" — the model already decides how much thinking each reply needs. Define what "done" means and when to stop and ask.
- **Prompt cache survives effort changes**: Changing effort level mid-session no longer invalidates the prompt cache (Claude Code v2.1.280+), enabling long sessions to move between lighter and heavier reasoning without reprocessing cached context.
- **Opus 5.5 + Lean = 16 bug-fix PRs**: Boris Cherny formally verified the Claude Agent SDK, producing 16 PRs fixing bugs and race conditions. Formal verification is becoming usable without being a formal-methods expert.
- **OpenMuse: open-source alternative to Meta Muse**: Self-hostable personal agent with computer use, connectors, goal tracking, mobile and web clients. Runs on any agent harness.
- **Firecrawl's Alexandria**: One place for agents to search live web, 100+ data providers, custom connectors. Ask for jobs above $150K and apartments below $4K — agents compare entire datasets instead of scraping first few links.
- **Cloudflare Worker Previews**: Every Git branch gets its own production-like environment with separate code, config, URL, observability, and state. Durable Objects and Containers isolated per branch — teams and coding agents can test without colliding.
- **Unreal Agent harness**: Open-source, 62 on Terminal-Bench 4.0 at $3.60/task — 39% cheaper than Codex + Astra comparison while maintaining performance.

## Synthesis
This issue captures the AI industry's current phase perfectly: model competition has shifted from capability ceilings to price-performance ratios. Anthropic and OpenAI released dueling mid-tier models within 90 minutes of each other, both targeting the same sweet spot — near-flagship performance at significantly reduced cost. The message is clear: the frontier hasn't stalled, but the action is now in making frontier-adjacent capabilities economically viable for production scale.

The Jev ecosystem is maturing rapidly. Jev-Omni extending decisions to multimodal inputs, JevBench providing public benchmarks, and the signup pause due to demand all signal that the classification model paradigm is gaining real traction. The fact that open alternatives (SemIf, djev) are within a point of Jev on the benchmark suggests the pattern will commoditize — but the category itself is establishing.

Boris Cherny's formal verification work with Opus 5.5 and Lean is a quietly important signal. If formal verification — traditionally requiring PhD-level expertise — is becoming accessible through AI assistance, it has implications for critical software reliability that go far beyond the Claude Agent SDK. The combination of Lean for correctness and TLA+ for concurrency/state analysis, guided by a model that doesn't know either language well, points toward a future where formal methods become a practical tool rather than an academic exercise.