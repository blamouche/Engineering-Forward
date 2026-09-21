# The two-week moat

*When 133 weeks of developer loyalty evaporated in 14 days, the question stopped being which model wins and started being what actually holds.*

For 133 weeks, Anthropic held the majority of developer API spend on OpenRouter. Developers routed more dollars through Claude than through GPT. Then, in the span of two weeks, OpenAI overtook them. Not because Claude got worse — because OpenAI cut Luna's price by 80 percent and launched GPT-6 Astra. The reversal was mechanical, not philosophical. Developers didn't change their minds about which model is better. They changed their routing rules.

The speed of the reversal is the story. If 133 weeks of accumulated developer preference can flip in 14 days, developer loyalty at the API layer is thinner than anyone assumed. Developers route through OpenRouter precisely because they can switch models without changing code. Price-performance, not brand, drives the decision. The implication is uncomfortable for every AI lab betting that model quality creates durable lock-in: it doesn't. The model is becoming a commodity input, and commodity inputs compete on price.

## What price collapse does to strategy

When model prices fall, the competitive question shifts from "who has the best model?" to "who owns what the model touches?" This is the logic driving several stories this week. Nubank launched in 35 countries without a single banking license, using a Swiss legal loophole that treats guaranteed stablecoin funds as non-deposits. The structure achieves 4 to 5 percent of a traditional bank's cost-to-serve by bypassing correspondent banking entirely. Nubank didn't build a better model — it built better rails. If regulators don't close the loophole, every consumer fintech will copy the structure, and the differentiator won't be intelligence. It will be infrastructure.

The same logic explains why ChatGPT quietly became an advertising network. Shopify's Global Catalog now powers product feeds across ChatGPT, Google AI Mode, and Copilot. When model API revenue compresses — and it is compressing, fast — the labs need adjacent revenue streams. OpenAI's answer is advertising, powered by a product catalog that spans every AI surface. Anthropic's answer is vertical products like Claude for Financial Advisors, the first role-specific AI platform covering roughly 80 percent of an advisor's workday through MCP connectors. Both strategies share the same premise: the model alone won't generate durable revenue. You need to own the workflow, the data, or the distribution. This is the same pattern [we saw when law firms started building their own AI](https://engineeringforward.substack.com/p/the-sovereigns-and-the-tenants) — the market splits between those who own intelligence and those who rent it, and the renters are the ones who discover too late that rent goes up.

Richard Sutton's 20-watt bet sharpens the point. The reinforcement learning textbook author is building a model that runs on 20 watts and rewrites its own weights on your data — on your desk, where no one can meter it. "You can't meter what runs on your desk," he says. If Sutton is even partially right, the rent-forever business model that underpins every frontier lab's valuation faces an existential threat. Google's Dream-RSI, which replays a model's own past runs to improve performance by up to 162x, makes the same threat visible from the other direction: self-improving models bend the cost curve down, not up. Recursive self-improvement went from existential risk boogeyman to product category in a single week, with a Chinese startup raising $50M for self-evolving models and AMD posting a job requisition for an RSI scientist.

The combined signal is clear. Model prices are falling. Developer loyalty is frictionless. Self-improvement is bending the cost curve further. The labs that survive will be the ones that own something the model can't commoditize — the same conclusion [the infrastructure land grab reached](https://engineeringforward.substack.com/p/the-land-grab) two months ago, now arriving at the model layer.

## What price collapse does to organizations

If the model is cheap and switching is free, the constraint moves inside the organization. The question becomes: how is your team structured to use intelligence that anyone can rent?

Peter Sellis — the first product manager at Snapchat and later head of product at Discord — offered one answer in a remarkably unfiltered interview this week. He designs teams like terrorist organizations: flat, autonomous, cell-like structures with clear missions and independent decision-making. The analogy is provocative, but the logic is straightforward. At consumer-product speed, the coordination costs of traditional hierarchy exceed the benefits. A cell that can decide and ship without seeking approval will outperform a team that needs three meetings to change a button.

Sellis's most damaging observation is about the median PM. Most product managers are bad, he argues, because the role is defined, hired, and measured in ways that produce mediocre outcomes. If PMs are measured on delivery — shipping features — rather than outcomes — moving metrics — they optimize for throughput over impact. The fix isn't better PMs. It's better systems: measurement that rewards outcomes, team structures that allow autonomous decisions, and a rejection of the feature-factory model. Growth, Sellis insists, comes from deepening the core product, not from bolting on features or chasing growth hacks.

Inherent, a London AI lab founded by three DeepMind alumni, takes the organizational question to an extreme. Employees narrate their stream of consciousness in headsets, creating a dataset of human thought that feeds the lab's research. The office layout is experimental — a Hollywood set designer may redesign the workspace. A linguist might be hired to develop a communication language for agents. The premise is that building AI capable of scientific discovery requires running a company in ways that look bizarre from the outside. Whether this works remains to be seen — Inherent's Faraday model claims to outperform Anthropic and OpenAI at reproducing published scientific findings, but the lab is early. The point is that they're treating organizational design as a first-class research problem, not an HR afterthought.

Matt Pocock, the TypeScript educator, arrived at a similar conclusion from a different direction. His concept of "memento-driven development" reframes code quality as an agent optimization problem. Since AI agents start fresh every session — they wake up with no memory of yesterday's decisions — codebases need to be healthier than ever. Clean code, clear naming, and good architecture aren't aesthetic preferences. They're the difference between an agent that can navigate your system and one that can't. The insight, Pocock notes, is that software fundamentals have been trying to achieve this for decades. The agent just makes the cost of bad fundamentals more visible.

