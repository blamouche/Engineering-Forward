# Claude Cowork Commands, Scheduled Tasks & Automation Workflows: The Operator's Playbook
**Source**: https://linas.substack.com/p/claude-cowork-commands-automations-playbook
**Date**: May 1, 2026
**Author**: Linas Beliūnas
**Keywords**: Claude Cowork, AI automation, scheduled tasks, slash commands, AI workflows, business automation, token costs, AI operating system, Claude Code, Routines, Anthropic

## Elevator pitch
A comprehensive operational guide to Claude Cowork that maps every real slash command, distinguishes Scheduled Tasks from Claude Code Routines, provides five engineered workflow prompts for business use cases, and documents failure modes with workarounds.

## Takeaways
- Claude Cowork launched generally on April 9, 2026, and contains a full slash command system, automation layer, and scheduled task capabilities distinct from Claude Code's Routines
- Scheduled Tasks run on your desktop and die when your laptop closes; Routines run in the cloud but belong to Claude Code, not Cowork — the distinction determines whether your morning briefing exists
- Five engineered workflow prompts target high-ROI use cases: deal intake pipeline (300 pitch decks cut from 60min to 2min review), call-to-action debriefs from meeting recordings, investor update drafting, SOP documentation from domain expertise, and CRM pipeline hygiene
- Token consumption varies dramatically by workflow: a 10-PDF synthesis burns 80,000-120,000 tokens and requires the Max Plan
- Seven documented failure modes each come with specific workarounds, and plan requirements are matched to workflow complexity

## Synthesis
Linas Beliūnas's May 1, 2026 guide is the operational companion to his earlier Claude Cowork-as-COO framework, focusing on the systems layer rather than the mental model. The piece addresses what Beliūnas identifies as the missing half of effective Cowork usage: knowing which commands actually exist, how the automation layer works, where it breaks, and how to build workflows that compound rather than degrade.

The guide opens with the verified command reference — distinguishing real Cowork slash commands from those circulating in social media that don't exist. This is positioned as essential ground truth in a fast-moving tool where community lore often outpaces documentation. The core infrastructure distinction that Beliūnas emphasizes is between Scheduled Tasks and Routines: two different automation systems, two different products. Scheduled Tasks run on your desktop within Cowork and die when your laptop closes. Routines run in the cloud but belong to Claude Code, not Cowork. Understanding this distinction is what determines whether your automated morning briefing was actually generated or silently failed.

Five workflow prompts form the practical center of the guide, each engineered for a specific business function. The deal intake pipeline processed 300 pitch decks, cutting first-pass review from 60 minutes to 2 minutes per deck. A call-to-action system auto-generates debriefs and follow-up emails from Fathom or Fireflies meeting recordings. An investor update writer drafts in the user's voice with one honest challenge baked into each update. An SOP machine converts domain expertise into documentation a new hire can follow. A CRM pipeline hygiene workflow catches stale deals, stage mismatches, and concentration risk every Friday.

Token costs receive detailed treatment, matched to workflow type and plan tier. A 10-PDF synthesis workflow burns 80,000-120,000 tokens, requiring the Max Plan. Simpler workflows like daily status reports operate within lower plan limits. The cost analysis helps users match workflows to their subscription tier without hitting rate limits mid-task.

Seven failure modes are documented with specific workarounds: what happens when sub-agents fail silently, when file access permissions are misconfigured, when connectors lose authentication, when scheduled tasks time out, when token limits truncate complex outputs, when parallel workers produce inconsistent results, and when context windows overflow on long-running sessions. Each failure mode comes with the specific workaround Beliūnas has validated through testing since Cowork's general availability on April 9, 2026.

The guide is explicitly positioned as the operational layer beneath the strategic COO framework from Beliūnas's earlier piece — the commands, automations, and failure handling that turn the mental model into reliable daily execution.
