# Perplexity Computer のご紹介
**Source**: https://www.perplexity.ai/ja/hub/blog/introducing-perplexity-computer
**Date**: 2026-02-25
**Author**: Perplexity Team
**Keywords**: Perplexity Computer, digital worker, subagents, tool orchestration, multi-model

## Elevator pitch
Perplexity Computer is positioned as a general-purpose digital worker that operates a real computer interface, decomposes work into subagents, and coordinates multiple models and tools to complete long-running tasks end to end.

## Takeaways
- The product frames itself as a “computer” for AI: a unified system that can browse, reason, and execute tasks.
- Tasks are decomposed into subagents that run asynchronously and can work for hours or days.
- The system emphasizes a real, isolated environment with filesystem access, browser control, and integrations.
- It is model-agnostic and can route to different frontier models depending on the subtask.
- Access is tied to a Max subscription with plans to expand to enterprise tiers.

## Synthesis
The Perplexity Computer announcement introduces a new product concept: a general-purpose digital worker that uses a real computer environment to execute tasks, rather than a narrow chatbot interface. The message is that AI should not just answer questions but operate like a human coworker who can open a browser, manage files, and perform multi-step work without constant supervision. Perplexity positions this as a shift from single-model chat toward a unified system that orchestrates multiple tools and models to complete end-to-end workflows.

A key idea is decomposition. Rather than treating a task as one monolithic request, Perplexity Computer splits the work into subagents that can run in parallel and asynchronously. This allows the system to handle long-running tasks, such as multi-hour research or complex operational workflows, without requiring a user to keep the session alive. The announcement emphasizes that these subagents can be coordinated by a central controller, which monitors progress, resolves dependencies, and synthesizes results. This is presented as a step toward more reliable “agentic” behavior where the system does not stall on intermediate steps.

The environment matters. Perplexity describes a real, isolated computer environment that mirrors the setup a human would use: a browser, a file system, and integrations with external tools. That isolation is meant to improve safety and traceability while still letting the agent work with realistic interfaces. Instead of abstract API calls alone, the system can interact with web pages, read and write files, and carry out tasks in a way that looks like a human operating a machine. This framing also suggests a focus on observability: you can see what the agent did and inspect the intermediate artifacts it produced.

Model orchestration is another pillar. Perplexity Computer is designed to route work to different models depending on the task. It highlights access to multiple frontier models, implying that some subagents may require strong reasoning, others multimodal capability, and others speed or cost efficiency. The system is therefore not tied to a single LLM but to a selection of models that can be combined. This multi-model approach is positioned as a practical response to the reality that no single model excels across every modality and constraint.

The announcement also speaks to the product packaging. Perplexity Computer is offered under a Max subscription, with an enterprise version planned, implying that Perplexity views this as a premium productivity product rather than a basic consumer feature. The emphasis on long-running tasks, background execution, and multi-tool orchestration suggests that the intended audience includes professionals who want to delegate substantial chunks of work. It also hints at future integrations, because long-lived agents become more useful as they can connect to more data sources and systems.

Overall, the announcement paints Perplexity Computer as an operating system layer for AI work: a system that combines an environment, a controller, and a model router into a single product experience. The core promise is not just better answers, but a more autonomous worker that can take a goal, break it down, and complete it with minimal supervision. If the system delivers, it represents a shift from “ask and answer” to “assign and execute,” which could broaden how AI is used in daily knowledge work.
