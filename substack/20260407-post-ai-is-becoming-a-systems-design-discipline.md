# AI is becoming a systems design discipline

*The next advantage is not having a smarter model in isolation, but designing better memory, context, tooling, and workflows around it.*

The most interesting thing happening in AI right now is not a single model release. It is the quiet shift in where the real work lives. A year ago, the dominant story was model horsepower: bigger context windows, stronger benchmarks, more multimodal tricks, faster iteration. That story is still running, but the center of gravity has moved. The latest batch of articles points to a more practical and more consequential reality: once models are good enough, progress stops looking like “get a better chatbot” and starts looking like systems design.

That is why so many of the strongest recent pieces are less obsessed with raw intelligence than with the plumbing around it. They talk about context engineering, memory structures, virtual filesystems, skill graphs, training harnesses, environment design, and operational workflows. Even the pieces about writing, support, and product management are really saying the same thing. The hard part is no longer convincing people that AI can generate output. The hard part is deciding what the system should know, when it should know it, how it should act on it, and how humans stay in control.

This is a healthier phase for the industry. It is also a more demanding one. Hype thrives on demos. Systems design thrives on constraints.

## The bottleneck has moved from generation to organization

Several of these articles circle the same diagnosis from different angles. ByteByteGo’s guide to context engineering argues that bigger windows do not solve the core problem of relevance. More text is not automatically more intelligence. In practice, overloaded context produces distraction, loss-in-the-middle effects, and expensive confusion. Linas Beliūnas makes a similar point in his case for skill graphs: the future is not giant prompt blobs, but linked, modular knowledge that can be loaded selectively. David Caddy, from another direction, argues that procedural “skills” are useful but are not enough as a general integration layer; for live service access, he still prefers MCP because it handles portability, authentication, and remote connectivity better.

Put together, these are not minor implementation debates. They are arguments about the architecture of AI work. The old assumption was that if models got bigger, prompt engineering would matter less. What is happening instead is that prompt engineering is being absorbed into a broader discipline: context engineering. The question is no longer “what prompt should I write?” It is “what information topology gives this agent the best shot at succeeding?”

Karpathy’s sketch of llm-wiki pushes that logic further. Instead of repeatedly asking models to re-synthesize raw documents through retrieval, he suggests a persistent markdown knowledge layer that compounds over time. OpenClaw’s experimental Dreaming system makes a similar bet from the memory side: not everything deserves long-term retention, so memories should be staged, scored, and only promoted when they repeatedly prove their value. LangChain’s piece on continual learning lands in the same neighborhood. Most practical improvement, it argues, will come not from retraining base weights every week, but from making harnesses and memory systems smarter with traces.

This is a big conceptual upgrade. AI products are ceasing to be stateless response machines. They are becoming evolving environments.

That change also helps explain why some of the most compelling engineering work now looks almost boring. Mintlify’s virtual filesystem is a good example. Instead of treating documentation as a bag of chunks for RAG, it created a navigable file abstraction that lets the assistant move through docs more like a codebase. The payoff was not theoretical elegance. It was brutal practicality: boot times collapsed from tens of seconds to roughly a hundred milliseconds, and the system no longer needed to pay the cost of sandbox startup on every session. This is what the current phase of AI engineering looks like when it works: fewer mystical claims, more careful interface design.

## Good agents are made of harnesses, not wishes

Another cluster of articles points to the same conclusion from the training and workflow side. Lee Han Chung’s taxonomy of RL environments argues that the unit of progress is not just the model, but the environment around it: tasks, verifiers, state, configuration, and harness. Unwind AI’s write-up on Karpathy’s AutoAgent says roughly the same thing in operational terms. The meta-agent does not simply ask for better prompts; it runs experiments, studies full execution traces, and improves the task agent’s surrounding setup. LangChain frames this as harness learning. However you label it, the pattern is unmistakable.

Agents are no longer being treated as monolithic brains. They are being treated as workers embedded in designed environments.

That matters because most real-world failures are environmental failures. The model forgot a constraint because the context was too noisy. The tool chain was too brittle. The memory format was too vague. The evaluation loop rewarded the wrong behavior. The action space was underspecified. The human review step was missing or arrived too late. These are not failures that disappear because the next model scores three points higher on a benchmark.

The support workflows described by Al Chen and highlighted by Lenny’s Newsletter make the same point in an especially grounded way. Claude Code becomes useful for enterprise support not because it is magically omniscient, but because it is connected to 15 repositories, Confluence, and customer-specific deployment notes. The workflow has been made legible. Reality has been organized into an environment the model can traverse. That is why customers notice the difference. The magic is in the curation.

The same is true in writing. Katie Parrott’s essay on AI-assisted writing is one of the better antidotes to both naive evangelism and lazy criticism. Her point is not that AI eliminates thinking. It is that good AI writing externalizes parts of the editorial loop: interviewing, outlining, critique, revision, tone checking, structural alternatives. The human still supplies judgment, taste, and ownership. In other words, the tool works when the workflow is designed. Again: systems design.

Even the pieces that seem furthest from core infrastructure fit the pattern. “What I Learned Onboarding Our AI Project Manager” and the essay on why product managers are built for AI both suggest that the new leverage comes from decomposing ambiguous work into explicit states, instructions, and feedback loops. AI does not reward vague authority. It rewards operational clarity.

