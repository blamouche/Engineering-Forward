# Models.dev: An Open-Source Database of AI Models
**Source**: https://github.com/anomalyco/models.dev
**Date**: 2026-05-26
**Author**: AnomalyCo (OpenCode team)
**Keywords**: AI models database, open-source, AI SDK, model specifications, pricing, TOML, community-contributed

## Elevator pitch
Models.dev is a community-contributed open-source database of AI model specifications, pricing, and capabilities, built as TOML files organized by provider, with an API and AI SDK integration — a single source of truth for the fragmented AI model landscape.

## Takeaways
- A structured, machine-readable catalog of AI models with pricing, context windows, modalities, and capability flags (tool calling, reasoning, structured output, attachments).
- Data stored as TOML files organized by provider, with GitHub Action validation ensuring schema compliance — community contributions via PR welcome.
- Exposes a JSON API at models.dev/api.json and provider logos at models.dev/logos/{provider}.svg.
- Built by the team behind OpenCode.ai, using it internally; MIT licensed.
- Supports model inheritance via `extends` for wrapper providers, reducing duplication for mirrored models from first-party labs.

## Synthesis
Models.dev tackles a genuine pain point in the AI ecosystem: there is no canonical, up-to-date database of AI model specifications, pricing, and capabilities. Every provider publishes their own format, benchmarks vary wildly, and developers waste time hunting down model limits and costs. AnomalyCo's approach is pragmatic — a flat-file TOML repository that doubles as both a human-readable catalog and a machine-readable API.

The design is deliberately low-friction for contributors. Adding a model means creating a TOML file with structured fields: name, modalities (text, image, audio), cost per million tokens (input, output, reasoning, cache), context limits, capability flags (attachment, reasoning, tool_call, structured_output), and release dates. The GitHub Action validates submissions automatically, lowering the barrier for community contributions.

The `extends` mechanism is a clever piece of design. Instead of duplicating model definitions for wrapper providers (Cloudflare Workers AI mirroring Llama, for instance), contributors can point to a canonical model and only override what differs. This prevents the database from fragmenting as wrapper services proliferate.

The AI SDK integration — using model IDs as lookup keys — makes this immediately useful for developers building with Vercel's AI SDK. The API is dead simple: `curl https://models.dev/api.json` returns the entire database. Provider logos are served as SVGs with a consistent pattern.

The project is MIT licensed and actively maintained, with 90 open issues and 79 pull requests indicating a healthy community. It reflects a broader need in the AI tooling ecosystem: as the number of models explodes, infrastructure for discovery, comparison, and programmatic access becomes as important as the models themselves.
