from pathlib import Path
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
import subprocess, re, json, unicodedata

REPO = Path('.').resolve()
TODAY = '2026-04-23'
TS = '150300'
TS_HUMAN = '2026-04-23 15:03:00'
BASE = 'https://github.com/blamouche/Engineering-Forward/blob/main/'

entries = [
    {
        'original': 'https://arstechnica.com/ai/2026/04/google-unveils-two-new-tpus-designed-for-the-agentic-era',
        'title': 'Google unveils two new TPUs designed for the "agentic era"',
        'date': 'April 23, 2026',
        'author': 'Ryan Whitwam',
        'keywords': 'Google, TPU, inference, training, AI infrastructure, data centers, Gemini',
        'elevator': 'Google is splitting its eighth-generation TPU line into separate training and inference chips, betting that agent-heavy AI workloads need different hardware and tighter efficiency tuning.',
        'takeaways': [
            'Google introduced TPU 8t for training and TPU 8i for inference instead of treating both jobs as one hardware problem.',
            'The company frames the shift as a response to agentic workloads, where long-running inference and massive training have different bottlenecks.',
            'Google is emphasizing efficiency, with better performance per watt, larger SRAM caches, and ARM-based host CPUs.',
            'The launch reinforces Google’s strategy of owning the full stack from models to chips to data center design.',
            'For customers, the real pitch is lower operational cost and better scaling for production AI systems, not just bigger benchmark numbers.'
        ],
        'synthesis': 'Google’s latest TPU launch is notable less for raw speed than for the product decision behind it. Instead of shipping a single chip family and asking customers to stretch it across the full model lifecycle, Google is now separating training and inference into TPU 8t and TPU 8i. That reflects a more mature view of the market. Training frontier models and serving them in production are no longer adjacent workloads with slightly different tuning needs. They are different economic problems. Training rewards massive cluster scale and resilience. Inference rewards memory locality, cache efficiency, and cost control across many concurrent jobs.\n\nThat distinction matters even more in what Google calls the “agentic era.” Agents do not simply answer one prompt and stop. They hold longer context, call tools, run multi-step tasks, and often sit inside business workflows that need predictable cost and latency. TPU 8i’s larger SRAM and Google’s emphasis on key-value cache retention point directly at that production reality. Meanwhile TPU 8t is about shortening frontier model training cycles so Google can keep feeding Gemini and third-party model builders faster iteration loops.\n\nThe broader strategic point is that Google continues to play a full-stack game. These chips are tied to Google-designed CPUs, Google networking, Google data center layouts, and Google’s own model ambitions. That gives the company more room to optimize for efficiency at a time when AI spending is under pressure to justify itself. It also makes TPU adoption more attractive for developers who want a coherent platform rather than a pile of loosely integrated components.\n\nThe article also hints at the industry’s real constraint. AI infrastructure is no longer just about buying the most compute. It is about getting more useful work from each watt, each rack, and each inference run. Google’s split TPU strategy suggests the next phase of competition will be won by the companies that tailor hardware to the actual economics of training and serving agents, not by the ones that simply make one giant chip faster.',
    },
    {
        'original': 'https://sierra.ai/blog/the-ai-native-interview',
        'title': 'The AI-native interview',
        'date': 'April 23, 2026',
        'author': 'Sierra',
        'keywords': 'hiring, software engineering, coding agents, interviews, product thinking, AI-native teams',
        'elevator': 'Sierra redesigned engineering hiring around an AI-assisted build session, arguing that judgment, product sense, and scope management now matter more than raw syntax recall.',
        'takeaways': [
            'Sierra replaced coding and algorithms interviews with a plan-build-review onsite built around AI tools.',
            'The company wants interviews to mirror real work, where engineers define scope, use agents, and iterate under constraints.',
            'Its process prioritizes agency, product judgment, and technical tradeoffs over whiteboard-style mechanics.',
            'Sierra also swapped its coding phone screen for system design and is piloting an AI-native debugging interview.',
            'The shift suggests hiring loops are adapting to a world where coding leverage increasingly comes from orchestration and decision quality.'
        ],
        'synthesis': 'Sierra’s hiring redesign is a useful signal that engineering evaluation is starting to move with the tooling. The company argues that traditional loops still over-index on mechanical fluency, such as typing syntax from memory or solving algorithm puzzles detached from any product context. That made sense when implementation throughput was a strong proxy for output. It makes less sense when strong candidates can rely on coding agents to generate boilerplate, explore options, and scaffold whole features in a fraction of the time.\n\nIts replacement is an AI-native onsite with three phases: define a product, build it with the tools of your choice, then review both the outcome and the choices behind it. The core idea is that engineering value is shifting toward judgment. Can the candidate choose scope intelligently, recover when they get stuck, and make product and architectural tradeoffs that fit the time box? Those are much closer to the questions actual teams care about than whether someone can reproduce a memorized algorithm under pressure.\n\nThe interesting part is that Sierra is not treating AI use as cheating or as an optional add-on. It is making tool use part of the signal. That is probably where many companies are heading. If AI is part of the day-to-day job, interview loops that ban it entirely risk selecting for an increasingly irrelevant skill mix. At the same time, Sierra is not saying raw engineering quality no longer matters. The review stage still looks closely at code structure, extensibility, data modeling, and the path to production. The difference is that these concerns are examined in context rather than in abstraction.\n\nMore broadly, the article shows how AI is changing the shape of engineering careers. When implementation gets cheaper, the gap between “can build something” and “can build the right thing” widens. Hiring has to measure taste, initiative, and systems thinking more directly. Sierra’s process is one early attempt to do exactly that.',
    },
    {
        'original': 'https://maggieappleton.com/zero-alignment',
        'title': 'One Developer, Two Dozen Agents, Zero Alignment',
        'date': 'April 23, 2026',
        'author': 'Maggie Appleton',
        'keywords': 'agents, software teams, coordination, GitHub Next, collaboration, developer tools',
        'elevator': 'Maggie Appleton argues that agentic development will fail if teams only scale individual output, because the real bottleneck is shared context and alignment before code gets generated.',
        'takeaways': [
            'The essay criticizes the fantasy that one developer with many agents can replace the coordination work of a team.',
            'As implementation gets cheaper, choosing the right work and aligning on it becomes more important and more fragile.',
            'Pull requests and issues are described as outdated primitives for a world of fast, parallel agent output.',
            'Appleton highlights how business context, politics, user insight, and product vision live outside the codebase.',
            'Her Ace prototype explores multiplayer prompting and shared cloud workspaces as a better surface for collaborative agent work.'
        ],
        'synthesis': 'Maggie Appleton’s argument lands because it targets the weakest assumption in a lot of agent hype. The fantasy is simple: if one engineer can supervise a wall of coding agents, software output will scale linearly. Her critique is that software has never been bottlenecked only by typing speed. Teams fail because they build the wrong thing, duplicate work, collide in the same files, or discover too late that nobody agreed on the plan. Agents reduce implementation cost, which means those alignment failures get amplified rather than solved.\n\nThat is why her attack on the “single-player interface” matters. Many current tools are optimized for one operator delegating work privately, then pushing the result into a PR once the code already exists. But when agent output becomes cheap and abundant, the pull request is carrying too much weight. It becomes the place where planning, review, and coordination all collapse into one late-stage checkpoint. Appleton argues that this is the wrong primitive for the next phase of software development.\n\nHer deeper point is that most of the important context for building software does not live in repositories. It lives in people’s heads and in organizational systems: goals, constraints, user pain, political ownership, and previous decisions. Agents cannot infer that reliably on their own. If the tooling does not make it easy for humans to surface that context early and continuously, teams will generate more code but not necessarily more value.\n\nThe Ace prototype she describes is one answer: multiplayer sessions, shared sandboxes, visible prompting history, and a common workspace where PMs, designers, and engineers can shape the work together while agents execute. Even if Ace itself is just a prototype, the framing feels right. The next generation of developer tools probably needs to optimize less for solo coding velocity and more for collective alignment around fast, agent-assisted execution.',
    },
    {
        'original': 'https://kwokchain.com/2026/04/23/cursor-and-spacex-in-search-of-a-complete-loop',
        'title': 'Cursor and SpaceX: In search of a complete loop',
        'date': 'April 23, 2026',
        'author': 'Kwokchain',
        'keywords': 'Cursor, SpaceX, xAI, coding agents, compute, product-model loop, AI strategy',
        'elevator': 'This essay argues that top AI labs now need both model compute and product distribution, framing the rumored Cursor-SpaceX tie-up as an attempt to close that loop.',
        'takeaways': [
            'The piece claims frontier AI competition increasingly requires owning both the model layer and the product harness around it.',
            'Coding is presented as the clearest domain where the feedback loop between product usage and model improvement already compounds.',
            'Cursor is portrayed as strong on product and user traction but weaker on long-term compute and frontier training capacity.',
            'SpaceX/xAI is portrayed as compute-rich but weak on product, data, and research continuity in coding.',
            'The proposed deal structure is interpreted as a way to align both sides without forcing an immediate full acquisition.'
        ],
        'synthesis': 'Kwokchain’s piece is speculative, but the framework is more useful than the rumored transaction details. The central claim is that being a serious AI contender no longer means choosing between models and products. It means building a loop in which the product generates the usage, data, and operational feedback that improve the model, while the model expands what the product can do. Coding is where that loop is easiest to see because model quality, harness quality, and workflow fit all feed each other quickly.\n\nThat is why Cursor sits in an awkward but interesting position. On one hand, it has product traction, distribution, and a user-facing understanding of how coding agents are actually used. On the other, the market is drifting toward labs that own more of the stack, including training, inference economics, and proprietary models. The article argues that Cursor’s biggest strategic risk is not weak growth but incomplete vertical integration. If the best coding products increasingly need their own model advantage, product momentum alone may not be enough.\n\nThe mirror image is xAI or SpaceX. If they have access to large-scale compute but lack the product, data flywheel, and research-product rhythm that coding agents require, then they also have only half the machine. That is what the author means by a “complete loop.” Whether or not this specific tie-up proves real or durable, the idea resonates with a broader trend across the market. Labs want products. Product companies want proprietary models. Everyone is being pushed toward convergence.\n\nThe useful takeaway is strategic rather than gossipy. AI companies increasingly have to decide whether they are content to sit at one layer or whether they need tighter control over the entire feedback loop. Coding agents may simply be the first market where that pressure becomes impossible to ignore.',
    },
    {
        'original': 'https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more',
        'title': 'OpenAI unveils Workspace Agents, a successor to custom GPTs for enterprises that can plug directly into Slack, Salesforce and more',
        'date': 'April 23, 2026',
        'author': 'VentureBeat',
        'keywords': 'OpenAI, workspace agents, enterprise AI, Slack, Salesforce, Codex, governance',
        'elevator': 'OpenAI is turning custom GPTs into shared, permissioned workplace agents backed by Codex sessions, with connectors, scheduling, persistence, and enterprise controls.',
        'takeaways': [
            'Workspace Agents are positioned as a no-code successor to custom GPTs for business and enterprise teams.',
            'The product is notable because it runs on top of Codex-style cloud sessions with tools, memory, and code execution.',
            'OpenAI wants agents to live inside Slack and other work tools instead of staying inside one ChatGPT tab.',
            'Scheduling and persistence make the agents suitable for recurring multi-step workflows rather than one-off chats.',
            'Governance, approval policies, and role-based controls are central because these agents can act across business systems.'
        ],
        'synthesis': 'OpenAI’s Workspace Agents launch matters because it pushes enterprise AI another step away from chat and toward operational software. Custom GPTs gave organizations a way to package instructions and connectors around a chatbot. Workspace Agents appear to move that idea onto a more capable substrate: Codex-backed cloud sessions with tools, memory, code execution, scheduling, and shared organizational visibility. That is a different category of product. It is much closer to an agent runtime than a customized assistant.\n\nThe most important shift is where these agents can live. OpenAI is not asking teams to keep jumping back into ChatGPT to get value. It wants the agents to show up in Slack, pull from systems like Salesforce or Google Drive, and keep working when the user is no longer present. That is the enterprise wedge. Real business processes span tools, permissions, and handoffs. If an agent can follow the work across those surfaces and persist between runs, it becomes much more likely to automate a useful recurring job instead of just helping one person draft text faster.\n\nThe article also highlights why the Codex connection matters. Once an agent can run code, transform files, remember corrections, and execute multi-step operations in a controlled environment, it can do more than summarize. It can actually complete work. That is a stronger promise, but it also raises the stakes on governance. OpenAI’s emphasis on approval flows, admin controls, service accounts, and auditability suggests it knows enterprise adoption will be won on trust as much as capability.\n\nSeen more broadly, Workspace Agents look like OpenAI’s attempt to replace the “chat with a smart model” paradigm with “deploy and manage a fleet of AI coworkers.” If that product holds up in practice, the company is not just iterating on ChatGPT. It is trying to become part of the orchestration layer for knowledge work.',
    },
    {
        'original': 'https://www.digitalocean.com/blog/llm-inference-tradeoffs',
        'title': 'The LLM Inference Trilemma: Throughput, Latency, Cost',
        'date': 'April 23, 2026',
        'author': 'DigitalOcean',
        'keywords': 'LLM inference, latency, throughput, GPU cost, batching, quantization, serving',
        'elevator': 'DigitalOcean lays out the core serving tradeoff in LLM systems: pushing throughput, latency, and cost at the same time is impossible, so teams need to optimize around workload shape rather than a single benchmark.',
        'takeaways': [
            'The piece frames inference as a trilemma between throughput, latency, and cost instead of a one-dimensional pricing problem.',
            'It argues that real serving cost includes hardware, operations, utilization gaps, and engineering labor.',
            'Model architecture, quantization, parallelism, and batching are presented as the main economic levers.',
            'Dense and MoE models create different infrastructure bottlenecks, especially around memory and interconnects.',
            'The article encourages teams to benchmark against their own workload and business priorities, not generic token metrics.'
        ],
        'synthesis': 'This DigitalOcean post is useful because it treats LLM serving as a systems problem rather than a slogan about dollars per million tokens. The central idea is simple: inference lives inside a trilemma. If you want higher throughput, latency usually worsens. If you clamp latency, utilization falls and costs rise. If you optimize aggressively for cost, you often sacrifice one of the other two. That framing sounds obvious, but it cuts against a lot of shallow infrastructure discussion that pretends there is one universally best deployment setup.\n\nThe article’s strongest move is widening the meaning of cost. Hardware rental or depreciation is only part of the picture. Idle capacity, low overnight utilization, orchestration complexity, tuning time, and engineering effort all shape the real economics of serving models. That is especially true for dedicated GPU nodes, where you often pay for an entire box even if your workload only uses part of it efficiently. Inference economics are therefore inseparable from scheduling, traffic shape, and whether the team can keep expensive hardware busy.\n\nIts breakdown of levers is also practical. Quantization, batching, tensor or expert parallelism, and model choice all push the system toward different points on the cost-latency-throughput surface. Dense models reward one set of decisions, MoE models another. Some workloads justify low latency at high cost, like interactive copilots. Others want bulk throughput, like overnight document processing. The article’s implicit advice is that teams should stop looking for a single serving recipe and instead choose an operating point that matches product reality.\n\nThat is the broader lesson. As AI products mature, serving infrastructure becomes a business design choice, not just an optimization problem for infra specialists. The right stack depends on how users wait, how often they return, and what economics the product can sustain. This post does a good job making that tradeoff legible.',
    },
    {
        'original': 'https://linas.substack.com/p/fintechpulse1071',
        'title': 'AngelList USVC Review: 2.5% Fees for Retail VC',
        'date': 'April 23, 2026',
        'author': 'Linas Beliunas',
        'keywords': 'AngelList, USVC, venture capital, retail investing, AI startups, fees, fintech',
        'elevator': 'Linas argues that AngelList’s new retail VC vehicle packages elite AI startup exposure into an accessible product, but the real story is the fee stack, valuation opacity, and liquidity tradeoffs under the hood.',
        'takeaways': [
            'The piece examines USVC as a retail-friendly venture product tied to hot AI company exposure.',
            'Its main critique is that marketing excitement masks layered fees, subjective valuation methods, and weak liquidity terms.',
            'The article treats the fund as a sign of how AI hype is pulling retail investors deeper into private-market narratives.',
            'It suggests managers are being paid for asset gathering as much as for long-term returns.',
            'The broader implication is that access to elite startup baskets is only attractive if the structure is fair and legible.'
        ],
        'synthesis': 'This newsletter issue is nominally about AngelList’s USVC product, but the more interesting point is what it says about the current AI investment cycle. A vehicle like this only works because private-market AI exposure has become aspirational enough that retail investors will tolerate complexity for a shot at owning a slice of the story. Linas’s argument is that the prospectus matters more than the brand halo. Once you read beyond the marketing, the product starts to look less like democratized venture access and more like a heavily packaged financial wrapper built to capture demand.\n\nThe critique focuses on familiar private-market weaknesses: layered fees, uncertain valuation marks, manager incentives tilted toward gathering assets, and liquidity terms that leave buyers with much less flexibility than the branding suggests. None of that automatically makes the product bad. Venture exposure is inherently messy. But it does mean the product should be judged on structure and incentives, not just on the glamour of the underlying names. If the portfolio is a basket of the most talked-about AI companies, that may attract attention, but it does not remove the frictions that make venture investing hard in the first place.\n\nThe AI angle matters because it increases the temptation to ignore those frictions. In a market where OpenAI, Anthropic, and similar companies dominate headlines, products that promise indirect participation become easier to sell. That turns retail curiosity into a monetizable distribution channel. The danger is that access gets confused with alignment. Investors may feel closer to the upside than they really are once fees, lockups, and valuation subjectivity are accounted for.\n\nSo the article works as a reminder that AI finance products deserve the same skepticism as any other financial engineering. The story may be new, but the structural questions are old: who gets the upside, who bears the uncertainty, and who gets paid regardless of performance?',
    },
    {
        'original': 'https://linas.substack.com/p/aistartupmarket',
        'title': 'These AI Startups Just Raised $187M, and They Reveal Exactly Where the Market Is Headed',
        'date': 'April 23, 2026',
        'author': 'Linas Beliunas',
        'keywords': 'AI startups, venture capital, funding, pitch decks, vertical AI, startup market',
        'elevator': 'By looking past mega-round headlines, Linas argues that the more revealing signal is how mid-sized AI startups are pitching focused vertical depth, proprietary data, and workflow ownership.',
        'takeaways': [
            'The piece notes that most AI funding is still highly concentrated in a few giant companies.',
            'It argues that smaller but meaningful rounds reveal where investors still see differentiated opportunity.',
            'The winning pattern is depth over generic wrappers, especially around proprietary data and mission-critical workflows.',
            'Pitch decks are treated as a lens into how founders position traction, moats, and market narratives in 2026.',
            'The broader market is described as K-shaped, with a widening gap between standout startups and everyone else.'
        ],
        'synthesis': 'Linas’s funding roundup is useful because it looks below the spectacular mega-rounds that dominate AI coverage. The headline market is distorted by a handful of giant financings, but those deals do not necessarily tell founders what kinds of smaller companies can still raise meaningful money. By focusing on roughly $187 million spread across ten startups, the piece tries to identify the more actionable pattern. The answer is not broad, generic AI tooling. It is companies that own narrow workflows, differentiated data, and real domain-specific leverage.\n\nThat framing matches a wider shift in the market. Once capital floods into foundational labs, the rest of the ecosystem is forced to justify itself more sharply. Thin wrappers and vague horizontal assistants are harder to fund because investors increasingly assume that generic capability will be eaten by the platforms themselves. What still looks attractive are startups that can embed into a valuable operational loop, collect proprietary signal, and become difficult to replace even as model quality rises.\n\nThe pitch deck angle adds another layer. Decks are not just fundraising artifacts. They are compressed statements of how founders think the market rewards them. If many of the better-funded companies are emphasizing domain depth, workflow control, and systems of action rather than broad “AI for everyone” language, that tells you how capital allocators are screening opportunity in 2026. The message is that depth now beats breadth.\n\nThe broader implication is slightly harsher. AI venture remains huge, but the distribution is increasingly uneven. A small set of category leaders absorbs enormous capital, while everyone else has to prove much more specific defensibility. That does not make the market unattractive, but it does make it much less forgiving for startups that do not own something hard to copy.',
    },
    {
        'original': 'https://linas.substack.com/p/top10aistartups2026',
        'title': 'Top 10 AI Startups to Watch in 2026',
        'date': 'April 23, 2026',
        'author': 'Linas Beliunas',
        'keywords': 'AI startups, venture capital, startup strategy, pitch decks, ElevenLabs, Synthesia, Reflexivity',
        'elevator': 'This curated list spotlights AI startups with real traction and clear category narratives, using their decks and metrics as a shortcut for how ambitious founders are selling the next wave of AI businesses.',
        'takeaways': [
            'The list focuses on AI startups that already show revenue, category momentum, or unusually strong investor backing.',
            'It spans areas such as voice, video, automation, and financial workflows rather than only foundational models.',
            'The emphasis is on practical business quality, including traction, go-to-market choices, and competitive narrative.',
            'Pitch decks are used as a tactical resource for builders and investors studying how winning companies frame themselves.',
            'The roundup reflects a 2026 market that values monetization and category leadership, not just technical novelty.'
        ],
        'synthesis': 'Lists of “startups to watch” are often disposable, but this one is still a useful market snapshot because of what it chooses to emphasize. Linas is not only ranking companies by hype. He is using decks, operating metrics, and investor backing to frame what a convincing AI company looks like in 2026. The pattern is clear: investors want signs that a company can become a durable business, not just a technically interesting demo. Revenue quality, go-to-market clarity, and category ownership show up more strongly than abstract claims about intelligence.\n\nThat matters because the startup conversation around AI is maturing. In earlier waves, it was enough to show that a product used a new model or felt magical. Now many categories are crowded, and foundational capability diffuses quickly. Startups therefore need a sharper reason to exist. Some in this list stand out by dominating a modality like voice or video. Others matter because they own a workflow, especially in categories like finance where distribution, trust, and domain fit can be stronger moats than pure model quality.\n\nThe pitch deck framing is also practical. Good decks reveal how founders translate raw momentum into investor conviction. They show which metrics matter, how teams define their wedge, and where they claim defensibility. For operators, that can be as valuable as the company names themselves. It helps decode the narrative templates that capital is currently rewarding.\n\nThe bigger takeaway is that the AI startup market is no longer asking whether there will be big companies outside the labs. It is asking what kinds of companies can still build lasting value as model access becomes more common. This list suggests the answer lies in owned workflows, strong distribution, and monetization discipline rather than in generic “AI-powered” positioning.',
    },
    {
        'original': 'https://linas.substack.com/p/claude-managed-agents-guide',
        'reuse_path': 'src/2026-04/20260422-the-ultimate-guide-to-claude-managed-agents.md'
    },
    {
        'original': 'https://linas.substack.com/p/fintechpulse1043',
        'title': 'Robinhood: the $4.5 billion revenue dark horse Wall Street still underestimates; Shopify is the commerce OS that prints cash while building the rails for AI’s shopping revolution',
        'date': 'April 23, 2026',
        'author': 'Linas Beliunas',
        'keywords': 'Robinhood, Shopify, fintech, AI commerce, financial results, retail investing, shopping agents',
        'elevator': 'This issue pairs two business analyses, arguing that Robinhood is becoming a broader financial platform while Shopify is positioning itself as the infrastructure layer for AI-native commerce.',
        'takeaways': [
            'Robinhood is framed as more diversified and operationally stronger than the market narrative around crypto volatility suggests.',
            'Shopify is framed as a commerce platform whose AI relevance comes from controlling merchant infrastructure, not from flashy consumer chat features.',
            'The article emphasizes revenue mix, margin quality, and platform leverage rather than short-term stock moves alone.',
            'It ties fintech performance to broader questions about who owns distribution in an AI-mediated buying journey.',
            'The piece suggests that AI commerce winners may be the companies that already sit in the transaction flow.'
        ],
        'synthesis': 'This newsletter combines two company analyses, but the deeper connection is about platform position in an AI-shaped market. On Robinhood, Linas argues that investors are still viewing the company through an outdated lens: a volatile retail brokerage tied too closely to crypto trading cycles. The counterpoint is that Robinhood has become a broader financial services platform with more diversified revenue lines and much stronger operating leverage than the old meme-stock narrative implies. That does not make the stock obviously cheap, but it does suggest the business deserves a different category in investors’ mental model.\n\nThe Shopify side is even more relevant to AI strategy. The article presents Shopify not as a generic ecommerce software vendor, but as infrastructure for how digital commerce will function when agents increasingly influence or execute purchasing flows. That is a more powerful position than simply adding AI features to a merchant dashboard. If shopping becomes more automated and intent moves through agentic interfaces, the platforms that control catalog, checkout, merchant tooling, and transaction rails gain leverage. They become the substrate that AI systems have to route through.\n\nRead together, the two sections make a common point. In AI-adjacent markets, the winners are often the companies that already own a critical system of action, not the ones making the loudest claims about intelligence. Robinhood owns user relationships and financial activity. Shopify owns merchant infrastructure and commerce execution. Those positions can be strengthened by AI, even if the companies are not the ones training frontier models.\n\nThat is a useful reminder for watching public markets. AI value will not only accrue to labs and flashy startups. It will also accrue to incumbents that sit close to money movement, workflow execution, or distribution and can quietly become the default rails for agent-mediated activity.',
    },
    {
        'original': 'https://www.anthropic.com/news/managed-agents',
        'fetch_error': 'FETCH_ERROR: https://www.anthropic.com/news/managed-agents — 404 Not Found'
    }
]


