# Claude Code Scheduled Tasks (Thread)
**Source**: https://threadreaderapp.com/thread/2035122989533163971.html
**Date**: March 25, 2026
**Author**: @noahzweben
**Keywords**: Claude Code, scheduling, automation, MCP, cloud tasks

## Elevator pitch
A short thread announcing scheduled, cloud‑run tasks in Claude Code, enabling recurring prompts that run on a schedule without a local machine.

## Takeaways
- Claude Code now supports scheduled, recurring tasks in the cloud.
- Users set repo(s), a schedule, and a prompt; the agent runs server‑side.
- Suggested use cases include PR sweeps, CI failure analysis, and doc sync.
- Scheduled tasks can access MCPs connected via claude.ai.
- The feature is accessible via claude.ai/code/scheduled or desktop.

## Synthesis
This short thread announces a new scheduling capability for Claude Code. Instead of keeping a local agent running, users can define recurring, cloud‑based tasks by specifying a repository, a schedule, and a prompt. Claude runs the task on its own infrastructure, enabling hands‑off automation.

The author highlights typical use cases: sweeping through open pull requests, building features from approved issues, analyzing CI failures overnight, and syncing documentation after merges. These are tasks that benefit from regular cadence and would otherwise require manual checks or persistent local automation.

A key detail is integration with MCPs connected via claude.ai. Scheduled tasks can use the same MCP access the user has configured, implying that workflows can rely on external tools and APIs without manual re‑authentication or local setup.

Overall, the update positions Claude Code scheduling as a practical step toward reliable background automation: recurring jobs, cloud execution, and access to connected tools, enabling teams to automate maintenance and analysis workflows without keeping a local agent running.
