# Former GitHub CEO Launches Competitor Designed for the Age of Vibe Coding
**Source**: https://www.theregister.com/ai-and-ml/2026/07/08/former-github-ceo-launches-competitor-designed-for-the-age-of-vibe-coding/5268694
**Date**: 2026-07-08
**Author**: The Register
**Keywords**: Entire, GitHub, Git hosting, Thomas Dohmke, vibe coding, AI agents, decentralized Git, developer tools

## Elevator pitch
Former GitHub CEO Thomas Dohmke launches Entire.io, a decentralized Git hosting network designed for AI agents, claiming 2.1M pushes/hour and positioning it as the infrastructure layer for the vibe coding era.

## Takeaways
- Thomas Dohmke, former GitHub CEO, has launched Entire.io, a new Git hosting network designed specifically for the age of AI agents and vibe coding.
- GitHub has been struggling with infrastructure stress from AI coding agent interactions, a problem that Entire aims to solve by providing a parallel environment where agents can operate without impacting production resources.
- Entire claims its network can handle 2.1 million pushes per hour and 570,000 clone operations per hour, significantly outperforming Cursor Origin's reported 81,000 pushes and 296,000 clones per hour.
- The platform allows developers to mirror their GitHub repos (public or private) into a parallel universe where AI agents can work without straining GitHub's infrastructure.
- Entire plans to open source its Git network and allow self-hosting in the months ahead, and includes an "Entire CLI" that tracks AI agent sessions alongside code commits—capturing prompts, responses, and file changes.

## Synthesis
The launch of Entire.io by former GitHub CEO Thomas Dohmke signals a growing recognition that existing Git hosting infrastructure wasn't built for AI agents. GitHub, used by an estimated 93.87% of developers, has been struggling under the load of AI coding agent interactions—a trend that's only accelerating as vibe coding becomes mainstream.

Entire's core proposition is decentralization. While Git was always designed to be decentralized, in practice most development has centralized on GitHub. Entire argues this model breaks down when agents enter the picture: they generate massive volumes of concurrent requests, create numerous branches and commits, and need environments where their fumbling can happen without impacting production systems.

The approach is pragmatic rather than revolutionary. Rather than asking developers to abandon GitHub, Entire allows mirroring of repos, creating a parallel universe where agents can operate freely. The Entire CLI adds an auditing layer that captures not just what changed but why—tracking prompts, responses, and file changes from AI coding agents. This addresses a real gap: understanding agent decision-making is becoming critical as agents produce more code.

The competitive landscape is getting crowded. SpaceX's Cursor launched its own agent-friendly GitHub alternative called Cursor Origin, and Entire is directly competing on performance metrics. Entire's claimed 2.1M pushes/hour vs. Cursor Origin's 81,000 is a striking gap, though these are vendor-provided numbers that need independent verification.

For engineering teams, the broader signal is clear: Git hosting infrastructure is being rethought for the agent era. Whether it's Entire, Cursor Origin, or GitHub's own eventual response, the days of agents running on infrastructure designed for human-paced development are numbered. The question isn't whether this infrastructure needs to change, but how quickly.