def normalize(url: str) -> str:
    p = urlparse(url)
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not (k.startswith('utm_') or k in {'ref', 'fbclid', 'gclid', 'mc_cid', 'mc_eid'})]
    return urlunparse((p.scheme, p.netloc, p.path, p.params, urlencode(q), ''))


def slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii').lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text[:90].rstrip('-')


def bump_version(message: str) -> str:
    vp = Path('.prompt-hub/version.md')
    parts = vp.read_text().strip().split('.')
    parts[-1] = str(int(parts[-1]) + 1)
    new = '.'.join(parts)
    vp.write_text(new + '\n')
    rp = Path('.prompt-hub/releases.md')
    rp.write_text(f'## {new} - {TODAY}\n- {message}\n\n' + rp.read_text())
    return new


def append_memory(action: str, files_or_cmds: str, outcome: str, next_step: str):
    mp = Path('.prompt-hub/memory.md')
    with mp.open('a') as f:
        f.write(f"\n## {TS_HUMAN} +0200\n- actor: agent\n- action: {action}\n- files_changed_or_commands: {files_or_cmds}\n- outcome: {outcome}\n- next_step: {next_step}\n")


def remove_url(original: str):
    p = Path('LIST.md')
    urls = [line.strip() for line in p.read_text().splitlines() if line.strip()]
    urls = [u for u in urls if u != original]
    p.write_text(('\n'.join(urls) + '\n') if urls else '')


