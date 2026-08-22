# How Meta Is Reinventing Product Management
**Source**: https://www.lennysnewsletter.com/cp/203444316
**Date**: 2026-06-24
**Author**: Lenny Rachitsky (interview with Jagjit Chawla, VP Product at Meta)
**Keywords**: Meta, product management, AI agents, PRD, compression algorithm, first-principles thinking, AI transformation

## Elevator pitch
Meta is rebuilding product management from top to bottom — the PRD is now a paragraph and a prototype, an AI agent reads every code diff overnight to replace the org-chart information pipeline, and the PM's job has shifted from process management to judgment.

## Takeaways
- The "compression algorithm" — the org chart that summarized ground truth from engineer to VP — has been replaced by an AI agent that reads every diff, email, and chat overnight and produces a morning punch list with red/yellow/green status per project
- The PRD has been compressed from a detailed document to one paragraph describing the problem, coupled with a prototype and (for ML areas) an eval set — the PM judges outcomes rather than writing specs
- None of the tools were bought — Jagjit built them himself from generally available tools, with a nightly tuning loop that compares his actual comments against the system's predictions
- Ideas are now cheap and judgment is the bottleneck: when anyone can produce a 50-page deck in 30 minutes, the scarce skill is deciding what deserves to exist
- Generalists are making a comeback: PhDs in economics and physics are outperforming engineering-background PMs because first-principles thinking matters more than technical pedigree when AI tools handle the technical execution

## Synthesis
Lenny Rachitsky's interview with Jagjit Chawla, VP of Product at Meta running Feed, Reels, and Search in the Facebook app, is a window into one of the most advanced AI-driven transformations of a product management function at scale. The changes described are not experiments or pilots — they are how Meta actually operates today, at a scale of billions of users and tens of thousands of employees.

The most striking change is the death of what Chawla calls the "compression algorithm." In a thousand-person organization, the ground truth is the code being written. Between that truth and the executive sits a compression algorithm: the engineer knows what they checked in, the manager summarizes it, and by the time it reaches the VP, each project has been squeezed to a sliver. That sliver-times-fifty was the job. Now, Chawla's AI agent reads everything overnight — every diff, every email and chat, every document — and produces a morning punch list at 7 AM. Decisions his team made, decisions waiting on him, decisions he needs to carry upward. Project by project: red, yellow, green. He opens this dashboard with his morning coffee, not his inbox.

The PRD transformation is equally radical. Two years ago, the IC job was to sit with engineers and researchers, write a detailed PRD, and fill holes as they surfaced during building. Today the artifact is one paragraph describing the problem, coupled with a prototype. For ML-heavy areas, add an eval set — test cases run repeatedly because these systems don't give the same answer twice. The PM sits next to the engineer judging whether outputs are good or bad. The work happens in pods of five people sitting together, not in document review cycles.

Perhaps the most important insight for the broader industry is about the shifting skill set. For a decade, the mid-career PM skill set was dominated by process — prioritization, stakeholder management, running the machine. Ideation barely mattered because so few ideas made it through the engineering bottleneck. That constraint just dissolved. When agents can prototype and test almost anything, "what are your ideas?" becomes a real interview question. The PMs outperforming on Chawla's team are PhDs in economics and physics, not engineering backgrounds — they reason from first principles about marketplace incentives rather than jumping to how something gets built.

The practical playbook is accessible: build the morning brief (a nightly run over email, chat, docs, and tickets), stop doing tasks the old-school way (route work through the system even when imperfect, teaching it every time it misses), shrink the PRD (one paragraph, prototype, eval set), and if you lead, create real space (cancel meetings for a week and let people rebuild how they work). The tools don't matter — "find a scissor, doesn't matter what scissor." The discipline of writing things down is the real prerequisite.