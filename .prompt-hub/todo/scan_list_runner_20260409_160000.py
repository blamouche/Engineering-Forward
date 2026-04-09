from pathlib import Path
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
import subprocess, re, json

REPO = Path('.').resolve()
BASE = 'https://github.com/blamouche/Engineering-Forward/blob/main/'
RUN_STAMP = '2026-04-09 16:00:00'
RUN_FILE_STAMP = '2026-04-09 - 160000'
RUN_TODO = Path('.prompt-hub/todo/todo-20260409-160000-scan-list.md')

month_nums={'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}

ARTICLES = {
    'https://arstechnica.com/ai/2026/04/metas-superintelligence-lab-unveils-its-first-public-model-muse-spark/': {
        'path': 'src/2026-04/20260409-metas-superintelligence-lab-unveils-its-first-public-model-muse-spark.md',
        'title': "Meta's Superintelligence Lab unveils its first public model, Muse Spark",
        'date': 'April 9, 2026',
        'author': 'Kyle Orland',
        'keywords': 'Meta, Muse Spark, Superintelligence Labs, AI models, reinforcement learning, contemplation mode, benchmarks',
        'elevator': 'Meta is rebooting its AI strategy around a proprietary Muse family, betting that parallel-agent reasoning, tighter RL, and social-platform distribution can reset momentum after the uneven Llama 4 reception.',
        'takeaways': [
            'Muse Spark is framed as a clean break from Meta’s recent open-model narrative, even if Zuckerberg still promises future open releases in the Muse family.',
            'Meta is leaning on a “Contemplating” mode with up to 16 parallel agents to improve reasoning without paying a large latency penalty.',
            'The company claims RL is now delivering both higher reliability and better token efficiency through reasoning compression.',
            'Meta still admits weakness in long-horizon agentic workflows and coding, which are exactly the categories shaping current developer demand.',
            'Distribution through Meta AI, WhatsApp, Instagram, Facebook, Messenger, and glasses could matter as much as benchmark scores if the product feels integrated into everyday consumer behavior.'
        ],
        'synth': "The interesting part of Meta’s Muse Spark launch is not just the benchmark table. It is the strategic reset embedded in the announcement. Meta is effectively acknowledging that the previous Llama-centered story did not create the level of excitement or perceived leadership the company wanted. Muse Spark gives Meta a chance to redraw the map: a proprietary flagship, a new lab identity, and a more explicit claim that the company is rebuilding its AI stack from the ground up rather than incrementally patching an aging narrative.\n\nThe technical framing reinforces that shift. Meta’s emphasis on a contemplation mode, where multiple agents reason in parallel, fits the broader industry move from single-pass chat completion toward orchestrated systems. That matters because frontier differentiation is increasingly coming from runtime design, inference strategy, and training loops, not just model scale. The reinforcement-learning story is also notable. Meta is arguing that additional RL does not merely improve accuracy; it can produce reasoning compression, where the model arrives at similar answers with fewer tokens before re-expanding when needed for harder tasks. If that pattern holds in production, it points toward a more economically efficient path to stronger reasoning.\n\nStill, the announcement also reveals where Meta is not yet strongest. The company explicitly calls out long-horizon agentic systems and coding workflows as ongoing gaps. That is important because those are precisely the categories where developers and enterprise buyers are assigning the highest value today. So Muse Spark may improve Meta’s consumer AI posture faster than its developer-platform credibility.\n\nThe larger bet is distribution. Meta has something most labs do not: a giant social graph and several mass-market surfaces where AI features can be inserted directly into daily use. If Muse Spark becomes the layer that helps people navigate places, trends, creators, and content across Meta’s properties, then benchmark parity may be enough. The model does not need to dominate every eval if the product sits closer to everyday attention than its rivals do."
    },
    'https://linas.substack.com/p/fintechpulse1066': {
        'path': 'src/2026-04/20260409-anthropics-managed-agents-the-ai-infrastructure-play.md',
        'title': 'Anthropic’s Managed Agents: The AI Infrastructure Play',
        'date': 'April 9, 2026',
        'author': 'Linas Beliunas',
        'keywords': 'Anthropic, Managed Agents, agent infrastructure, enterprise AI, platform strategy, orchestration, session logs',
        'elevator': 'Linas argues that Anthropic’s Managed Agents launch matters less as a feature release than as a platform move to own the hosted runtime, state layer, and operational tooling behind enterprise-grade autonomous agents.',
        'takeaways': [
            'Managed Agents is positioned as a hosted runtime with sandboxes, persistent session logs, credential isolation, checkpointing, and tracing rather than a simple prompt wrapper.',
            'The architecture separates the model “brain,” disposable execution sandboxes, and durable session state, making recovery and orchestration first-class concerns.',
            'Anthropic’s security and infrastructure abstractions directly target enterprise objections around secrets handling, auditability, and operational reliability.',
            'If this stack becomes standard, many startups focused on agent plumbing rather than differentiated workflows could be squeezed.',
            'The deeper strategic play is platform lock-in: once enterprises define agent behavior and operations inside Anthropic’s runtime, switching costs rise materially.'
        ],
        'synth': "This piece is useful because it treats Anthropic’s Managed Agents launch as infrastructure strategy, not just product marketing. The core claim is that Anthropic is trying to make agent deployment feel as boring and consumable as cloud compute eventually became. Instead of asking enterprises to assemble their own state handling, tracing, sandboxing, secret management, and crash recovery, Anthropic wants to provide the full managed runtime. That changes the value proposition from ‘here is a smarter model’ to ‘here is a safer and faster path from prototype to production agent.’\n\nThe architectural split Linas highlights is the right lens. A stateless model layer is not enough for real agent systems. Once agents run longer tasks, invoke tools, survive retries, and touch credentials, the hard problem becomes operational continuity. By separating the “brain” from disposable sandboxes and a durable session log, Anthropic is encoding a view of agent systems as recoverable distributed software rather than ephemeral chats. That is exactly the kind of abstraction enterprises tend to pay for because it removes whole categories of platform work.\n\nThe security angle is probably just as important. A lot of enterprise hesitation around agents has not been about whether models are impressive. It has been about whether someone wants to trust them with secrets, regulated workflows, or unattended execution. Managed vaults, tracing, scoped permissions, and checkpointing do not eliminate that concern, but they convert it into a procurement conversation enterprises already know how to have. In other words, Anthropic is narrowing the gap between agent experimentation and enterprise governance.\n\nThe strategic implication is lock-in. If teams define agent workflows, observability, and recovery semantics inside Anthropic’s runtime, they are no longer just choosing a model vendor. They are choosing an operating substrate. That is why the launch feels more consequential than a benchmark jump. It hints at a future where value in AI shifts from raw model access toward the managed systems that make autonomous behavior deployable at scale."
    },
    'https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html': {
        'path': 'src/2026-04/20260409-feedback-flywheel.md',
        'title': 'Feedback Flywheel',
        'date': 'April 9, 2026',
        'author': 'Martin Fowler / Thoughtworks',
        'keywords': 'AI coding, team learning, knowledge priming, prompts, workflows, retrospectives, software engineering',
        'elevator': 'This essay argues that teams only compound value from AI tools when they systematically feed working patterns, failures, and missing context back into shared artifacts like priming docs, commands, and playbooks.',
        'takeaways': [
            'Many teams plateau with AI because individual prompting lessons stay personal instead of being folded into shared team infrastructure.',
            'The right destination for new learning depends on signal type: context updates, instruction refinements, workflow playbooks, or documented failure boundaries.',
            'The feedback loop should operate at lightweight cadences, from quick post-session reflection to retrospective and periodic artifact review.',
            'Useful success metrics are not raw output speed but first-pass acceptance, iteration count, post-merge rework, and principle alignment.',
            'Treating AI artifacts like living engineering infrastructure is what lets teams compound capability instead of merely adopting tools.'
        ],
        'synth': "Martin Fowler’s ‘Feedback Flywheel’ is one of the clearer explanations of why early AI gains often stall. Teams adopt the tools, learn a few good prompting habits, and then stop improving because the learning remains trapped in individual heads. Fowler’s point is that AI effectiveness becomes durable only when the organization creates surfaces that can absorb lessons: priming documents, shared commands, playbooks, and anti-pattern lists. Without that loop, each developer keeps rediscovering the same corrections and frustrations.\n\nWhat makes the piece strong is its specificity. It does not just say ‘share best practices.’ It categorizes the signal AI sessions generate. Missing context belongs in the priming layer. Prompt patterns that work belong in shared instructions. Repeatable interaction structures become workflow playbooks. Recurrent failure modes become guardrails or documented boundaries. That mapping matters because it turns vague improvement into a maintainable operational habit. A team can ask, after any notable session, not just what happened, but where that lesson should live.\n\nThe cadence advice is equally practical. Fowler does not propose a new bureaucracy. He suggests tiny checkpoints attached to work that already exists: a post-session question, a standup note, a retrospective agenda item, an occasional review of whether the artifacts are still aligned with practice. That is a smart design choice. Heavy process would be ignored precisely when teams are busiest, and busy periods are when useful lessons accumulate fastest.\n\nThe broader implication is that successful AI adoption looks a lot like mature engineering culture. Good teams already externalize knowledge, refine standards, learn from incidents, and update their operating system when reality changes. AI just increases the payoff for doing that well. The teams that treat prompts, priming files, and workflow conventions as living infrastructure will get compounding returns. The teams that treat them as one-time setup documents will plateau even if the models keep getting better."
    },
    'https://polypane.app/blog/the-intl-api-the-best-browser-api-youre-not-using/': {
        'path': 'src/2026-04/20260409-the-intl-api-the-best-browser-api-youre-not-using.md',
        'title': "The Intl API: The best browser API you're not using",
        'date': 'April 9, 2026',
        'author': 'Kilian Valkhof',
        'keywords': 'JavaScript, Intl API, browser APIs, i18n, formatting, performance, frontend',
        'elevator': 'Kilian Valkhof makes the case that modern frontend teams can replace a surprising amount of date, number, list, and text-formatting library baggage by leaning on the browser’s built-in Intl APIs.',
        'takeaways': [
            'Intl covers far more than translation: it provides native formatting for dates, times, relative time, durations, numbers, currencies, lists, pluralization, segmentation, and sorting.',
            'Because Intl is built into the browser, it reduces bundle weight and runtime parsing compared with common formatting libraries.',
            'Locale awareness matters even for single-language products because regional conventions for dates, numbers, and currencies still vary widely.',
            'The main performance pattern is to instantiate formatters once and reuse them rather than rebuilding them repeatedly in hot paths.',
            'Intl is a formatting layer, not a calculation layer, so developers still need separate logic for date diffs, unit conversion, and data wrangling.'
        ],
        'synth': "This article is a good reminder that a lot of frontend complexity persists by inertia. Developers reach for Moment, date-fns, or bespoke formatting utilities because those habits are old and familiar, not always because the browser is missing the capability. Kilian Valkhof’s argument is that the Intl family has quietly become rich enough to cover most mainstream formatting needs directly in the platform. That means less JavaScript shipped, less parsing overhead, and fewer dependencies maintained for problems the browser already knows how to solve.\n\nThe important nuance is that Intl is not just about translation. Even a product written entirely in English still serves users in different locales, each with different conventions for dates, decimals, currencies, and list formatting. When teams ignore that, they often build interfaces that feel subtly wrong or untrustworthy outside their home market. Intl solves a lot of that by making locale-sensitive output the default instead of an afterthought. In practice, that shifts internationalization from ‘big enterprise requirement’ to ‘basic frontend correctness.’\n\nThe article also exposes a common engineering tradeoff. The cost of native APIs is often up-front unfamiliarity rather than missing power. Intl has a broad surface area and many constructors, but the pattern is consistent: choose locale, choose options, create formatter, reuse it. That reuse point matters because the expensive part is initialization, not formatting itself. Once teams internalize that pattern, the API becomes much less intimidating and much more obviously useful in performance-sensitive code.\n\nThe broader lesson is about browser maturity. There are many places where frontend stacks still carry polyfills and utility libraries that made sense years ago but are no longer the best default. Intl is a concrete example of how platform capabilities have caught up. Teams that revisit those assumptions can simplify their bundles, reduce dependency risk, and get more correct user-facing behavior at the same time."
    },
    'https://veralang.dev/': {
        'path': 'src/2026-04/20260409-vera-a-programming-language-designed-for-llms-to-write.md',
        'title': 'Vera: A programming language designed for LLMs to write, not humans',
        'date': 'April 9, 2026',
        'author': 'Allan Allan',
        'keywords': 'Vera, programming languages, LLMs, verification, contracts, De Bruijn indices, agent tooling',
        'elevator': 'Vera is an experiment in redesigning programming language ergonomics around machine authorship, replacing naming freedom and implicit behavior with structurally referenced bindings, mandatory contracts, typed effects, and verification-first feedback.',
        'takeaways': [
            'Vera assumes that the main weakness of model-written code is not syntax but maintaining coherence, invariants, and naming discipline across larger programs.',
            'The language removes variable names in favor of typed structural references, aiming to reduce a class of naming-related hallucinations.',
            'Contracts, effect declarations, and refinement-style constraints are mandatory so correctness can be checked mechanically instead of guessed.',
            'Compiler diagnostics are intentionally written as natural-language repair instructions for LLMs, treating errors as part of the agent interface.',
            'The project suggests a broader thesis: if models become primary code authors, languages and tooling may evolve to optimize for machine-checkability rather than human convenience.'
        ],
        'synth': "Vera is interesting less as a likely mass-adoption language and more as a sharp provocation about where software tooling could go if LLMs become primary code producers. Most languages evolved around human ergonomics: readability, expressiveness, shorthand, naming, and developer preference. Vera inverts that assumption. It asks what a language would look like if the top priority were not making humans comfortable, but making model-generated programs easier to verify, repair, and reason about mechanically.\n\nThat framing explains its unusual design choices. Replacing variable names with typed structural references sounds hostile to humans, but it directly targets a known model failure mode: inconsistent naming and scope confusion. Mandatory contracts and typed effects push the same way. Instead of trusting the model to implicitly do the right thing, Vera tries to make the important properties explicit and checkable. The compiler becomes less a passive parser than an active supervisor, with diagnostics designed to guide another machine toward a fix. That is a fascinating shift because it treats the language, compiler, and agent as one combined system.\n\nThe strongest idea here may be the notion of ‘checkability over correctness.’ Models do not need to be omniscient if the environment makes wrong outputs easy to detect and repair. That aligns with a lot of current agent practice, where the best systems win not by generating perfect first drafts, but by operating inside loops with tests, validators, and constrained interfaces. Vera extends that philosophy all the way down to the language level.\n\nWhether Vera itself wins is almost secondary. The project matters because it makes visible a design space many people are only vaguely gesturing at. If AI-written code becomes common, we may eventually see more languages, DSLs, or frameworks that trade some human elegance for machine legibility and proof. Vera is one of the clearer early examples of that future being taken seriously enough to prototype."
    },
    'https://www.a16z.news/p/ai-adoption-by-the-numbers': {
        'path': 'src/2026-04/20260409-where-enterprises-are-actually-adopting-ai.md',
        'title': 'Where Enterprises are Actually Adopting AI',
        'date': 'April 9, 2026',
        'author': 'a16z',
        'keywords': 'enterprise AI, adoption, coding, support, search, Fortune 500, healthcare, legal',
        'elevator': 'a16z argues that enterprise AI adoption is already materially real—especially in coding, support, and search—and that the fastest-moving sectors share traits like verifiability, text-heavy workflows, clear ROI, and easy human fallback paths.',
        'takeaways': [
            'a16z estimates that roughly 29% of the Fortune 500 and 19% of the Global 2000 are live, paying customers of leading AI startups rather than merely piloting the technology.',
            'Coding is by far the breakout enterprise use case because it combines dense training data, verifiable outputs, clear ROI, and relatively low organizational friction.',
            'Support and search are also scaling quickly because they are text-heavy, bounded, measurable, and can often escalate cleanly to humans when needed.',
            'Tech adopted first, but legal and healthcare have also become strong early markets because AI maps well onto dense-document and workflow-heavy tasks that traditional software handled poorly.',
            'The article’s implicit framework is that adoption depends not just on model capability, but on whether a workflow is auditable, bounded, and organizationally easy to integrate.'
        ],
        'synth': "The main contribution of this piece is that it tries to replace AI adoption vibes with a rough operating model for what is actually getting bought and deployed. a16z’s numbers are inevitably selective, but the directional claim is persuasive: enterprise AI is no longer mostly experimentation. Meaningful shares of very large companies are already paying for production deployments, and the distribution of those deployments is not random. It clusters where the economics and workflow shape are favorable.\n\nCoding sits at the center because it offers almost everything AI systems like: lots of training data, highly structured text, immediate feedback, and outputs that can be checked. It also offers everything buyers like: expensive labor, measurable productivity gains, and users who are already comfortable adopting new tools. Support and search follow for similar reasons. They are bounded, text-rich, and easy to measure, with natural human escalation paths when the AI falls short. That pattern is more useful than the absolute percentages because it suggests a practical adoption heuristic: AI lands fastest where work is verifiable, repetitive, and operationally legible.\n\nThe sector analysis around legal and healthcare is especially interesting because both markets were historically hard for conventional software vendors. AI changes that by targeting labor and judgment workflows rather than forcing wholesale system replacement. In legal, parsing and drafting dense text is the work. In healthcare, scribes, search, and administrative processing sit adjacent to entrenched systems of record without requiring rip-and-replace. That makes adoption faster than many people expected.\n\nThe broader lesson is that enterprise AI is not diffusing evenly across the economy. Model capability matters, but workflow design matters more. The winning categories tend to have clear outputs, some human oversight, and obvious business value. That is a useful corrective to both hype and cynicism. AI is not universally transforming every corporate function yet, but it is already very real where the task structure is right."
    },
    'https://www.testingcatalog.com/anthropic-launches-claude-managed-agents-for-businesses/': {
        'path': 'src/2026-04/20260409-anthropic-launches-claude-managed-agents-for-businesses.md',
        'title': 'Anthropic launches Claude Managed Agents for businesses',
        'date': 'April 9, 2026',
        'author': 'TestingCatalog',
        'keywords': 'Anthropic, Claude Managed Agents, enterprise AI, cloud agents, sandboxes, tracing, orchestration',
        'elevator': 'Anthropic is packaging sandboxed execution, session persistence, orchestration, permissions, and tracing into a public-beta Claude Managed Agents stack meant to shorten the path from agent prototype to enterprise deployment.',
        'takeaways': [
            'Claude Managed Agents gives developers a cloud-hosted runtime for agents rather than only model endpoints.',
            'Key features include secure code sandboxes, long-running sessions, checkpointing, scoped permissions, tracing, and research-preview multi-agent coordination.',
            'Anthropic claims measurable gains on structured generation tasks compared with standard prompting alone.',
            'The launch is explicitly aimed at organizations that do not want to build their own execution, state, and orchestration infrastructure from scratch.',
            'Early named adopters suggest Anthropic is targeting workflow automation in code, productivity, HR, and finance rather than only experimental demos.'
        ],
        'synth': "This launch matters because it shows Anthropic moving up the stack from model vendor to agent runtime provider. For developers, the most painful parts of production agents are rarely the raw API calls. They are everything around them: secure execution, session state, retries, permissions, tracing, and recovery when a long-running task breaks halfway through. Claude Managed Agents bundles those concerns into a managed platform, which makes the offer much easier for enterprise teams to evaluate.\n\nThe feature set also reveals how the market is maturing. Sandboxed execution, persistent sessions, checkpointing, and scoped permissions are not flashy capabilities, but they are the difference between a credible internal prototype and something a security or platform team can support. Anthropic is effectively saying that agents should be treated like real operational software, with the same expectations around observability, reliability, and controlled access. That shift is important because it suggests the next wave of competition will be as much about operational tooling as model intelligence.\n\nThere is also a time-to-market angle. Many companies want the benefits of agent automation without dedicating months to inventing the underlying infrastructure. By offering a hosted path, Anthropic can become the default choice for teams that care more about shipping workflows quickly than about owning every layer of the stack. That is a powerful wedge if the platform proves stable enough and flexible enough for varied enterprise use cases.\n\nThe larger implication is that ‘managed agents’ may become a standard product category, much like managed databases or managed Kubernetes. Once that happens, the value conversation changes. Enterprises will not just ask which model is smartest. They will ask which platform makes autonomous systems safest, fastest to deploy, easiest to govern, and hardest to regret. Anthropic clearly wants to be in that conversation early."
    },
}

DUPLICATES = {
    'https://linas.substack.com/p/claudecodesource': 'src/2026-04/20260404-anthropic-accidentally-leaked-claude-codes-entire-source.md',
    'https://linas.substack.com/p/skill-graphs': 'src/2026-04/20260406-skill-graphs-fix-your-ai-agents-context-problem.md',
}

ERRORS = {
    'https://piecechowski.io/post/git-commands-before-reading-code/': 'FETCH_ERROR: source host unreachable (DNS lookup failed); related result found: Git Commands Before Reading Code - YouTube.'
}


def normalize(url: str) -> str:
    p = urlparse(url)
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if not (k.startswith('utm_') or k in {'ref', 'fbclid', 'gclid', 'mc_cid', 'mc_eid'})]
    return urlunparse((p.scheme, p.netloc, p.path, p.params, urlencode(q), ''))


