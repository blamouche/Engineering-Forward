# The inversion of the org chart

*AI agents aren't just changing how work gets done — they're changing who reports to whom, and the implications go deeper than most companies are ready for.*

Something genuinely unusual is happening in enterprise AI, and it's not a new model release. Two of the most interesting pieces of operational data published in the past month come from the same company — SaaStr — and together they describe a world in which AI agents have moved from "experiment" to "line item," and from "assistant" to "boss."

The first piece is a job posting for a human marketing executive who will report to 10K, SaaStr's AI VP of Marketing. The second is a cost breakdown showing that two AI VPs — one for marketing, one for customer success — cost $257 combined for the month, replacing what used to be five human roles. Neither of these is a press release from a frontier lab. They are operational documents from a real company running a real business. And the picture they paint is more specific, more useful, and more destabilizing than anything in the latest model card.

Three threads have surfaced in the past few weeks that make this moment feel like a genuine structural shift, not just another chapter in the AI hype cycle. The first is the economics: we now know what AI agents actually cost to run, and the answer is both shockingly low and surprisingly lopsided. The second is the organizational design problem: companies running agent deployments at scale are discovering that the right unit of AI is not the personal assistant but the shared team agent with a defined job. The third is the broader market signal: investors are now picking specific startups in the agentic AI category, which means the conversation has moved from "is this real?" to "where does defensibility live?"

## The economics have inverted

Jason Lemkin's numbers tell the story more clearly than any forecast. Two AI VPs — 10K for marketing and an unnamed agent for customer success — cost $257 combined for the month. That number sits on top of roughly $500 to $800 in infrastructure: Salesforce API calls, Clerk, ElevenLabs, hosting. The AI inference itself — the part everyone assumed would be the expensive bit — accounts for almost none of the budget. Ninety-five percent of model calls go to GPT-4o-mini at less than a penny per call. Postgres on Replit costs roughly twenty cents a month.

This inverts the cost assumption most startups have been operating under. The AI isn't the line item you need to manage. It's the existing SaaS tools that the AI plugs into. The AI is the cheap part of the stack; the expensive parts are the software subscriptions that the human team already needed.

Tomasz Tunguz, analyzing the same question from a different angle, reached a complementary conclusion. His breakdown of what AI-powered email would cost — $22 to $130 per month in raw inference — suggests a SaaS price of roughly $500 per year, or about double what Google Enterprise costs. But his deeper point was about optimization strategy. By segmenting email workloads — deterministic rules for filters, small local models for routine triage, frontier models only for genuinely hard classification tasks — the cost drops by a factor of one hundred. The winning companies, Tunguz argues, will treat inference as a tiered system, not a monolithic "call the best model" operation.

His companion piece, "Localmaxxing," makes this concrete in a way that every engineering leader should read. Over five weeks tracking 1,478 agentic tasks, Tunguz found that 50% could run successfully on a 35B-parameter local model on his MacBook. The local model was twice as fast as the cloud API and produced output that was terser and equally correct for routine work. For agentic pipelines where one model's output feeds another, brevity is a feature — shorter outputs mean less token blowup downstream. And the hardware is a sunk cost that depreciates whether you use it or not. Running inference on it extracts value from an already-sinking asset.

The convergence is clear. The real cost optimization problem in AI-native products is not model inference but intelligent workload routing. Which tasks need a frontier model? Which can run on something smaller and cheaper? Which can be handled by deterministic rules? This is an engineering discipline, not a research breakthrough. And it is one that most teams are not yet practicing.

## The org chart is becoming the frontier

If the economics are shifting faster than most companies realize, the organizational implications are arriving even faster — and they come with an edge that no amount of corporate comms can soften.

Lemkin's job posting is the most provocative document I have read in enterprise AI this year. It is a real listing for a real human marketing director who will report directly to 10K, SaaStr's AI VP of Marketing. The AI VP already autonomously ships end-to-end campaigns: daily briefs from pacing data, audience builds, copy variants, send sequences, and post-mortems. Some of its campaigns meaningfully outperform what humans were sending because 10K can do what no human can — truly personalize every communication at the scale of 400,000 recipients.

The human role in this structure is not strategy. It is not agent management. It is hands-on execution: plan daily with the AI, review everything it proposes, and do the relationship work — sponsor calls, partner conversations, key account outreach — that requires actually picking up the phone. Lemkin's framing is deliberately blunt: "If 'I report to a bot' sounds insulting rather than interesting, this isn't the role."

This isn't a thought experiment. It is a job description. And it inverts the organizational assumption that has governed enterprise software since the mainframe era: that tools serve people, not the other way around. When the tool has autonomous campaign execution, audience targeting, and performance measurement capabilities that exceed what a human team can do, the question becomes: who is serving whom?

Every's retrospective on their own experiment — giving every employee a personal AI agent via Slack — provides the counterpoint. They discovered that one-agent-per-employee was the wrong model. The infrastructure was too unstable. The maintenance burden fell entirely on individuals. Agents frequently claimed they lacked access they had, responded with "Terminated" errors, or sent yawning emojis instead of completing tasks. The company is now pivoting to shared team agents with defined roles: one analytics agent serving the whole team, one engineering agent handling support tickets. When one person updates a capability, everyone benefits. Knowledge persists when employees leave.

Both SaaStr's success and Every's struggles converge on the same insight. AI agents in organizations need structure. They need defined jobs, shared infrastructure, and clear boundaries about who maintains what. The one-agent-per-person model is the AI equivalent of giving every employee their own server — it sounds empowering but creates maintenance chaos. The team-agent model is the AI equivalent of shared services: less personal, more reliable, and far more likely to survive contact with production.

