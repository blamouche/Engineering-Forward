# The Agent Stack Bet

**Source**: https://addyo.substack.com/p/the-agent-stack-bet
**Date**: Unknown
**Author**: Unknown
**Keywords**: agent infrastructure, identity, governance, context, orchestration

## Elevator pitch
This essay argues that the hard problems in production agents are no longer model quality but identity, governance, context, and durable execution, and that teams should treat the agent stack as shared infrastructure instead of rebuilding it piecemeal.

## Takeaways
- The piece frames current agent deployments as fragile systems with too much autonomy and too little policy, observability, and traceability.
- Agent identity is presented as the missing primitive because prompt-level promises cannot replace platform-level access control and auditable permissions.
- Universal, cross-system context is described as the ceiling-lifting requirement for agents that need to act across real business workflows.
- Durable execution matters less as session persistence and more as mission persistence across approvals, handoffs, credential rotations, and long-running work.
- The recommendation is to stop spending engineering effort on commodity plumbing and instead build on open, production-ready agent foundations.

## Synthesis
This essay is really an infrastructure argument disguised as an opinion piece about agents. Its central claim is that most of the failure modes teams encounter in production are no longer primarily about prompting or raw model intelligence. They come from the surrounding system: shaky identity boundaries, brittle context management, weak governance, and execution models that collapse when a task lasts longer than a single session. In that framing, the “agent problem” has become a platform problem.

The strongest part of the piece is its description of governance debt. Many teams still run agents through shared service accounts, inherited human credentials, or thin middleware checks that are supposed to constrain behavior after the fact. That works until an agent crosses a boundary it should not cross, touches sensitive data, or performs an action no one can cleanly attribute. The essay argues that agent identity needs to be embedded lower in the platform, so permissions are enforced at the same level as any other machine actor. That is a useful distinction because it moves governance from an aspirational prompt contract to an enforceable systems primitive.

The second argument concerns context. Today, a lot of agent work still depends on custom session stores, brittle serialization, and narrow windows into a single application surface. That prevents agents from operating across the systems where real companies keep state, from CRMs to data warehouses to ticketing systems. The essay’s call for “universal context” is essentially a call for better cross-system integration and durable memory. Without that, agents remain limited to shallow task automation rather than the longer, messier workflows enterprises actually care about.

The third major point is that durability needs to be defined at the mission level, not the session level. An agent that survives a disconnect is useful, but enterprises need agents that can survive days of work, approval gates, model changes, and handoffs between people or systems. That means checkpointing, long-horizon memory, auditable trails, and explicit human-in-the-loop pauses. The piece is persuasive here because it reflects where many real deployments break down. The ambition of agentic software increasingly exceeds the lifespan and governance assumptions of the containers it runs inside.

There is also a product strategy argument tucked underneath the technical one. The author suggests that teams should stop spending their scarce engineering effort on undifferentiated plumbing, from custom memory layers to homemade tracing and retry systems. Instead, they should build on shared open primitives and focus on domain reasoning, policy, and business logic. That mirrors earlier infrastructure cycles in cloud, containers, and CI/CD, where the winners were often the teams that stopped hand-rolling everything and moved up the stack.

Overall, the essay captures an important shift in how serious teams think about agents. The frontier is no longer just “can the model do the task?” but “can the surrounding system make the task trustworthy, durable, and governable?” That is a more mature framing of the market. It also implies that the durable winners in agent software may be determined as much by their infrastructure layer as by their model layer.