def read_text(path):
    return Path(path).read_text()


def extract_meta(path):
    txt = read_text(path)
    title = txt.splitlines()[0].lstrip('# ').strip()
    m = re.search(r'## Elevator pitch\n(.+)', txt)
    return title, (m.group(1).strip() if m else '')


def bump_version(msg):
    vf = Path('.prompt-hub/version.md')
    parts = vf.read_text().strip().split('.')
    parts[-1] = str(int(parts[-1]) + 1)
    ver = '.'.join(parts)
    vf.write_text(ver + '\n')
    rel = Path('.prompt-hub/releases.md')
    rel.write_text(f'## {ver} - 2026-04-09\n- {msg}\n\n' + rel.read_text())
    return ver


def update_readme(new_link=None):
    p = Path('README.md')
    text = p.read_text()
    if new_link and new_link not in text:
        marker = '#### April ('
        idx = text.index(marker)
        line_end = text.index('\n', idx)
        text = text[:line_end+1] + new_link + '\n' + text[line_end+1:]
    lines = text.splitlines()
    counts = {}
    current_year = None
    current_month = None
    for l in lines:
        m = re.match(r'### (\d{4})', l)
        if m:
            current_year = m.group(1)
        m2 = re.match(r'#### ([A-Za-z]+) \((\d+) article[s]?\)', l)
        if m2:
            current_month = m2.group(1)
        elif l.startswith('#### '):
            current_month = None
        elif current_year and current_month and l.startswith('- ['):
            counts[f'{current_year}-{month_nums[current_month]}'] = counts.get(f'{current_year}-{month_nums[current_month]}', 0) + 1
    out = []
    current_year = None
    for l in lines:
        m = re.match(r'### (\d{4})', l)
        if m:
            current_year = m.group(1)
        m2 = re.match(r'#### ([A-Za-z]+) \((\d+) article[s]?\)', l)
        if m2 and current_year:
            name = m2.group(1)
            c = counts.get(f'{current_year}-{month_nums[name]}', 0)
            suffix = 's' if c != 1 else ''
            l = f'#### {name} ({c} article{suffix})'
        out.append(l)
    stat = ['## Statistics', '', 'Articles per month:', '']
    items = sorted(counts.items())
    for i, (k, c) in enumerate(items):
        stat.append(f"{k} | {'█' * c} {c}{'<br>' if i < len(items)-1 else ''}")
    text = '\n'.join(out)
    text = re.sub(r'## Statistics\n.*?\n## Articles\n', '\n'.join(stat) + '\n\n## Articles\n', text, flags=re.S)
    p.write_text(text)


