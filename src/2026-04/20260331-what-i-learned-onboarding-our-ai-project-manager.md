# What I Learned Onboarding Our AI Project Manager

**Source**: https://every.to/p/what-i-learned-onboarding-our-ai-project-manager
**Date**: March 31, 2026
**Author**: Nityesh Agarwal
**Keywords**: AI project manager, Claudie, subagents, context windows, handbooks, agent management

## Elevator pitch
Every’s experience training an AI project manager shows that reliable agents depend less on raw model power than on architecture, clear role definition, source access, and explicit operating handbooks.

## Takeaways
- The team had to define Claudie’s job precisely before expecting reliable output.
- Passing summaries between subagents caused failures; routing raw data through shared local files improved reliability.
- Agents need a living handbook that they are forced to read on startup to stay aligned with role expectations.
- Agent performance improved as the team treated failures as design flaws rather than proof the model could not do the work.
- Once reliability was established, responsibility could expand gradually just like a human employee’s scope would.

## Synthesis
This article is one of the better operational accounts of what it actually takes to make an agent useful inside a team. The core lesson is simple: if an AI employee is unreliable, the problem is often not the model’s top-line intelligence but the structure around it. Nityesh Agarwal describes how Every repeatedly rebuilt “Claudie,” an AI project manager, until the team understood the real sources of failure. That process mirrors classic management more than it resembles prompt tinkering. Define the role, map the information dependencies, observe failure modes, and redesign the system.

The breakthrough around context windows is especially instructive. Claudie initially relied on subagents that summarized data back to an orchestration layer. That looked elegant but introduced information loss precisely where fidelity mattered. By shifting the architecture so data-gathering agents wrote raw material into local files, the orchestration agent could direct work without compressing evidence into summaries. The design principle is broader than this specific case: agents often perform better when coordination preserves access to primary data rather than forcing each handoff through an LLM abstraction layer.

The employee handbook point is equally strong. Human workers can interpolate from partial context, ask clarifying questions, and learn socially. Agents cannot be trusted to do that consistently. Giving Claudie a handbook—and forcing her to read it at startup—turns tacit organizational knowledge into explicit runtime context. That is a practical pattern for any team deploying agents: codify success criteria, escalation rules, team structure, and process expectations as if you were onboarding a new colleague who forgets everything between sessions.

What emerges is a management philosophy for AI coworkers. Diagnose before blaming. Upgrade responsibilities only after proving reliability. Build systems that make the right behavior easy. The article’s title is about one project manager, but the real subject is the shift from using AI as a tool to integrating it as a governed participant in team operations.
