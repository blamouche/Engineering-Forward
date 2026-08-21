# We Built Our Own Agent-Native Tool. It Overhauled How We Build Software.
**Source**: https://every.to/p/we-built-our-own-agent-native-tool-it-overhauled-how-we-build-software
**Date**: 2026-06-16
**Author**: Stella Garber
**Keywords**: agent-native, Claude Code, Hoop, AI tools, startup, customer discovery, Slack agent, architecture

## Elevator pitch
A pre-product-market fit startup (Hoop) built an internal agent-native tool to process customer discovery calls, and the process of building it reshaped how they construct their actual product—demonstrating that agent-native architecture isn't just about AI features, but about giving models tools and letting them reason about usage.

## Takeaways
- Hoop's cofounders (none with "engineer" in their title) built an internal customer-discovery analysis tool in under 10 hours using Next.js, ShadCN, Supabase, and Claude's API
- The initial tool generated quality analysis but had too much manual friction: downloading transcripts, uploading, filling in metadata, sharing results in Slack
- Adopting agent-native architecture (giving the model tools rather than hard-coding prompt sequences, and bringing the tool to where people already work rather than a destination app) transformed both the internal tool and the product
- Non-technical cofounder Brian learned agent-native architecture from Claude in 2 hours at 10pm, building a feature where the Slack agent could edit its own prompts—demonstrating that agent-native patterns are accessible to non-engineers
- The tool surfaced a critical pattern (4 of 6 recent calls mentioned involuntary subscription churn) that no individual had connected; the agent also autonomously detected and deleted duplicate records

## Synthesis
Stella Garber's account from Hoop offers a grounded, practical look at agent-native architecture from a startup perspective. The story begins with a common pain point: scattered customer discovery notes across Slack, Granola transcripts, and Claude Code, with no systematic way to identify patterns. The initial solution was a traditional web app—upload a transcript, run it through prompts, get structured analysis. It worked, but adoption was poor because it required people to visit yet another tool.

The pivotal shift came from embracing two agent-native principles. First, instead of hard-coding a sequence of prompts, give the model tools and let it reason about how to use them. Second, bring the tool to where people already work (Slack) rather than building a destination app. The result was a Slack-based agent that handles transcript upload, analysis, summary creation, and sharing—all triggered by simply sending a transcript to the app.

What makes this story compelling is that the same architectural principles then shaped Hoop's external product. Justin, the product cofounder, started checking every new feature against the agent-native architecture guidelines. Brian, the other cofounder, went from not understanding what "make the prompt an editable field and pass it to the agent" meant to building a self-editing agent prompt system in two hours. Even the CEO (Garber herself) shipped features directly via Claude Code, including a Trello-like pipeline view—merging code directly to the shared repo.

The broader insight: agent-native architecture isn't just about AI features. It's about a fundamentally different relationship between builder and tool, where the model becomes a reasoning participant rather than a fixed pipeline component. The fluency gained—knowing when to give a model a tool versus hard-coding a workflow—mattered more than any specific feature.