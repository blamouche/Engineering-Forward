# Anthropic's Claude Can Now Control Your Computer
**Source**: https://www.cnet.com/tech/services-and-software/claude-control-your-computer-to-perform-tasks/
**Date**: Unknown
**Author**: Blake Stimac
**Keywords**: Anthropic, Claude, computer use, agentic AI, automation

## Elevator pitch
Anthropic is rolling out a research preview that lets Claude control a user’s computer—using apps, browser, and files—with permission checks and safety guards, pushing the assistant toward more autonomous, tool-using workflows.

## Takeaways
- Claude can now operate a computer via mouse/keyboard actions when connectors aren’t available.
- The feature targets paid subscribers and currently focuses on macOS.
- Anthropic positions the capability as a step toward agentic workflows, including task dispatch from a phone.
- Safety concerns include prompt injection and rapid unintended actions; Anthropic adds safeguards and warnings.
- The rollout is framed as a research preview to learn from failures and improve reliability.

## Synthesis
CNET reports that Anthropic has launched a research preview enabling Claude to take control of a user’s computer to perform tasks, bringing the assistant closer to autonomous agent behavior. The feature allows Claude to use apps like Google Calendar or Slack through connectors, and when connectors are missing, it can still complete tasks by directly controlling the mouse and keyboard. That means Claude can interact with a browser, dev tools, and local files much like a human user would.

The release is positioned in the context of a broader “agentic AI” trend, where models are expected to take action rather than simply respond to prompts. The article notes that the open-source OpenClaw ecosystem helped popularize this idea, and highlights that vendors are now racing to provide agent-like capabilities as part of their commercial offerings. Anthropic’s move puts Claude in direct competition with other platforms pursuing similar autonomy and workflow automation.

The feature is limited to qualifying subscription plans and appears to be restricted to macOS at launch. Claude will always request permission before taking actions, and users can interrupt or stop tasks at any time. Anthropic also encourages pairing the computer-use feature with Dispatch, which lets users assign tasks remotely via phone. The combination effectively turns Claude into a background operator that can do things like compile a morning briefing or run tests while the user is away.

Security and reliability concerns are central to the rollout. Giving an AI assistant control of a computer introduces risks such as prompt injection, accidental destructive actions, or data exposure. The article notes that Anthropic has built safeguards and automatic scanning for vulnerabilities, but also issues explicit warnings: the feature is new, may contain errors, and should not be trusted with sensitive applications. Some classes of apps are disabled by default to limit harm. The company frames this as a research preview precisely to gather feedback on what goes wrong and where safety and reliability need to improve.

Overall, the article frames Claude’s computer-control capability as a significant step in the evolution from conversational assistants to action-oriented agents. It promises clear convenience—delegating routine or remote tasks—but also underscores that the tradeoff is increased operational risk. Anthropic’s strategy is to ship early under controlled constraints, learn from real usage, and iterate toward a more dependable agent platform.