def create_article(entry):
    slug = slugify(entry['title'])
    path = Path(f"src/2026-04/20260423-{slug}.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {entry['title']}",
        '',
        f"**Source**: {normalize(entry['original'])}",
        f"**Date**: {entry['date']}",
        f"**Author**: {entry['author']}",
        f"**Keywords**: {entry['keywords']}",
        '',
        '## Elevator pitch',
        entry['elevator'],
        '',
        '## Takeaways',
    ]
    lines += [f"- {x}" for x in entry['takeaways']]
    lines += ['', '## Synthesis', entry['synthesis'], '']
    path.write_text('\n'.join(lines))
    subprocess.run(['python3', '.prompt-hub/todo/update_readme_engineering_forward.py', str(path)], check=True)
    return path


processed = []
errors = []

for entry in entries:
    original = entry['original']
    clean = normalize(original)
    if 'fetch_error' in entry:
        remove_url(original)
        errors.append(entry['fetch_error'])
        bump_version(f"Process article error: {clean}")
        append_memory(
            f"scan-list removed `{clean}` after article fetch failed with 404.",
            "`LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`",
            'partial',
            'Continue with next URL in LIST.md.'
        )
        subprocess.run(['git', 'add', 'LIST.md', '.prompt-hub/version.md', '.prompt-hub/releases.md', '.prompt-hub/memory.md'], check=True)
        subprocess.run(['git', 'commit', '-m', f'Process article: {clean}'], check=True)
        continue

    if 'reuse_path' in entry:
        path = Path(entry['reuse_path'])
        text = path.read_text()
        title = re.search(r'^#\s+(.+)$', text, re.M).group(1).strip()
        elevator = re.search(r'## Elevator pitch\n(.+)', text).group(1).strip()
        remove_url(original)
        bump_version(f"Process article: {title}")
        append_memory(
            f"scan-list reused existing synthesis for `{clean}` and removed it from the queue.",
            "`LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`",
            'success',
            'Continue with next URL in LIST.md.'
        )
        subprocess.run(['git', 'add', 'LIST.md', '.prompt-hub/version.md', '.prompt-hub/releases.md', '.prompt-hub/memory.md'], check=True)
        subprocess.run(['git', 'commit', '-m', f'Process article: {title}'], check=True)
        processed.append({'title': title, 'elevator': elevator, 'path': str(path)})
        continue

    path = create_article(entry)
    remove_url(original)
    bump_version(f"Process article: {entry['title']}")
    append_memory(
        f"scan-list created synthesis for `{clean}` and removed it from the queue.",
        f"`{path}`, `README.md`, `LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`",
        'success',
        'Continue with next URL in LIST.md.'
    )
    subprocess.run(['git', 'add', str(path), 'README.md', 'LIST.md', '.prompt-hub/version.md', '.prompt-hub/releases.md', '.prompt-hub/memory.md'], check=True)
    subprocess.run(['git', 'commit', '-m', f"Process article: {entry['title']}"], check=True)
    processed.append({'title': entry['title'], 'elevator': entry['elevator'], 'path': str(path)})

