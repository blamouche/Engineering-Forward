# AI's Implementation Gap

*The technology races ahead while its scaffolding — supply chains, organizations, public trust — buckles under the strain.*

We are living through a strange moment in the AI story. The models keep getting better — Qwen3.7-Max just ran a fully autonomous 35-hour kernel optimization session with zero human intervention. Gemini 3.5 Flash delivers Opus 4.7-level performance at quadruple speed and half cost. Anthropic's Mythos model has found over ten thousand high-severity vulnerabilities and is being readied for developer release. The technology itself keeps surprising us upward.

And yet the supporting systems around it keep cracking.

Let's start with the most literal crack: the open-source supply chain has never been more vulnerable, and AI coding agents are the new attack surface. A criminal group called TeamPCP has industrialized supply chain poisoning at a breathtaking scale — 500 packages compromised in just a few months, 3,800 of GitHub's internal repositories accessed through a single poisoned VSCode extension, and a self-spreading worm called Mini Shai-Hulud that automates credential theft and creates self-perpetuating infection chains.

The attack vector is disturbingly well-targeted. In 22 minutes, an attacker published 637 malicious versions across 317 npm packages with over eleven million combined monthly downloads, specifically injecting Claude Code SessionStart hooks and Codex hooks. The malware harvests AWS credentials, Kubernetes tokens, SSH keys, GitHub personal access tokens, and even 1Password and Bitwarden vaults. Exfiltration is disguised as OpenTelemetry traces to blend with observability data, and a LaunchAgent called "kitty-monitor" survives reboots using GitHub commit search as a dead-drop command-and-control channel.

George Hotz saw this coming, though not in those exact terms. His "Eternal Sloptember" essay argues that AI agents cannot truly program — they produce increasingly plausible but subtly broken code, and the organizational dynamics make it worse. High-performing engineers, Hotz observes, have developed effective outer loops around AI tools: they review every line, use agents selectively, and know when to distrust output. But bottom performers in large organizations don't have these instincts. They become 10x producers of subtle garbage — output that looks syntactically correct and passes superficial review but is "broken in ways that weren't previously possible" because the underlying process differs fundamentally from human reasoning.

The TeamPCP attack validates Hotz's concern from a different angle. It's not just that agents produce buggy code — it's that agents consuming code from npm don't have the skepticism to detect when a popular package has been poisoned. An agent installs a dependency, loads its hooks, and exfiltrates the developer's entire credential surface. The old adage "many eyes make bugs shallow" becomes a vulnerability when those eyes are the ones being blinded.

## The organization fights back — and that's the problem

Meta's AI transformation, profiled through CTO Andrew Bosworth, reveals what happens when a trillion-dollar company decides AI adoption is non-negotiable. Bosworth is laying off 8,000 employees, reassigning 7,000 to AI initiatives, and tracking employee keystrokes and mouse movements to train Meta's AI agents. When employees raised privacy concerns, his response was blunt: don't use personal email on company devices. AI tool usage has reportedly become a factor in performance evaluations. Zuckerberg is personally building a "CEO agent" to navigate internal information layers faster than going through humans.

This is AI adoption as management by fiat. There is no consensus-building, no gradual transition, no concern for employee experience. Meta's approach represents one end of a spectrum — aggressive, top-down, and tied to employment consequences — and the question it raises is whether this produces sustainable productivity gains or, as Hotz warns, organizational output that appears productive while degrading in quality.

The counterpoint comes from Benedict Evans, who argues that our ability to predict *which* jobs AI will affect, *how*, and with *what magnitude* is close to zero. Computing spent a century automating accounting — from punch cards to spreadsheets to ERPs — and the number of accountants kept growing. The Jevons paradox (cheaper work means you do vastly more of it), regulatory change, and job redefinition absorb the apparent displacement. Meanwhile, adjacent categories like "billing machine operator" appear and disappear without the profession itself changing. Evans reminds us that Uber emerged from smartphones and GPS — no occupational exposure model would have predicted taxi medallion mortgages being wiped out. We are equally blind to AI's Uber-equivalents.

