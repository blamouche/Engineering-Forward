# Choose Boring Technology and Innovative Practices
**Source**: https://buttondown.com/hillelwayne/archive/choose-boring-technology-and-innovative-practices/
**Date**: Unknown
**Author**: Hillel Wayne
**Keywords**: engineering strategy, maintenance, practices, tooling

## Elevator pitch
Hillel Wayne argues teams should be conservative in core technology choices while freely experimenting with processes and tools that are easy to abandon.

## Takeaways
- The true cost of technology is long‑term maintenance, not initial build speed.
- New tech creates unknown risks and permanent support burdens.
- Practices are easier to adopt and discard than core tech.
- “Material” systems (code, data, architecture) should be boring; tools can be innovative.
- Process innovation can be reversed without legacy costs.

## Synthesis
The essay builds on the “Choose Boring Technology” argument by separating the long‑term risk of tech choices from the relative flexibility of practices. Hillel Wayne highlights two core problems with choosing shiny, new tech: unknown failure modes and ongoing maintenance burdens. Even if a technology helps you ship faster at first, you pay for it over years in training, compatibility, and operational costs. Crucially, core infrastructure can’t simply be abandoned once deployed. If a team adopts a novel database or language, reversing that decision often means an expensive migration or a permanent need to keep expertise alive.

By contrast, practices—like a testing workflow or a commit policy—can be changed or dropped with comparatively little legacy burden. If a process stops working, teams can usually stop doing it without rewriting their system. That asymmetry suggests a principle: be conservative in technology choices but more experimental in operational practices. Wayne reframes “innovation tokens” accordingly: use few tokens for core technology, but feel free to spend more on process changes because the exit costs are lower.

The piece also introduces a distinction between “material” and “tools.” Material refers to the production system that must keep running—codebases, data stores, architectures, and the infrastructure that supports them. Tools are the ephemeral scaffolding used to build the material, such as editors or scripts. Because tools are easier to replace than material, teams can afford to be more innovative in tooling even when they avoid novel infrastructure.

The overall message is pragmatic rather than anti‑innovation. It encourages teams to experiment where reversibility is high and long‑term risk is low, while reserving conservatism for foundational technology decisions. This framing helps reconcile the desire to improve engineering practices with the reality that long‑term maintenance is the dominant cost in software.