def remove_url(original):
    urls = [u.strip() for u in Path('LIST.md').read_text().splitlines() if u.strip()]
    urls = [u for u in urls if u != original]
    Path('LIST.md').write_text(('\n'.join(urls) + '\n') if urls else '')


def append_memory(action, files, outcome='success', next_step='Continue with next URL in LIST.md.'):
    mem = Path('.prompt-hub/memory.md')
    mem.write_text(mem.read_text() + f"\n## {RUN_STAMP} +0200\n- actor: agent\n- action: {action}\n- files_changed_or_commands: {files}\n- outcome: {outcome}\n- next_step: {next_step}\n")


def git_commit(msg, files):
    subprocess.run(['git', 'add'] + files, check=True)
    subprocess.run(['git', 'commit', '-m', msg], check=True)


def make_article_file(a, clean):
    path = Path(a['path'])
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {a['title']}",
        '',
        f"**Source**: {clean}",
        f"**Date**: {a['date']}",
        f"**Author**: {a['author']}",
        f"**Keywords**: {a['keywords']}",
        '',
        '## Elevator pitch',
        a['elevator'],
        '',
        '## Takeaways',
    ]
    lines += [f'- {x}' for x in a['takeaways']]
    lines += ['', '## Synthesis', a['synth'], '']
    path.write_text('\n'.join(lines))


