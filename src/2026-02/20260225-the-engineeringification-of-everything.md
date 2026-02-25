# The engineeringification of everything
**Source**: https://newsletter.posthog.com/p/the-engineeringification-of-everything
**Date**: 2026-02-25
**Author**: Ian Vanagas
**Keywords**: engineering culture, tooling, identity, AI assistants, GTM engineering

## Elevator pitch
As tools and AI assistants make complex systems accessible, more roles adopt engineering methods and titles—creating a reinforcing loop where skills, identity, and tooling co-evolve.

## Takeaways
- “Engineeringification” describes engineering tools/mindsets spreading beyond software roles (design, sales, marketing, ops).
- A feedback loop drives it: tools get more powerful → usage gets complex → non-engineers learn → identity shifts → new tools/marketing appear.
- LLMs accelerate the loop by lowering learning barriers and enabling non-engineers to automate, prototype, and build.
- Titles and boundaries blur: “engineer” becomes more about building and shipping than formal training or gatekeeping.
- Winners, regardless of role, adopt a builder mindset; companies can support this by offering APIs, machine-readable docs, and integration points.

## Synthesis
This piece argues that “engineering” has escaped the codebase: the tools, techniques, and identity associated with software engineering increasingly shape work across an organization. The author calls this trend the “engineeringification of everything” and points to emerging labels like design engineer, GTM engineering, and sales engineer as signals that building, automating, and shipping are no longer confined to traditional engineering teams.

The proposed mechanism is a reinforcing loop. First, tools in a domain become more powerful and closer to production outcomes—design tools influence real UI components; GTM tools increasingly program workflows; analytics and experimentation systems expose powerful configuration surfaces. Second, power brings complexity: to use these tools effectively, practitioners must learn systems thinking, constraints, and sometimes code. Third, because specialist engineering time is scarce and iteration speed matters, non-engineers learn enough to unblock themselves. AI accelerates this step by acting as a tutor and a translator: generating Tailwind components, wiring automations, producing prototypes, and helping users navigate complex configuration.

As people accumulate these capabilities, the nature of their work changes. They are no longer merely handing off artifacts to engineers; they are implementing, debugging, and making trade-offs between correctness, performance, and user experience. At that point, identity shifts: calling the work “just design” or “just marketing” undersells what’s happening. New titles crystallize that identity, and the market responds—companies hire for it, tools market to it, and the loop repeats with clearer segmentation and stronger incentives.

The essay also addresses the tension around the word “engineer.” In some jurisdictions it’s regulated; culturally it has implied a bounded body of knowledge reinforced by gatekeeping. Software’s relatively low cost of failure has already weakened those boundaries, and AI-driven tooling weakens them further. The boundary moves from “who is allowed” toward “who can and will build,” emphasizing practice and output over credentials.

The conclusion is pragmatic. The technical/non-technical line isn’t disappearing; it’s being redrawn. Individuals should lean into being builders, and organizations can enable this by providing APIs, machine-readable documentation, and integration points (including MCP servers) so that empowered practitioners—helped by LLMs—can safely extend systems without constant engineering mediation.