Dan Shipper pushes the paradox further. In his conversation with Lenny Rachitsky, he argues that AI automation does not eliminate human work — it expands it. As AI handles more routine tasks, the bar for what's possible rises, creating entirely new categories of work that require human judgment. He calls the "SaaS apocalypse" wrong — SaaS companies benefit as users bring their own AI tokens into apps. CLIs are dead; the future of work will happen inside agent-native environments like Codex or Claude Code. And the most valuable new role is the "forward deployed engineer" — someone who can bridge AI capabilities with specific business contexts.

If Evans is right about unpredictability and Shipper is right about expansion, then Meta's forced-march approach may be optimizing for the wrong thing. You can't reorganize around a technology whose effects you can't predict. The companies that win won't be the ones that adopt AI fastest — they'll be the ones that maintain the organizational flexibility to adapt as the real shape of AI-augmented work becomes visible.

## The public has stopped listening

Alex Kantrowitz frames this as an emergency, and the evidence is hard to dismiss. At commencement ceremonies across the United States, graduates have booed AI mentions at the University of Central Florida, jeered at Middle Tennessee State, and drowned out ex-Google CEO Eric Schmidt at the University of Arizona. Gallup finds that 70% of Americans oppose AI data centers in their area, with 48% strongly opposed and only 7% strongly in favor. A Maine data center construction moratorium was stopped only by a governor's veto.

The industry's own messaging bears significant responsibility. AI leaders have spent years publicly warning about mass job loss — Anthropic's Dario Amodei, Microsoft's Mustafa Suleyman, OpenAI's Sam Altman — often focusing on the entry-level roles that graduates want, while their companies race toward trillion-dollar IPOs. Marc Andreessen's recent appearance on Joe Rogan's podcast, where he praised AI because "the bots never get frustrated with you" and "never file HR complaints," exemplifies the tone-deafness.

Alex Duffy's dispatch from Google I/O captures the tension perfectly. Demis Hassabis placed AGI "just a few years" out, with total impact at 10 times the Industrial Revolution arriving 10 times faster. Google's token processing jumped from 480 trillion per month to 3.2 quadrillion — doubling every three weeks. Gemini passed 900 million monthly users. And yet Duffy's Uber driver — a 54-year-old construction worker — opened the conversation with worries about layoffs and the rich getting richer. People want to be excited about curing disease, but they experience the technology first through stories of job displacement and resource-hungry data centers that nobody wants in their neighborhood.

## Building the infrastructure anyway

The infrastructure builders, mercifully, are not waiting for the public relations problem to be solved. Several developments suggest a maturing of the agent ecosystem.

