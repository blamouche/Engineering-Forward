# Microsoft's quiet Claude Code retreat and the real cost of enterprise AI
**Source**: https://thenextweb.com/news/microsoft-claude-code-retreat-ai-cost
**Date**: May 25, 2026
**Author**: TNW (The Next Web)
**Keywords**: Microsoft, Claude Code, GitHub Copilot, token economics, enterprise AI, cost, agentic coding, Uber

## Elevator pitch
Microsoft is winding down its internal Claude Code experiment — not because the tool is bad, but because the unit economics of enterprise AI coding don't work at current token prices, as evidenced by Uber blowing its entire 2026 AI budget in four months.

## Takeaways
- Microsoft cancels most Claude Code licences in its Experiences and Devices group, mandating migration to GitHub Copilot CLI by June 30
- Uber's CTO burned through the entire 2026 AI coding budget in 4 months: engineers spending $500-$2,000/month each on tokens, 70% of code now AI-originated
- Nvidia VP Bryan Catanzaro says compute cost now far exceeds employee cost for his team
- Gartner: 25% of planned 2026 AI budget will slip to 2027; only 28% of AI infrastructure projects fully deliver against business case
- The era of "give every employee a Claude Code seat" is ending — what replaces it looks more like AWS billing than Office licences

## Synthesis
TNW reports that Microsoft is quietly winding down its internal Claude Code experiment, the most significant signal yet that the unit economics of enterprise AI coding are broken. In December 2025, Microsoft told thousands of engineers, product managers, and designers they could use Anthropic's Claude Code on the company dime. Six months later, the Experiences and Devices group — which builds Windows, Microsoft 365, Outlook, Teams, and Surface — is cancelling most direct Claude Code licences and mandating migration to GitHub Copilot CLI by June 30, the last day of Microsoft's fiscal year.

The official rationale is toolchain unification. The timing tells a different story. Microsoft is uniquely positioned to know what enterprise-scale Claude usage actually costs because its own engineers were the heaviest users outside Anthropic's customer base. If the maths had improved with scale, this would be the moment Microsoft locked in a multi-year deal. Instead, it's unwinding the experiment at fiscal year-end.

The Uber case crystallizes the problem. CTO Praveen Neppalli Naga told The Information that the company burned through its entire planned 2026 AI coding budget in four months. Claude Code adoption jumped from 32% to 84% of Uber's roughly 5,000-engineer organization. Individual engineers spent between $500 and $2,000 per month on tokens. Around 70% of committed code now originates with AI, and roughly one in ten live backend updates ships with no human in the loop. Naga's summary: "I'm back to the drawing board, because the budget I thought I would need is blown away already."

The structural issue is that agentic coding makes models think a lot — sessions run for hours, spawn parallel threads, and generate context volumes that bear no resemblance to autocomplete interactions. Nvidia VP Bryan Catanzaro confirmed that for his team, compute cost now far exceeds employee cost. A 2024 MIT analysis suggests AI automation pencils out as cheaper than human labour for only about a quarter of the jobs people thought it would replace at current pricing. Gartner now places generative AI in the "trough of disillusionment," predicting 25% of planned 2026 AI budgets will slip to 2027.

The implications go beyond a single vendor switch. The era of "give every employee a Claude Code seat" is closing. What replaces it will look more like AWS billing than Office licences: capped budgets per engineer, tiered access for high-leverage roles, agent runtime quotas. Token-level pricing will continue falling — roughly 10x every 18 months — but per-task token consumption rises with each generation of more capable, more reasoning-heavy models. The question is whether cost reduction outpaces consumption growth, and the evidence so far suggests it doesn't.
