import os, re, subprocess, sys, json
from pathlib import Path

ROOT = Path('/Users/openclaw/github/Engineering-Forward')
README = ROOT/'README.md'
LIST = ROOT/'LIST.md'
VERSION = ROOT/'.prompt-hub/version.md'
RELEASES = ROOT/'.prompt-hub/releases.md'
MEMORY = ROOT/'.prompt-hub/memory.md'
TODAY='2026-04-08'
NOW='2026-04-08 18:06:59 +0200'
BATCH_STAMP='2026-04-08 - 180659'
BATCH_DISPLAY='2026-04-08 18:06:59'
REPO_URL='https://github.com/blamouche/Engineering-Forward/blob/main'

articles = [
  {
    'url':'https://www.anthropic.com/glasswing','title':'Project Glasswing','author':'Anthropic','date':'April 8, 2026','keywords':'anthropic, cybersecurity, zero-day, vulnerability discovery, critical infrastructure, model deployment','pitch':'Anthropic says frontier coding models have crossed a threshold where they can autonomously find and exploit serious software bugs, and it is launching Project Glasswing to use that capability defensively across critical software ecosystems.','takeaways':[
      'Anthropic frames Mythos Preview as a cybersecurity inflection point rather than a normal model release.',
      'Project Glasswing pairs Anthropic with major tech and security firms plus critical open-source maintainers.',
      'The core defensive thesis is to use the same vulnerability-finding power that could help attackers to patch systems first.',
      'Anthropic is backing the effort with large usage credits and direct funding for open-source security work.',
      'The announcement argues that industry coordination now matters more than benchmark talk later.'
    ],
    'synthesis':'The interesting part here is not just the model capability claim, but the operational response. Anthropic is effectively arguing that vulnerability research has become automatable at a level that changes the default security posture for critical software. Instead of waiting for broad release and hoping defensive tooling catches up, it wants to concentrate access in a coordinated coalition of infrastructure owners, hyperscalers, hardware vendors, and security companies. That makes this article more about deployment strategy than raw model marketing. For engineering leaders, the implication is that software assurance may soon depend much more on who can run frontier-code models safely and continuously against their own codebases. If that thesis is right, the next few years of secure software practice will look less like occasional audits and more like permanent AI-assisted red teaming.'
  },
  {
    'url':'https://z.ai/blog/glm-5.1','title':'GLM-5.1: Towards Long-Horizon Tasks','author':'Z.ai','date':'April 7, 2026','keywords':'glm-5.1, agentic engineering, coding model, open weights, long-horizon tasks','pitch':'Z.ai positions GLM-5.1 as a flagship open-weight agentic coding model aimed at long-running engineering work, with strong benchmark gains on repo generation, terminal tasks, and SWE-style repair.','takeaways':[
      'GLM-5.1 is presented as an agentic engineering model optimized for long-horizon coding tasks.',
      'Z.ai highlights benchmark wins on SWE-Bench Pro, repo generation, and terminal-style task suites.',
      'The release matters because it keeps serious open-weight competition alive in coding agents.',
      'The emphasis is less on chat quality and more on sustained autonomous execution over hours.',
      'If the claims hold up, it raises the ceiling for self-hosted or customizable engineering agents.'
    ],
    'synthesis':'Even from the limited public details, the framing is clear: this is an attempt to define the next competitive frontier for open models around durable software execution rather than general chatbot polish. The important shift is from short coding bursts to agents that can stay coherent across repo exploration, terminal use, repair loops, and multi-step implementation. That is exactly where closed models have been building moat via product integration and reliability. So GLM-5.1 matters if it narrows that gap in an open package. For teams building internal developer agents, the relevant question is not whether it wins a single leaderboard, but whether it makes “hours-long autonomous coding with acceptable failure modes” cheaper and more controllable.'
  },
  {
    'url':'https://www.greaterwrong.com/posts/WjaGAA4xCAXeFpyWm/my-picture-of-the-present-in-ai','title':'My picture of the present in AI','author':'Unknown','date':'April 2026','keywords':'ai forecasting, productivity, coding agents, r&d acceleration, present-state analysis','pitch':'This post tries to describe the AI landscape as it already exists in early 2026: real but uneven engineering acceleration, stronger long-horizon agents, and capability growth that is now outpacing many of the old ways of measuring it.','takeaways':[
      'The author estimates meaningful but not absurd engineering speedups from AI inside frontier labs.',
      'Capability gains are strongest on long, verifiable engineering work rather than on conceptually tricky judgment tasks.',
      'Benchmarks are becoming less informative because frontier models are saturating them.',
      'Humans still add value by correcting agent attractor states, reward hacking, and bad delegation.',
      'The piece is useful as a synthesis of how capability progress feels operationally inside labs.'
    ],
    'synthesis':'What makes this post valuable is that it is trying to describe the messy middle rather than either hype or dismissal. The picture is not “AGI solved everything” and not “benchmarks are fake”; it is that frontier labs are getting tangible software and research acceleration, but with enough sloppiness, oversight burden, and task variance that the gains are hard to summarize cleanly. That aligns with what many engineering teams are seeing in practice: agentic systems are best where verification is cheap, iteration is abundant, and recovery from mistakes is possible. The post also usefully highlights that internal workflow adaptation can make uplift look larger than it really is. In other words, AI is already changing the shape of work, but not in a uniform or easily benchmarked way.'
  },
  {
    'url':'https://red.anthropic.com/2026/mythos-preview','title':'Claude Mythos Preview','author':'Anthropic Frontier Red Team','date':'April 7, 2026','keywords':'mythos preview, exploit generation, zero-day, cyber capability, autonomous vulnerability research','pitch':'Anthropic’s red-team write-up argues that Mythos Preview represents a real step change in autonomous cyber capability, including zero-day discovery and exploit construction across major operating systems and browsers.','takeaways':[
      'Anthropic claims Mythos Preview can both find subtle vulnerabilities and often exploit them autonomously.',
      'The team says the model has saturated many prior cyber benchmarks, forcing a shift toward real-world evaluation.',
      'Examples include deep bugs in mature codebases and multi-stage exploit chains.',
      'The write-up stresses that these abilities emerged from general coding and reasoning gains, not narrow cyber tuning.',
      'The report is essentially an argument for restricted deployment plus urgent defensive preparation.'
    ],
    'synthesis':'Compared with the higher-level Glasswing announcement, this post is where Anthropic tries to earn the scary claim. The notable thing is not just bug finding, but the combination of real code reading, exploit synthesis, and enough autonomy to complete long vulnerability workflows with minimal human steering. If accurate, that shifts the conversation from “LLMs help security researchers” to “frontier models are becoming independent cyber operators in constrained environments.” For engineering orgs, the practical implication is that secure development and patch management may soon need to assume both defenders and attackers can cheaply automate parts of offensive research. That would make exploit windows shorter and the value of continuous code scanning much higher.'
  },
  {
    'url':'https://www.mercor.com/blog/Finance-tasks-ai-failures-modes','title':'AI failures modes when we pushed frontier models on real finance tasks','author':'Mercor','date':'2026','keywords':'finance, multimodal reasoning, document extraction, visual QA, benchmarking','pitch':'Mercor tested frontier models on realistic finance documents and found the main bottleneck is not arithmetic but extracting the right numbers from messy charts, tables, and investor decks.','takeaways':[
      'Image-based finance tasks materially underperform the same tasks when the numbers are provided as text.',
      'The biggest weakness is visual extraction from dense real-world documents, not pure calculation.',
      'Models also make surprisingly basic operation mistakes even when the relevant values are available.',
      'The benchmark design is interesting because it separates reading failures from reasoning failures.',
      'The article is a useful antidote to overgeneralizing from clean chart or DocVQA benchmarks.'
    ],
    'synthesis':'This is one of the more practical benchmarking write-ups because it isolates where the failure actually occurs. Lots of business workflows look “reasoning-heavy” from a distance, but the first challenge is often just reading the source artifact correctly. In finance that means crowded slides, multi-panel charts, ambiguous labels, and presentation layouts designed for humans, not models. Mercor shows that when you strip away the messy visual layer, model performance becomes much more respectable. So the blocker to analyst replacement is currently more “robust document ingestion in the wild” than “basic financial math.” That distinction matters for product builders: better OCR-plus-structure pipelines may unlock more value faster than trying to fine-tune ever more domain reasoning.'
  },
  {
    'url':'https://cursor.com/blog/warp-decode','title':'Better MoE model inference with warp decode','author':'Cursor','date':'2026','keywords':'moe inference, blackwell, gpu kernels, warp decode, performance engineering','pitch':'Cursor describes a new Blackwell-optimized MoE decode approach that reorganizes parallelism around outputs rather than experts, reducing bookkeeping and improving both throughput and numerical fidelity.','takeaways':[
      'Warp decode flips the traditional MoE inference organization from expert-centric to output-centric.',
      'The design removes multiple staging and data-layout steps that dominate small-batch decode overhead.',
      'Cursor reports major throughput gains on B200 GPUs plus better numerical closeness to FP32 reference.',
      'The article is a sharp example of hardware-aware inference work translating directly into product velocity.',
      'It also shows why inference engineering is now a serious competitive layer, not just an optimization footnote.'
    ],
    'synthesis':'This is a strong mechanical-sympathy piece. The clever move is not a magical new algorithm, but changing the unit of parallelism to fit the realities of Blackwell decode workloads. At small-batch autoregressive decode, expert-centric data movement creates too much overhead relative to the actual math, so Cursor rethinks the problem around independently computed outputs. The result is less staging, fewer buffers, and better scheduler freedom. The broader lesson is that frontier model performance increasingly depends on these “boring” inference details. When model quality is expensive to improve, a big systems win that makes training loops cheaper and deployment faster has outsized leverage.'
  },
  {
    'url':'https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale','title':'TorchTPU: Running PyTorch Natively on TPUs at Google Scale','author':'Google','date':'2026','keywords':'torchtpu, pytorch, tpu, xla, stablehlo, distributed training','pitch':'Google’s TorchTPU effort aims to make TPUs feel like a native PyTorch target, combining eager usability with XLA-backed compilation and distributed support for large TPU deployments.','takeaways':[
      'TorchTPU is built around a “feels like PyTorch” goal rather than forcing users into a foreign programming model.',
      'The stack supports multiple eager modes plus torch.compile integration through XLA and StableHLO.',
      'Google is emphasizing portability, compiler reuse, and support for distributed PyTorch APIs.',
      'The design acknowledges real TPU-specific optimization tradeoffs without abandoning developer ergonomics.',
      'If executed well, it lowers one of the biggest adoption barriers for TPU-backed training and inference.'
    ],
    'synthesis':'The significance here is strategic as much as technical. Google knows that TPU adoption is limited not only by hardware access but by software friction. PyTorch became the default developer interface, so a TPU stack that still feels like a custom ecosystem will always face resistance. TorchTPU is Google’s attempt to invert that dynamic: meet developers in native PyTorch, preserve eager debugging, then route serious optimization through a battle-tested XLA path. If this works, TPU usage becomes less of a framework migration and more of a device choice. That matters in a market where the winning accelerator platform increasingly depends on software convenience as much as raw silicon.'
  },
  {
    'url':'https://www.lesswrong.com/posts/gfkJp8Mr9sBm83Rcz/we-re-actually-running-out-of-benchmarks-to-upper-bound-ai','title':'We\'re actually running out of benchmarks to upper bound AI capabilities','author':'LawrenceC','date':'April 7, 2026','keywords':'benchmarks, ai evaluation, upper bounds, metr, frontier safety','pitch':'This post argues that frontier models are saturating fixed capability benchmarks so quickly that benchmark-based “upper bounds” are losing credibility as a safety and governance tool.','takeaways':[
      'Benchmark saturation is happening fast enough that expensive new suites risk irrelevance by launch.',
      'Upper-bound style evaluations were already strained in 2025 and are worse in early 2026.',
      'Alternatives like uplift studies, expert elicitation, and auditing each have major tradeoffs.',
      'The post is really about institutional lag: capabilities are moving faster than measurement systems.',
      'It raises a governance problem, not just a benchmarking problem.'
    ],
    'synthesis':'This is a useful articulation of a failure mode many people vaguely feel but do not state cleanly: our evaluation machinery was built for a slower-moving world. Once models saturate fixed tests rapidly, “the benchmark says it’s safe enough” becomes much less reassuring. The post also correctly points out that replacement methods are expensive, slow, or socially fragile. That means organizations may end up making deployment decisions with weaker evidence exactly when stakes are rising. For engineers, this reinforces a simple lesson: benchmark wins tell you less and less about operating behavior at the frontier. For policymakers, it suggests the bottleneck is now institutional measurement capacity, not lack of clever test ideas.'
  },
  {
    'url':'https://epochai.substack.com/p/google-controls-the-most-ai-computing','title':'Google controls the most AI computing power, driven by its custom TPUs','author':'Epoch AI','date':'April 7, 2026','keywords':'ai compute, tpu, google, hyperscalers, infrastructure economics','pitch':'Epoch AI claims Google now controls the largest share of recent AI compute, with an unusually large fraction coming from its own TPU fleet rather than Nvidia dependence.','takeaways':[
      'The headline is that Google allegedly leads in owned AI compute sold since 2022.',
      'What differentiates Google is not only scale but the share supplied by custom TPUs.',
      'That makes Google structurally different from hyperscalers that remain mostly Nvidia buyers.',
      'Compute ownership is increasingly a strategy story, not just a capex statistic.',
      'The article reinforces why model and cloud competition cannot be analyzed without chip supply.'
    ],
    'synthesis':'This is short, but the implication is big. If Google really controls the largest portion of frontier AI compute and much of that is homegrown TPU capacity, then its strategic position is stronger than typical market narratives suggest. It means Google is not just another customer in the Nvidia queue; it has an internal compute stack that can compound with software and model advantages. That matters for both pricing power and research velocity. In practical terms, compute discussions that focus only on model quality or cloud revenue miss the underlying industrial story: the most important AI companies are becoming vertically integrated infrastructure companies.'
  },
  {
    'url':'https://googlecloudplatform.github.io/scion/overview','title':'Scion Overview','author':'Google Cloud Platform','date':'2026','keywords':'multi-agent orchestration, containers, remote clusters, harnesses, agent infrastructure','pitch':'Scion is presented as an experimental orchestration layer for running many isolated LLM agents across local and remote containerized environments with configurable runtimes and harnesses.','takeaways':[
      'Scion treats multi-agent work as an orchestration problem over isolated identities, workspaces, and runtimes.',
      'Profiles, runtimes, and harnesses are the core abstraction for switching execution environments.',
      'The project is aimed at dynamic graphs of specialized agents rather than one giant general-purpose agent.',
      'It reflects growing demand for infrastructure that manages agent concurrency, isolation, and resumeability.',
      'The emphasis is on testbed flexibility more than polished end-user workflow today.'
    ],
    'synthesis':'Scion is interesting because it represents the infrastructure view of agent systems. Once teams start using multiple specialized agents for research, coding, testing, and auditing, the hard problem becomes lifecycle management: workspaces, credentials, replay, isolation, and scheduling across machines. Scion is trying to become that substrate. The project also suggests a shift in how serious teams think about agents: less as a chat product, more as a distributed execution graph. That is probably where a lot of real enterprise agent work ends up once experimentation gives way to repeatable operations.'
  },
  {
    'url':'https://autocli.ai/','title':'AutoCLI.ai — Turn Any Website Into Structured CLI Output by AI','author':'AutoCLI.ai','date':'2026','keywords':'cli generation, web scraping, adapters, structured extraction, ai tooling','pitch':'AutoCLI.ai wants to turn websites into reusable structured CLI adapters, so users can query sites through a consistent command-line interface without hand-writing scrapers first.','takeaways':[
      'The product promise is “point at a site, declare a goal, get a CLI adapter.”',
      'Adapters can be generated on demand or reused if they already exist for the target site.',
      'The output focus is structured data rather than raw browser automation.',
      'This sits in the gap between one-off scraping and full API integration work.',
      'The idea is compelling wherever teams repeatedly need extract-transform-query behavior from web properties.'
    ],
    'synthesis':'This is a neat product concept because it packages web extraction as a durable interface instead of a disposable script. The real value is not “AI can read websites,” which is obvious, but “AI can generate and share repeatable adapters that behave like a CLI.” That lowers the cost of operationalizing web data access for internal workflows, small automations, and analysis tasks. The risk, of course, is durability: websites change, and AI-generated adapters need maintenance. But as a developer ergonomics story, AutoCLI is pointing in the right direction: structured access beats copy-paste browsing when the same task recurs.'
  },
  {
    'url':'https://blog.bytebytego.com/p/how-spotify-ships-to-675-million','title':'How Spotify Ships to 675 Million Users Every Week Without Breaking Things','author':'ByteByteGo','date':'2026','keywords':'spotify, release engineering, mobile app delivery, feature flags, rollout','pitch':'This explainer packages Spotify’s release process as a layered rollout system where trunk-based development, staged exposure, feature flags, and release management tooling make weekly shipping compatible with scale and safety.','takeaways':[
      'Spotify separates fast trunk development from release stabilization with a weekly branch-and-rollout rhythm.',
      'The release process is built around multiple exposure rings: employees, alpha, beta, 1%, then full rollout.',
      'Feature flags let code ship before capability is activated, reducing coupling between deploy and launch.',
      'A dedicated release dashboard and automation reduce human coordination overhead.',
      'The article is a good system-level narrative for how release speed and reliability can reinforce each other.'
    ],
    'synthesis':'ByteByteGo mostly synthesizes Spotify’s own engineering posts, but the summary is still useful because it makes the operating model easy to explain. The key idea is not a single tool; it is the combination of trunk-based development, branch-based stabilization, progressive exposure rings, and feature flags layered on top. That architecture turns release management into a control system rather than a heroic QA ritual. For teams trying to ship faster, the takeaway is not “copy Spotify’s exact process,” but “design explicit safety layers so that faster merges do not imply riskier launches.”'
  },
  {
    'url':'https://engineering.atspotify.com/2025/04/how-we-release-the-spotify-app-part-1','title':'A Behind-the-Scenes Look at How We Release the Spotify App (Part 1)','author':'Spotify Engineering','date':'April 2025','keywords':'release management, trunk-based development, staged rollout, mobile releases, spotify','pitch':'Spotify details the human and process side of its weekly mobile release machine, from nightly internal builds through branch cut, regression testing, store submission, and gradual rollout.','takeaways':[
      'The release team balances short merge-to-user time against strict quality thresholds.',
      'Major launches are isolated through coordination and backend flags rather than long-lived branches.',
      'The process relies on constant telemetry, bug triage, and explicit release-blocker handling.',
      'Manual regression remains selective and focused, not a blanket ritual for every team.',
      'The article makes clear that disciplined process still matters even with strong tooling.'
    ],
    'synthesis':'Part 1 is valuable because it shows the socio-technical layer of release engineering. The mechanics are familiar—nightly builds, branch cut, testing, rollout—but the interesting detail is the release manager’s role in prioritization, coordination, and deciding what risk is acceptable now versus next week. Spotify’s weekly cadence works because the process narrows what must be perfect in the current release and defers the rest. That is a strong argument for frequent shipping: a shorter cycle lets teams classify more issues as “next release” without losing responsiveness. The feature-flag examples also underline how product rollout planning and release engineering are inseparable at scale.'
  },
  {
    'url':'https://engineering.atspotify.com/2026/2/how-we-release-the-spotify-app-part-2','title':'How We Release the Spotify App: A Look Under the Hood (Part 2)','author':'Spotify Engineering','date':'February 2026','keywords':'release dashboard, backstage, state machine, automation, release tooling','pitch':'Part 2 focuses on the tooling behind Spotify’s release process: a Backstage-based dashboard, a unifying backend, and a “Robot” state machine that advances releases when conditions are met.','takeaways':[
      'Spotify built the Release Manager Dashboard to reduce context switching across many data sources.',
      'Caching and pre-aggregation were necessary to make the dashboard operationally cheap and fast.',
      'The release process is modeled as an explicit state machine with advancement conditions.',
      'Automation removed hours of delay caused by waiting for a human to click the next step.',
      'This is a strong example of tooling evolving directly from observed process bottlenecks.'
    ],
    'synthesis':'Part 2 is the more reusable engineering story because it translates release operations into productized internal tooling. The dashboard is not just a UI convenience; it is a way to collapse fragmented release evidence into a single operational view. More interestingly, Spotify used the resulting time-series data to identify that some delays were pure coordination waste, then encoded the workflow as a state machine and automated it. That progression—observe, centralize, measure, automate—is exactly how mature platform teams should attack operational toil. It is a nice reminder that the best internal tools usually start as relief valves for specific human pain.'
  },
  {
    'url':'https://workos.com/docs/pipes','title':'Pipes – WorkOS Docs','author':'WorkOS','date':'2026','keywords':'oauth, integrations, token management, third-party data, workos pipes','pitch':'WorkOS Pipes offers a managed way to let users connect third-party services and then fetch fresh access tokens without every product team rebuilding OAuth storage, refresh, and provider setup themselves.','takeaways':[
      'Pipes abstracts away token storage, refresh, and much of provider-specific OAuth plumbing.',
      'The docs position the product around a hosted widget plus backend token retrieval.',
      'Shared credentials reduce setup friction in development and sandbox environments.',
      'The offering is essentially integration infrastructure packaged as a platform service.',
      'It is especially relevant for AI products that need cross-tool context without bespoke auth work.'
    ],
    'synthesis':'The docs make the product’s appeal obvious: third-party integrations are mostly undifferentiated auth toil, yet modern products increasingly need them everywhere. Pipes tries to turn that repetitive work into a managed primitive. The AI angle is especially important because agents and copilots often need access to calendars, code hosts, CRMs, and chat tools at the same time. If token freshness and OAuth edge cases are outsourced, product teams can focus on the actual workflow value. The tradeoff, as always, is platform dependence, but for many teams that is a good trade: integration latency to market matters more than owning every auth edge case.'
  },
  {
    'url':'https://workos.com/blog/workos-pipes-third-party-integrations','title':'WorkOS Pipes: Third-party integrations without the headache','author':'WorkOS','date':'2026','keywords':'third-party integrations, oauth, ai apps, token refresh, developer tooling','pitch':'WorkOS’s launch post for Pipes argues that integration work is mostly repetitive OAuth infrastructure and that AI-heavy products especially benefit from a simpler way to connect external systems.','takeaways':[
      'The blog frames integration work as plumbing that steals time from differentiated product work.',
      'Pipes decouples authentication from third-party service authorization.',
      'The product story is strongest for apps that need many user-authorized services quickly.',
      'Shared credentials are positioned as a strong developer-experience wedge during prototyping.',
      'The article complements the docs by explaining the customer pain and target use cases.'
    ],
    'synthesis':'The blog is basically the business justification for the docs. WorkOS is betting that OAuth infrastructure is becoming more painful precisely as products become more interconnected and AI features demand broader context access. The clever part of the positioning is the distinction from login: users may authenticate one way and still need to authorize a completely different set of services for application behavior. That decoupling is increasingly common in SaaS and agent products. So Pipes is less about “easy OAuth” and more about making external connectivity a composable feature layer.'
  },
  {
    'url':'https://en.wikipedia.org/wiki/Branching_(version_control)','title':'Branching (version control)','author':'Wikipedia contributors','date':'2026','keywords':'branching, version control, trunk, merge, software configuration management','pitch':'The article is a general refresher on why branches exist in version control, how they relate to trunks and merges, and the organizational tradeoffs behind parallel development.','takeaways':[
      'Branching isolates work so teams can develop fixes, features, and releases in parallel.',
      'The trunk/mainline concept remains the central baseline from which many workflows branch.',
      'Branching strategies are deeply tied to release policy and team coordination, not just tooling.',
      'Distributed VCS changed the practical cost and ubiquity of branching.',
      'It is basic reference material, but still useful context when comparing branching philosophies.'
    ],
    'synthesis':'On its own this is just a reference page, but in the context of the Spotify release articles it becomes a nice baseline. Branching is easy to explain mechanically and much harder to optimize organizationally. The Wikipedia article reminds us that branches are simply a way to create parallel lines of change and eventually merge them. The interesting part is always the policy wrapped around that capability: long-lived feature branches, release branches, trunk-based development, vendor branches, and so on. In practice, branching debates are rarely about Git mechanics; they are about how teams want to manage risk, integration cost, and release cadence.'
  },
  {
    'url':'https://martinfowler.com/articles/feature-toggles.html','title':'Feature Toggles (aka Feature Flags)','author':'Martin Fowler','date':'2017','keywords':'feature flags, release toggles, canary release, a/b testing, trunk-based development','pitch':'Martin Fowler’s classic feature-toggle essay explains how flags let teams keep shipping from trunk while separating deploy from exposure, canarying risky changes, and experimenting safely.','takeaways':[
      'Feature flags are presented as a core enabling pattern for continuous delivery and trunk-based development.',
      'The article distinguishes different kinds of toggles with different lifetimes and operational needs.',
      'Toggle routers can evolve from simple config checks to per-request dynamic decisions.',
      'Canary releases and A/B tests become far easier when feature exposure is decoupled from deployment.',
      'The biggest caution is that toggle systems create complexity unless actively managed.'
    ],
    'synthesis':'This remains one of the clearest explanations of why feature flags matter beyond “turn things on and off.” Fowler frames them as a control mechanism for delivering incomplete or risky code safely, which is exactly why they pair so naturally with trunk-based development and staged rollouts. The examples still feel current because modern product teams use flags for the same reasons: testing, internal exposure, canaries, experimentation, and operational fallback. The important nuance is that flags are not free. They buy release flexibility at the cost of runtime and codepath complexity. Teams that internalize both sides of that trade tend to use flags well; teams that do not end up with permanent conditional archaeology.'
  },
]