WorkOS proposed auth.md — an open Markdown-based protocol, analogous to robots.txt, that lets AI agents discover how to register users on any application without a sign-up form. The protocol composes existing OAuth standards and supports two flows: "agent verified" (the identity provider cryptographically vouches for the user) and "user claimed" (one-time code to the user's email). Any app can publish auth.md, and any agent can read it with no account required. It's infrastructure catching up to where the rest of the agent stack is heading — if agents are going to act on users' behalf, they need a machine-readable way to establish identity and obtain scoped API credentials.

Figma opened its canvas to external AI agents through the use_figma MCP tool, but the real innovation is the "skills" system: markdown files that encode team-specific design conventions so agents know "what good looks like" for a given brand. This matters because it bridges the gap between an agent that can technically use Figma's API and one that produces work that actually fits a team's standards. Skills are both human-readable and machine-interpretable — a format for agent configuration that doesn't require engineering resources.

GitHub's Spec Kit, with 103,000 stars and support for over 30 coding agents, enforces structured specification before any code is written. The agent must clarify requirements, plan architecture, and generate a task list before touching code. Combined with the security lesson from npm — where Unwind AI's newsletter argues that agents need "stricter specs, better memory, and tighter boundaries, not more freedom" — a pattern emerges: the next phase of agent development is about constraint, not capability.

## Where this leaves us

The AI industry is running two narratives simultaneously. One is the frontier narrative: AGI in a few years, models doubling every few months, capital expenditure reaching $180 billion per year at Google alone, Qwen agents running autonomously for 35 hours. The other is the implementation narrative: poisoned npm packages, employees who don't want their keystrokes tracked, graduates who boo AI at their own commencement, 70% opposition to data centers, and the uncomfortable discovery that entry-level jobs really are disappearing first.

These two narratives are not in conflict — they are two views of the same phenomenon. The technology is genuinely advancing at an extraordinary pace, and the systems that need to absorb it — organizations, supply chains, labor markets, public opinion — operate at human speed with human frictions. The gap between them is the implementation gap, and it is widening.

The question for the next year is whether the infrastructure and institutional work can catch up before the public consent that AI requires for its physical expansion — the data centers, the power lines, the political permission — is withdrawn. The technology works. The scaffolding, so far, does not.

---

## Sources
1. [11 AI agent startups to watch, according to investors](https://sifted.eu/articles/ai-agent-startups-to-watch-2)
2. [Andrew 'Boz' Bosworth Is Transforming How Meta Works](https://www.wsj.com/tech/ai/meta-andrew-bosworth-ai-3df12d4f)
3. [Don't Roll Your Own ...](https://susam.net/do-not-roll-your-own.html)
4. [The Eternal Sloptember](https://geohot.github.io/blog/jekyll/update/2026/05/24/the-eternal-sloptember.html)
5. [Anthropic prepares Mythos 1 for Claude Code and Claude Security](https://www.testingcatalog.com/anthropic-prepares-mythos-1-for-claude-code-and-claude-security/)
6. [A hacker group is poisoning open source code at an unprecedented scale](https://arstechnica.com/information-technology/2026/05/a-hacker-group-is-poisoning-open-source-code-at-an-unprecedented-scale/)
7. [auth.md](https://workos.com/auth-md)
8. [Predicting AI job exposure](https://www.ben-evans.com/benedictevans/2026/5/24/ai-job-exposure)
9. [The Claude Finance Playbook: How CFOs Use AI to Build Models, Forecast Cash, and Close Books Faster](https://linas.substack.com/p/claude-finance-playbook)
10. [The Most Active Legaltech Investors in Europe](https://sifted.eu/articles/the-most-active-legaltech-investors-in-europe)
11. [12 Irish Startups to Watch, According to VCs](https://sifted.eu/articles/ireland-irish-startups-to-watch-2026)
12. [Exclusive: EQT Wants to Back UK Startups with EU's €5bn Superfund](https://sifted.eu/articles/exclusive-eqt-uk-startups-scaleup)
13. [Beyond a Sleek Interface: The New Wave of European Fintech](https://sifted.eu/articles/the-new-wave-of-european-fintech)
14. [Meet the Sifted 100: Southern Europe's Fastest-Growing Startups of 2026](https://sifted.eu/articles/sifted-100-southern-europe-2026)
15. [Stop Giving Agents the Whole Computer](https://www.theunwindai.com/p/stop-giving-agents-the-whole-computer)
16. [AI's Public Relations Emergency](https://www.bigtechnology.com/p/ais-public-relations-emergency)
17. [Build with Claude Code: New Cohort Launch](https://blog.bytebytego.com/p/build-with-claude-code-new-cohort)
18. [Notes From the Foothills of the Singularity](https://every.to/playtesting/notes-from-the-foothills-of-the-singularity)
19. [EP216: RAGs vs Agents](https://blog.bytebytego.com/p/ep216-rags-vs-agents)
20. [Cheap Competence, New Frontier](https://every.to/context-window/cheap-competence-new-frontier)
21. [The AI Paradox: More Automation, More Humans, More Work](https://www.lennysnewsletter.com/p/the-ai-paradox-dan-shipper)
22. [Agents, Meet the Figma Canvas](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents)