def init_todo(url_count):
    RUN_TODO.parent.mkdir(parents=True, exist_ok=True)
    RUN_TODO.write_text(f"# Scan-list run — {RUN_STAMP}\n\n- [x] Load prompt-hub context and repo instructions\n- [x] Sync repo with `git pull --rebase`\n- [x] Note LIST.md timestamp and queue length ({url_count} URLs)\n- [ ] Process each URL sequentially\n- [ ] Create batch recap and verify contents\n- [ ] Push all commits\n")

order = [u.strip() for u in Path('LIST.md').read_text().splitlines() if u.strip()]
init_todo(len(order))
append_memory(
    action=f'Initialized the 16:00 scan-list run after syncing the repo and noting {len(order)} queued URL(s) in LIST.md.',
    files=f'`{RUN_TODO}`; `git pull --rebase`; `LIST.md`; `.prompt-hub/lessons.md`; `.prompt-hub/memory.md`; `.prompt-hub/releases.md`; `agents.md`.',
    next_step='Process each queued URL from top to bottom.'
)
processed = []
errors = []

for original in order:
    clean = normalize(original)
    if clean in ARTICLES:
        a = ARTICLES[clean]
        make_article_file(a, clean)
        update_readme(f"- [{a['title']}]({a['path']})")
        title = a['title']
        elevator = a['elevator']
        path_str = a['path']
        remove_url(original)
        bump_version(f'Process article: {title}.')
        append_memory(
            action=f'Processed scan-list URL `{clean}`; created a new synthesis, updated README stats, and removed the URL from LIST.md.',
            files=f'`{path_str}`, `README.md`, `LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`, `{RUN_TODO}`.'
        )
        git_commit(f'Process article: {title}', [path_str, 'README.md', 'LIST.md', '.prompt-hub/version.md', '.prompt-hub/releases.md', '.prompt-hub/memory.md', str(RUN_TODO)])
        processed.append({'title': title, 'elevator': elevator, 'path': path_str})
    elif clean in DUPLICATES:
        path_str = DUPLICATES[clean]
        title, elevator = extract_meta(path_str)
        remove_url(original)
        bump_version(f'Process article: {title}.')
        append_memory(
            action=f'Processed scan-list URL `{clean}` as a duplicate of existing synthesis `{path_str}` and removed it from LIST.md.',
            files=f'`{path_str}`, `LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`, `{RUN_TODO}`.'
        )
        git_commit(f'Process article: {title}', ['LIST.md', '.prompt-hub/version.md', '.prompt-hub/releases.md', '.prompt-hub/memory.md', str(RUN_TODO)])
        processed.append({'title': title, 'elevator': elevator, 'path': path_str})
    else:
        err = ERRORS.get(clean, 'FETCH_ERROR: unavailable source.')
        remove_url(original)
        bump_version(f'Process article error: {clean}.')
        append_memory(
            action=f'Failed to process scan-list URL `{clean}`; logged a fetch error and removed the URL from LIST.md to continue the run.',
            files=f'`LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`, `{RUN_TODO}`.',
            outcome='partial_success'
        )
        git_commit(f'Process article: {clean}', ['LIST.md', '.prompt-hub/version.md', '.prompt-hub/releases.md', '.prompt-hub/memory.md', str(RUN_TODO)])
        errors.append(f'{clean} — {err}')

