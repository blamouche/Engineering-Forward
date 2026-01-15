# How to write a great agents.md: Lessons from over 2,500 repositories

**Source**: https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/

**Date**: November 19, 2025 (Updated November 25, 2025)

**Author**: Matt Nigh (@mattnigh)

**Keywords**: agentic AI, generative AI, GitHub Copilot, agents.md, agent configuration, AI coding assistants, custom agents

## Elevator pitch

Successful agent configuration files aren't vague helpers but specialized professionals with specific directives—analysis of 2,500+ repositories reveals that precise instructions, code examples, and clear boundaries dramatically outperform generic guidance.

## Takeaways

- Generic statements like "you are a helpful coding assistant" significantly underperform compared to specific role definitions with clear directives
- Executable commands should appear prominently with complete flags and options, with one real code snippet outperforming three paragraphs of description
- Explicit constraints, particularly "never commit secrets," represent the most common helpful boundary across successful agent configurations
- Effective agents cover six core areas: commands, testing, project structure, code style, git workflow, and boundaries, organized in three-tier frameworks (always do/ask first/never do)
- Six practical agent types worth building: docs, test, lint, api, security, and dev-deploy agents, each focused on specific development tasks

## Synthesis

Matt Nigh's analysis of over 2,500 `agents.md` files reveals fundamental principles for configuring AI coding assistants that deliver real value rather than generic helpfulness. The research challenges common assumptions about how to communicate with AI agents, demonstrating that specificity, concreteness, and clear boundaries dramatically outperform abstract guidance and vague role definitions.

The most critical finding centers on instruction precision. The most common failure pattern across analyzed repositories involves imprecise directives that leave agents guessing about expectations. Generic statements like "you are a helpful coding assistant" provide no actionable guidance about what helpfulness means in context—which commands to run, which conventions to follow, which boundaries to respect. In contrast, successful configurations define precise roles with specific responsibilities, essentially treating the agent as a specialized professional rather than a general-purpose helper.

The principle of early command placement emphasizes that executable commands should appear prominently in agent configuration, complete with flags and options. Rather than describing what commands might be useful, effective configurations show exactly what to run: `npm test -- --coverage --watchAll=false` rather than "run tests." This specificity eliminates ambiguity about which flags matter, how to invoke commands properly, and what output to expect. Commands represent the primary interface between agents and codebases, making their precise specification foundational to effective agent behavior.

Code examples versus description represents another key insight. Nigh emphasizes that "one real code snippet outperforms three paragraphs describing it" when teaching agents about project conventions. This principle reflects a broader pattern where agents learn more effectively from concrete examples than abstract descriptions. If you want an agent to follow specific code style conventions, showing example code conforming to those conventions provides clearer guidance than describing the conventions in prose. This mirrors how human developers learn—reading actual code often communicates patterns more effectively than written style guides.

Clear boundaries, particularly around security-sensitive operations, emerge as the most common helpful constraint across successful configurations. The explicit directive "never commit secrets" appears frequently because it addresses a high-stakes failure mode where agents might inadvertently include API keys, passwords, or credentials in code or commits. More broadly, effective configurations establish three-tier boundary frameworks: actions agents should always take, decisions requiring human approval before proceeding, and operations agents must never perform. This structure provides agents with clear decision frameworks rather than forcing them to infer appropriate caution levels.

Stack specificity matters significantly for agent effectiveness. Precise technology versions—"React 18.2, using functional components and hooks, with TypeScript 5.1"—eliminate ambiguity about which patterns and APIs agents should use. Vague references like "modern React" leave agents guessing whether that means class components, functional components, hooks, Suspense, Server Components, or other paradigm shifts that have occurred across React versions. Precise version specifications ensure agents apply patterns appropriate to the actual codebase context rather than mixing conventions across eras.

The six core coverage areas represent domains that effective agent configurations address systematically: commands for development operations, testing approaches and frameworks, project structure and file organization conventions, code style and formatting rules, git workflow expectations, and operational boundaries. Covering these areas comprehensively ensures agents have guidance for the full spectrum of development activities rather than narrow slices. An agent that knows how to write code but doesn't understand testing conventions or git workflow will produce incomplete contributions requiring significant human intervention.

The recommended agent types—docs, test, lint, api, security, and dev-deploy—reflect common development tasks that benefit from agent assistance. Each represents a specialized role with well-defined inputs, outputs, and success criteria. A docs agent generates API documentation from code, requiring understanding of code structure and documentation conventions. A test agent writes unit and integration tests based on implementation code. A lint agent fixes code style and formatting issues. An api agent creates REST endpoints and resolvers. A security agent analyzes security risks in code. A dev-deploy agent manages local and development environment builds. These specialized roles perform better than generalist agents because they focus on specific problem domains with clear evaluation criteria.

The emphasis on iterative development over comprehensive upfront planning represents an important practical insight. Rather than attempting to create perfect agent configurations initially, Nigh recommends starting with templates and refining based on observed behavior. This approach acknowledges that predicting exactly what instructions agents need proves difficult until you observe them working with actual codebases. Iterative refinement based on real usage patterns produces better configurations than theoretical completeness.

The broader implications for AI agent adoption center on the mental model shift required for effective usage. Developers accustomed to generic AI assistants that respond to conversational prompts must transition to thinking about agents as specialized professionals requiring clear role definitions, explicit instructions, and defined boundaries. This represents less of a "chat with a helper" interaction model and more of a "configure a team member" paradigm where upfront clarity about responsibilities and constraints determines effectiveness.

The security boundary emphasis throughout the article reflects growing awareness of risks associated with AI agents operating autonomously on codebases. Generic "be helpful" directives provide no protection against agents inadvertently introducing vulnerabilities, committing secrets, or making dangerous operational changes. Explicit boundaries—what to never do, what requires approval, what to always verify—provide essential guardrails for autonomous agent operation in production environments.

The specificity requirement Nigh documents may initially seem burdensome to teams adopting AI agents. Writing detailed configuration files with precise commands, code examples, technology versions, and boundaries requires upfront investment. However, this investment pays returns through more predictable agent behavior, reduced need for supervision, and fewer instances where agents produce plausible-looking but incorrect or inappropriate code. The alternative—minimal configuration with vague guidance—generates ongoing costs through constant course correction and output validation.

The article's practical focus on what works rather than theoretical possibilities distinguishes it from much AI agent discourse. Rather than speculating about future capabilities or debating philosophical questions about AI autonomy, Nigh documents patterns that demonstrably improve agent effectiveness in real repositories. This empirical grounding makes the findings immediately actionable for teams implementing AI agents, providing concrete templates and principles rather than abstract aspirations.

The evolution from generic AI assistants to specialized, well-configured agents represents a maturation of how organizations deploy AI in development workflows. Early adoption often focuses on basic autocomplete and conversational assistance with minimal configuration. As teams gain experience, they recognize that investment in agent configuration—defining precise roles, providing concrete examples, establishing clear boundaries—yields significantly better results than relying on default behaviors. This pattern mirrors broader software engineering principles where initial flexibility gives way to explicit conventions as systems mature and reliability becomes critical.
