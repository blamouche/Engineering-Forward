# Skill Graphs: Fix Your AI Agent's Context Problem

**Source**: https://linas.substack.com/p/skill-graphs
**Date**: Unknown
**Author**: Linas Beliūnas
**Keywords**: AI agents, context windows, skills, markdown, knowledge graphs, context engineering

## Elevator pitch
Linas Beliūnas argues that agent skill systems should be organized as small linked files rather than monolithic prompts, so agents load only the context they need instead of degrading under oversized input windows.

## Takeaways
- Larger context windows do not eliminate context-management problems because reasoning quality often degrades as more text is loaded.
- Monolithic skill files trade domain breadth for poorer model performance and higher token cost.
- A graph of small markdown nodes connected by links lets agents retrieve only the few pieces relevant to the current task.
- The proposed approach pushes domain knowledge to disk and treats context assembly as selective navigation rather than bulk injection.
- The article points toward a more modular design philosophy for agent memory, instruction systems, and reusable operational knowledge.

## Synthesis
This article addresses one of the most practical problems in agent design: giving a model enough domain knowledge without overwhelming its reasoning ability. Linas Beliūnas argues that many teams are handling this badly by stuffing large “skill files” or instruction dumps into every session. That approach feels safe because it maximizes available information, but it can backfire. As context grows, reasoning quality often degrades and token costs rise. More information does not automatically mean better performance.

The proposed solution is a “skill graph.” Instead of maintaining one monolithic instruction file, the system is broken into many small markdown notes linked together. The agent navigates those notes the way a researcher follows citations, pulling in only the two or three nodes relevant to the current task. Most knowledge remains on disk rather than in the active prompt. That changes context engineering from a preload problem into a retrieval and traversal problem.

This is a strong idea because it aligns with a broader pattern already visible in good agent systems. High-performing workflows increasingly separate durable knowledge from active working memory. Rather than making the model read everything every time, they build structures that let it discover the right local context at the right moment. In practice, that means skills, memory, documentation, and heuristics should often be modular, composable, and selectively loaded. Beliūnas applies that logic specifically to markdown-based skill systems, but the principle extends to retrieval, task decomposition, and tool design more broadly.

The article is also useful because it reframes context windows as a scarce cognitive resource rather than a bucket to fill. Frontier models may accept enormous inputs, but that does not mean they reason equally well across all of them. If context length has a quality cost, then agent builders should care about the marginal value of every paragraph they inject. Linked notes become attractive not just because they are tidy, but because they preserve attention for the parts of the task that actually matter.

The practical takeaway is that teams building agent workflows should rethink giant instruction files. A better pattern may be to maintain a graph of narrow, well-named, reusable pieces that can be traversed dynamically. That reduces token waste, improves legibility, and creates a cleaner path for maintaining operational knowledge over time. Beliūnas’ argument is really an argument for modularity under AI constraints: if context is expensive and cognition degrades with excess input, then structure becomes a performance feature.
