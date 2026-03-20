# Open SWE: An Open-Source Framework for Internal Coding Agents
**Source**: https://blog.langchain.com/open-swe-an-open-source-framework-for-internal-coding-agents/
**Date**: 2026-03-17
**Author**: LangChain
**Keywords**: Open SWE, coding agents, LangChain, LangGraph, enterprise, Stripe, Ramp, Coinbase, sandbox, Slack integration

## Elevator pitch
Open SWE is an MIT-licensed framework distilling architectural patterns from Stripe, Ramp, and Coinbase's internal coding agents into composable, production-ready components for organizations building their own AI software engineers.

## Takeaways
- Inspired by Stripe's Minions, Ramp's Inspect, and Coinbase's Cloudbot—three of the most-discussed enterprise coding agent deployments
- Isolated cloud sandboxes with full permissions but contained boundaries are the dominant execution pattern across all three source implementations
- Slack-first integration means primary invocation happens through Slack and GitHub rather than requiring new interfaces
- Agents receive full issue/thread context before starting work, reducing overhead from discovering requirements via tool calls
- Built on LangGraph and Deep Agents with pluggable sandbox providers including Modal, Daytona, Runloop, and LangSmith

## Synthesis
Open SWE's origin story is significant: rather than theorizing about what enterprise coding agents should look like, LangChain reverse-engineered what the most sophisticated real-world implementations actually do, then extracted those patterns into a reusable framework.

Stripe's Minions, Ramp's Inspect, and Coinbase's Cloudbot represent some of the most public and detailed accounts of AI coding agents deployed in production financial services—environments with high correctness requirements, significant regulatory exposure, and engineering cultures skeptical of half-measures. That these three independent teams converged on similar architectural patterns is strong evidence those patterns solve real problems rather than reflect theoretical preferences.

The isolated execution pattern is the most fundamental. Tasks run in dedicated cloud sandboxes with full permissions but contained boundaries. This design choice reflects hard experience with the alternative: agents that can directly modify production systems create unpredictable blast radius when they make mistakes. Sandboxed execution means a failed agent task is always recoverable—the worst case is a wasted sandbox run, not an irreversible production change.

Curating tool selection—approximately 15 well-tested capabilities rather than accumulating every available tool—addresses a subtle quality issue in agent systems. More tools means more opportunities for the agent to choose incorrectly, more surface area for tool-tool interference, and more cognitive overhead per tool call as the agent maintains awareness of a larger option space. The Stripe/Ramp/Coinbase convergence on lean toolsets suggests that richness of available tools correlates negatively with reliability.

Slack-first integration is a distribution insight as much as a technical one. Requiring engineers to learn a new interface creates adoption friction. Meeting developers where they already work—in Slack threads, GitHub issues, and Linear tasks—removes that friction and embeds AI assistance into existing workflows rather than creating parallel ones. The rich startup context approach (giving agents complete issue or thread history before they begin) reduces the exploratory tool calls that consume tokens without advancing work.
