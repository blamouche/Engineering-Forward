# Mitchell Hashimoto’s new way of writing code
**Source**: https://newsletter.pragmaticengineer.com/p/mitchell-hashimoto
**Date**: 2026-02-26
**Author**: Unknown
**Keywords**: engineering workflow, open source, agents, version control, leadership

## Elevator pitch
In a podcast conversation, HashiCorp cofounder Mitchell Hashimoto describes how agents reshape his daily workflow—keeping an agent running for research and planning while he reviews—alongside reflections on open source trust, Git’s limits under agent churn, and pragmatic career advice.

## Takeaways
- A new personal operating rule: always have an agent running in the background (research, comparisons, edge cases) while you code/review.
- AI changes open source economics and trust: “default trust” shifts toward “default deny” as low-quality contributions scale.
- Git workflows may buckle under agent-generated churn (branch proliferation, merge queues, repo growth), hinting at a coming tooling shift.
- The story of Terraform/HashiCorp highlights execution (community + DX) over first-mover advantage.
- Practical adoption advice: start by delegating research to agents if you’re skeptical of AI writing production code.

## Synthesis
This episode summary captures how a highly pragmatic infrastructure builder is integrating AI agents into real work. Mitchell Hashimoto—best known for cofounding HashiCorp and creating widely used tools like Vagrant and Terraform—talks about the evolution of his workflow now that agents can take on meaningful “background cognition.” His core tactic is not “let the agent write everything,” but “keep the pipeline full”: if he’s implementing, an agent should be researching or planning; if an agent is implementing, he should be reviewing.

The idea is essentially throughput optimization via parallelism. Agents are treated like always-available assistants that can run library comparisons, enumerate edge cases, draft design options, or summarize relevant docs while the human focuses on judgment and integration. This reframing makes AI useful even to people uncomfortable with delegating code: research delegation is low-risk, high-leverage.

The conversation also surfaces systemic implications. Hashimoto argues open source has historically depended on trust, but AI makes it easy to generate plausible-looking yet wrong contributions at scale. That pushes projects toward more stringent review gates (“default deny”), changing how communities operate. Similarly, he questions whether Git and GitHub workflows will hold up when agents generate lots of small changes: merge queues, branches, and repository churn could become the bottleneck, implying a future “Gmail moment” for version control (archive-everything, never-delete, new interaction models).

The episode includes retrospective lessons from HashiCorp’s history—like Terraform winning despite not being first—and observations about building durable businesses around open-source tooling. But the throughline is operational: the main competitive advantage in the agentic era may be building a workflow that is continuously moving, continuously verified, and resilient to noise.

Overall, it reads as a pragmatic blueprint for adopting agents without surrendering engineering standards: use them to expand capacity, not replace judgment.