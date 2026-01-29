# What's important now - The 10% Programmer

Somewhere in San Francisco, a developer opens their laptop on a Tuesday morning to discover that the bug they planned to fix has already been resolved. Not by a colleague working late, not by an offshore team in a different timezone, but by an AI agent that spent the night methodically working through the issue backlog. The developer reviews the pull request, approves the changes, and moves on to the next task—which another agent is already working on.

This scene, described by Kieran Klaassen in a recent article for Every, is no longer unusual. Klaassen claims that every piece of code he has shipped in the past two months was written by AI. Not assisted by AI. Written by AI. He runs five parallel Claude Code instances across different git worktrees, functioning less like a programmer and more like a technical director overseeing a small team of tireless, reasonably competent junior developers.

The implications of this shift are only beginning to register.

## The Inversion

According to interviews with Cursor's engineering team, some developers now spend as little as 10% of their time writing code manually. The remaining 90% involves managing AI agents, reviewing their outputs, and making strategic decisions about what to build next. Developer education lead Lee Robinson puts it bluntly: "The IDE is kind of dead."

This inversion—from primarily writing code to primarily directing machines that write code—represents the most significant change in software development since the advent of high-level programming languages. The traditional 5:1 to 10:1 ratio of code-writing to review time collapses entirely when AI generates thousands of lines overnight.

The practical demonstrations are striking. Cursor's research team built a functional web browser from scratch using AI agents running continuously for weeks. The project generated three million lines of code across thousands of files at approximately $80,000 in token costs. They migrated their own codebase from Solid to React with over 450,000 line changes across three weeks. These are not toy projects or weekend experiments. This is production software at scale, written predominantly by machines.

Yet the infrastructure enabling this shift is surprisingly accessible. GitHub has released the Copilot SDK, providing a production-tested agent runtime across Node.js, Python, Go, and .NET. Anthropic's Claude Code runs within existing terminal workflows. The barrier to entry is not technical sophistication but mindset transformation.

## The New Competencies

The skills that matter are changing. Traditional prompting techniques—tricks like "I'll pay you $1,000 for better outputs"—no longer work with current models. What matters instead is model selection for specific tasks, understanding that Claude Opus excels at conceptual problem-solving while GPT 5.2 Codex delivers thorough methodical work. Power users run parallel comparisons across up to eight models simultaneously.

John Lindquist, co-founder of egghead.io, describes a counterintuitive documentation strategy where Mermaid diagrams in markdown files compress application architecture into formats optimized for AI rather than human consumption. The artifacts that make systems understandable to machines increasingly differ from those that make systems understandable to people.

The concept of "compounding engineering" emerges as a key differentiator. Instead of starting fresh each session, sophisticated practitioners document workflows in CLAUDE.md files that preserve context across sessions. Each bug fix and code review becomes a permanent lesson embedded in system behavior. Klaassen describes a breakthrough moment when Claude autonomously applied three months of prior code review feedback without being asked, citing specific pull requests. The AI had internalized patterns from past corrections and applied them proactively.

This creates a positive feedback loop: investment in teaching the tools compounds over time, making future work progressively faster. The developers who understand this dynamic—who treat development as architectural teaching rather than daily problem-solving—gain cumulative advantages that widen with each project.

## The Organizational Gap

But here is where the story gets complicated. While individual practitioners achieve remarkable productivity gains, organizations are struggling to adapt. Harvard Business Review recently published research on a phenomenon called "workslop"—low-effort AI-generated work that appears professionally polished but shifts cognitive burden to recipients rather than solving problems.

The numbers are troubling. Fifty-three percent of surveyed employees admitted to sending substandard AI work to colleagues. Forty-one percent received unclear guidance on how to implement AI in their roles. The researchers locate the root cause in management failure: boards pressuring leadership to demonstrate AI ROI quickly, leading to vague directives like "use AI everywhere, every day." Employees receive mandates without training, producing polished-looking garbage that corrodes organizational trust.

The damage extends beyond wasted time. Engineers resign in frustration after receiving AI-generated responses to substantive technical questions. Researchers feel violated when colleagues outsource genuine intellectual engagement to algorithms. The social fabric that enables collaboration frays under the weight of delegated cognition.

Zvi Mowshowitz identifies a related risk he calls "hypomania"—getting caught in infinite loops of configuring and optimizing AI setups without producing actual work. The tool mastery displaces tool use. The configuration becomes the activity.

## The Governance Question

Against this backdrop of individual empowerment and organizational dysfunction, Dario Amodei's recent essay strikes a sobering note. The Anthropic CEO frames humanity's current moment as "the adolescence of technology," borrowing from Carl Sagan's question: "How did you evolve, how did you survive this technological adolescence without destroying yourself?"

