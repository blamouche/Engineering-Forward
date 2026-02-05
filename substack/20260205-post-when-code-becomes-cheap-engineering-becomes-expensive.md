# When Code Becomes Cheap, Engineering Becomes Expensive

*Agents are making software faster to produce—and harder to manage, price, and govern.*

The headline story of software in 2026 is supposed to be abundance. Code is pouring out of models the way HTML poured out of the early web: fast, cheap, and increasingly decent. A skilled developer can spin up a working prototype in an afternoon, and a mediocre one can ship something that looks suspiciously like production in a week. The punchline writes itself: if code is cheap, software should be cheap too.

And yet the lived experience inside teams is the opposite. Engineering is getting more expensive, not less. Not because compute is pricey or because models aren’t good enough, but because the unit of work is shifting. We’re moving from writing code to managing systems that write code, and the “management” part has the nasty property that it compounds.

What we call this matters. Addy Osmani draws a clean line between “vibe coding” and what he calls agentic engineering: letting an agent sprint ahead is fine, but professional work still requires human ownership of architecture, careful diff review, and an obsession with tests. That distinction is not pedantry. It’s the difference between a fun weekend project and an organization that can be trusted with money, safety, and time.

The uncomfortable truth is that agentic engineering doesn’t eliminate discipline; it demands more of it. The agents don’t remove the need for judgment. They scale the consequences of not having it.

## The new bottleneck isn’t typing—it’s verification

If you want a single sentence version of the moment, it’s this: generation is linear, verification is not.

As soon as you introduce agents, you get what feels like free parallelism. One agent can implement a feature while another drafts tests, a third updates docs, and a fourth refactors some gnarly module you’ve been postponing. But the cost curve doesn’t stay friendly. The more agent output you accept, the more surface area you must validate. Michael Spencer’s “expensively quadratic” framing is the right instinct: coordination and review costs grow faster than the amount of work produced.

Teams are discovering that the old constraints were doing hidden work for them. When a human writes code, the time spent writing is also time spent understanding. When an agent writes code, you can get the output without the comprehension. The bill comes due later, as bugs you can’t localize, architecture you can’t explain, and changes you can’t safely make.

This is why testing becomes the central asset. In Osmani’s view, the test suite is the safety rail that lets an agent iterate until green. In practice, it’s also the boundary between “cheap code” and “cheap reliability.” A test suite is a contract with the future: it’s how you keep speed without gambling your weekends.

There’s a second-order effect too: better tools are making review measurable. Claude Code’s /insights is a small example, but it points to a broader pattern: the development environment is turning into an observability stack. We’re instrumenting our own work. Once you can see what changed, why it changed, and which actions led to success, you can begin to manage agents like you manage production services: with traces, guardrails, and budgets.

The result is paradoxical. Agents make it easier to produce diffs, but they push the craft of engineering toward designing constraints: tests, interfaces, review rituals, and automated checks that turn raw output into trustworthy software.

## Competition is compressing, and “moats” are moving

If it feels like every month brings a new contender, it’s because it does. Big Technology’s data suggests OpenAI’s lead is contracting, and the direction of travel matters more than the ranking. When capability gaps shrink, the market stops rewarding “best model” narratives and starts rewarding workflows.

Qwen’s push on small hybrid models is another signal. The future isn’t one giant model that does everything; it’s a zoo of specialized engines that trade off cost, latency, and accuracy depending on the task. That pushes organizations to think less like “we bought AI” and more like “we built a system of AI components.”

Open source is the accelerant here. Hugging Face’s survey of the post-DeepSeek ecosystem reads like a reminder that distribution is a force of nature. Once a capability is cheap enough to run and permissive enough to remix, it becomes infrastructure. The winners aren’t the ones who can build the first version; they’re the ones who can build the safest, most ergonomic, most integrated version.

This has two implications. First, developer platforms become the primary battleground. Apple adding support for the Claude Agent SDK inside Xcode is not a novelty feature; it’s a declaration that the IDE is becoming an orchestration layer. Second, the “moat” shifts from model access to organizational competence: the ability to turn a stream of cheap output into a consistent product.

That competence is hard to copy because it’s cultural. It lives in how teams write specs, how they review, how they build tests, and how they decide what not to ship.

## The software business won’t die—it will reprice reality

The Wall Street Journal argument that AI won’t kill software, only its growth story, is provocative because it attacks a sacred assumption: that SaaS margins will expand forever. If building features gets cheaper, buyers will expect prices to follow. The spreadsheet logic is simple. The strategic reality is messier.

As software becomes easier to produce, it becomes more contingent. Customers will demand faster changes, deeper customization, and tighter integration. That increases not just engineering output, but engineering responsibility. The work shifts from “shipping features” to “operating relationships with live systems.”

In other words, AI makes software more like a service in the old-fashioned sense: ongoing, negotiated, and context-dependent. The costs don’t disappear; they move into support, governance, compliance, and assurance. The company that wins is the one that can promise speed without chaos.

This is why it’s a mistake to treat “AI coding” as a pure productivity story. It’s a product strategy story. If your competitors can ship your features, your differentiation becomes trust: reliability, security, and the confidence that what you ship won’t become tomorrow’s incident.

