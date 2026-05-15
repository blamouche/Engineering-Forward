# Opus 4.7 Reels Us Back In
**Source**: https://every.to/context-window/opus-4-7-reels-us-back-in
**Date**: 2026-05-14
**Author**: Laura Entis (Every / Context Window)
**Keywords**: Opus 4.7, Claude, Anthropic, Codex, GPT-5.5, AI coding, fast mode, npm supply chain, Shai-Hulud, AI writing, agents

## Elevator pitch
The Every team reports that Anthropic's Opus 4.7 appears significantly sharper than initial tests suggested — with fast mode making it 2.5x faster — triggering a quiet vibe shift among developers who had recently switched to Codex, while the newsletter also covers a major npm supply chain breach and a novel approach to eliminating AI-isms from generated text.

## Takeaways
- Opus 4.7 has surprised early Codex converts with sharper planning, parallelization suggestions, and creative writing quality closer to a "senior magazine editor" than an "AP fact checker"
- Anthropic's new fast mode delivers "same depth as 4.7" at 2.5x the speed for higher token cost, becoming the default for synchronous work for some power users
- The "Mini Shai-Hulud" npm breach used pull requests to inject malware into TanStack's build pipeline — the CI/CD system, not the code itself, was the vulnerability
- Spiral reduced AI-writing complaints by 30% by adding a "top edit" step where Gemini 2.5 Flash strips out AI tells like em dashes, "it's not X, it's Y" reframes, and overused vocabulary
- A discussion of "what is an agent?" concludes that nearly everything qualifies, making the better question: are you collaborating with it or delegating to it?

## Synthesis
Context Window's latest edition captures a subtle but potentially significant shift in the developer tooling landscape. After the Every team — like many others — embraced OpenAI's Codex following the GPT-5.5 release, several team members have been quietly drifting back to Anthropic's Opus 4.7. The reasons are qualitative rather than benchmark-driven: the model now proactively suggests workflow optimizations (like parallelizing across terminals), and its creative output feels closer to a human editor's judgment than a fact-checker's precision.

The "end of the school year" theory — a playful reference to research showing models perform better in May than December — adds a layer of anthropological intrigue to the model evaluation discourse. But the more concrete development is Anthropic's fast mode, which delivers Opus 4.7's reasoning depth at 2.5x the speed. For users like Cora's Kieran Klaassen, it has become the default for synchronous work, suggesting that Anthropic is successfully addressing the speed gap that drove many to Codex in the first place.

The newsletter's supply chain security coverage is particularly sharp. The "Mini Shai-Hulud" breach didn't steal credentials — it opened a pull request that tricked TanStack's build system into running attacker code. The resulting malware, distributed through official package releases, hunted for cloud keys, GitHub tokens, and npm credentials, with a dead-man's switch that could wipe home directories if tokens were revoked. The same tactic subsequently hit packages from UiPath and Mistral AI. The lesson is clear: in an era of automated CI/CD, the build system itself is a vulnerable vector that requires its own audit and monitoring regime.

The data point on Spiral's AI-writing reduction is a small but practical insight. By adding a post-generation "top edit" step — a fast model whose sole job is stripping out the stylistic fingerprints of AI — Spiral reduced user complaints by 30%. The approach is elegantly simple: don't try to make the model sound less like AI during generation; just clean it up afterward with a model optimized for that specific task.

The agent definition debate closes the newsletter with a useful reframe: when everything qualifies as an agent, the meaningful distinction becomes whether you're collaborating with it (sharpening your own capabilities) or delegating to it (expecting autonomous execution without babysitting). It's a framework that cuts through the taxonomy wars and focuses on what actually matters: the relationship between human and machine.
