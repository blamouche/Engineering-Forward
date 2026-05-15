# Claude Cowork Commands, Scheduled Tasks & Automation Workflows: The Operator's Playbook
**Source**: https://linas.substack.com/p/claude-cowork-commands-automations-playbook
**Date**: 2026-05-01
**Author**: Linas Beliūnas
**Keywords**: Claude Cowork, slash commands, scheduled tasks, automation workflows, Anthropic, AI operations, Routines, founder tools, investor tools, deal flow

## Elevator pitch
Belinas provides the operational layer for Claude Cowork: a verified command reference, the distinction between Scheduled Tasks and Routines, five engineered workflow prompts for founders and investors, and every failure mode with workarounds—turning the COO mental model into production-grade systems.

## Takeaways
- Belinas differentiates Scheduled Tasks (desktop-based, dies when laptop closes) from Routines (cloud-based, part of Claude Code not Cowork)—a distinction that determines whether your morning briefing exists or was never generated.
- Five engineered workflow prompts cover high-ROI business use cases: deal intake pipeline (300 pitch decks, first-pass review from 60min to 2min), call-to-action system (auto-generates debriefs from Fathom/Fireflies), investor update writer, SOP machine, and CRM pipeline hygiene.
- Token cost math matters: a 10-PDF synthesis burns 80,000-120,000 tokens (Max Plan territory), and different workflows require different subscription plans based on token consumption.
- Seven failure modes are documented with specific workarounds for each, including issues with file access, stalled agents, and context window limitations.
- The article builds on the earlier COO Guide, covering the systems layer after establishing the mental model—commands, automation architecture, and workflows that compound.

## Synthesis
Linas Belinas follows up on his viral Claude Cowork COO Guide with the operational companion piece: a detailed systems-layer manual for the automation features Anthropic shipped when Cowork went generally available on April 9, 2026. While the earlier guide established the mental model of treating Cowork as a $20/month COO replacement for $300K+ human hires, this piece covers the machinery that makes that abstraction work in practice.

The centerpiece is a verified command reference—every real Cowork slash command documented with what it actually does, explicitly distinguishing real commands from ones circulating on social media that don't exist. This is paired with a critical architectural distinction: Scheduled Tasks run on your desktop and die when your laptop closes, while Routines run in the cloud but belong to Claude Code, not Cowork. Confusing the two systems means the difference between a morning briefing that's waiting for you and one that was silently never generated.

Five fully engineered workflow prompts demonstrate the concept in practice. The deal intake pipeline processed 300 pitch decks and cut first-pass review from 60 minutes to 2 minutes. A call-to-action system auto-generates debriefs and follow-up emails from Fathom or Fireflies recordings. An investor update writer drafts in the founder's voice with one honest challenge baked in. An SOP machine converts tacit process knowledge into documentation a new hire can follow. And a CRM pipeline hygiene workflow catches stale deals, stage mismatches, and concentration risk every Friday before the week ends.

Belinas also tackles the economics: a 10-PDF synthesis consumes 80,000-120,000 tokens, squarely in Max Plan territory. Seven documented failure modes each come with workarounds, from file access problems to context window limitations to stalled agents. The practical upshot is a guide that bridges the gap between Claude Cowork's theoretical power and reliable day-to-day operation for founders, operators, and investors.