## What price collapse does to judgment

When experimentation is cheap, judgment becomes the scarce resource. Dan Shipper, CEO of Every, consumes more than three times as many tokens as the next-highest user at his company. He considers that gap a feature. Low token spend, in his view, is a smoke signal that teams are thinking too small. A 4.5 billion token failure — a janky 3D face model that revealed an "unruly swarm" problem with unlimited subagents — was a good investment because it exposed a structural flaw now fixed with a five-subagent cap and a judge agent.

The counterintuitive lesson is that companies should worry less about token spend and more about whether teams experiment enough. But the corollary matters equally: expensive experiments are only worth it if you can evaluate the results. This is where the Jev ecosystem's maturation becomes significant. Jev, a decision model that makes choices rather than generating text, matched human labels in a LangChain evaluation at $0.34 per run, compared to $28.17 for Claude — one-eightieth the cost, with less variance. That changes the economics of evaluation. When checking an agent's output costs pennies instead of dollars, you can run evaluation loops at a scale that was previously prohibitory. [The checking floor is still where most of the saved time goes back](https://engineeringforward.substack.com/p/the-checking-floor), but the floor is getting cheaper to stand on.

Tulsee Doshi, who leads product for Google's Gemini models, describes the same problem from the model side. Frontier model product management is a new category because no customer hands you a requirements document. The team decides what the model should get better at, and the scarce skill is saying precisely what "good" looks like. Doshi's "twenty prompts" exercise — where win and loss are obvious — forces vague aspirations into something concrete enough for researchers to optimize against. The practice is transferable to any team working with AI: if you can't write twenty prompts where the right answer is unambiguous, you can't specify what you want from the model. [This is the specification problem](https://engineeringforward.substack.com/p/what-good-looks-like) — the skill that compounds when tool mastery depreciates.

Pocock's "leading words" concept adds another layer. He discovered that feeding agents phrases from classic software engineering books — "tracer bullets" from The Pragmatic Programmer, for instance — causes them to produce better code. The agent doesn't need the full book. It needs the framing. The right word unlocks the right architecture. This is judgment encoded in language, and it compounds in ways that tool-specific knowledge doesn't. When the harness changes every quarter and the model changes every month, the ability to frame a problem precisely outlasts mastery of any particular tool.

## The thin moat

There is a paradox at the center of this week's stories. The easier intelligence becomes to rent, the harder it is to build a business on renting it. OpenAI broke Anthropic's 133-week lead with a price cut and a model launch. Anthropic will respond with its own price cut and model launch. The cycle will repeat, compressing margins each time, until the model layer looks like cloud computing — a utility dominated by a few hyperscalers competing on price and lock-in.

The companies building durable positions aren't competing on model quality. They're competing on ownership: of data, of distribution, of workflow, of trust. Nubank owns the rails. ChatGPT owns the product catalog. Claude for Financial Advisors owns the advisor's workday. Inherent owns its organizational design. Sutton owns the 20-watt model on your desk. Sellis owns the team structure. Pocock owns the leading words. Doshi owns the twenty prompts.

The two-week moat isn't a model. It's everything the model can't commoditize — and the list of things the model can't commoditize is getting shorter every week.

---

## Sources
1. [What US VCs Want to Know: AI Safety, Robotics, and Europe's Edge](https://sifted.eu)
2. [Nubank Goes Global Without Licenses; Claude Targets Financial Advisors; OpenAI Overtakes Anthropic in Developer Spend](https://linas.substack.com/p/weeklyfintechpulse416)
3. [90 Minutes of Unfiltered Product Advice from Snap and Discord's Product Chief](https://www.lennysnewsletter.com/p/90-minutes-of-unfiltered-product)
4. [Get Started With Jev for Free: Needle, Postgres Integration, and the Jev Ecosystem](https://www.theunwindai.com/p/get-started-with-jev-for-free)
5. [Copy Our Homework: Agent Workflows, Astra VFX, and 13 Beliefs About Writing With AI](https://every.to/context-window/copy-our-homework)
6. [EP226: API Concepts, Prompt Injection Defenses, and 12 AI Papers That Changed Everything](https://blog.bytebytego.com/p/ep226-api-concepts-every-software)
7. [Vibe Check: Is Astra a Breakthrough for Indie Filmmakers?](https://every.to/p/vibe-check-is-astra-a-breakthrough-for-indie-filmmakers)
8. [Nuance Labs Is Betting That Text Broke AI Conversation](https://linas.substack.com/p/nuance-labs-pitch-deck)
9. [Inside London's Weirdest Neolab](https://sifted.eu/articles/deepmind-researchers-new-ai-lab-nears-4bn-valuation-reports-say)
10. [Inside Gemini: How Google Runs Product for Its Model](https://theskip.substack.com/p/inside-gemini-how-google-runs-product)
11. [Why You Should Burn More Tokens](https://every.to/context-window/burn-more-tokens)
12. [Migrations at Scale: Changing the Application Engine at 30,000 Feet](https://blog.bytebytego.com/p/migrations-at-scale-changing-the)
13. [AI Skills with Matt Pocock](https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock)
14. [Groundhog Day: Google's AI Now Improves Itself](https://coai.beehiiv.com/p/groundhog-day-7839)
15. [OpenAI Overtakes Anthropic in Developer AI Spend for the First Time Since 2024](https://linas.substack.com/p/fintechpulse1127)