def sh(cmd):
    subprocess.run(cmd, shell=True, check=True, cwd=ROOT)

def capture(cmd):
    return subprocess.check_output(cmd, shell=True, cwd=ROOT, text=True)

def slugify(s):
    s=s.lower()
    s=re.sub(r"[^a-z0-9]+", '-', s).strip('-')
    return s[:80]

def current_version():
    return VERSION.read_text().strip()

def bump_version_and_log(msg):
    parts=current_version().split('.')
    parts[-1]=str(int(parts[-1])+1)
    new='.'.join(parts)
    VERSION.write_text(new)
    rel=RELEASES.read_text()
    RELEASES.write_text(f"## {new} - 2026-04-08\n- {msg}\n\n"+rel)
    return new

def add_memory(action, files, outcome, next_step):
    existing=MEMORY.read_text()
    entry=f"## {NOW}\n- actor: agent\n- action: {action}\n- files_changed_or_commands: {files}\n- outcome: {outcome}\n- next_step: {next_step}\n\n"
    MEMORY.write_text(existing+"\n"+entry)

list_lines=[l.strip() for l in LIST.read_text().splitlines() if l.strip()]
errs=[]
processed=[]
assert len(list_lines)==len(articles), f"LIST count {len(list_lines)} != metadata {len(articles)}"

