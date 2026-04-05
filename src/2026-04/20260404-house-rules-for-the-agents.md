# House Rules for the Agents

**Source**: https://every.to/context-window/house-rules-for-the-agents
**Date**: April 4, 2026
**Author**: Every Staff
**Keywords**: OpenClaw, Anthropic, prompt caching, AI subscriptions, video understanding, Gemma 4, Cursor, AI adoption

## Elevator pitch
Every argues that model providers should meter costly usage patterns instead of banning specific interfaces, while highlighting how falling multimodal costs and agent-native tools are reshaping practical AI work.

## Takeaways
- Every criticizes Anthropic’s decision to single out OpenClaw in Claude Max policy changes and argues usage should be priced by cost rather than by interface.
- Prompt caching is presented as the underlying technical reason third-party clients can become more expensive to serve.
- Gemma 4 materially lowers the cost of practical video understanding, potentially unlocking consumer and operational use cases.
- The issue ties product policy, infra economics, and tool design together instead of treating them as separate topics.
- Its curated links reinforce a broader pattern: agent-native workflows are becoming the center of software design and adoption.

## Synthesis
House Rules for the Agents is a newsletter-format piece, but its strongest section is an argument about platform economics. Every’s team pushes back on Anthropic’s decision to name OpenClaw specifically in new subscription restrictions. Their point is not that serving heavy third-party usage is free. It is that the boundary should be set at cost, not at interface. If prompt caching failures or other integration details increase inference expense, then meter those users accordingly. Do not punish a category of client outright.

The prompt-caching discussion is useful because it moves the debate beyond vibes. Small changes to prior conversation state can invalidate cache reuse and force expensive recomputation. That makes some wrappers materially more costly for model providers. But the piece argues that technically understandable costs do not automatically justify strategically clumsy policy. Singling out one interface risks confusing users, weakening trust, and creating churn precisely when providers are competing to become the default substrate for third-party tools.

The second notable thread is Mike Taylor’s estimate that video understanding has become dramatically cheaper thanks to Gemma 4. If the numbers are directionally right, the implication is significant: video analysis is moving from expensive novelty to usable infrastructure. A fortyfold drop in effective cost changes what builders consider feasible, especially for security footage review, sports commentary, and consumer-device summaries. These are not moonshots; they are straightforward product categories that were previously too awkward or expensive to justify.

Taken together, the newsletter sketches the shape of the next platform fight. Model providers want to control cost and capture value. Tool builders want flexibility and interface freedom. Users want predictable pricing and practical capability. As multimodal costs fall and agent-native products mature, the winners will likely be the companies that can balance those three pressures without making the ecosystem feel hostile.