The practical takeaway for anyone planning an agent deployment is that the org chart question — who reports to whom, who maintains what, where does knowledge live — is more important than the model selection question. The model will improve in three months. The organizational design you pick today will shape your team's relationship with AI for years.

## The market is learning to pick winners

Beneath the operational stories, a quieter but structurally important signal is emerging. Sifted published a roundup of 11 AI agent startups that European investors — Speedinvest, Creandum, Firstminute Capital, and Cherry Ventures — are watching. The piece is a market map, not a definitive ranking, and its value is less in which specific companies made the list than in what the list reveals about investor thinking.

The roundup mixes specialist agent builders with broader AI productivity plays. Companies like Ankar AI, Manex AI, and Granola appear alongside more horizontal tooling bets. That mix matters because it suggests investors are no longer asking "is agentic AI a real category?" They are asking "which implementation layers will create durable value?" The conversation has moved from existence proof to competitive analysis.

This is the same pattern that played out in SaaS, in cloud infrastructure, and in mobile apps. First comes the category-defining technology. Then comes the flood of startups all claiming to be "X for AI." Then comes the sorting — the process by which capital and customer attention concentrate on the companies that turn capability into product, not just demo. The Sifted list is evidence that the sorting has begun.

The timing is notable. Enterprise AI adoption is still in its early innings — most companies haven't deployed a single agent in production, let alone restructured their org chart around one. But the startups that will serve those deployments are already being identified and funded. For engineering leaders, the implication is practical: the tooling you'll be using in eighteen months is being built right now by companies you may not have heard of. Watching the investor signal — not for stock tips, but for capability maps — is becoming part of the job.

## Specialization is winning over generality

A quieter trend runs through all three of these threads: specialization is beating generality. Anthropic released 20 MCP connectors for legal technology — document management, e-discovery, contracts, M&A, legal research — plus 12 practice-area-specific plugins. Claude can now sit inside a law firm's entire workflow, carrying context across Word, Outlook, Excel, and PowerPoint. Perceptron's Mk1 model matches frontier models on video benchmarks while costing less than Gemini Flash Lite, because it is built specifically for video understanding and embodied reasoning. Every's move from one-agent-per-employee to shared team agents with defined roles is a specialization play. SaaStr's AI VPs each have specific, bounded responsibilities rather than being general-purpose assistants.

The pattern is consistent: the era of the universal AI assistant is giving way to the era of specialized AI workers with defined jobs, bounded scope, and measurable output. The companies that succeed are not the ones deploying the most powerful general model. They are the ones deploying the right model — often a much smaller and cheaper one — for each specific job.

## What comes next

I think this moment will be remembered as the transition from the experimental phase of enterprise AI to the operational phase. The experimental phase was defined by "can it do this?" The operational phase is defined by "what does it cost to run reliably at scale?" and "what happens to the org chart?" and "who reports to whom?"

The answers emerging now are surprisingly concrete. Cost is not the constraint anyone expected. The organizational structure that works is shared team agents with defined jobs, not individual agents as personal assistants. The investor community is already identifying which companies will build the infrastructure for this next phase. And the hardest question — the one no one has a clean answer to — is what it means for human identity and motivation when the org chart inverts and the tool becomes the manager.

The SaaStr job posting asks the question directly. If "I report to a bot" sounds insulting rather than interesting, this isn't the role. That is either a bracing dose of honesty or a preview of a workplace dynamic that most of us are not emotionally ready for. Probably both.

---

## Sources
1. [11 AI agent startups to watch, according to investors](https://sifted.eu/articles/ai-agent-startups-to-watch-2)
2. [EP215: The Anatomy of an AI Agent](https://blog.bytebytego.com/p/ep215-the-anatomy-of-an-ai-agent)
3. [Clawdmeter: ESP32 desk dashboard that shows Claude Code usage](https://github.com/HermannBjorgvin/Clawdmeter)
4. [We're Hiring a Human Marketing Exec to Report to 10K, Our AI VP Marketing](https://www.saastr.com/were-hiring-a-human-marketing-exec-to-report-to-10k-our-ai-vp-marketing-the-bottleneck-isnt-great-ideas-anymore/)
5. [Two AI VPs for $257. A Website Became Our 21st Agent.](https://www.saastr.com/two-ai-vps-for-257-a-website-became-our-21st-agent-killed-a-4k-saas-app-in-60-minutes-the-agents-005-is-out/)
6. [OpenAI Has Already Created 300+ Decamillionaires](https://www.saastr.com/openaidecamillionaires/)
7. [Introducing Perceptron Mk1](https://www.perceptron.inc/blog/introducing-perceptron-mk1)
8. [Anthropic Goes All-In on Legal](https://www.lawnext.com/2026/05/anthropic-goes-all-in-on-legal-releasing-more-than-20-connectors-and-12-practice-area-plugins-for-claude.html)
9. [Gemini Intelligence brings proactive AI to Android](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/)
10. [China, AI, and the Battle for Mythos](https://www.nytimes.com/2026/05/12/us/politics/china-ai-anthropic-openai-mythos-chatgpt.html)
11. [We Gave Every Employee an AI Agent. Here's What We're Doing Differently Now.](https://every.to/source-code/we-gave-every-employee-an-ai-agent-here-s-what-we-re-doing-differently-now)
12. [What Would AI Email Cost?](https://www.tomtunguz.com/cost-of-ai-email/)
13. [The 6 Messages That Actually Matter](https://www.tomtunguz.com/the-disappearance-of-email/)
14. [Localmaxxing](https://www.tomtunguz.com/localmaxxing/)
15. [Chinese Grey Market Sells Claude API Access at 90% Off](https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-grey-market-sells-claude-api-access-at-90-percent-off-through-proxy-networks-that-harvest-user-data)
