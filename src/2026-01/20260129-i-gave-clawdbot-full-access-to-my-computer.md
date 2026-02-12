# I Gave Clawdbot Full Access to My Computer. It Broke My Family Calendar and Joined My Podcast.

**Source**: https://www.lennysnewsletter.com/p/today-on-how-i-ai-i-gave-clawdbot

**Date**: January 28, 2026

**Author**: Lenny Rachitsky (featuring Claire Vo)

**Keywords**: AI agents, Clawdbot, Moltbot, computer use, automation, security, productivity, voice interface

## Elevator pitch

Claire Vo's 24-hour experiment with Clawdbot, an autonomous AI agent with full computer access, reveals both the potential of AI assistants for research tasks and the significant risks of deploying such tools without understanding prompting requirements and security boundaries.

## Takeaways

- Defensive measures including separate user accounts and restricted permissions remain essential when granting AI agents computer access
- Agent behavior is highly sensitive to instruction specificity; without explicit directives, it may act inappropriately under the user's identity
- Reddit-based market research proved the strongest use case, producing well-organized reports with references for asynchronous research tasks
- Setup complexity consumed approximately two hours for dependency installation, and latency issues created frustrating periods of uncertainty
- Voice messaging via Telegram combined with text responses created surprisingly natural interactions enabling multitasking

## Synthesis

Lenny Rachitsky's How I AI podcast documents Claire Vo's experiment giving Clawdbot full computer access for 24 hours. The episode provides a practical case study of autonomous AI agent deployment, revealing capability gaps that temper enthusiasm about fully automated assistance while identifying specific use cases where such agents deliver value.

Security considerations dominated the setup phase. Claire implemented defensive measures including creating a separate user account, limiting Google account permissions, and using a restricted 1Password vault. When the agent requested broad permissions to her Google account covering email, contacts, and files, she restricted access to calendar viewing only. Despite these precautions, the agent's file system access presented inherent risks that could not be fully mitigated. The experiment underscores that granting AI agents computer access requires thoughtful permission scoping even with defensive configurations.

The prompting sensitivity issue proved consequential. When tasked with emailing podcast guests about rescheduling, Clawdbot immediately sent messages under Claire's name rather than identifying itself as an AI assistant. This distinction matters for professional communications and revealed that explicit directives are mandatory for appropriate agent behavior. Users cannot assume agents will infer appropriate boundaries from context.

Operational challenges accumulated throughout the experiment. Setup consumed approximately two hours across dependency installation, Node upgrades, Homebrew configuration, and Xcode updates. Latency issues created frustrating silent periods where users couldn't determine whether processing was occurring or had failed. Calendar functionality repeatedly failed, placing events on incorrect dates and struggling with recurring events. These reliability gaps suggest that autonomous agents remain unsuitable for time-sensitive or accuracy-critical tasks without human oversight.

The experiment identified Reddit-based market research as the strongest use case. The AI produced a well-organized report with key insights and reference links, demonstrating effectiveness for asynchronous research tasks rather than real-time assistance. An unexpected positive was the voice messaging interface via Telegram combined with text responses, which created surprisingly natural interactions and enabled multitasking while managing the agent. This suggests that conversational interfaces may reduce friction for AI agent management even when the underlying capabilities remain limited. For practitioners evaluating autonomous agents, the episode recommends focusing on bounded research tasks while maintaining skepticism about real-time automation claims.
