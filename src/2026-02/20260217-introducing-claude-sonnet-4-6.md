# Introducing Claude Sonnet 4.6
**Source**: https://www.anthropic.com/news/claude-sonnet-4-6
**Date**: 2026-02-17
**Author**: Anthropic
**Keywords**: ai, model, claude

## Elevator pitch
Anthropic announces Claude Sonnet 4.6, highlighting major upgrades in coding, computer use, long-context reasoning, and safety at unchanged pricing.

## Takeaways
- Sonnet 4.6 is a full capability upgrade with a 1M-token context window in beta.
- It becomes the default model for Free/Pro users and keeps Sonnet 4.5 pricing.
- Computer-use performance improves materially on OSWorld and real tasks.
- Safety evaluations show strong behavior and improved resistance to prompt injection.
- Claude Code and developer-platform tools see better instruction following and workflow support.

## Synthesis
Anthropic introduces Claude Sonnet 4.6 as the most capable Sonnet model to date, positioning it as a broad upgrade across coding, computer use, long-context reasoning, agent planning, knowledge work, and design. The model ships with a 1M-token context window in beta and becomes the default model for Free and Pro users on claude.ai and Claude Cowork. Pricing remains unchanged relative to Sonnet 4.5, starting at $3/$15 per million tokens on the API, signaling a push to deliver higher capability without a cost increase for users.

On coding tasks, Anthropic reports that early-access developers prefer Sonnet 4.6 to Sonnet 4.5 by a wide margin, and even to Opus 4.5 in many cases. Users cite improved consistency, better instruction following, fewer hallucinations, and fewer false claims of success. The model is described as less prone to overengineering and “laziness,” with better follow-through on multi-step tasks. These traits are particularly relevant for long-lived coding sessions where earlier models would drift or duplicate logic. Anthropic also claims that Sonnet 4.6 now delivers performance that previously required an Opus-class model on economically meaningful office tasks.

A major focus of the release is computer use—models that interact with software via a simulated screen, mouse, and keyboard rather than APIs. Anthropic notes that many organizations still rely on legacy or specialized tools that are hard to automate via standard interfaces. A model that can use a computer like a human reduces the need for bespoke connectors. The company points to OSWorld, a benchmark that simulates tasks across real applications such as Chrome, LibreOffice, and VS Code, to show steady gains in Sonnet performance over sixteen months. Early users report human-level capability in tasks like navigating complex spreadsheets and multi-step web forms, though Anthropic acknowledges the model still trails expert humans.

The release also addresses safety. Anthropic says it ran extensive evaluations and found Sonnet 4.6 as safe as, or safer than, other recent Claude models. The safety team describes the model’s behavior as warm, honest, prosocial, and robust against high-stakes misalignment. In the context of computer use, the company highlights prompt injection as a concrete risk—malicious instructions hidden in web content that can hijack a model’s behavior. Anthropic claims Sonnet 4.6 shows significant improvement in resistance to prompt injection relative to Sonnet 4.5, and performs similarly to Opus 4.6 on this dimension.

The long-context window is presented as more than a raw capacity increase. Anthropic emphasizes that Sonnet 4.6 can reason effectively across large context, enabling longer-horizon planning. It cites the Vending-Bench Arena evaluation—simulated business management with competitive dynamics—where Sonnet 4.6 used a strategy of heavy early investment followed by a pivot to profitability, outperforming competitors. This serves as evidence of improved multi-step planning over long contexts.

Developer tooling also receives upgrades. On the Claude Developer Platform, Sonnet 4.6 supports adaptive and extended thinking and introduces context compaction in beta to summarize older conversation segments and extend effective context. On the API, web search and fetch tools can automatically write and execute code to filter results, improving relevance and token efficiency. Additional capabilities such as code execution, memory, programmatic tool calling, and tool search are noted as generally available.

Anthropic frames Sonnet 4.6 as a model that approaches Opus-level intelligence at a more accessible price, while still positioning Opus 4.6 as the preferred option for tasks that demand the deepest reasoning or high-stakes correctness, such as large-scale refactoring or multi-agent workflows. The overall message is a shift of high-end capability into a cheaper, default tier, with safety and tooling improvements designed to support broader adoption.
