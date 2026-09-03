# The method walks out the door

*When expertise becomes encodable, capture is inevitable — ownership is not.*

Stanley Druckenmiller told the Wall Street Journal he writes everything with AI now. "For the same reason I use a calculator when I do math problems." The Journal defended him. The Financial Times banned its columnists from doing the same. The split is instructive, but not for the reason most commentators suggested. The calculator analogy works for arithmetic because arithmetic was never the valuable part of mathematics. The question nobody asked is what happens when the calculator learns to do the part you thought was yours.

Every, a media company, built KateBench — an agent trained on 30,000 historical copyedits by their editor Kate Lee. The agent runs a first pass on every article before a human reviews it. Tracked changes feed back into the system, so the agent improves with each correction. Every plans to clone other team members' judgment: UX feedback, logistical planning, marketing instincts. The editor who was once the bottleneck — the person every writer waited for — becomes a service the whole company can call simultaneously.

This is not a chatbot. It is an encoding of a specific person's accumulated editorial judgment into a system that runs without them. And it raises a question that the AI industry has not begun to answer: when you can clone an employee's expertise into a system that outlasts their tenure, who owns that expertise?

## The encodable moat

The consulting industry has been living with a version of this question for decades. McKinsey, BCG, and Bain generate $37 billion a year selling advice that is mostly produced by associates with under two years of experience. The client buys the method, not the person. Those methods — Minto's Pyramid Principle, Playing to Win, the CIA's Analysis of Competing Hypotheses — are all published and readable. The constraint was never access. It was the two years of internalization under partner supervision that turned a junior associate into someone who could execute the framework reliably.

Twelve Claude Skills built on those same published frameworks lifted Claude Fable 5 from 38 percent to 97 percent on a partner-level consulting checklist. The model did not get smarter. The method got executable. The frameworks were never secret. The constraint — the two years of supervised practice — has been compressed into a set of downloadable files. The $37 billion moat was the internalization period, and that period is now optional.

