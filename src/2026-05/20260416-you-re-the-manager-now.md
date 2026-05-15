# You're the Manager Now
**Source**: https://every.to/context-window/you-re-the-manager-now
**Date**: April 16, 2026
**Author**: Laura Entis
**Keywords**: AI management, Claude Code, Mythos, developer tools, agent etiquette, confidence check, Dia browser, OpenClaw, framing

## Elevator pitch
As AI agents increasingly handle technical execution, knowledge workers must shift from doing the work to managing it — setting frames, evaluating confidence, and programming social norms into AI coworkers.

## Takeaways
- Claude Code's redesigned desktop app signals the shift from CLI-first to UI-centered agent supervision with parallel work management, git context, and build previews
- The "smaller models can match Mythos" debate is a framing issue: Mythos operates at a higher abstraction level, finding vulnerabilities autonomously without being pointed at code
- As models improve, the human role shifts from describing problems mechanically to defining which problems matter most ("frame climbing")
- A practical workflow: ask Claude Code for a confidence score (1-100) before shipping; send back anything under 90; ship at 90 without chasing diminishing returns
- Every built "Tact", an OpenClaw plugin that classifies whether agents should respond in Slack, programming social norms into AI coworkers
- Head of tech consulting Mike Taylor burned 2.2M Claude Code tokens in March; engineers running agentic workflows use significantly more

## Synthesis
This Context Window edition explores the transformation from "doing the work" to "managing the work" that AI agents are forcing across knowledge work. The piece opens with Claude Code's UI redesign, which signals a broader shift: the primary developer interface is no longer text-based command lines but visual dashboards for overseeing parallel agent work. CLI won't eat UI — the future is managing multiple agents, tracking git state, and previewing builds.

Dan Shipper contributes a sharp analysis on the "smaller models can do what Mythos does" discourse, reframing it through the concept of "frame climbing." When a cybersecurity researcher claimed smaller models found the same vulnerabilities as Mythos when pointed at code, it missed the point: Mythos autonomously discovered zero-days across every major OS and browser without guidance. Better models raise the abstraction level at which humans operate, from describing bugs to defining what problems are worth solving. The higher the frame, the more possible solutions emerge — and the harder it becomes to know what constitutes success.

Austin Tedesco's "confidence check" workflow is a practical implementation of this management mindset: before shipping, ask Claude Code to rate its confidence 1-100. Under 90, iterate. At 90, ship. This single question, from someone without an engineering background, has transformed the quality of his output — proving that managerial meta-skills increasingly outweigh domain expertise.

The piece also covers the social challenges of agent-infested workplaces. Every built "Tact," a classifier plugin that determines whether agents should speak up in Slack channels. Hard rules ("only respond in this channel") are brittle; Tact aims to program social norms the way humans learn them — through examples. It's a glimpse of the emerging field of agent etiquette engineering. A striking data point: Mike Taylor's 2.2 million monthly Claude Code tokens suggests agent usage is already comparable to traditional software licensing in cost and scale.