for art in articles:
    if not list_lines or list_lines[0] != art['url']:
        errs.append(f"ORDER_MISMATCH for {art['title']}")
        if art['url'] in list_lines:
            idx=list_lines.index(art['url'])
        else:
            continue
    else:
        idx=0
    slug=slugify(art['title'])
    path=ROOT/f"src/2026-04/20260408-{slug}.md"
    content = [f"# {art['title']}","",f"**Source**: {art['url']}",f"**Date**: {art['date']}",f"**Author**: {art['author']}",f"**Keywords**: {art['keywords']}","","## Elevator pitch",art['pitch'],"","## Takeaways"]
    for t in art['takeaways']:
        content.append(f"- {t}")
    content += ["","## Synthesis",art['synthesis'],""]
    path.write_text('\n'.join(content))
    readme = README.read_text()
    marker='#### April (1 articles)\n'
    insert=f"- [{art['title']}](src/2026-04/{path.name})\n"
    if insert not in readme:
        README.write_text(readme.replace(marker, marker+insert, 1))
    list_lines.pop(idx)
    LIST.write_text(('\n'.join(list_lines)+'\n') if list_lines else '')
    sh(f"git add {path.relative_to(ROOT)} README.md LIST.md")
    sh(f"git commit -m {json.dumps('Process article: '+art['title'])}")
    processed.append((art['title'], path.name))
    bump_version_and_log(f"Process article: {art['title']}.")

