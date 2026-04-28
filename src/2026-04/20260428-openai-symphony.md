# openai/symphony
**Source**: https://github.com/openai/symphony
**Date**: April 28, 2026
**Author**: OpenAI
**Keywords**: agent orchestration, coding agents, Linear, CI, autonomous implementation

## Elevator pitch
Symphony presents a model for turning backlog items into isolated autonomous implementation runs, shifting engineers from supervising coding agents directly to governing work, evidence, and merge decisions.

## Takeaways
- Symphony watches a project board and spawns isolated agents to complete implementation tasks.
- The system emphasizes proof of work, including CI status, PR feedback, complexity analysis, and walkthrough artifacts.
- OpenAI frames it as a natural extension of harness engineering rather than a standalone coding assistant.
- The project is positioned as an engineering preview intended for trusted environments.
- The core idea is organizational: move humans up a level from micromanaging agents to managing workflows and acceptance criteria.

## Synthesis
Symphony is interesting because it pushes the current coding-agent conversation one step up the stack. Most coding tools still assume the human is the direct dispatcher, reviewer, and traffic controller for each agent run. Symphony proposes a different abstraction. Work originates in a project system, gets executed in isolated runs, returns with evidence, and only then moves back into the human approval path. The promise is not just more automation. It is less supervisory overhead.

That distinction matters. Coding agents have become capable enough that the main bottleneck is often not code generation itself but the coordination layer around it. Someone has to decide what task is in scope, what environment it should run in, how progress is validated, and what evidence is sufficient before something can merge. Symphony packages those concerns into an orchestration model where task systems such as Linear become the control plane and agents become implementation workers inside a governed pipeline.

The proof-of-work concept is central to the pitch. OpenAI is implicitly acknowledging that autonomous implementation is only useful when it produces artifacts humans and systems can trust. CI results, review comments, complexity analysis, and walkthroughs are not decorative extras. They are the substrate of delegation. If an engineer cannot understand what happened and why the system believes a change is safe, the autonomy gains collapse back into manual babysitting.

The reference to harness engineering is also revealing. OpenAI is arguing that agent performance depends heavily on the surrounding structure, not just the model. Good prompts, isolated environments, deterministic checks, and explicit acceptance logic matter as much as raw coding capability. Symphony turns that idea into a project operating model. It treats the agent as one component in a larger execution harness rather than as a magical employee replacement.

In practical terms, Symphony hints at where engineering management may be heading. Teams may increasingly define work as machine-executable tickets backed by validation rules, with humans focusing on prioritization, risk, architecture, and approval. That is a meaningful shift from using agents as faster autocomplete. Symphony’s significance is that it tries to operationalize that shift in a way that fits existing software delivery systems.