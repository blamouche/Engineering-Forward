# The AI engineering stack we built internally — on the platform we ship

**Source**: https://blog.cloudflare.com/internal-ai-engineering-stack
**Date**: 2026-04-20
**Author**: Unknown
**Keywords**: Cloudflare, AI Gateway, Workers AI, internal tooling, MCP, developer productivity

## Elevator pitch
Cloudflare details how it used its own AI platform to build an internal engineering stack that now supports widespread coding-tool adoption, large token volumes, and measurable gains in merge-request throughput across the company.

## Takeaways
- Cloudflare says 93% of its R&D organization now uses internal AI coding tools built on the same platform the company sells externally.
- The stack combines internal MCP servers, access controls, AI Gateway, Workers AI, and supporting tooling to make agents safe and usable for employees.
- The company reports 20 million requests routed through AI Gateway and 241 billion tokens processed, indicating production-scale internal adoption.
- Cloudflare ties the rollout to a sharp rise in merge requests, suggesting AI assistance is materially improving engineering throughput.
- The post doubles as a product signal: Cloudflare wants customers to see its own internal usage as proof that the platform is mature enough for enterprise AI operations.

## Synthesis
Cloudflare’s post is both an internal case study and an external product argument. The company says it spent the last eleven months building an AI engineering stack for its own teams using the same infrastructure it ships to customers. That framing is important because it positions Cloudflare as its own reference deployment. Rather than describing a generic vision for AI-enabled development, the post claims the company is already running a large internal system with meaningful adoption and measurable output.

The numbers are the headline. Cloudflare says 3,683 internal users are actively using AI coding tools, representing around 60% of the company and 93% of R&D. It also reports 20 million requests through AI Gateway and 241 billion tokens processed. Whether or not each metric maps directly to productivity, they show that the tooling is no longer experimental. This is industrialized internal AI infrastructure, with routing, observability, access controls, and inference all treated as a core engineering platform rather than a collection of one-off tools.

A notable part of the story is the emphasis on plumbing. Cloudflare highlights internal MCP servers, an access layer, and governance pieces required to make agents genuinely useful inside a company. That matters because many organizations discover that model access alone is not enough. The hard part is connecting models to internal systems safely, controlling permissions, handling traffic, and making the whole thing reliable enough for day-to-day work. Cloudflare is effectively arguing that it solved these integration problems on its own stack.

The productivity claim is also striking. The company says merge-request volume increased sharply as adoption grew, reaching levels well above prior baselines. That does not automatically prove quality improved, but it does suggest AI tooling is changing the speed and amount of engineering output. For Cloudflare, this supports a broader narrative that AI coding tools are becoming a standard part of software development, and that the winning infrastructure providers will be the ones that can support both experimentation and scaled internal operations.

Overall, the article shows Cloudflare trying to turn internal dogfooding into market leverage. If customers believe the company genuinely runs its own AI workflows on AI Gateway, Workers AI, and related services, the platform becomes easier to trust. The deeper takeaway is that enterprise AI adoption increasingly depends on operational stack design, not just model quality, and Cloudflare wants to be seen as a serious contender for that layer.
