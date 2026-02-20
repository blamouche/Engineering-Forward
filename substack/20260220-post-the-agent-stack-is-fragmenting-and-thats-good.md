# The agent stack is fragmenting—and that’s good

*We’re watching AI move from “one chatbot” to an ecosystem of composable capabilities, and the winners will be the teams who design for seams, not monoliths.*

If you’ve spent the last year asking a model to “just do the thing,” the last couple of weeks have probably felt like whiplash. Models are getting faster. Context windows are getting stranger. Tool APIs are turning into product surfaces. And the loudest announcements aren’t even about “a better chat”—they’re about packaging intelligence into pieces that can be wired together: reasoning modes, skills, browser agents, coding harnesses, and social infrastructure for agents.

At a distance, it can look like fragmentation. One framework says “MCP.” Another says “skills.” A third says “agents.” Your org ships a “copilot.” Your competitor ships an “app server.” The market adds yet another “fast mode,” another “deep think,” another “tokenizer,” another “integration.”

Up close, though, this is the most encouraging pattern we’ve seen since the first wave of code copilots: intelligence is being forced to meet engineering reality. And engineering reality always wins. Not because it’s glamorous, but because it’s where costs, constraints, failure modes, and human trust live.

The shift is subtle: we’re moving from *a model you talk to* toward *a system you operate*. When that happens, fragmentation isn’t a bug. It’s the birth of an interface.

## From “chat” to “capabilities”

Google’s “Deep Think” framing is a useful tell. It’s not positioned as “Gemini but smarter”; it’s presented as a *mode*—a specialized configuration meant for science, research, and engineering, where the right answer is rarely a single sentence and the work is iterative (data, code, checks, revisions). That’s a product claim as much as a benchmark claim. It says: the unit of value is no longer “a reply,” it’s “a tractable workflow.”

Meanwhile, OpenAI’s public narrative around Codex keeps pulling in the same direction: it’s less about magical code completion, more about a harnessed agent that can be deployed into real constraints. “Harness engineering” reads like a confession that raw model intelligence is only half the story; the other half is orchestration—how you shape tasks, handle retries, manage permissions, capture traces, and make outputs auditable.

Stripe’s “one-shot, end-to-end agents” push the idea to an extreme. The pitch is simple: if you can hand an agent a well-bounded objective, the system should do the whole job in one run. Under the hood, that can only work if there’s a lot of discipline around inputs, scaffolding, and evaluation. One-shot doesn’t mean “no engineering.” It means the engineering moved into the substrate.

There’s a parallel story in OpenAI’s “skills” direction: a deliberate attempt to standardize repeatable, tool-backed competencies so they can be invoked reliably. Once a platform lets you invoke “skills” rather than pray over prompts, it’s admitting something important: we’re building *APIs for cognition.*

That’s the capability turn. It leads to a messy middle, because capabilities need boundaries, and boundaries create ecosystems.

## The interfaces are the product now

Two things make this moment different from previous platform transitions.

First, the models are becoming fast enough that interaction patterns are changing. When latency drops toward “train of thought speed,” the UI isn’t a page anymore; it’s a loop. Fast inference makes iterative steering viable. It makes “agentic” feel less like a research demo and more like a development environment. It also raises expectations: if the model is quick, the bottleneck becomes tool execution, context assembly, and the human’s ability to supervise.

Second, the internals are becoming legible enough that people can reason about them. Tokenizers sound boring until you realize they reshape incentives: what content compresses well, what languages are favored, what a “200k context” really means in practice, and how retrieval and summarization strategies interact with token economics. Reverse engineering a tokenizer is a niche sport, but the fact that it’s being done (and circulated) shows how quickly these systems are becoming engineering objects rather than mystical ones.

This is why the argument “it’s not OpenClaw, it’s the architecture” resonates. If you treat an assistant as a monolithic tool, you’ll keep getting brittle behavior and surprising costs. If you treat it as an architecture—permissions, memory, tool surfaces, runtimes, human-in-the-loop controls—you start to see where reliability actually comes from.

And once you see that, you can’t unsee it. The question stops being “which model is best?” and becomes “what is my agent stack?”

## Agents, MCP, RAG: the false taxonomy

The ByteByteGo frame—MCP vs RAG vs agents—captures the confusion well, but it’s also a trap. These labels are not mutually exclusive categories; they’re layers.

RAG is a strategy for supplying context when you don’t have it in the prompt. MCP is a pattern for describing and accessing tools and resources consistently. Agents are an execution model: a loop that plans, calls tools, observes results, and updates state.

In practice, modern systems will use all three. The only real question is where you draw seams.

You can build an “agent” that directly calls internal APIs, but you’ll quickly reinvent a tool protocol. You can standardize a protocol, but you’ll still need retrieval to make it useful at scale. You can do retrieval, but you’ll need an agentic loop to decide what to retrieve, when to stop, and what to do with the results.

So the more interesting engineering decision is not choosing a label; it’s choosing a decomposition.

Do you centralize context assembly into a service, or let each agent own its own memory strategy? Do you put permissions in the runtime, or in each tool? Do you treat web browsing as “just another tool call,” or as a first-class environment with state, guardrails, and traceability? Do you allow agents to create new tools (and if so, who reviews them)?

These are architecture questions, not model questions.

## The new constraint: trust at scale

As agents move from toy to infrastructure, trust becomes the limiting resource.

