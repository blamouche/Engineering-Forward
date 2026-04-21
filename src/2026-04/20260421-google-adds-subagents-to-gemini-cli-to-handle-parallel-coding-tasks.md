# Google adds subagents to Gemini CLI to handle parallel coding tasks

**Source**: https://tessl.io/blog/google-adds-subagents-to-gemini-cli-to-handle-parallel-coding-tasks/
**Date**: April 21, 2026
**Author**: Unknown
**Keywords**: tessl, google, adds, subagents, gemini, handle, parallel, coding

## Elevator pitch
Google's Gemini CLI now supports subagents, enabling parallel task handling by distributing work across specialized agents

## Takeaways
- Back to articles Google adds subagents to Gemini CLI to handle parallel coding tasks 20 Apr 2026 6 minute read Paul Sawers Freelance tech writer at Tessl, former TechCrunch senior writer covering startups and open source LinkedIn X Substack Share this article Table of Contents Delegating work inside the CLI Parallel execution and context separation How to use subagents in Gemini CLI Back to articles Google adds subagents to Gemini CLI to handle parallel coding tasks 20 Apr 2026 6 minute read Table of Contents Delegating work inside the CLI Parallel execution and context separation How to use subagents in Gemini CLI AI coding agents might be able to take on more complex work, but they still tend to work through tasks one at a time.
- And that can become a huge bottleneck once tasks start to stack up.
- Google is addressing that with a new “ subagents ” feature in its Gemini CLI , introducing a way to split work across multiple specialised agents within the same environment.
- Subagents are defined with their own instructions, tools, and context.
- The main agent can delegate parts of a task to them, allowing work to be broken down and handled in parallel.

## Synthesis
Back to articles Google adds subagents to Gemini CLI to handle parallel coding tasks 20 Apr 2026 6 minute read Paul Sawers Freelance tech writer at Tessl, former TechCrunch senior writer covering startups and open source LinkedIn X Substack Share this article Table of Contents Delegating work inside the CLI Parallel execution and context separation How to use subagents in Gemini CLI Back to articles Google adds subagents to Gemini CLI to handle parallel coding tasks 20 Apr 2026 6 minute read Table of Contents Delegating work inside the CLI Parallel execution and context separation How to use subagents in Gemini CLI AI coding agents might be able to take on more complex work, but they still tend to work through tasks one at a time. And that can become a huge bottleneck once tasks start to stack up. Google is addressing that with a new “ subagents ” feature in its Gemini CLI , introducing a way to split work across multiple specialised agents within the same environment. Subagents are defined with their own instructions, tools, and context. The main agent can delegate parts of a task to them, allowing work to be broken down and handled in parallel. Rather than one agent working through everything step by step, tasks can be distributed and executed at the same time. For example, a developer could tell Gemini CLI that the backend for an analytics API is done and ask it to update the frontend, tests, and documentation, with subagents then spun up for each part of the job — a frontend specialist, a unit test agent, and a docs writer. Subagents in Gemini CLI Delegating work inside the CLI The setup is designed to handle tasks that would otherwise overload a single agent session. A developer can create subagents for specific roles — such as code review, testing, or documentation — and call on them when needed. Each subagent runs with its own context, allowing the main agent to hand off work and receive results without carrying everything in a single thread.
