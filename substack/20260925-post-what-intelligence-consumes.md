# What intelligence consumes

*The AI industry's appetite has moved past the internet and into the physical world — silicon, paper, and the server rack.*

For a decade, cloud computing trained engineers to treat compute as infinite and elastic. Spot pricing let you buy CPU capacity at 90 percent off, and if your job got interrupted, you just retried. That world is gone. Cloud providers have effectively killed spot pricing for CPUs. Reservations now need months of advance planning. Server orders that used to take one to two weeks now take six months. Some cloud regions are rejecting new tenants entirely because every CPU is already leased. Customers are paying today for capacity that comes online in December.

The cause is not a surge in web traffic or a sudden boom in traditional enterprise workloads. It is AI agents. Reinforcement learning requires CPUs to run the software that models learn to use. General-purpose agents need CPUs to execute tools, compile code, and run tests. The ratio of CPU to GPU in AI data centers has shifted from 1:8 to 1:4, and it is heading toward 1:1. Simon Eskildsen from turbopuffer gave the clearest articulation: the machines that learn need machines to practice on, and those machines run on regular processors. The bottleneck everyone missed is the one nobody thought was scarce.

## The silicon double squeeze

The CPU shortage is structural, not cyclical. Katelyn Lesse from Anthropic laid out the supply chain dynamics: at TSMC, GPUs and CPUs compete for the same production lines, and GPUs are more profitable per wafer. Memory manufacturers — SK Hynix, Samsung, Micron — have shifted capacity to high-bandwidth memory for AI accelerators, which is more profitable than standard DRAM. The result is a double squeeze: fewer CPU wafers and more expensive CPU memory. AMD, which does not own its fabs, is particularly exposed. Prices are up 10 to 20 percent, and Lesse's advice to teams that never planned CPU capacity is blunt: forecast 12 months ahead, or do not expect to have servers.

