# AI's scaling problem is no longer technical

*The most interesting questions in AI right now are about org charts, monthly bills, grey markets, and geopolitical flashpoints — not model architecture.*

Something has shifted in the AI conversation over the past few weeks. The articles landing on my desk are still full of model releases, agent launches, and big numbers. But the questions they raise are no longer mainly about what the technology can do. They are about who controls it, what it actually costs to run in production, and what happens to organizations — and entire labor markets — when it becomes cheap enough to treat like a utility.

Three threads have converged to make this moment feel different from the previous cycle of AI excitement.

The first is economic. We now have real production data on what AI agents cost, and the numbers are simultaneously shockingly low and revealingly lopsided. The second is organizational. Companies are starting to publish honest retrospectives about what happened when they gave every employee an AI agent, and the lessons are not what the hype cycle promised. The third is geopolitical. A frontier model has become an instrument of national security tension, and a parallel grey market has emerged to route around every control that frontier labs have built.

Taken together, these threads point to the same conclusion: the scaling problem in AI is no longer primarily about making models smarter. It is about making intelligence governable, affordable, and strategically coherent.

## The real cost of AI agents is not the AI

Jason Lemkin at SaaStr published the most useful operational data I have seen on running AI agents in a real business. His two AI VPs — one for marketing, one for customer success — cost $257 combined for the month. That number replaced what used to be five human roles. Even with full infrastructure costs — Salesforce API calls, Clerk, ElevenLabs, hosting — the all-in monthly spend lands somewhere between $500 and $800.

The cost structure is instructive. Ninety-five percent of model calls go to GPT-4o-mini at less than a penny per call. Postgres on Replit costs roughly twenty cents a month. The inference is the cheap part. The expensive parts are the surrounding SaaS tools that the agents plug into. This inverts the assumption most startups are operating under: the AI isn't the budget line item you need to worry about. It is the existing software stack that the AI connects to.

Tomasz Tunguz reached a similar conclusion from a different angle. His analysis of what AI-powered email would actually cost arrived at $22 to $130 per month in raw inference — or roughly $500 per year as a SaaS product. That is about twice what Google Enterprise costs today. But his real point was about optimization. By segmenting workloads — deterministic rules for filters, small local models for routine triage, frontier models only for genuinely hard decisions — the cost can drop by a factor of one hundred. The companies that win, Tunguz argues, will treat inference not as a monolithic "call the best model" operation but as a tiered system where every task gets exactly the compute it needs and nothing more.

His companion piece, "Localmaxxing," makes this concrete. Over five weeks tracking 1,478 agentic tasks, Tunguz found that 50% could run successfully on a 35B-parameter local model on his MacBook. The local model was twice as fast as the cloud API and produced output that was terser and equally correct for routine work. For agentic pipelines where one model's output feeds another, brevity is a feature, not a bug. The hardware is a sunk cost that depreciates whether you use it or not. Running inference on it extracts value from an already-sinking asset.

These three analyses converge on a single point. The assumption that AI-native products will be expensive to run is wrong. The real cost optimization problem is not model inference but intelligent workload routing — knowing which tasks need a frontier model and which can run on something much smaller and cheaper. This is an engineering discipline, not a breakthrough research problem. And it is one that most teams are not yet practicing.

## The org chart is becoming the frontier

If the economics are changing faster than expected, the organizational implications are arriving even faster.

The most provocative document in this batch is Lemkin's job posting for a human marketing director to report to 10K, SaaStr's AI VP of Marketing. This is not a thought experiment. 10K already autonomously ships end-to-end campaigns: daily briefs from pacing data, audience builds, copy variants, send sequences, and post-mortems. Some of its campaigns meaningfully outperform what humans were sending, because 10K can do what no human can — truly personalize every communication at the scale of 400,000 recipients.