batch_path = ROOT/f"synthesis/{BATCH_STAMP} - batch recap.md"
lines=[f"# Batch recap — {BATCH_DISPLAY}",""]
for title, name in processed:
    lines.append(f"- **{title}** — {REPO_URL}/src/2026-04/{name}")
batch_path.write_text('\n'.join(lines)+'\n')
assert batch_path.exists()
assert sum(1 for l in batch_path.read_text().splitlines() if l.startswith('- **')) == len(processed)
msg=f"Add batch recap: {BATCH_DISPLAY}."
bump_version_and_log(msg)
add_memory(
    action=f"scan-list run: processed {len(processed)} URLs, created {len(processed)} synthesis files in src/2026-04/, updated README April section, emptied LIST.md, created batch recap {batch_path.relative_to(ROOT)}",
    files=f"LIST.md (cleared), src/2026-04/*.md ({len(processed)} new files), README.md, {batch_path.relative_to(ROOT)}, .prompt-hub/version.md, .prompt-hub/releases.md",
    outcome='success' if not errs else 'partial success',
    next_step='Commit recap, prompt-hub logs, and push.'
)
sh('git add synthesis .prompt-hub/version.md .prompt-hub/releases.md .prompt-hub/memory.md .prompt-hub/todo/todo-20260408-180659-scan-list.md .prompt-hub/todo/scan_list_20260408.py')
sh(f"git commit -m {json.dumps('Add batch recap and logs for 2026-04-08 180659')}")
print(json.dumps({'processed':processed,'errors':errs}, ensure_ascii=False))