And there’s a human dimension. The “AI that called its human” anecdote is funny until it isn’t. Agents that take initiative blur boundaries: what counts as acceptable autonomy, what counts as escalation, and what counts as a bug versus a breach of expectation. Once agents act in the world—contacting humans, making purchases, modifying systems—you inherit governance questions that look more like finance and safety than like software.

Even the most charming agent will eventually make a mistake at the speed of automation.

## From copilots to organizations: the agent stack

If you zoom out, you can see the stack assembling.

At the bottom are models, increasingly commoditized and increasingly diverse. Above them are agent frameworks and SDKs that let tools be called, actions be audited, and policies be enforced. Above that are the environments where work happens: the IDE, the terminal, the ticketing system, the CI pipeline.

NanoClaw is an instructive artifact in this context. A “small, container-isolated assistant” sounds like a toy until you realize it’s pointing at the right architectural instinct: isolate, constrain, log, and contain. If agents are going to operate on your machine and your codebase, the security posture can’t be an afterthought. The safest agent is the one with the smallest blast radius.

Meanwhile, OpenAI Codex is a reminder that the product shape is stabilizing. Users don’t want a model; they want a partner embedded in their workflow, with enough autonomy to be useful and enough transparency to be trusted.

Which brings us back to the bottleneck: trust is built by instrumentation and constraint. That’s why /insights-like features matter. That’s why SDK integrations matter. That’s why test suites matter.

The most underappreciated question for 2026 is not “can the agent write code?” It’s “can we prove what the agent did, and can we reverse it safely?”

## The next managerial skill: governing invisible labor

In a traditional engineering org, labor is visible. You see tickets move, PRs open, discussions happen. With agents, a lot of labor becomes invisible until the diff lands. That’s exhilarating, but it’s also dangerous. The team can appear to be moving faster while quietly accumulating misunderstanding.

This is where workplace governance enters. Patrice Cochin’s argument that we need to move beyond algorithmic transparency is useful because it pushes the conversation from “show me the model” to “show me the system.” Transparency isn’t a PDF explaining how a model works. It’s a living set of practices: what the agent is allowed to do, how it is supervised, what metrics define success, and what recourse exists when it fails.

The board-game customer support story is a perfect microcosm. Training an AI on a constrained domain produced a better support agent because the task had clear boundaries and feedback. In the wild, most organizational work doesn’t. It’s ambiguous, political, and full of unspoken context. Agents can help, but only if we make the context explicit enough to be actionable.

That suggests a new managerial skill for tech leaders: governing invisible labor. Setting budgets for agent work. Creating review processes that scale. Deciding when speed is worth risk. Teaching teams to write specs that are legible to both humans and machines.

And yes, that’s “engineering” now.

The cheap part isn’t the code. The expensive part is the organization that makes the code safe.

---

## Sources
1. [Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/?utm_source=tldrnewsletter)
2. [Qwen3-Coder-Next: Pushing Small Hybrid Models on Agentic Coding](https://qwen.ai/blog?id=qwen3-coder-next&utm_source=tldrai)
3. [Anthropic Performance Team Take-Home for Dummies](https://www.ikot.blog/anthropic-take-home-for-dummies)
4. [AI Won’t Kill the Software Business, Just Its Growth Story](https://www.wsj.com/tech/ai/ai-wont-kill-the-software-business-just-its-growth-story-05673e07?st=4rDCyV&reflink=desktopwebshare_permalink&mod=tldr&utm_source=tldrnewsletter)
5. [Expensively Quadratic: the LLM Agent Cost Curve](https://blog.exe.dev/expensively-quadratic?utm_source=tldrai)
6. [The AI That Called Its Human](https://www.fintechbrainfood.com/p/the-ai-that-called-its-human?utm_source=tldrai)
7. [NanoClaw: a small, container-isolated Claude assistant](https://github.com/gavrielc/nanoclaw?utm_source=www.theunwindai.com&utm_medium=newsletter&utm_campaign=clawdbot-in-just-500-lines-of-code&_bhlid=ee1649147d4a6aa7be0dafb677e397d95ebacbb8)
8. [Deep Dive: How Claude Code's /insights Command Works](https://www.zolkos.com/2026/02/04/deep-dive-how-claude-codes-insights-command-works.html?utm_source=tldrai)
9. [The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-3?utm_source=tldrai)
10. [Apple’s Xcode now supports the Claude Agent SDK](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk?utm_source=tldrai)
11. [AI at work: beyond algorithmic transparency](https://patricecochin.substack.com/p/ai-at-work-beyond-algorithmic-transparency?publication_id=4666503&post_id=186850631&isFreemail=true&r=fhb7r&triedRedirect=true&utm_source=substack&utm_medium=email)
12. [New Data: OpenAI's Lead Is Contracting as AI Competition Intensifies](https://www.bigtechnology.com/p/new-data-openais-lead-is-contracting)
13. [We Trained an AI on a Board Game. It Became a Better Customer Support Agent.](https://every.to/playtesting/we-trained-an-ai-on-a-board-game-it-became-a-better-customer-support-agent-299b5938-09dd-4881-803f-aea21f0d461f)
14. [OpenAI Codex: AI Coding Partner](https://openai.com/fr-FR/codex/)
15. [Anthropic Is About to Drop Sonnet 5 During Super Bowl Week](https://www.testingcatalog.com/anthropic-is-about-to-drop-sonnet-5-during-super-bowl-week/)
