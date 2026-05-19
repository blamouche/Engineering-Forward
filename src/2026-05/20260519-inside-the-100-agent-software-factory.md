# Inside the 100-agent Software Factory
**Source**: https://every.to/context-window/inside-the-100-agent-software-factory
**Date**: May 19, 2026
**Author**: Katie Parrott
**Keywords**: AI agents, multi-agent engineering, Gas City, software factory, HTML vs Markdown, Grok algorithm

## Elevator pitch
A mini-vibe check on Gas City (a tool for running 100+ coding agents in parallel), why HTML is overtaking Markdown as the default format for agent-generated content, and how Grok's open-sourced ranking algorithm can improve your X posts.

## Takeaways
- Gas City, the successor to Gas Town, coordinates ~100 coding agents that merge ~50 PRs/day but remains experimental — skip the toolkit but learn from its ideas (dark vs light factory, one pet/many cattle, multi-model code review).
- OpenAI's Symphony is a more accessible, enterprise-ready alternative that works with existing Linear boards.
- HTML is becoming the new Markdown for AI agents because context windows are now large enough to handle it, and it enables richer outputs (styled tables, charts, collapsible sections).
- Markdown remains better for documents humans will edit; HTML wins when output is agent-to-agent or consumed once.
- xAI open-sourced its ranking algorithm — running drafts through Grok's "banger classifier" before posting can improve X post distribution.
- Every team members are now working with their agents in public Slack channels, creating shared learning about agent collaboration.

## Synthesis
Katie Parrott's mini-vibe check for Every's Context Window newsletter covers three interconnected trends shaping how developers work with AI agents in May 2026.

The centerpiece is Gas City, the successor to Steve Yegge's viral Gas Town project, rebuilt as a toolkit by Chris Sells and Julian Knutsen. At a recent New York workshop, Mike Taylor observed the system coordinating roughly 100 agents that merge about 50 pull requests per day, burning through a billion tokens daily. Gas City introduces several conceptual frameworks worth internalizing: the "dark factory vs. light factory" distinction (agent-only work stays in the dark, human-agent collaboration stays visible), the "one pet, many cattle" pattern (one persistent supervisor agent delegates to disposable worker agents), and multi-model code review (running Claude, Codex, and Kimi on the same code catches different bugs). However, Gas City suffers from practical limitations — every task spins up a fresh session without context continuity, costs multiply linearly per step, and its command-line task tracker is awkward for humans. OpenAI's Symphony, which integrates with existing Linear boards, offers a more mature alternative for most teams.

The second major shift is the emergence of HTML as the preferred output format for AI agents. Anthropic's Thariq Shihipar published "The Unreasonable Effectiveness of HTML" on May 8, arguing that agents should produce single-file HTML instead of Markdown. The post went viral (4.4M views in 16 hours), winning endorsements from Andrej Karpathy and longtime Markdown advocate Simon Willison. The logic is straightforward: as context windows grow large enough to handle full HTML documents, there's no reason to accept Markdown's formatting limitations when agents — not humans — will be the primary consumers and producers of documentation. The practical guidance is nuanced: use Markdown for files humans will edit (AGENTS.md, system prompts, project plans) and HTML when the output is agent-to-agent or meant for one-time human consumption (research summaries, dashboards, spec demos).

The newsletter also covers a practical workflow tip: xAI open-sourced its X ranking algorithm, revealing a Grok-powered "banger classifier" that scores posts on quality and slop. Users can paste drafts into Grok with the same scoring prompt to optimize before publishing. Posts scoring below 0.4 on quality or above 1 on slop get penalized; the algorithm also heavily discounts beyond 3 posts per day, suggesting quality over quantity.

Finally, an internal Every experiment shows team members working with their agents in public Slack channels instead of direct messages, creating shared organizational learning about how to collaborate effectively with AI agents.
