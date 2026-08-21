# Build from Anywhere with Cursor for iOS
**Source**: https://cursor.com/blog/ios-mobile-app
**Date**: 2026-06-29
**Author**: Chris Brauchli, Rikki Mukherjee & Kevin Niparko
**Keywords**: cursor, ios, mobile, cloud-agents, ai-coding, remote-control

## Elevator pitch
Cursor launches a native iOS app that turns the phone into a control plane for AI coding agents — enabling developers to launch cloud agents, control local agents remotely, and merge PRs from anywhere.

## Takeaways
- Cursor for iOS is a native app in public beta that lets developers launch always-on cloud agents or control agents running on their computer via Remote Control.
- Cloud agents run in isolated virtual machines with full development environments, operating asynchronously to iterate toward merge-ready PRs without intervention.
- The app supports voice input, slash commands, Live Activities on the lock screen, push notifications, and direct PR merging from the phone.
- New workflows enabled by the mobile app: handling incidents while on call, resolving customer bugs away from desk, and acting on feedback from other mobile apps by sending screenshots to agents.
- Fluid handoff between local and cloud: agents can be moved from local machine to cloud and back, enabling work to continue regardless of proximity to a computer.

## Synthesis
Cursor's iOS app represents a paradigm shift in how developers interact with AI coding agents. Rather than being a code editor squeezed onto a phone screen, it is a control plane for agents that do the heavy lifting elsewhere. This distinction matters: the phone becomes a place to delegate, review, and approve work, not to write code line by line.

The architecture relies on two core capabilities. First, always-on cloud agents that run in isolated VMs with full development environments — they can edit code, run tests, verify changes, and prepare PRs without any human intervention. Second, Remote Control for agents already running on a developer's local machine, allowing them to continue directing work from their phone when they step away from their desk. The combination means developers are never disconnected from their agents' progress.

The practical workflows the team highlights are telling: an on-call engineer gets paged at lunch, kicks off an agent from their phone to investigate, and returns to a PR ready for review. A developer sees user feedback on social media, takes a screenshot, sends it to an agent as visual context, and starts working on a fix. These are not hypothetical — they are patterns the Cursor team and early testers are already using daily.

The broader implication is about where the value in AI-assisted development lies. As agents become more capable and autonomous, the interface that matters most may not be the code editor but the control surface — the place where tasks are launched, monitored, redirected, and approved. The phone is uniquely positioned for this because it is always with you, making it the natural home for "ambient software development" where progress happens continuously and you intervene only when needed.