The human role in this structure is explicitly not strategy or agent management. It is hands-on execution: plan daily with the AI, review everything it proposes, and do the relationship work — sponsor calls, partner conversations, key account outreach — that requires actually picking up the phone. The org chart inverts. The human reports to the AI VP. Lemkin's framing is blunt: "If 'I report to a bot' sounds insulting rather than interesting, this isn't the role."

Every's retrospective on their own experiment — giving every employee a personal AI agent via Slack — provides the counterpoint. They discovered that one-agent-per-employee was the wrong model. The infrastructure was too unstable. The maintenance burden fell entirely on individuals. Agents frequently claimed they lacked access they had, responded with "Terminated" errors, or sent yawning emojis instead of completing tasks. The company is pivoting to shared team agents with defined roles: one analytics agent serving the whole team, one engineering agent handling support tickets. When one person updates a capability, everyone benefits. Knowledge persists when employees leave.

Both SaaStr's success and Every's struggles point toward the same insight. AI agents in organizations need structure. They need defined jobs, shared infrastructure, and clear boundaries about who maintains what. The one-agent-per-person model is the AI equivalent of giving every employee their own server — it sounds empowering but creates maintenance chaos. The team-agent model is the AI equivalent of shared services: less personal, more reliable, and far more likely to survive contact with production.

## The borderless problem

The third thread is darker and harder to contain.

China's attempt to access Anthropic's Claude Mythos model — reportedly through an informal request at a Carnegie Endowment meeting in Singapore — triggered White House alarm because Mythos genuinely is exceptional. It autonomously discovered thousands of zero-day vulnerabilities across every major operating system, including flaws that had persisted for 27 years. Access is confined to roughly 40 US and UK institutions. China, which runs the same underlying software in its banks, energy infrastructure, and government systems, has no seat at the defense table.

The grey market is filling the gap faster than policy can close it. Chinese API "transfer stations" resell Claude access at 90% discounts by routing through stolen credentials, AI-generated fake IDs for biometric verification, and even real human KYC harvesting operations in lower-income countries. User prompts and outputs are systematically logged and resold as AI training data. Every layer of control — geo-blocking, phone verification, credit card requirements, live biometric KYC — produces a corresponding and increasingly sophisticated layer of evasion.

Google's announcement of the first confirmed AI-developed zero-day exploit in the wild adds another dimension. The company's Threat Intelligence Group discovered — and likely prevented — a planned "mass exploitation event" using a vulnerability that was both discovered and weaponized by AI. China and North Korea-associated actors have shown "significant interest" in applying AI to vulnerability exploitation. GTIG's chief analyst called it "a taste of what's to come."

The security picture is not uniformly grim. Anthropic's Project Glasswing uses Claude Mythos to find vulnerabilities defensively. Google uses its own models for preventative threat intelligence. The tools are symmetric. But the discovery timeline is compressing on both sides, and the governance mechanisms — export controls, access restrictions, KYC — are structurally reactive. They respond to the last evasion technique while the market invents the next one.

## Specialization is the new scale

Beneath all three of these threads runs a quieter but equally important trend: specialization is winning over generality.

Anthropic's release of 20 MCP connectors for legal technology — covering document management, e-discovery, contracts, M&A, and legal research, plus 12 practice-area-specific plugins — is the most aggressive vertical expansion by any frontier AI company to date. Claude can now sit inside a law firm's entire workflow, carrying context across Word, Outlook, Excel, and PowerPoint. Thomson Reuters, whose flagship AI product was rebuilt on Anthropic's technology, now has Claude calling CoCounsel as a tool. The foundation model both underpins and competes with the application layer — a pattern that will repeat across industries.

Perceptron's Mk1 model is specialized in a different way. It is built specifically for video understanding and embodied reasoning, matching frontier models from Google and Anthropic on video benchmarks while costing less than Gemini Flash Lite. It outputs structured spatial primitives — points, boxes, polygons, tracks — as first-class outputs alongside text, making it directly consumable by robotics policies without custom parsers. This is specialization as a competitive strategy: narrower scope, deeper integration with the target domain, and radically lower cost.

