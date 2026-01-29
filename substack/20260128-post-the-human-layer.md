# What's important now - The Human Layer

*As AI generates 90% of the code and reviews millions of pull requests, the skills that matter are taste, trust, and the precision to tell machines exactly what you want.*

Benji built an elegant icon system where any of twenty-one icons can smoothly morph into any other. The technical foundation is simple: every icon uses exactly three SVG lines, with unused lines collapsed to invisible center points. Framer Motion handles the animation tweening. Claude Code implemented the whole thing.

But Claude couldn't identify when transitions "felt off." When a right-facing arrow morphed into a down-facing arrow through coordinate interpolation instead of rotation, the result looked wrong—awkward intermediate states that violated users' intuitive expectations of physical motion. Claude excelled at implementing functional code but lacked the ability to evaluate aesthetic quality. Benji had to watch the animations, recognize the problem, and guide the AI toward better approaches.

This pattern—AI handling implementation while humans provide judgment—appears across every domain where AI has achieved meaningful deployment. The question is no longer whether AI can generate code, write content, or process information. The question is what happens to the human layer when AI handles the mechanical work.

## The Precision Requirement

Matt Nigh's analysis of over 2,500 `agents.md` files reveals a critical insight about working effectively with AI: generic prompts fail spectacularly. The most common failure pattern involves imprecise directives that leave agents guessing about expectations. "You are a helpful coding assistant" provides no actionable guidance. Successful configurations treat agents as specialized professionals requiring specific role definitions, explicit instructions, and defined boundaries.

One real code snippet outperforms three paragraphs describing it. Executable commands should appear prominently with complete flags and options. Clear boundaries—particularly "never commit secrets"—represent the most common helpful constraint. Effective configurations establish three-tier frameworks: actions agents should always take, decisions requiring human approval, and operations agents must never perform.

Jakub Krehel, a design engineer, arrives at similar conclusions from practice. AI should accelerate workflow execution rather than replace creative thinking. Establishing explicit codebase rules—animation performance, design systems, code utilities—in dedicated files helps AI produce consistent, project-aligned code. Always assume AI has zero context when starting conversations. Custom commands like `/deslop` help remove AI-generated redundancies and maintain code quality.

The precision requirement represents a fundamental shift in how professionals create value. Success depends not on knowing how to code but on knowing exactly what code should do. The ability to specify requirements precisely, provide concrete examples, and establish clear boundaries determines whether AI produces excellence or mediocrity. This is management skill applied to machines—clear direction, explicit formats, quality examples, systematic evaluation, and task decomposition.

## The Trust Network

Lewis Kallow introduces a framework that explains why some AI products achieve widespread adoption while others languish despite technical merit. Drawing on sociological research dating back to the 1933 Iowa hybrid corn study, he distinguishes between simple and complex contagions.

Simple contagions are low-risk ideas that spread easily through single exposure: a song recommendation, a meme, trivial information. Complex contagions involve significant behavioral changes that require multiple reinforcements from trusted sources before adoption occurs. Using new AI tools falls squarely in the complex contagion category because it demands time investment, workflow changes, and implicit admission that current methods may be insufficient.

The key insight involves "social dandelions"—individuals who are exceptionally socially active, present across multiple communities and organizations. Traditional marketing wisdom prioritizes influencers with large followings. Kallow argues instead for identifying people who naturally disperse ideas through widespread visibility, creating the multiple exposure points that complex contagions require.

ChatGPT didn't win because it was technically superior to alternatives. It succeeded by being freely accessible and by first reaching AI researchers embedded in passionate, interconnected communities who could validate and recommend it to peers. Airbnb's founders succeeded by physically meeting hosts, embedding themselves in communities where trust could be demonstrated repeatedly.

This has profound implications for AI builders. As AI increasingly commoditizes the ability to create software and generate marketing content, competitive advantage shifts entirely to distribution strategy—understanding which communities to target, identifying the social dandelions within them, and reducing every possible friction point. Building great technology becomes table stakes; understanding human trust becomes the game.

## The Internal Revolution

Gergely Orosz and Elin Nilsson reveal a significant disconnect between public perception and actual MCP usage patterns. While discussions focus on public server marketplaces, most meaningful Model Context Protocol adoption occurs behind corporate firewalls, serving internal business needs rather than external developer audiences.

