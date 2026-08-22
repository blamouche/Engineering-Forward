# The Orchestration Tax: Why Spawning More Agents Doesn't Mean More Output
**Source**: https://addyosmani.com/blog/orchestration-tax
**Date**: 2026-05-24
**Author**: Addy Osmani
**Keywords**: agent-orchestration, cognitive-bandwidth, concurrent-systems, code-review, backpressure, parallel-agents, gil-analogy, attention-architecture

## Elevator pitch
Spawning agents is cheap but closing the loop on each one is expensive — all the judgment to steer agents and merge their work still routes through exactly one serial processor (you), making the "orchestration tax" an architecture problem, not a discipline problem.

## Takeaways
- There is a hidden asymmetry in agentic workflows: starting an agent is very cheap (a keystroke or prompt), but closing the loop — checking if the result is correct and reconciling it with what other agents touched — is not cheap at all
- The human is the single-threaded resource in agent development, analogous to Python's Global Interpreter Lock (GIL): you can spawn many agents but judgment still has to acquire the lock one at a time
- Running 20 agents does not mean there is more of you; spawning 8 agents doesn't speed up your judgment time, it just makes the queue feeding into it much deeper
- The right number of parallel agents is how many you can actually code review properly — for most developers this is a low single digit, even though the UI happily lets you spawn 20
- Grinding won't fix structural limits: the constraint shows up as shallow code reviews or "cognitive surrender" where you just accept the agent's code because forming your own opinion costs attention you no longer have
- Practical fixes include: scale fleet to review rate (not the UI), sort work into isolated-delegatable vs. complex-judgment tasks, batch reviews to minimize context switching, and only spend the lock on judgment — let agents prove the boring 80% with tests and screenshots

## Synthesis
Addy Osmani names a structural problem in agentic engineering that he encountered at Google I/O: the orchestration tax. The core insight is that running multiple agents does not parallelize your cognitive bandwidth. All the judgment required to steer agents, verify their output, and merge their work into the codebase still has to route through exactly one serial processor — you. This is not a discipline problem; it is an architecture problem.

The hidden asymmetry is that starting an agent is nearly free — a keystroke or a sentence prompt — but closing the loop on each agent is expensive. Someone has to check whether what came back is correct and reconcile it with whatever other agents touched. As agent count grows, the reconciliation queue deepens faster than any single human can process it. The analogy to Python's Global Interpreter Lock is precise: you can spawn as many threads as you want, but only one executes Python bytecode at a time because they must acquire the lock. In agent development, the serial fraction is judgment. Spawning eight agents doesn't speed up judgment time; it makes the queue feeding into it much deeper.

The failure mode when this limit is ignored is subtle. It doesn't manifest as an error — it shows up as shallow code reviews where you rubber-stamp agent output, or as "cognitive surrender" where you accept the agent's code because forming your own independent opinion costs attention you no longer have. The system doesn't break loudly; it degrades quietly, and you may not realize how bad things have gotten until a bug surfaces in production and you discover you no longer understand how the system works.

Osmani's prescription is to architect your attention like any other concurrent system. Scale the agent fleet to your actual review rate, not to what the UI allows — backpressure should slow the producer to match the consumer. Sort work into two piles: isolated tasks that can run async in the background with only a final gate review, and complex tasks where the judgment is the work and parallelizing just thrashes the lock. Batch reviews to minimize context-switching costs. And only spend your scarce attention on the 20% that genuinely needs human judgment — let agents prove the boring 80% themselves with passing tests, generated screenshots, and automated verification. The takeaway is that feeling busy with 20 agents running is not the same as being productive, and the only real fix is to start treating your own attention as the scarce serial resource it actually is.