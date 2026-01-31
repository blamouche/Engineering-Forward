# I Replaced a $120/Year Micro-SaaS in 20 Minutes with LLM-Generated Code

**Source**: https://blog.pragmaticengineer.com/i-replaced-a-120-year-micro-saas-in-20-minutes-with-llm-generated-code/

**Date**: January 29, 2026

**Author**: Gergely Orosz

**Keywords**: SaaS, LLM, code generation, AI tools, micro-SaaS, software replacement, developer productivity, Claude

## Elevator pitch

A tech newsletter author replaced a $120/year testimonials service in 20 minutes using LLM-generated code, illustrating how unmaintained SaaS products are increasingly vulnerable to DIY replacement.

## Takeaways

- Static, maintenance-free SaaS products are most vulnerable to LLM-generated replacement
- The replacement was feasible because developers are comfortable with command-line interfaces and can verify LLM outputs
- Non-developers face steeper learning curves for similar tasks, limiting the immediate threat to enterprise SaaS
- SaaS products offering ongoing compliance updates, real-time analytics, and continuous value remain difficult to replicate
- Deteriorating customer service combined with stagnant features accelerates customer departure to DIY solutions

## Synthesis

Gergely Orosz, author of The Pragmatic Engineer newsletter, documents his experience replacing Shoutout.io, a testimonials display service he had paid $120 annually for, with a custom solution built using Claude's Codex in just 20 minutes. The article serves as both a practical tutorial and a broader commentary on the changing economics of micro-SaaS businesses.

The catalyst for the switch was not purely economic. The service had not received feature updates in four years, and its billing system had been broken for three years. When Orosz attempted to retrieve invoices for accounting purposes, he encountered broken links and inadequate customer support responses. The combination of neglect and poor service drove him to explore alternatives.

The replacement solution was straightforward for someone with development experience. Orosz used an LLM to create a modular JSON-based system for storing testimonials, with a compile-time build step that generates static HTML. The resulting code deploys through his existing GitHub repository and Netlify infrastructure. The entire process, from frustrated customer to working replacement, took less than half an hour.

Orosz is careful to note that this experience does not generalize to all SaaS replacement. The task was manageable specifically because developers are comfortable working at the command line and can verify that LLM-generated code actually works. Non-developers attempting similar replacements would face substantially steeper learning curves, even with the same AI tools available.

The article distinguishes between SaaS products that are vulnerable to this kind of replacement and those that are not. Static, write-once products that provide a fixed set of features without ongoing updates are most at risk. In contrast, services that provide ongoing compliance updates, real-time analytics, or continuous value through regular improvements remain difficult to replicate with LLMs. The value proposition of such services extends beyond the initial code.

The broader implication is troubling for a certain category of software business. Products that follow a "write-once, never-update" model have long relied on customer inertia and switching costs to maintain subscriptions. When AI tools make it trivial for technical users to build replacements for their specific use cases, that inertia evaporates. Poor customer service, which might once have been tolerated, becomes the final push toward departure.

Orosz stops short of declaring micro-SaaS dead. Entire platforms remain complex to rebuild, and most users lack the technical skills to leverage LLMs effectively. But the margin for error has narrowed. Products that stop evolving and stop caring about their customers now face competition from AI-assisted DIY solutions in ways they did not just a few years ago.