The Pragmatic Engineer's report lands alongside a signal that demand will only intensify. Anthropic released Claude Opus 5.5, matching the company's top model at 40 percent less cost, with 30 percent faster output. OpenAI answered 90 minutes later with GPT-6 Sol and Luna at $2/$10 per million tokens — half the promotional pricing of GPT-5.6. [The two-week moat](https://engineeringforward.substack.com/p/the-two-week-moat) described how 133 weeks of developer loyalty evaporated in 14 days when prices dropped. The same dynamic applies to compute: cheaper models do not reduce demand. They amplify it. More capable models at lower cost means more agents doing more work, which means more CPU consumption. AWS Distinguished Engineer Marc Brooker predicted that humans will have no role in routinely reviewing code by hand — a future that requires even more automated compilation and test execution, all running on processors nobody can buy.

## The data frontier goes physical

If silicon is the first constraint, data is the second. CO/AI reported that more than 50 tons of used books have been shipped from Japan to the United States, likely for AI training. Used bookstores across Japan received machine-timed bulk orders for philosophy, law, medicine, and Edo-era history, all routed to a single warehouse in Okayama. The trade follows a playbook Anthropic established in 2025: buy millions of used books, cut the bindings, scan them, discard the physical copies. A federal judge ruled it fair use in Bartz v. Anthropic. Japan's out-of-print shelves are, as CO/AI put it, a reservoir no model has touched.

The internet has been scraped. What remains is physical archives: books, film, video, and eventually first-person capture from wearables. The reality TV math is staggering. Warner Bros. Discovery's cable networks produce 3,000-plus hours of programming per year. At a 100:1 shooting ratio — the raw footage behind every edited show — that is 300,000 hours annually of people arguing, cooking, crying, and flipping houses. A decade of archives equals millions of hours of unscripted human behavior. YouTubers are already selling unpublished footage for $1 to $4 per minute to OpenAI and Google. The reality TV tape, now owned by Paramount carrying roughly $80 billion in debt from its $111 billion WBD acquisition, is orders of magnitude larger. Debt that size goes hunting for assets nobody has priced.

Meta's glasses are the frontier that regulators have not caught up with. Muse is coming to Ray-Ban glasses with live video, AI on by default, voice recordings kept for up to a year, and no opt-out from training. The privacy implications extend beyond the wearer: everyone in the room never signed a release. First-person video, captured continuously in every setting, is the purest training data trove yet — and the least consented. The Gallup-Microsoft data CO/AI cited adds a dimension: Americans are among the few populations who feel negatively about the AI they built. China, Singapore, and Kenya are most positive. The countries building the models and the countries most enthusiastic about them are not the same ones.

## The measurement layer goes mainstream

While the physical constraints tighten, the software layer is developing its own discipline. Nearly half of 25 product manager job openings that Lenny Rachitsky shared required eval-writing experience. Sentry went from near-zero eval runs in May to approximately 1,800 per month. Every's Context Window newsletter argues that the industry has crossed a threshold: AI quality assessment is no longer experimental. It is a core competency.

The logic is straightforward. Multiple frontier models can handle most knowledge work. The differentiator has shifted from raw intelligence to fit: which model suits your specific workflow, taste, and budget. Personal benchmarks operationalize this. Every is building them for each employee. Grok 4.7's uneven launch proved the point: it initially scored 42 percent versus Grok 4.6's 84 percent on personal benchmarks, improved before public release, but remained divisive — good for coding, poor for writing. One tester described its editorial judgment as having big Elon Musk energy. The benchmark cut through the marketing in a way that no public leaderboard could.

[The checking floor](https://engineeringforward.substack.com/p/the-checking-floor) described Jev as a verifier that returns calibrated probabilities for less than a cent per thousand judgments. The evals trend is the same pattern at the organizational level: companies that cannot define what "correct" means for their use case are not ready to automate. Those that can define it are building private regulatory frameworks — golden datasets, automated metrics, production monitoring — that function as internal quality gates. No external body mandates them. Companies build them because the cost of not building them is worse.

## The infrastructure nobody watches

ByteByteGo's guide to the data lifecycle is the kind of foundational topic that gets buried under model announcements. A single data point can live in a database, a cache, a search index, an analytics pipeline, and backups — each with its own update schedule and lifetime. As AI agents generate and consume data autonomously, they create new copies and derivatives that extend the lifecycle beyond traditional application boundaries. GDPR's right to deletion becomes harder to honor when an agent has propagated information across five systems, some of which update on different schedules.

The connection between data lifecycle and the CPU shortage is not obvious but it is real. Agents that run tools and compile code are not just consuming CPU cycles — they are generating data at every step. Logs, intermediate results, cached context, eval outputs. The data lifecycle article's framing, that growing systems amplify complexity because the same data point propagates to more components, applies with extra force when the components are autonomous agents creating their own derivative data. The infrastructure that nobody watches is the infrastructure that breaks first.

## The human adaptation

Lenny Rachitsky's field notes from inside an AI-native company capture something the infrastructure stories miss. The disorientation of a millennial who built their career in pre-AI tech — where individual expertise and manual work were valued — now navigating a workplace where AI augmentation is the default. The CPU shortage is an engineering problem. The data lifecycle is an architecture problem. The transition from pre-AI to AI-native work culture is a human problem, and it does not solve itself with better models.

Maggie Appleton's concept of capability gaslighting — when frontier models convince you they are experts, then fail the same task the next day — names the trust problem at the center of this transition. [The adapter economy](https://engineeringforward.substack.com/p/the-adapter-economy) described how adapters and judges close the gap between demonstration and reliability. But the gap exists because the physical world does not behave like a language model. CPUs are not tokens. You cannot generate more silicon by prompting harder. Books weigh tons. Server racks take six months to deliver. Intelligence consumes resources, and those resources are finite.

The companies that win the next phase will be the ones that planned for the physical costs before the software was ready. Capacity planning for CPUs. Data pipelines that account for agent-generated derivatives. Evals that define correct before deployment. The work is less glamorous than model launches. It is also the work that determines whether the intelligence you deployed survives contact with the real world.

---

## Sources
1. [Revolut Security Breach; Europe's Leading Pre-Seed Investors in 2026](https://sifted.eu)
2. [Why Evals Are So Hot Right Now](https://every.to)
3. [What It's Like to Work at an AI-Native Company](https://www.lennysnewsletter.com)
4. [The Pulse: A New Trend of CPU Shortages](https://newsletter.pragmaticengineer.com)
5. [The Life of Data: From Creation to Deletion](https://blog.bytebytego.com)
6. [Japan's Books by the Ton; Reality TV Tape; Meta Glasses — The Next AI Training Data](https://coai.beehiiv.com)
7. [Affirm's AI Underwriting Works Best on Borrowers with No FICO Score](https://linas.substack.com)
8. [Anthropic: We're Not Trying to Eat Startups' Lunch](https://sifted.eu)
9. [How to Get the Most Out of Jev](https://every.to)
10. [Design Engineering with Maggie Appleton](https://newsletter.pragmaticengineer.com)
11. [How to Customize a Model to Learn New Tricks](https://blog.bytebytego.com)
12. [Opus 5.5, GPT-6 Sol and Luna](https://www.theunwindai.com)
13. [Why Muse Makes Sense for Everyone — Except Amazon](https://coai.beehiiv.com)
14. [Amazon Blocked Meta's Muse AI Agent to Protect $76 Billion in Ad Revenue](https://linas.substack.com)
15. [Inside Mistral's Latest Acquisition](https://sifted.eu)