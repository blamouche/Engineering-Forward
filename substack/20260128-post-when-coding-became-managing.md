# What's important now - When Coding Became Managing

*The developers shipping the most code are writing the least of it—and the skills making them effective look nothing like programming.*

Kieran Klaassen starts his mornings with a routine that would have seemed absurd three years ago. He opens five terminal windows, launches five AI agents across different git worktrees, and assigns each one a task from his backlog. By lunch, pull requests arrive with tests and documentation included. Every piece of code he shipped over the past two months, he claims, was written by AI—not assisted by AI, but authored by it.

This is not an isolated case. Jack Clark, co-founder of Anthropic, describes similar scenes: research agents processing thousands of academic papers while he hikes, sleeps, or writes. A vector search system he had stalled on for years was completed by Claude in a single session. The pattern emerging from these accounts suggests something fundamental has shifted. The developers producing the most output are increasingly those who write the least code themselves.

## The Management Revelation

What makes these practitioners effective? The answer appears to have little to do with traditional programming skills. Mike Taylor frames it provocatively: the skills that make AI agents reliable are identical to those that make human teams effective. Give clear direction with specific style references. Specify the desired format explicitly. Provide examples of quality work. Evaluate and measure results systematically. Divide complex goals into sequential steps.

These are not programming principles. They are management principles—the same ones taught in business schools and practiced by effective team leads. Taylor calls this convergence "New Taylorism," drawing a deliberate parallel to Frederick Winslow Taylor's scientific management movement of the 1880s. The original Taylorism failed because humans resented being treated as mechanical components. Workers pushed back against dehumanizing efficiency optimization. With AI agents, these objections disappear entirely. The mechanical approach that failed with humans succeeds precisely because AI lacks the qualities that made scientific management unpalatable.

Teresa Torres, author of Continuous Discovery Habits, demonstrates this management mindset in practice. She uses Claude primarily as an extension of her working memory—a personalized search engine for her knowledge base rather than a content generator. When she does use it for output, Claude serves as an editor applying consistent standards rather than an author producing first drafts. This inverts the typical AI writing workflow: human as creator, AI as quality control.

The implications are significant. If prompting is fundamentally about task definition, quality evaluation, and requirement specification, then its future belongs in business schools rather than computer science departments. As Taylor observes, the technical aspects of working with AI will increasingly automate themselves. What remains is management.

## The Infrastructure Behind the Magic

But not everyone can simply start directing five agents tomorrow. The practitioners shipping code at scale depend on infrastructure that did not exist a year ago.

ByteByteGo's detailed breakdown of Cursor's production coding agent reveals the engineering required. Three challenges had to be solved. First, what Cursor calls "the diff problem"—general-purpose models struggle with precise edits, hallucinating line numbers and breaking formatting. The solution required training on edit trajectories using tens of thousands of GPUs until search-and-replace mechanics became foundational behaviors. Second, latency compounds across iteration loops, demanding architectural techniques like Mixture of Experts routing and speculative decoding. Third, sandboxing at scale meant treating secure execution environments as core serving infrastructure rather than an afterthought.

NVIDIA's methodology for training AI agents adds another dimension. Most specialized tools lack the massive usage logs needed for conventional training. Their solution combines synthetic data generation—bootstrapping examples from seed commands—with Reinforcement Learning with Verifiable Rewards, where valid commands receive positive signals and invalid ones receive negative signals. Group Relative Policy Optimization reduces memory requirements by 50%, enabling single-GPU fine-tuning. The result: organizations can train agents for proprietary tools in days rather than months.

Anthropic's documentation on subagents reveals the architectural patterns making sophisticated workflows possible. Subagents function as independent AI assistants with their own context windows, system prompts, and tool permissions. The Explore agent handles fast, read-only codebase navigation. The Plan agent focuses on research without write capabilities. Custom configurations enable specialized agents for code review, debugging, or database queries—each with precisely scoped permissions and validation hooks.

The combination creates a layered system where Skills encode procedural knowledge, Projects maintain persistent context, MCP connects to external data sources, and subagents handle task decomposition. Claude is evolving from chat assistant to orchestration layer for sophisticated agentic systems.

## The Cognitive Bargain

Not everyone is celebrating. Julien Ricciarelli-Bonnal offers a pointed warning from France: "La machine ne pense pas mal. Elle pense comme tout le monde"—the machine does not think poorly, it thinks like everyone else.

When organizations across industries rely on identical AI tools for strategy, marketing, and communication, their outputs converge. Corporate messaging becomes interchangeable. Innovation is minoritized while standardized outputs become default. The algorithms, trained on vast corpora of existing content, excel at synthesizing what already exists rather than generating genuinely novel approaches.

Worse, users increasingly outsource the initial stages of thinking to algorithms—requesting structures before conceptualizing their own frameworks, seeking solutions before properly analyzing problems. This cognitive delegation, repeated across the workforce, may gradually weaken independent reasoning capacity. The convenience of AI assistance creates dependency that atrophies the muscles of original thought.

Phil Eaton offers a counterbalancing perspective for developers. Coding with LLMs, he argues, is not fundamentally different from coding with Rails or perusing Stack Overflow. Competitive developers have always combined pragmatism with genuine curiosity about underlying systems. Those who treated all code as impenetrable black boxes were already at a disadvantage. AI assistants do not change this dynamic; they merely make the distinction more visible.

The career advice follows: deepen knowledge in systems fundamentals. Companies operating at scale and those building infrastructure—databases, compilers, networking stacks—will persistently value developers who understand core principles. Use AI tools to accelerate routine work while investing the time savings into understanding why systems behave as they do.