recap = Path(f'synthesis/{RUN_FILE_STAMP} - batch recap.md')
recap.parent.mkdir(parents=True, exist_ok=True)
parts = [f'# Batch Recap - {RUN_STAMP}', '']
for item in processed:
    parts += [item['title'], item['elevator'], f"Synthese: {BASE}{item['path']}", '']
if errors:
    parts += ['## Errors', ''] + [f'- {e}' for e in errors] + ['']
recap.write_text('\n'.join(parts).rstrip() + '\n')
recap_text = recap.read_text()
assert all(item['title'] in recap_text for item in processed)
assert Path('LIST.md').read_text() == ''
RUN_TODO.write_text(RUN_TODO.read_text().replace('- [ ] Process each URL sequentially', '- [x] Process each URL sequentially').replace('- [ ] Create batch recap and verify contents', '- [x] Create batch recap and verify contents').replace('- [ ] Push all commits', '- [x] Push all commits'))
bump_version(f'Add batch recap: {RUN_FILE_STAMP}; finalize scan-list run.')
append_memory(
    action=f'Created and verified the scan-list batch recap `{recap}`; confirmed LIST.md is empty and the run is ready to push.',
    files=f'`{recap}`, `LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`, `{RUN_TODO}`.',
    next_step='Push all remaining commits.'
)
git_commit(f'Add batch recap: {RUN_FILE_STAMP}', [str(recap), '.prompt-hub/version.md', '.prompt-hub/releases.md', '.prompt-hub/memory.md', str(RUN_TODO)])
subprocess.run(['git', 'push'], check=True)
print(json.dumps({'processed': len(processed), 'errors': errors, 'titles': [p['title'] for p in processed]}, ensure_ascii=False))
