# The Claude Code Projects Playbook: Make Claude Your Chief of Staff
**Source**: Linas's Newsletter (linas@substack.com)
**Date**: 2026-09-25
**Author**: Linas (Linas's Newsletter)
**Keywords**: Anthropic, Claude Code, Projects, parallel threads, coordinator, agents, chief of staff, playbook, Pro, Max, multi-repo, pull requests, usage limits

## Elevator pitch
Anthropic's redesigned Claude Code Projects (in beta since September 17) lets one conversation split work into parallel threads that keep running after you close your laptop. Linas provides a comprehensive playbook arguing that success depends on setting up projects like a firm runs an engagement — clear brief, named workstream owners, shared decision file, standing rules, review gates, and a budget — rather than pasting in a vague goal and hoping for the best.

## Takeaways
- **Projects as ongoing engagements**: A project is one ongoing conversation where Claude scopes work, splits it into threads, reviews results, and assembles the output. Each thread is a full Claude Code session on its own branch, sharing repositories, instructions, and memory.
- **The firm model**: The coordinator maps to an engagement lead, threads to workstreams with named owners, memory to institutional knowledge, and review gates to quality checkpoints. People who set up Projects this way get dramatically better results.
- **7-step setup**: Includes the multi-repo setting that quietly switches off hooks and permission rules — a gotcha that can cause security issues if not understood.
- **8 engagement templates**: Client/market research, build from spec, multi-repo migration, goal-driven optimization loop, recurring ops, investor technical diligence, founder's chief-of-staff inbox, and overnight idea incubator.
- **Auto-resume trap**: Threads that hit plan limits resume automatically when limits reset, potentially draining usage budgets overnight. Understanding plan economics on Pro and Max is essential.
- **Human review remains the bottleneck**: The Register noted parallel threads still produce merge conflicts and pull requests that don't fit together. Anthropic's own compiler experiment showed 16 agents hitting the same bug and overwriting each other's fixes until work was split differently.

## Synthesis
Linas's playbook captures the maturation of AI-assisted development from single-session interactions to project-scale engagements. The redesign of Claude Code Projects is essentially an attempt to solve the orchestration problem: how do you manage multiple autonomous coding agents working in parallel without producing chaos? The answer, according to this playbook, is governance — the same governance that makes human teams work. The firm analogy is apt but also reveals the limitation: if you need to set up a project the way you'd set up a consulting engagement, the tool's accessibility is limited to those who understand project management. The auto-resume trap and the 16-agent compiler experiment failure show that parallelism without coordination is worse than serial work. The key insight is that Claude Code Projects doesn't eliminate the need for human oversight — it changes the nature of it from line-by-line code review to engagement-level project management, which is a higher-value but also higher-skill role.