That is why the current moment feels simultaneously promising and slightly unforgiving. Companies that hoped AI would simply “make everyone faster” are discovering that speed only appears after a lot of structure is imposed. Models reward explicitness more than aspiration.

## This is why economics and strategy are getting sharper

Once AI becomes a systems discipline, the economics get sharper too. You can see that in Anthropic’s move to charge extra for Claude Code usage through third-party harnesses like OpenClaw. That change reads less like a side drama than a market signal. If the real value is migrating from a raw chat subscription to long-running, tool-using, environment-aware workflows, then pricing will follow that workload. Companies will stop charging as if every user is just typing into a neat little box.

That also explains the tension around the tooling layer. If developers increasingly operate through external harnesses, agent runtimes, memory frameworks, and orchestration systems, the balance of power changes. Model providers want the upside from that usage. Product builders want flexibility and margin. Open ecosystems want interoperable standards. Closed ecosystems want optimized capture. The MCP-versus-skills argument is partly technical, but it is also about where dependency accumulates.

Google’s push around Gemma 4 shows another strategic angle. On-device and edge agent workflows are not just a product feature; they are a distribution bet. If useful agentic behavior can run on phones, laptops, and embedded hardware, the market widens beyond centralized API consumption. It also changes the privacy, latency, and control equation. In that world, architecture choices around skills, memory, and context packaging become even more important, because edge systems have stricter constraints and fewer margins for waste.

Meanwhile, Anthropic’s reported acquisition of Coefficient Bio is a reminder that once the general-purpose layer matures, the next move is often into domain-specific workflow ownership. Life sciences is a good candidate because the work is high value, data rich, and process heavy. The lesson is not that every sector needs a custom foundation model. In fact, several of these articles argue the opposite. The lesson is that vertical advantage may come from owning the environment, the data interfaces, the tacit operating patterns, and the verification loops.

That has consequences for builders. The defensible product is less likely to be “we wrapped a model.” It is more likely to be “we turned a messy domain into an agent-readable system.”

## The next winners will make AI legible

If there is one central insight running through these 15 articles, it is this: the next wave of AI advantage will come from making work legible to machines without making it illegible to humans.

That sounds abstract, but the examples are concrete. A virtual filesystem makes docs navigable. A wiki makes knowledge persistent. Skill graphs break giant prompts into composable nodes. Memory consolidation prevents accumulation from turning into noise. Support workflows connect code, docs, and customer quirks. Training harnesses turn vague capability into measurable improvement. Writing workflows expose editorial reasoning instead of pretending the first draft is the product.

This is also why the current phase feels more mature than the last one. The industry is slowly admitting that intelligence in isolation is not enough. What matters is structured access to the right information, the right tools, the right constraints, and the right review loops. The model is still the engine, but the product is the vehicle.

That should change how teams prioritize. Less obsession with giant prompt templates. More attention to interfaces. Less magical thinking about autonomous agents. More work on environments, memory, verifiers, permissions, and failure handling. Less bragging about raw model access. More care around whether a system can actually do useful work repeatedly under realistic constraints.

The irony is that this shift may make AI feel less flashy even as it becomes more powerful. The headline demo is easy. The hard-won workflow that quietly saves hours every day is harder to show off. But that quieter layer is where value is accumulating.

The companies and teams that understand this first will have an advantage that is both simpler and more durable than the usual hype cycle suggests. They will not just deploy stronger models. They will build clearer systems around them.

And that may turn out to be the real dividing line of the next phase: not who has access to AI, but who knows how to organize work so AI can actually help.

---

## Sources
1. [Writing With AI is Harder Than You Think](https://every.to/working-overtime/writing-with-ai-is-harder-than-you-think)
2. [How Al Chen Uses Claude Code and 15 Repos to Answer Any Customer Question](https://www.chatprd.ai/how-i-ai/claude-code-and-repos-to-answer-any-customer-question)
3. [This week on How I AI: I gave Claude Code our entire codebase. Our customers noticed.](https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-i-gave-claude)
4. [A Guide to Context Engineering for LLMs](https://blog.bytebytego.com/p/a-guide-to-context-engineering-for)
5. [Karpathy’s Autoresearch for Agent Engineering](https://www.theunwindai.com/p/karpathy-s-autoresearch-for-agent-engineering)
6. [How we built a virtual filesystem for our Assistant](https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant)
7. [Dreaming (experimental)](https://docs.openclaw.ai/concepts/dreaming)
8. [Bring state-of-the-art agentic skills to the edge with Gemma 4](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4)
9. [I Still Prefer MCP Over Skills](https://david.coffee/i-still-prefer-mcp-over-skills)
10. [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
11. [A Taxonomy of RL Environments for LLM Agents](https://leehanchung.github.io/blogs/2026/03/21/rl-environments-for-llm-agents)
12. [Continual learning for AI agents](https://blog.langchain.com/continual-learning-for-ai-agents)
13. [Anthropic buys biotech startup Coefficient Bio in $400M deal: Reports](https://techcrunch.com/2026/04/03/anthropic-buys-biotech-startup-coefficient-bio-in-400m-deal-reports)
14. [Anthropic says Claude Code subscribers will need to pay extra for OpenClaw usage](https://techcrunch.com/2026/04/04/anthropic-says-claude-code-subscribers-will-need-to-pay-extra-for-openclaw-support)
15. [Skill Graphs: Fix Your AI Agent's Context Problem](https://linas.substack.com/p/skill-graphs)
