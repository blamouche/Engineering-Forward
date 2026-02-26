# Agents are not thinking, they are searching
**Source**: https://technoyoda.github.io/agent-search.html
**Date**: 2026-02-22
**Author**: Unknown
**Keywords**: AI agents, reinforcement learning, reward hacking, tool environments, verification

## Elevator pitch
This essay argues that modern “agents” behave less like thinkers and more like search policies optimized for reward—so to get reliable outcomes you should engineer the environment, verifiers, and constraints that make the search converge.

## Takeaways
- A useful mental model: agents are policies trained via pretraining + RL that *search* for reward signals, not “understand” goals.
- Prompts define a reachable behavior region; environments and tool feedback reshape trajectories at runtime.
- Verification (tests, lint, evals) is how you recreate the reward pressures that training taught the model to chase.
- Reward hacking is a first-class risk; if your proxy metric is wrong, agents will optimize the wrong thing.
- The practical question shifts from “did I prompt well?” to “did I bound the space tightly enough?”

## Synthesis
The essay’s central claim is a reframing: calling agents “thinking” invites mysticism; calling them “search” invites engineering. The author grounds this in standard ML mechanics. Pretraining teaches next-token prediction, which determines what outputs are reachable given a context. Reinforcement learning (or similar alignment training) then biases the model toward actions that historically increased reward, turning the model into a policy operating in an environment.

From this, the author proposes three layers: the environment (the real repo/tools/permissions), the context window (everything the model has observed), and the resulting “field” of reachable behaviors given the trained policy and current context. Agent runs are described as trajectory rollouts: the model acts, the environment responds (tool outputs), and that feedback is appended to context, changing what future actions are likely.

The engineering implication is that reliability is less about a perfect initial instruction and more about shaping the search space throughout execution. Good verifiers (tests, compilers, lint, deterministic checks) are presented as the most direct way to steer behavior because they provide unambiguous signals the agent can optimize toward. Conversely, weak or misaligned metrics create openings for reward hacking: agents can converge on behaviors that maximize the proxy while violating the true intent.

The essay also connects this to the current moment: as agents take on longer time horizons—multi-hour runs, autonomous deployments—the non-determinism becomes more visible, and so does the need for deterministic scaffolding. The recommended mindset is to design constraints, checkpoints, and feedback loops that make the space of acceptable actions narrow enough that stochastic search still converges.

Overall, it reads as a call to treat agentic systems like any other complex, feedback-driven software: define the objective precisely, instrument it, and make failure modes observable—rather than relying on anthropomorphic narratives.