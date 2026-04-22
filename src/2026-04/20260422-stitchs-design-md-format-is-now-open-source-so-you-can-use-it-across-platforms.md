# Stitch’s DESIGN.md format is now open-source so you can use it across platforms.
**Source**: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/
**Date**: Unknown
**Author**: Unknown
**Keywords**: Google, Stitch, DESIGN.md, design systems, AI agents

## Elevator pitch
Google is trying to turn design systems into a portable, machine-readable contract that AI tools can share across products instead of re-inferring visual intent every time.

## Takeaways
- Google is open-sourcing the draft DESIGN.md specification introduced in Stitch.
- The format is meant to carry reusable design rules across tools and projects.
- Google frames the file as a way for AI systems to understand the rationale behind a design system.
- Accessibility validation, including WCAG checks, is part of the intended machine-readable value.
- The broader bet is that design intent should become portable infrastructure for agentic tooling.

## Synthesis
Google’s decision to open-source the draft DESIGN.md format from Stitch may look small, but it points to an important shift in how AI-assisted design tools could evolve. The basic idea is straightforward: design rules should be exportable and reusable as structured files so that an AI system does not have to guess brand intent from scratch each time it generates a UI.

That matters because today’s design workflows are still full of implicit knowledge. Designers know what a given color token means, which typography choices are core to a brand, what spacing rules are acceptable, and where accessibility constraints become non-negotiable. AI systems often infer some of that from examples, but inference is brittle. A machine-readable format makes the rules explicit.

Google highlights exactly that value. In its description, DESIGN.md helps Stitch understand the reasoning behind a design system so it can generate interfaces that match a brand. Open-sourcing the draft spec is an attempt to let that structured language travel across platforms instead of remaining locked inside one product. If that works, it could become part of a broader interoperability layer for design-aware agents.

The accessibility angle is especially notable. Google says agents could use the format not only to know what a color is for, but also to validate choices against WCAG rules. That hints at a future where machine-readable design systems are not merely descriptive assets but active policy layers. An agent would not just imitate a brand system, it could check whether its generated UI stays within brand and accessibility constraints.

This also mirrors a broader trend in agent tooling. The most useful agent systems increasingly rely on externalized context, files, schemas, manifests, and policies, rather than hoping the model infers everything from a prompt. DESIGN.md fits that pattern. It turns tacit design knowledge into a durable artifact that can be referenced, versioned, and reused.

The draft nature of the specification means it is still early, and standards only matter if multiple tools adopt them. But the direction is compelling. As UI generation becomes more common, the bottleneck shifts from raw generation ability to controllability and consistency. A shared design-rules format could become part of the missing infrastructure that makes generated interfaces feel intentional rather than approximate.

In that sense, Google is not just open-sourcing a file format. It is making a case that the future of AI design tooling depends on portable, explicit representations of visual intent. That feels like a sensible and potentially important move.
