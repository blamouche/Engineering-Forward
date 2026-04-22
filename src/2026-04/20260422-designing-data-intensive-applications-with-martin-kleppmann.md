# Designing Data-intensive Applications with Martin Kleppmann
**Source**: https://newsletter.pragmaticengineer.com/p/designing-data-intensive-applications
**Date**: April 22, 2026
**Author**: Gergely Orosz
**Keywords**: distributed systems, data infrastructure, cloud architecture, formal verification, local-first software

## Elevator pitch
A conversation with Martin Kleppmann on why engineers need distributed-systems intuition to reason about tradeoffs in modern data infrastructure, cloud scaling, and AI-era software reliability.

## Takeaways
- Kafka and LinkedIn’s data systems helped shape the mental model behind Designing Data-Intensive Applications.
- The book was written to give application engineers stronger foundations for design and debugging decisions, not just database specialists.
- Multi-region and multi-cloud choices are business tradeoffs between risk and cost, not universal best practices.
- Cloud platforms have reduced the need for manual sharding for many teams, while replication for fault tolerance remains broadly relevant.
- Martin sees formal verification becoming more practical as LLMs increase code volume and improve at writing proofs.

## Synthesis
This Pragmatic Engineer interview revisits the ideas behind Designing Data-Intensive Applications through Martin Kleppmann’s career across startups, LinkedIn, and academia. The discussion frames the book less as a manual for database specialists and more as a way for application engineers to build intuition about system behavior, failure modes, and design tradeoffs. Kleppmann explains that the motivation for writing the book came from painful early startup experience, when his team faced database bottlenecks without a strong conceptual foundation for choosing among unfamiliar technologies. The goal of the book was to make those concepts legible before engineers are forced to learn them under production pressure.

A recurring theme is that architecture decisions are rarely about a single technically correct answer. Instead, engineers need language for describing tradeoffs clearly to the business. Kleppmann uses decisions such as multi-region or multi-cloud deployment to illustrate this. These are not default best practices, but risk and cost choices that depend on how much resilience a company needs and what it can afford. In the same spirit, the interview highlights how the cloud has changed scaling assumptions. Teams still need to understand scaling, but the dominant problems have shifted. For many workloads, larger machines and managed infrastructure mean manual sharding is less central than it once was, while replication and fault tolerance still matter at almost every scale.

The conversation also surfaces how distributed systems theory can feel extreme because it assumes worst cases around clocks, networks, and failures. Kleppmann argues this pessimism is useful precisely because production systems do eventually hit edge cases. That mindset extends to ethics and governance: engineers are responsible not only for technical tradeoffs, but also for surfacing reputational and societal risks so decision-makers can act with better information. This is part of a broader view of engineering as disciplined risk communication, not just implementation.

The forward-looking section is especially relevant to current software practice. Kleppmann notes that formal verification has historically been too expensive for routine industry use, but the economics may change if LLMs generate much more code while also becoming capable of drafting proofs. He also points to local-first software as an area full of unsolved engineering challenges, particularly around decentralized access control and conflict resolution. Overall, the interview is a concise argument for why distributed-systems literacy still matters: not because every engineer will build infrastructure primitives, but because modern software work increasingly depends on understanding the reliability, scalability, and coordination properties of the systems underneath the application layer.
