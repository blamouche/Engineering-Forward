# What I Learned Onboarding Our AI Project Manager
**Source**: https://every.to/p/what-i-learned-onboarding-our-ai-project-manager
**Date**: March 31, 2026 (Updated May 14, 2026)
**Author**: Nityesh Agarwal
**Keywords**: AI project management, agent onboarding, Claude Code, workplace AI, context window, subagents, AI coworkers, parallel organization

## Elevator pitch
Onboarding Every's AI project manager "Claudie" was harder than hiring a human — but she now saves 15 hours a week, and the painful process revealed critical lessons about defining jobs before hiring and understanding how agents do their best work.

## Takeaways
- Claudie, built in Claude Code, now tracks all client project statuses and saves the consulting team 15 hours per week
- The agent had to be "fired" multiple times and restructured before becoming reliable — onboarding was harder than a human hire
- Critical lesson 1: Define the job before you "hire" — agents can only work with the context and tools you give them, so be specific about responsibilities and information access upfront
- Critical lesson 2: Understand how your agent does its best work — context window limits forced a redesign from a single agent to a layered architecture with orchestrator + subagent fleets
- Claudie initially failed at tasks an experienced human PM would handle easily, because she tried processing too much information at once
- Every now runs a "parallel organization chart" with both human and agent employees (4 humans, 3 agents on the consulting team)

## Synthesis
Nityesh Agarwal's candid account of onboarding Claudie — Every's AI project manager built in Claude Code — reveals that deploying workplace agents requires fundamentally rethinking how we structure work, not just giving an LLM access to tools. The consulting team went through multiple versions of Claudie, each iteration uncovering deeper structural lessons about agent design.

The first challenge: Claudie was initially asked to handle the sprawling admin work of maintaining client project dashboards — tracking action items, meeting notes, client feedback, and session attendance across email, Google Docs, Sheets, calendar, and meeting transcripts. Early failures were often simple access problems: she lacked meeting transcripts or pivot table tools. The lesson: be ruthlessly specific about what information and tools an agent needs before it starts.

The deeper challenge was architectural. Like many first-time agent builders, the team initially treated Claudie like a human hire — give her the big picture and let her figure it out. This failed because of context window limitations. Breaking Claudie into layers (orchestration agent + subagent fleets for extraction, identification, and updates) improved results but remained unreliable — key dates kept getting dropped.

The piece frames this as a new category of management work: agent onboarding that is harder than human onboarding because you can't rely on common sense and general experience. Every human PM knows to track dates; Claudie had to be explicitly architected to do so. This has implications for the "parallel organization chart" Every is building, where AI colleagues have names, managers, and real responsibilities alongside humans. The consulting team now operates with 4 humans and 3 agents, with Claudie saving 15 hours weekly — but only after the painful process of learning how to structure agent work properly.
