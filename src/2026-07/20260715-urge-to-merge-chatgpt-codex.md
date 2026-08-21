# The Urge to Merge: ChatGPT and Codex
**Source**: https://every.to/context-window/the-urge-to-merge-chatgpt-and-codex
**Date**: 2026-07-14
**Author**: Katie Parrott
**Keywords**: OpenAI, Codex, ChatGPT, Anthropic, Fable, model delegation, agentic work, AI products

## Elevator pitch
OpenAI merged Codex into ChatGPT, Anthropic merged Cowork into Claude, and both labs are betting that a single agentic interface will win the knowledge-work OS—but power users revolted, and the real question is whether consolidation serves users or just platform lock-in.

## Takeaways
- OpenAI folded Codex into the new ChatGPT desktop app with three modes (Chat, Work, Codex), relabeling the old app "ChatGPT Classic"—but Codex power users called the merge a "generational fumble" with duplicate apps, buried chats, broken plugins, and unclear limits
- The merge is a strategic bet: ChatGPT has 800M+ weekly users versus Codex's 5M, so OpenAI is trading some power-user satisfaction for massive distribution of agentic features
- Anthropic mirrored the move by merging Chat and Cowork into one "home" tab in Claude, adding a browser to Claude Code, and extending Fable access—both labs want their flagship to become the starting point for any knowledge-work task
- A practical workflow emerges: use expensive models (Fable, Opus) as planners and reviewers while delegating bounded tasks to cheaper models (Sonnet, GPT-OSS-120B), either within the same lab or cross-lab via shared project files
- A new paper shows AI agents' error rates drop 53% when they stop rewriting code from scratch and instead save working solutions as reusable tools—a compounding benefit that mirrors the "token smarter" philosophy

## Synthesis
The convergence of OpenAI's Codex into ChatGPT and Anthropic's Cowork into Claude marks a pivotal moment in AI product strategy: both frontier labs are consolidating their agentic interfaces into a single "home" rather than maintaining separate apps for chat and agent-driven work. The moves are driven by distribution logic—getting agentic capabilities in front of hundreds of millions of chat users rather than millions of power users—but they come at a real cost. Codex enthusiasts reported broken workflows, lost project spaces, and a sense that the features they relied on were buried beneath a more consumer-friendly veneer.

Beneath the product drama lies a deeper pattern: the emerging practice of model delegation. Power users are learning to treat the most expensive model as a senior consultant that plans, delegates, and reviews, while cheaper models execute bounded tasks. This "Fable leads, Sol executes" pattern can operate within a single lab (Fable → Sonnet in Claude Code) or cross-lab (Fable → GPT-5.6 Sol via shared project directories). The workflow requires discipline: settle the spec first, then delegate with an objective check. If the cheaper model can't deliver, the economics don't work yet.

Meanwhile, the 53% error-rate reduction from saving working solutions as reusable tools points to a meta-lesson: the best AI workflows compound. Instead of re-solving the same sub-problems, agents that persist their solutions as tools build a growing advantage over time. This is the technical expression of the same principle driving the product mergers—both are bets on consolidation and reuse, whether at the interface level or the code level.