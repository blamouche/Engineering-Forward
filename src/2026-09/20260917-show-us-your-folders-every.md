# Show Us Your Folders: Give Your Agents a Garden and a Yard
**Source**: Every (hello@every.to) — https://every.to/emails/click/context-window/show-us-your-folders
**Date**: 2026-09-16
**Author**: Katie Parrott (Every)
**Keywords**: AI workspace, agent organization, folder architecture, Claude Code, Codex, Compound Engineering, agent memory, workspace audit

## Elevator pitch
Every's "Show Us Your Folders" series opens Kieran Klaassen's AI workspace—a four-part architecture (Tuin, Erf, dashboard, Mac mini) that treats the folder as the agent, with practical principles for organizing agent context, memory, and dispatch.

## Takeaways
- **The folder is the agent**: Everything an AI needs to work the way you want should live in the folder. Kieran's setup has four parts: Tuin (personal workspace), Erf (coordinator/dispatcher), a dashboard (interface), and a Mac mini (always-on compute).
- **Separate context from dispatch**: Tuin stores goals, notes, projects, and memories. Erf starts sessions and sends each task to the right folder. Keeping these separate lets you change agent assignment without reorganizing source material.
- **Organize memory by time scale**: Kieran keeps daily, weekly, monthly, and yearly memory files, paired with matching planning routines. A daily plan and a monthly review need different amounts of history and shouldn't draw from the same catch-all file.
- **Compound Engineering's ce-doc-review can audit your workspace**: The review checks coherence (do files agree on priority?), feasibility (can agents follow the load order?), product (does the setup support its use?), scope (has one file taken on too many roles?), and adversarial (where could automatic capture create failure modes?).
- **Custom-fit to your style**: Kieran's folder setup builds on a planning practice he's followed for 15 years. Better results come from a system custom-fit to your existing workflow than from adopting someone else's wholesale.

## Synthesis
The article launches Every's "Show Us Your Folders" series, where team members open their AI workspaces and explain their setups. The inaugural tour features Kieran Klaassen, general manager of Cora, who introduces a philosophy he calls "the folder is the agent"—everything an AI needs to work should live within a folder structure designed for that purpose.

Kieran's architecture has four components. Tuin ("garden" in Dutch) is his personal AI workspace, storing goals, tasks, meeting notes, ideas, projects, and personal records in folders. Erf ("yard") is the coordinator—it starts agent sessions and dispatches each task to the folder containing relevant files and instructions. A dashboard serves as the interface, showing plans, to-dos, scheduled tasks, active agents, and their sessions. A Mac mini provides always-on compute, so agents continue working after Kieran closes his laptop. Critically, Claude Code, Codex, Cursor, and Kieran's own tools all use the same folders, enabling tool-switching without context migration.

The practical principles are immediately actionable. Making a separate folder for each job means each folder gives an agent one clear job and the context it needs. Separating context (Tuin) from dispatch (Erf) allows changing how agents are assigned without reorganizing the material they use. Memory organized by time scale—daily, weekly, monthly, yearly—prevents the common failure of drawing a daily plan and a monthly review from the same undifferentiated file.

The article also introduces a workflow for auditing your own setup using Compound Engineering's ce-doc-review skill. The author ran it on her workspace and it distinguished authoritative files from installed copies, exposed sprawl (25 top-level folders, over a thousand raw session files, three versions of a working project across two machines), and recommended consolidating duplicate roots, treating runtime copies as disposable, and requiring human review before captured context becomes shared guidance.

The three-step audit process is: (1) ask your agent to map one workspace before changing anything, naming what each folder owns and which files are authoritative; (2) run ce-doc-review on that map to flag duplicated homes, conflicting instructions, stale indexes, and material captured but never consolidated; (3) review findings yourself and approve only changes that fix real failure modes, never letting the agent move, rename, or delete files until approved.

The article also mentions Mike Taylor's expanded framework of 13 beliefs about writing with AI, emerging from his earlier distillation ratio heuristic, and an antivirus-for-the-AI-age piece on AI agent security—both worth separate exploration.