Amodei identifies economic disruption as one of five critical risk categories, warning that AI could displace half of entry-level white-collar positions within one to five years—potentially outpacing labor market adaptation mechanisms. This is not the timeline of generational change. This is the timeline of a single business cycle.

The paradox is acute. The same tools that enable a single developer to ship like a team of five threaten to make four of those five developers redundant. The productivity gains are real and substantial. The distribution of those gains remains deeply uncertain.

Anthropic's response, articulated in Claude's new constitution, emphasizes understanding rather than rules. The document explains why Claude should behave in certain ways rather than merely specifying what it should do. Four foundational principles structure the framework: safety, ethics, guideline compliance, and genuine helpfulness—prioritized in that order for conflict resolution.

This principle-based approach, Mowshowitz observes, paradoxically enables more permissive agent behavior than competitors' rule-list guardrails. Unlike OpenAI or Google, Claude Code accepts tasks that blanket prohibitions would block. The nuanced judgment creates more usable systems precisely because it avoids crude filtering.

## Where Difficulty Lives Now

The central insight emerging from this collection of developments concerns where difficulty lives. Building software is becoming easier through AI tooling. The hard part has shifted upstream to knowing what you want built and selecting appropriate tools to achieve those goals.

At Every's Vibe Code Camp, 16 developers from Anthropic, Google, Notion, and other companies demonstrated applications ranging from iOS apps to autonomous product improvement loops. The event identified what is ending: manual typing as the primary development method, trial-and-error feature development, command-line interface dominance. The mechanical aspects of traditional software development that defined the profession for decades are becoming automated substrates.

What remains essential—what cannot yet be automated—is strategic planning, specification clarity, and architectural judgment. The developers who thrive in this environment are those who can articulate requirements precisely, review generated code critically, and maintain coherence across AI-produced outputs. Traditional coding ability becomes less valuable than the ability to direct work effectively.

This is not a small shift. It changes who can contribute to software development (designers now commit directly to repositories), how projects are structured (hierarchical agent architectures outperform flat coordination), and what constitutes professional competence (system thinking over syntax knowledge).

The 10% programmer is not a lesser version of the traditional developer. They are a different kind of professional entirely—one whose primary tools are clarity, judgment, and the ability to orchestrate capabilities they could never build alone. Whether this represents liberation or alienation depends on perspective. What it represents without question is transformation.

The machines are writing our code. The question is no longer whether this will happen, but what we become when it does.

---

## Sources

1. [I Stopped Reading Code. My Code Reviews Got Better.](https://every.to/source-code/i-stopped-reading-code-my-code-reviews-got-better)
2. [OpenAI to Add Shopping Cart and Merchant Tools to ChatGPT](https://www.testingcatalog.com/openai-to-add-shopping-cart-and-merchant-tools-to-chatgpt/)
3. [The Adolescence of Technology: Confronting and Overcoming the Risks of Powerful AI](https://www.darioamodei.com/essay/the-adolescence-of-technology)
4. [A Reflection on SEO, GEO & AI Search in 2025](https://lilyraynyc.substack.com/p/a-reflection-on-seo-and-ai-search)
5. [Scaling Long-Running Autonomous Coding](https://cursor.com/blog/scaling-agents)
6. [My AI Had Already Fixed the Code Before I Saw It](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it-f4a29a07-ea95-409f-bcb2-487a970bed4a)
7. [MCP is Not the Problem, It's your Server: Best Practices for Building MCP Servers](https://www.philschmid.de/mcp-best-practices)
8. [Claude Codes #3](https://thezvi.substack.com/p/claude-codes-3)
9. [Claude's New Constitution](https://www.anthropic.com/news/claude-new-constitution)
10. [What the Team Behind Cursor Knows About the Future of Code](https://every.to/source-code/what-the-team-behind-cursor-knows-about-the-future-of-code)
11. [Why People Create AI Workslop—and How to Stop It](https://hbr.org/2026/01/why-people-create-ai-workslop-and-how-to-stop-it)
12. [GitHub Copilot SDK](https://github.com/github/copilot-sdk)
13. [Advanced Claude Code and Cursor Techniques for Power Users](https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-advanced-claude)
14. [The Vibe Coders' Guide to What's Next](https://every.to/context-window/the-vibe-coders-guide-to-what-s-next)
15. [How I Use Claude Code to Ship Like a Team of Five](https://every.to/source-code/how-i-use-claude-code-to-ship-like-a-team-of-five-6f23f136-52ab-455f-a997-101c071613aa)
