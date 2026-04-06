# How Al Chen Uses Claude Code and 15 Repos to Answer Any Customer Question

**Source**: https://www.chatprd.ai/how-i-ai/claude-code-and-repos-to-answer-any-customer-question
**Date**: April 6, 2026
**Author**: Claire Vo / chatPRD
**Keywords**: Claude Code, customer support, multi-repo search, Confluence, Slack, field engineering, knowledge base

## Elevator pitch
Al Chen’s workflow turns a 15-repo codebase into a customer-support engine by combining Claude Code, Confluence, and customer-specific notes to answer nuanced enterprise questions without depending on engineering interrupts.

## Takeaways
- Opening all repos in one workspace lets Claude Code reason across service boundaries.
- A simple generated script keeps every local repo on the latest main branch.
- Custom commands blend Confluence, code, and customer-specific deployment constraints into one answer.
- Pylon helps convert valuable Slack threads into public knowledge-base articles.
- The workflow turns customer support from reactive pinging into a compounding knowledge system.

## Synthesis
This piece is one of the better examples of AI creating leverage outside pure engineering. Al Chen is using Claude Code not to write product code directly, but to understand a complex platform deeply enough to support enterprise customers without constantly escalating to developers. That changes the economics of customer-facing technical work.

The core insight is that official documentation is often too abstract for real deployment questions. Enterprise customers need answers grounded in how services actually behave together. By pulling 15 repos into a single workspace and letting Claude Code search across them, Al effectively gives himself a live, queryable implementation map of the company’s product.

The workflow gets even stronger when it adds customer-specific context. The “quirks” page prevents answers from collapsing into generic best practices by injecting the local reality of each deployment environment—secrets management, air gaps, naming conventions, security rules. That is exactly the sort of context AI systems need to feel genuinely useful.

The second workflow—turning Slack threads into KB articles—shows how support knowledge can compound instead of vanishing into message history. Together, the two systems turn code plus conversations into a growing service advantage. That is a strong template for any technical company with complex products and overloaded engineers.
