# AI economics
**Source**: https://sriramkrishnan.substack.com/p/ai-economics
**Date**: 2026-05-11
**Author**: Sriram Krishnan
**Keywords**: AI economics, OpenAI, Anthropic, xAI, Meta, Google, Microsoft, Amazon, GPU infrastructure, token economics, inference costs, training costs, cloud providers, AI business models

## Elevator pitch
Each major AI lab faces a structurally different economic challenge—OpenAI struggles with low-revenue consumer usage mix, Anthropic with GPU supply constraints, and xAI with massive capacity but zero demand—while the fundamental question of who will fund the next training cluster remains unanswered for every lab.

## Takeaways
- OpenAI's 900M monthly active users create a usage mix problem: high consumer volume means low revenue per token and compounding inference costs from free/low-value prompts
- Anthropic's enterprise-heavy base (300K+ businesses, 1,000+ spending over $1M/year) gives great revenue per token but creates a persistent GPU supply shortage and constant rate-limiting
- xAI built massive GPU supply through Colossus but has no model utilization—leading to the Cursor partnership/acquisition and leasing Colossus capacity to Anthropic
- Meta's open-source Llama strategy is an economic weapon: one-time training cost with zero ongoing inference cost, designed to pressure competitors' pricing downward
- The core metrics that determine AI lab viability are tokens per watt-year (supply efficiency), revenue per token (demand quality), and revenue per watt-year (the single number that determines self-funding capability)

## Synthesis
Sriram Krishnan's analysis of AI industry economics provides a clear, deconstructed framework for understanding the radically different business positions of each major AI player. His central insight is that despite surface similarities—everyone is building large models and competing for users—each lab's economic structure creates fundamentally different strategic problems and constraints.

OpenAI's 900 million monthly active users, predominantly consumers, create what Krishnan terms a "usage mix problem." High volumes of free and low-value prompts generate low revenue per token while consuming massive inference compute. Every ChatGPT query that could have been a Google search represents both a cost center for OpenAI and a lost ad impression for Google. This structural dynamic—high volume, low yield—shapes everything from OpenAI's pricing strategy to its infrastructure planning.

Anthropic sits at the opposite pole. With 300,000 business customers and over 1,000 enterprises spending more than $1 million annually, Anthropic enjoys excellent revenue-per-token economics and predictable usage patterns. But this same enterprise concentration creates a GPU supply problem: demand consistently exceeds capacity, resulting in the constant rate-limiting that frustrates developers. Anthropic's need for more GPUs was made concrete by its deal to lease capacity from xAI's Colossus infrastructure.

xAI represents the most precarious position: massive GPU supply via the Colossus supercomputing cluster but effectively zero model utilization. This explains the aggressive moves toward acquiring Cursor (to generate developer demand) and leasing excess capacity to competitors like Anthropic. It's a vivid illustration that infrastructure without demand is just expensive idle hardware.

The platform companies play different games entirely. Google owns the full stack—TPUs, data centers, cloud, and applications—giving it the lowest AI cost structure, but every query deflected to ChatGPT or Claude is a lost ad impression. Meta uses its GPU investment for internal ad optimization and deploys open-source Llama as an economic pressure tactic: if Llama is 60-90% as good as proprietary models at zero inference cost, it forces competitors to lower prices. Microsoft and Amazon operate as cloud infrastructure providers, invested in both OpenAI and Anthropic with multi-billion dollar cloud deals that ensure they profit regardless of who wins the model race.

The core economic framework boils down to two metrics: tokens per watt-year (how efficiently you convert infrastructure into output) and revenue per token (how much you earn from that output). Their product—revenue per watt-year—determines whether a lab can self-fund its next training cluster or must return to outside capital. Krishnan's sobering conclusion: no major AI lab has yet crossed the self-funding threshold, making the question of who funds the next generation of compute one of the industry's most consequential unanswered questions.