## The Product Intuition Gap

Gergely Orosz and Drew Hoskins identify another dimension of value that AI cannot easily replicate: product intuition. Their insight centers on an overlooked aspect of engineering—error messages and diagnostics. When a system fails, the error message becomes the entire user experience at that moment. Treating it as an afterthought means abandoning users precisely when they need guidance most.

This exemplifies the product-minded thinking that distinguishes engineers who thrive in an AI-augmented world. As AI handles more code generation, engineers increasingly need to specify what systems should build rather than just executing predetermined solutions. The ability to anticipate user needs, craft appropriate interfaces, and make systems fail gracefully requires human judgment that cannot be reduced to training data.

The demand for product-minded engineers is rising alongside AI capabilities in code generation. This is not coincidental. When implementation becomes cheap, specification becomes valuable. When anyone can produce code, the differentiation moves to knowing what code to produce.

## The Economic Signal

Early evidence suggests these shifts are producing measurable effects. James Wang analyzes Q3 2025 Bureau of Labor Statistics data showing nonfarm business sector productivity increased 4.9%, driven by output growth of 5.4% while hours worked rose only 0.5%. This "pure" productivity gain—occurring during economic strength with stable employment—differs from historical patterns where productivity spikes typically coincided with recessions and layoffs.

Wang draws parallels to Anthropic's Claude Cowork launch as an accessibility milestone that packages AI agent capabilities for non-technical users, similar to how ChatGPT democratized GPT-3's capabilities. If this pattern holds, subsequent quarters could show strengthening effects as more organizations operationalize AI tools in core workflows.

Meanwhile, new distribution channels are emerging. Colin Matthews argues ChatGPT apps represent an opportunity comparable to the App Store in 2008 or early SEO. The key insight: ChatGPT apps enable contextual surfacing rather than active discovery. When users mention needing help with specific tasks, relevant apps appear automatically. This shifts distribution from marketing-driven to conversation-driven, potentially democratizing access for builders without advertising budgets.

## Looking Ahead

Anthropic's research on the "Assistant Axis" reveals something fascinating about how these systems work internally. Language models learn to simulate multiple character archetypes during training. When deployed as assistants, they occupy a specific position in this persona space—but natural conversation can cause them to drift toward alternative personas. Therapy-style conversations and philosophical discussions produce the most significant departures from the Assistant position. Coding tasks keep models more firmly anchored.

The solution the researchers developed—"activation capping" that constrains neural activity to normal ranges—reduced harmful response rates by 50% while preserving capabilities. This gives a glimpse of the safety engineering happening behind the scenes as these systems take on more consequential tasks.

The throughline across all these developments is role transformation. The developers shipping the most are becoming directors who happen to know how to code, not coders who occasionally direct. The skills in demand are shifting from syntax and algorithms to specification and evaluation. The infrastructure enabling this transition is maturing rapidly, while the cognitive and career implications are only beginning to be understood.

Jack Clark captured the unsettling reality most directly: the agents working for him today are "the dumbest they'll ever be." If current systems can already accomplish weeks of analytical work in hours, tomorrow's versions will compress that further. The question is not whether the role of the developer changes, but how quickly professionals adapt to being managers of increasingly capable AI teams.

---

## Sources

1. [How I Use Claude Code to Ship Like a Team of Five](https://every.to/source-code/how-i-use-claude-code-to-ship-like-a-team-of-five-6f23f136-52ab-455f-a997-101c071613aa)
2. [How Cursor Shipped its Coding Agent to Production](https://blog.bytebytego.com/p/how-cursor-shipped-its-coding-agent)
3. [IA: le risque silencieux de la pensée standardisée](https://www.journaldunet.com/intelligence-artificielle/1547465-ia-le-risque-silencieux-de-la-pensee-standardisee/)
4. [AI Gains Starting to Show in the Real Economy](https://weightythoughts.com/p/ai-gains-starting-to-show-in-the)
5. [Import AI 441: My agents are working. Are yours?](https://importai.substack.com/p/import-ai-441-my-agents-are-working)
6. [Without Benchmarking LLMs, You're Likely Overpaying 5-10x](https://karllorey.com/posts/without-benchmarking-llms-youre-overpaying)
7. [Create Custom Subagents in Claude Code](https://code.claude.com/docs/en/sub-agents)
8. [Skills Explained: How Skills Compares to Prompts, Projects, MCP, and Subagents](https://claude.com/blog/skills-explained)
9. [Claude Code for Product Managers](https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-claude-code)
10. [ChatGPT Apps Are About to Be the Next Big Distribution Channel](https://lennysnewsletter.com/p/chatgpt-apps-are-about-to-be-the)
11. [LLMs and Your Career](https://notes.eatonphil.com/2026-01-19-llms-and-your-career.html)
12. [How to Train an AI Agent for Command-Line Tasks with Synthetic Data and Reinforcement Learning](https://developer.nvidia.com/blog/how-to-train-an-ai-agent-for-command-line-tasks-with-synthetic-data-and-reinforcement-learning/)
13. [The Assistant Axis: Situating and Stabilizing LLM Character](https://www.anthropic.com/research/assistant-axis)
14. [Anthropic Works on Knowledge Bases for Claude Cowork](https://www.testingcatalog.com/anthropic-works-on-knowledge-bases-for-claude-cowork/)
15. [What AI Is Teaching Us About Management](https://every.to/also-true-for-humans/what-ai-is-teaching-us-about-management)
16. [The Product-Minded Engineer](https://newsletter.pragmaticengineer.com/p/the-product-minded-engineer)