Even the organizational experiments are specializing. Every's move from one-agent-per-person to shared team agents with defined roles is a specialization play. SaaStr's AI VPs each have specific, bounded responsibilities — marketing ops, customer success — rather than being general-purpose assistants. The pattern is consistent: the era of the universal AI assistant is giving way to the era of specialized AI workers with defined jobs, bounded scope, and measurable output.

## What this means for the next phase

I think the most useful way to read this moment is as a transition from the experimental phase of enterprise AI to the operational phase. The experimental phase was defined by questions like "can it do this?" The operational phase is defined by questions like "what does it cost to run reliably at scale?" and "what happens to the org chart?"

The answers emerging from the past few weeks are surprisingly concrete. Cost is not the constraint anyone thought it would be. Cheap models handle most routine work. Local inference handles half of it for free. The real expense is the SaaS ecosystem around the AI, not the AI itself. The organizational structure that works is shared team agents with defined jobs, not individual agents as personal assistants. The geopolitical dimension is evolving faster than governance can adapt, and the grey market is more creative than any export control framework.

For engineering leaders, the implication is practical. If you are planning an AI agent deployment, the right starting question is not "which model should we use?" It is "what are the five specific jobs we could give agents that would free up real human time, and how do we structure those jobs so one person's improvements benefit everyone?" The companies figuring this out now — SaaStr, Every, and a growing number of others — are building the playbook in public. The rest of us should be reading it carefully.

---

## Sources
1. [EP215: The Anatomy of an AI Agent](https://blog.bytebytego.com/p/ep215-the-anatomy-of-an-ai-agent)
2. [Clawdmeter: ESP32 desk dashboard that shows Claude Code usage](https://github.com/HermannBjorgvin/Clawdmeter)
3. [We're Hiring a Human Marketing Exec to Report to 10K, Our AI VP Marketing](https://www.saastr.com/were-hiring-a-human-marketing-exec-to-report-to-10k-our-ai-vp-marketing-the-bottleneck-isnt-great-ideas-anymore/)
4. [Two AI VPs for $257. A Website Became Our 21st Agent.](https://www.saastr.com/two-ai-vps-for-257-a-website-became-our-21st-agent-killed-a-4k-saas-app-in-60-minutes-the-agents-005-is-out/)
5. [OpenAI Has Already Created 300+ Decamillionaires](https://www.saastr.com/openaidecamillionaires/)
6. [Introducing Perceptron Mk1](https://www.perceptron.inc/blog/introducing-perceptron-mk1)
7. [Anthropic Goes All-In on Legal](https://www.lawnext.com/2026/05/anthropic-goes-all-in-on-legal-releasing-more-than-20-connectors-and-12-practice-area-plugins-for-claude.html)
8. [Gemini Intelligence brings proactive AI to Android](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/)
9. [China, AI, and the Battle for Mythos](https://www.nytimes.com/2026/05/12/us/politics/china-ai-anthropic-openai-mythos-chatgpt.html)
10. [We Gave Every Employee an AI Agent. Here's What We're Doing Differently Now.](https://every.to/source-code/we-gave-every-employee-an-ai-agent-here-s-what-we-re-doing-differently-now)
11. [What Would AI Email Cost?](https://www.tomtunguz.com/cost-of-ai-email/)
12. [The 6 Messages That Actually Matter](https://www.tomtunguz.com/the-disappearance-of-email/)
13. [Localmaxxing](https://www.tomtunguz.com/localmaxxing/)
14. [Chinese Grey Market Sells Claude API Access at 90% Off](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-grey-market-sells-claude-api-access-at-90-percent-off-through-proxy-networks-that-harvest-user-data)
15. [Google Announces Its First-Ever Discovery of a Zero-Day Exploit Made With AI](https://www.engadget.com/2170002/google-announces-its-first-ever-discovery-of-a-zero-day-exploit-made-with-ai/)