The median MCP user profile is someone seeking to access "company's own data warehouse through an MCP server." Internal data and platform teams have recognized MCP as a mechanism to grant non-technical stakeholders—product managers, business analysts, executives—access to complex systems without requiring technical expertise. Rather than building specialized interfaces for each stakeholder group, organizations expose systems through MCP and let AI agents handle translation between user intent and system capabilities.

Razorpay reports achieving 75% accuracy on first-generation code from Figma designs through MCP integration. Custom MCPs bridge integration gaps with complex legacy systems, enabling modernization without wholesale replacement. The practical use cases span development workflows, debugging through Sentry integration, testing automation with Playwright, and documentation access that reduces AI hallucinations.

This internal-first pattern reflects something important about where AI creates genuine value. Organizations aren't building flashy public tools; they're democratizing access to internal systems that were previously gatekept by technical complexity. Product managers can prototype features by having agents access data warehouses. Business analysts can query complex systems through natural language. The transformation happens invisibly, inside companies, serving people who previously lacked technical access to systems containing information they needed.

## The Economic Question

The panel discussion bringing together Michael Burry, Jack Clark, Dwarkesh Patel, and Patrick McKenzie crystallizes the central tension in current AI discourse. On one side, transformer architecture and scaling laws have enabled capabilities that surpass previous AGI benchmarks. On the other, the mathematics are stark: the software industry's total revenue falls below $1 trillion annually, yet AI infrastructure spending has reached $400 billion against less than $100 billion in actual AI product revenue.

The productivity paradox emerges repeatedly. While developers report transformative gains using AI coding assistants, independent research revealed that experienced programmers in familiar codebases actually experienced roughly 20% decreases in measurable output. Self-reported 50% gains contradict systematic measurement. This disconnect between perception and reality raises questions about whether AI benefits are real or merely redistributed from other activities.

OpenAI's financial position illustrates the pressure. The company plans to burn through $17 billion in cash in 2026, nearly double the $9 billion consumed in 2024. During the first half of 2025, inference costs actually exceeded revenue. Computing power requirements have grown from 200 megawatts in 2023 to 1.9 gigawatts in 2025, with plans to add another 30 gigawatts. The company pursues what would be the largest private fundraising round in history—$100 billion—with profitability not expected until 2030.

Edward Zitron's analysis of NVIDIA raises additional concerns. Hyperscalers and secondary buyers have raised $88 billion in debt specifically for GPU acquisition, with newer cloud providers using purchased GPUs as collateral for additional loans. NVIDIA's continued dominance requires companies to repeatedly purchase billions in GPUs for data centers that don't generate sufficient revenue to justify the expenditure. Whether this represents transformative investment or speculative bubble remains genuinely unclear.

## The Emerging Roles

The World Economic Forum estimates AI could create 170 million jobs by 2030, many in entirely new categories. Guillaume Renouard identifies five emerging roles that illustrate what the human layer looks like in practice.

Algorithm interpreters will address explainability—translating how LLMs function for non-technical audiences including regulators and executives. Data annotation specialists will combine domain expertise with data science skills; labeling genetic data requires understanding biology, not just technical competence. AI deployment engineers will function as hybrids between consultants and developers, working on-site with organizations through extended implementations. AI risk and governance specialists will navigate the expanding regulatory landscape across multiple jurisdictions. Custom AI chip specialists will translate organizational AI needs into hardware architecture decisions.

What unifies these roles is their hybrid nature. None represent pure technical positions or pure business roles; instead, they require combinations of technical expertise, domain knowledge, communication skills, and business understanding. The most valuable skills help humans and AI systems work together effectively rather than simply building or using AI systems in isolation.

Gergely Orosz frames the profession restructuring starkly. True engineering skills—tech leadership, product thinking, systems architecture—become more valuable as coding itself becomes commodified. Product management and engineering roles are converging as both gain overlapping capabilities through AI tools. The bits contributed by programmers are increasingly sparse; the value shifts to judgment about what to build and why.

## The Junior Advantage