The “two-slice team” idea—small, high-leverage groups that can ship quickly—sounds like an org-design story, but it’s also a systems story. A small team can hold the whole mental model. An agent stack cannot. Once you have multiple models, multiple tool servers, multiple memory stores, multiple permission boundaries, and multiple execution environments, no single human can keep it all in their head.

That’s where “capture agent sessions on every push” becomes more than developer ergonomics. It’s governance. If an agent is doing work that affects production systems, the transcript is the new log file. You will want to replay it, diff it, audit it, and learn from it. The organization will want proof that the agent didn’t leak secrets, didn’t execute the wrong command, didn’t quietly “fix” behavior in a way that breaks compliance.

The finance angle is instructive here. “Claude Code transforming finance without turning you into a coder” is basically an argument that the biggest adopter group won’t be engineers. It’ll be domain experts who need leverage without full-stack fluency. That only works if the system is safer than the raw CLI, and more intelligible than the raw model.

In other words: the agent stack must be *operable* by people who are not software engineers.

That’s a brutal constraint. It forces product teams to turn invisible engineering into visible interfaces: permissions prompts, previews, explicit tool selection, dry runs, undo mechanisms, provenance, and good defaults.

## A tale of two futures: monolith assistants vs composable stacks

There’s a plausible future where a single vendor ships “the assistant,” and everything else is just plug-ins. It’s a comforting story. It’s also unlikely to be stable.

The economic pressures are pulling in the opposite direction. The cost curve for agentic workflows is real, and it’s easiest to manage by splitting workloads across different inference profiles. You want cheap fast models for triage and routing, expensive slow models for deep reasoning, and specialized tool-backed routines for known tasks. That’s not a monolith; it’s a portfolio.

At the same time, the competitive landscape is increasingly multipolar. Grok gaining ground on incumbents, for messy reasons, is still a reminder that distribution, branding, and ecosystem can move faster than research. On the frontier, “best model” is a weekly headline; in product, “best stack” is a quarterly outcome.

So the likely future is composable. Different providers will win different niches: some will own reasoning modes in science and engineering, some will own code execution harnesses, some will own browser environments, some will own tool protocols, some will own safety layers, and some will own the human-facing UX.

If that’s right, fragmentation becomes a feature: it gives you bargaining power, redundancy, and the ability to evolve.

## How to engineer for seams

If you’re building inside this mess, the practical playbook is surprisingly old-fashioned.

Design your agent system as if you were designing any distributed system.

Keep state explicit. Make tool calls observable. Separate planning from execution. Bound permissions. Capture traces. Treat “memory” as data with lifecycle management, not as a magical prompt appendix. Build evaluation harnesses that reflect your real tasks rather than public benchmarks. And be honest about failure modes—especially the ones that look like success.

If you do that, you’ll find that the most important interfaces are not the UI and not the model. They’re the seams between components.

The teams who win won’t be the ones who pick the “best agent framework” on day one. They’ll be the ones who build a stack that can change its mind without rewriting everything: swap a model, change a tokenizer, add a tool server, modify a retrieval policy, tighten a permission boundary, or introduce a “deep think” lane when the task demands it.

That’s the deeper meaning of this moment. We aren’t watching AI “take over engineering.” We’re watching engineering reassert itself over AI.

The agent stack is fragmenting. Good. That’s how platforms are born.

---

## Sources
1. [Gemini 3 Deep Think: Advancing science, research and engineering](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/)
2. [Grok Is Gaining on ChatGPT and Gemini. How It Got There Isn’t Pretty.](https://www.bigtechnology.com/p/grok-is-gaining-on-chatgpt-and-gemini)
3. [Présentation de GPT‑5.3‑Codex‑Spark](https://openai.com/fr-FR/index/introducing-gpt-5-3-codex-spark/)
4. [EP202: MCP vs RAG vs AI Agents](https://blog.bytebytego.com/p/ep202-mcp-vs-rag-vs-ai-agents)
5. [AI as Fast as Your Train of Thought](https://every.to/context-window/ai-as-fast-as-your-train-of-thought)
6. [Reverse-Engineering the OpenAI’s GPT-5 Tokenizer: What 200,000 Tokens Reveal About AEO/GEO](https://metehan.ai/blog/reverse-engineering-the-gpt-5-tokenizer-aeo-geo/)
7. [the problem isn’t OpenClaw. it’s the architecture.](https://www.vulnu.com/p/the-problem-isnt-openclaw-its-the-architecture)
8. [OpenClaw, OpenAI and the future](https://steipete.me/posts/2026/openclaw)
9. [The Two-slice Team](https://every.to/chain-of-thought/the-two-slice-team)
10. [How Claude Code Is Transforming Finance—Without Turning You Into a Coder](https://every.to/p/how-claude-code-is-transforming-finance-without-turning-you-into-a-coder)
11. [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
12. [Skills in OpenAI API](https://developers.openai.com/cookbook/examples/skills_in_api/)
13. [Aletheia: a math research agent (Superhuman Reasoning)](https://github.com/google-deepmind/superhuman/blob/main/aletheia/Aletheia.pdf)
14. [Clawdbot and Moltbook are a False Alarm – For Now](https://secondthoughts.ai/p/clawdbot-and-moltbook)
15. [Scent, In Silico](https://press.asimov.com/articles/scent)