recap_path = Path(f'synthesis/{TODAY} - {TS} - batch recap.md')
recap_path.parent.mkdir(parents=True, exist_ok=True)
parts = [f'# Batch Recap - {TS_HUMAN}', '']
for item in processed:
    parts.extend([item['title'], item['elevator'], f'Synthese: {BASE}{item["path"]}', ''])
if errors:
    parts.extend(['## Errors', ''])
    parts.extend([f'- {e}' for e in errors])
recap_path.write_text('\n'.join(parts).rstrip() + '\n')
recap_text = recap_path.read_text()
assert all(item['title'] in recap_text for item in processed)
assert all(f'{BASE}{item["path"]}' in recap_text for item in processed)
assert Path('LIST.md').read_text() == ''
bump_version(f'Add batch recap: {TODAY} {TS}')
append_memory(
    f"scan-list created and verified `{recap_path}` after processing {len(processed)} URL(s) with {len(errors)} error(s).",
    f"`{recap_path}`, `LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`",
    'success',
    'Push all remaining commits.'
)
subprocess.run(['git', 'add', str(recap_path), 'LIST.md', '.prompt-hub/version.md', '.prompt-hub/releases.md', '.prompt-hub/memory.md'], check=True)
subprocess.run(['git', 'commit', '-m', f'Add batch recap: {TODAY} {TS}'], check=True)
print(json.dumps({'processed': len(processed), 'errors': errors, 'recap': str(recap_path)}, ensure_ascii=False))
