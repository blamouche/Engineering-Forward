# Securing an Always-On AI Employee
**Source**: https://every.to/how-to-secure-an-ai-employee
**Date**: August 14, 2026
**Author**: Nityesh Agarwal
**Keywords**: AI agents, security, prompt injection, least privilege, observability

## Elevator pitch
Every's framework treats an always-on agent as an employee with a constrained identity, enforced permissions, clear behavioral rules, and auditable activity.

## Takeaways
- The principal threats are supply-chain compromise, prompt injection, and accidental disclosure.
- A dedicated agent identity reduces the blast radius of failures.
- High-risk actions need programmatic controls that a model cannot override.
- Prompt instructions remain useful for nuanced routing decisions, but are not a security boundary.
- Complete session and tool logging makes containment and improvement possible.

## Synthesis
The guide is valuable because it starts from a realistic premise: a useful, persistent agent may have email, files, browser sessions, code execution, and several human requesters. Those capabilities make it materially different from a chat assistant. The authors classify the risks into malicious dependencies, instructions embedded in external content, and ordinary but harmful sharing across different access levels. Each can lead to a failure even without a sophisticated adversary.

Their response is a layered model. Least access comes first: the agent uses its own accounts and receives only the data necessary for a job. Programmatic controls come next, including sandboxing, tool hooks, command validation, and explicit blocks on consequential actions such as outbound email. Prompt rules define more contextual policies, such as ring-based access and safe handling of uncertain requests. Finally, observability captures sessions, tool calls, installations, and the reasoning trail needed to investigate incidents.

The ordering matters. A prompt that says not to exfiltrate information is not a substitute for an unbypassable denial of the relevant tool. Conversely, code-level permissions cannot encode every interpersonal or organizational nuance. The guide recommends choosing high-stakes actions, then auditing each through all four layers. That turns security from a generic policy document into a capability-by-capability engineering exercise. The remaining tension is utility: constraints intentionally remove some automation value, but they make the residual capability a defensible system rather than a hopeful demo.