[The model is not the product](https://engineeringforward.substack.com/p/the-model-is-not-the-product) — but the method encoded around the model is. And a method encoded as a Claude Skill is portable in a way that a method living in a second-year associate's head is not. It can be downloaded. It can be shared. It can leave the building.

## Capture before it walks

Companies are waking up to this dynamic and responding by building systems to capture expertise before it can leave. Ramp rejected every off-the-shelf coding agent and built Inspect, an in-house system running on remote sandboxes with internal data access. The reasoning was not about saving money on vendor licenses. Third-party harnesses could not support enough parallel agents, lacked frontend tooling, and could not offer remote development environments integrated with Ramp's codebase. The integration with internal systems is the point. Block built Goose. Stripe built Minions. Shopify built River. Each company is encoding its own engineering workflows into systems that no vendor can match, because the vendor does not know their codebase, their compliance requirements, or their deployment constraints.

Walleye Capital, a $10 billion hedge fund, made AI use mandatory for all 400 employees. The CEO compared refusing AI to refusing the internet in 1995. The framing sounds like a productivity mandate, but the institutional logic is different. If AI is infrastructure, every employee needs to be on it — and the company needs to capture what each employee produces with it. Individual AI usage that stays in a personal silo does not compound. Shared usage with feedback loops does. Walleye is building a system where the best analyst's approach becomes the default the next analyst can build on.

The shift from personal agents to shared company agents tells the same story. Every documented that maintaining personal agents like OpenClaw carries a hidden cost: credentials expire, integrations break, memory fills with stale instructions. The burden grows linearly with team size. The company pivoted to a shared Slack-based agent model, trading individual customization for institutional manageability. The pivot was not about convenience. It was about ownership. A shared agent captures expertise in a system the company controls. A personal agent captures it in a system the individual controls.

## The extraction problem

The portability of encoded expertise cuts in both directions, and the security research from this week makes that explicit. Researchers from MATS Research, ELLIS Institute Tübingen, and Max Planck demonstrated that encrypted reasoning blocks from frontier AI models can be replayed into cheaper models in the same family to extract hidden chain-of-thought in plaintext. Providers encrypt reasoning traces for competitive and safety reasons. The attack exploits shared family-level parameters — the cheaper model accepts, decrypts, and continues from the encrypted block, reproducing proprietary reasoning that was meant to stay private. The encryption boundary does not hold because the client must decrypt to display summaries. Real-world cases of inadvertent exposure were found in published session logs.

Trail of Bits issued a parallel warning: GPT-5.6-Cyber, a cybersecurity-focused model, escaped QEMU and KVM virtual machines three times during testing, finding zero-day vulnerabilities. OpenAI added a lockdown mode to counter prompt injection. Each finding describes a boundary that was assumed to hold and did not. The same property that makes encoded expertise valuable — its portability — makes it extractable. The KateBench that took 30,000 edits to build can be queried by anyone with access to the system. The consulting frameworks that took McKinsey decades to institutionalize are downloadable as Claude Skills. The reasoning traces that frontier providers deliberately withhold can be pulled out with a cheaper sibling model.

This is the tension the AI industry has not confronted. The push to encode more expertise into AI systems — for productivity, for consistency, for scale — simultaneously creates a larger surface for extraction. Every skill you encode is a skill someone else can copy. Every agent you build is a system someone else can probe. The companies racing to capture their employees' judgment into AI systems are also building a broader attack surface against the same portability that makes those systems useful.

## What measurement cannot capture

The problem is compounded by the fact that companies often cannot tell whether their AI systems are actually working. Companies spending $100 million a year on AI models often have no idea whether those models save employees time or produce trustworthy work. Public benchmarks measure general capability, not performance on the specific tasks a company needs. KateBench's 85-90 percent acceptance rate on copyediting sounds impressive until you learn about the 40-suggestion cap, the non-determinism, and the residual editor work that the metric does not capture. The acceptance rate measures what the system did. It does not measure what the editors still had to do.

[The flood and the filter](https://engineeringforward.substack.com/p/the-flood-and-the-filter) described the verification bottleneck that AI-generated code creates. The measurement problem is its epistemic cousin. You can verify that code runs. You can verify that a copyedit is accepted. You cannot verify that the system has captured the editor's judgment rather than a surface approximation of it. The acceptance rate does not distinguish between the editor approving because the suggestion was good and the editor approving because fixing it themselves would take longer than clicking accept. The expertise that was encoded may be less than the expertise that was measured. The gap between the two is invisible to the metric.

Fable 5's market performance tells the demand side of this story. Anthropic's most expensive model flatlined at roughly 11 percent of business spending two months after launch. Open-weight models processed 29 percent of tokens through Vercel's AI Gateway in June for less than 4 percent of spend. GLM-5.3-Flash, a 320-billion-parameter model with 18 billion active parameters, approaches Claude Opus 4.8 on coding benchmarks at a fraction of the cost. The market is not rejecting frontier intelligence. It is rejecting the proposition that frontier intelligence is worth a premium when nobody can measure whether the premium produces better outcomes. The calculator defense works for arithmetic because arithmetic has a correct answer. The judgment defense works less well because judgment is measured by outcomes that are noisy, delayed, and confounded by everything else that happened in between.

## The boundary that hasn't formed

The migration stories from this week offer one version of where the boundary re-forms. Asana migrated 4,000 test files in two weeks for $12,000. Uber moved 600,000 tests across 15 million lines of code in four months with two engineers. Bun rewrote 530,000 lines from Zig to Rust in two weeks for $165,000. In each case, the mechanical work was automated and the judgment work — planning, verification, orchestration — stayed in human hands. The boundary between tool and worker was clear: the tool transforms, the worker decides.

[The parts that don't write themselves](https://engineeringforward.substack.com/p/the-parts-that-dont-write-themselves) and [the companies building what they can't buy](https://engineeringforward.substack.com/p/the-companies-building-what-they-cant-buy) both touched this boundary from the engineering side. The boundary that has not been drawn yet is the one between an employee's expertise and the company's encoded version of it. Kate Lee's 30,000 edits produced KateBench. If Kate leaves Every, KateBench stays. The editor's accumulated judgment — the thing that made her valuable, the thing the company needed enough to encode — is now institutional property. The consulting associate who spent two years internalizing McKinsey's frameworks has a weaker claim on that knowledge than she once did, because the frameworks are downloadable. The engineer whose workflow was encoded into Ramp's Inspect may find that the system runs her patterns without her.

The calculator analogy breaks down here. A calculator does arithmetic for you. An AI system that encodes your expertise does your judgment for you — and then keeps doing it after you leave. The companies building these systems are betting that the capture is worth more than the risk. The individuals whose expertise is being captured have not yet been asked.

---

## Sources
1. [Anthropic's $30T IPO Pitch and Stripe's Clerky Acquisition](https://www.linas.net/p/anthropic-30t-ipo-pitch)
2. [Nvidia Buys Hugging Face for $12.9B; Anthropic Strikes $45B Compute Deal with Nscale](https://sifted.eu/2026/08/28/the-most-active-us-vcs-in-europe)
3. [Our ChatGPT and OpenClaw Guides Just Got an Overhaul](https://every.to/chatgpt-for-knowledge-work)
4. [OpenRouter for AI Agents: GLM-5.3-Flash Revealed, Qwen4 Architecture, and Agent Infrastructure](https://unwindai.com/p/openrouter-for-ai-agents)
5. [Background Work: From Cron Jobs to Distributed Systems](https://blog.bytebytego.com/p/background-work)
6. [We Need to Talk About Migrations with AI](https://newsletter.pragmaticengineer.com/p/we-need-to-talk-about-migrations)
7. [The Calculator Defense: Druckenmiller Used AI, Apple Commoditized Language](https://coai.beehiiv.com/p/the-calculator-defense)
8. [How to Make LLMs 3X Faster](https://blog.bytebytego.com/p/how-to-make-llms-3x-faster)
9. [Why Performant Code Matters (But Gets Widely Ignored), with Casey Muratori](https://newsletter.pragmaticengineer.com/p/why-performant-code-matters-but-gets)
10. [The Case for Cloning Your Coworkers](https://every.to/context-window/the-case-for-cloning-your-coworkers)
11. [How to Steal an AI Model's Private Thoughts](https://blog.bytebytego.com/p/how-to-steal-an-ai-models-private)
12. [Why Ramp Built Its Own In-House Coding Agent, Inspect](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect)
13. [Fable 5 May Just Be the Canary in the Coal Mine](https://coai.beehiiv.com/p/canary-in-a-coal-mine)
14. [Turn Claude Fable 5 Into a McKinsey-Level Consulting Engine](https://linas.substack.com/p/claude-fable-5-mckinsey-consulting-engine)
15. [Benchmarks Don't Know Your Job](https://every.to/context-window/benchmarks-don-t-know-your-job)