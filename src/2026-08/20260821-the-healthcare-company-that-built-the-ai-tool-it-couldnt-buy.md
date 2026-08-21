# The Healthcare Company That Built the AI Tool It Couldn't Buy
**Source**: https://every.to/context-window/the-healthcare-company-that-built-the-ai-tool-it-couldnt-buy
**Date**: 2026-08-21
**Author**: Katie Parrott
**Keywords**: AI agents, Claude Code SDK, MCP, enterprise AI, build vs buy, compliance, security, Docker, Headway

## Elevator pitch
Headway, a 900-person mental healthcare company, built its own AI assistant (Eddy) on the Claude Code SDK when off-the-shelf products couldn't meet its security, compliance, and workflow needs—achieving 650 daily active users and 260,000 conversations in under six months.

## Takeaways
- Off-the-shelf AI products failed Headway's unique combination of security, compliance, and workflow requirements; building a custom wrapper (Eddy) around Claude Code SDK proved more effective than waiting for vendors to catch up
- Every Eddy conversation runs in a fresh Docker container that's destroyed after use, enabling agent autonomy without risking sensitive data—Claude Code can erase the entire hard drive but it doesn't matter in a throwaway environment
- Eddy uses Model Context Protocol (MCP) connectors to integrate with Figma, Snowflake, Google Drive, and Slack, giving the agent context from tools employees already use
- 650 of 900 employees use Eddy daily; adoption was organic, not manager-mandated—driven by product decisions like HTML artifacts, inline commenting, and connectors to existing tools
- The build-vs-buy decision framework: wait when the capability is likely to arrive soon and cost of delay is low; buy when a vendor can meet security/data/workflow requirements; build when the constraint is durable, unusual, and important enough to justify owning reliability indefinitely

## Synthesis
Headway's CTO Arnaud Ferreri initially wanted to sign a deal with a major AI vendor for a desktop app, but concluded that waiting for vendors to meet their compliance and workflow requirements "felt like missing the train." The team built Eddy—a custom AI assistant running on the Claude Code SDK, hosted in Headway's AWS environment. The architecture is notable: every conversation spins up a sealed, disposable Docker container. This security-by-isolation approach means Eddy can take actions without asking permission at every step, because even if the agent goes rogue, it can only access a copy of data that's wiped when the job ends. The container can read from Snowflake but never write, cannot browse the open internet directly (only through a strict proxy), and cannot send emails.

The article traces Eddy's evolution from a 10-person alpha to company-wide adoption. Two product decisions drove organic spread: MCP connectors that let the agent work with existing tools (Figma, Snowflake, Slack, Google Drive), and HTML artifacts that were richer and easier to share than Google Docs. Headway later added inline commenting, turning Eddy output into collaborative documents.

But building came with costs. By May, Eddy experienced outages about twice a week, requiring two full-time engineers on reliability. Startup time remains a problem at ~30 seconds per conversation due to container spin-up. Keeping up with outside innovations (like Cursor features) forces the team to decide whether to build equivalents into Eddy or let engineers use external tools. Ferreri warns against becoming a "Christmas tree where every feature comes in"—just because you can doesn't mean you should.

The article proposes a three-part framework for the wait/buy/build decision, and offers practical advice for companies that choose to build: find the three or four engineers closest to the edge of AI, pair them with an executive sponsor and legal/compliance/security, broaden access only after safe permission boundaries exist, and connect AI-native builders with everyone else for lasting adoption.