Tug Grall offers a counterintuitive perspective on junior developers. Young programmers entering the field have AI familiarity from university training, creating strategic advantage for both professionals and employers. Unlike seasoned developers who must adapt to AI assistance, new graduates enter organizations already comfortable with human-AI collaboration.

AI handles routine coding tasks, freeing junior developers to engage earlier with higher-value work: system architecture, complex problem-solving, and strategic project contributions. Rather than spending years on syntax and implementation details, young programmers can tackle meaningful projects immediately. They develop essential competencies—teamwork, system design, and AI agent collaboration—more rapidly than previous generations could.

This reframes what "entry-level" means in software development. The learning curve doesn't disappear; it transforms. If syntax mastery becomes less central, programming opens to problem-solvers who may not have pursued traditional computer science education. The definition of "developer" may expand to include anyone capable of directing AI systems toward useful outcomes.

## Looking Ahead

Katie Parrott discovered something unexpected when she asked Claude to analyze her performance data. Operating under constant assumption that she was about to be fired, she struggled to accept positive feedback from supervisors. But receiving assessment from a machine made the validation emotionally credible in ways human feedback never had. The AI's perceived objectivity and emotional distance allowed her to actually internalize positive information about her work.

This small case study hints at the broader role AI may play at the human layer. Not replacing human judgment, but providing the psychological distance, objectivity, and neutral analysis that enables humans to make better decisions. The data showed Parrott produced 15% of company content while driving 25-27% of subscription trials—information that human managers had communicated but that she couldn't accept until a machine confirmed it.

Oracle France's CEO predicts 2026 will be the year of agentic platforms, but emphasizes that no enterprise clients currently delegate 100% task autonomy to AI agents. Human oversight remains essential in all deployments. The focus is workforce transformation where employees coexist with and supervise AI agents rather than being replaced by them.

The human layer isn't shrinking. It's changing. The skills that matter are becoming more distinctly human: taste that can recognize when animations feel wrong, trust relationships that drive adoption through dense social networks, precision in specifying exactly what machines should do, judgment about what to build and why. AI handles the mechanical translation; humans handle the decisions. As Jakub Krehel puts it: as AI commoditizes implementation, design and user experience will become the product. Human judgment on quality and craftsmanship remains irreplaceable.

---

## Sources

1. [Using AI as a Design Engineer](https://jakub.kr/work/using-ai-as-a-design-engineer)
2. [Morphing Icons with Claude](https://benji.org/morphing-icons-with-claude)
3. [AI Can Build Anything. Social Dandelions Decide What Spreads.](https://every.to/p/ai-can-build-anything-social-dandelions-decide-what-spreads)
4. [How to write a great agents.md: Lessons from over 2,500 repositories](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
5. [The Hater's Guide To NVIDIA](https://www.wheresyoured.at/the-haters-guide-to-nvidia/)
6. [Building MCP servers in the real world](https://newsletter.pragmaticengineer.com/p/mcp-deepdive)
7. [Gemini Introduces Personal Intelligence](https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence/)
8. [5 métiers que l'intelligence artificielle va créer](https://www.journaldunet.com/intelligence-artificielle/1547227-5-metiers-que-l-intelligence-artificielle-va-creer/)
9. [Recursive Language Models](https://alexzhang13.github.io/blog/2025/rlm/)
10. [I Asked Claude the Question I Could Never Ask My Boss](https://every.to/working-overtime/i-asked-claude-the-question-i-could-never-ask-my-boss)
11. [When AI Writes Almost All Code, What Happens to Software Engineering?](https://newsletter.pragmaticengineer.com/p/when-ai-writes-almost-all-code-what)
12. [Comment l'IA réinvente le rôle des jeunes développeurs](https://www.journaldunet.com/intelligence-artificielle/1546951-comment-l-ia-reinvente-le-role-des-jeunes-developpeurs/)
13. [2026 sera l'année des plateformes agentiques](https://www.journaldunet.com/intelligence-artificielle/1547067-christophe-negrier-oracle/)
14. [Pour OpenAI, 2026 est l'année de tous les dangers](https://www.journaldunet.com/intelligence-artificielle/1547047-pour-openai-2026-est-l-annee-de-tous-les-dangers/)
15. [The AI Revolution Is Here. Will the Economy Notice?](https://post.substack.com/p/the-ai-revolution-is-here-will-the)
