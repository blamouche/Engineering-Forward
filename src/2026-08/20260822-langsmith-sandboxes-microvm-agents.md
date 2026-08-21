# Give Your Agent Its Own Computer: LangSmith Sandboxes
**Source**: https://tldrnewsletter.com (TLDR AI, 2026-06-08)
**Date**: 2026-06-08
**Author**: TLDR AI / LangSmith
**Keywords**: langsmith, sandbox, microvm, agent-security, code-execution, infrastructure

## Elevator pitch
LangSmith introduces Sandboxes — hardware-virtualized microVMs that give AI agents their own secure computing environment, addressing the risks of running untrusted code by letting agents execute dynamic tasks, manage persistent state, and run complex workflows without compromising production infrastructure.

## Takeaways
- Sandboxes are hardware-virtualized microVMs providing AI agents with isolated computing environments
- Addresses the core security risk of running untrusted agent-generated code by isolating execution from production infrastructure
- Agents can execute dynamic tasks, manage persistent state, and run complex workflows within the sandbox
- The microVM approach provides hardware-level isolation, stronger than container-based sandboxes, at a fraction of the overhead of full VMs
- Part of LangSmith's broader infrastructure play for production agent deployment, complementing their observability and evaluation tools

## Synthesis
LangSmith's Sandboxes address one of the most challenging problems in production AI agent deployment: how to let agents execute code safely. When an agent needs to run a script, install a package, or manipulate files, doing so on production infrastructure creates unacceptable security risks. The agent's code may be buggy, malicious (via prompt injection), or simply incompatible with the production environment.

The Sandbox solution uses hardware-virtualized microVMs — lightweight virtual machines that provide hardware-level isolation without the overhead of traditional VMs. Each agent gets its own computing environment where it can execute dynamic tasks, manage persistent state, and run complex workflows. If the agent's code damages the environment, the damage is contained within the sandbox and does not propagate to production systems.

This is architecturally significant because it enables a class of agent capabilities that were previously too risky for production. Agents can now be given the autonomy to write and execute code, install dependencies, and manipulate file systems — all within a controlled, disposable environment. The microVM approach is stronger than container-based isolation (which shares a kernel with the host) while being more lightweight than full virtual machines.

The Sandbox is part of LangSmith's broader infrastructure stack for production agents, complementing their existing observability and evaluation tools. Together, these provide the full lifecycle: monitor agent behavior (observability), evaluate agent outputs (evaluation), and isolate agent execution (Sandboxes). This positions LangSmith as a full-stack agent infrastructure provider, not just a monitoring tool.