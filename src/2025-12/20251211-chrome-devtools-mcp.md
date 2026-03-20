# Let Your Coding Agent Debug Your Browser Session with Chrome DevTools MCP
**Source**: https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session
**Date**: 2025-12-11
**Author**: Sebastian Benz, Alex Rudenko
**Keywords**: Chrome DevTools, MCP, debugging, coding agent, browser session, remote debugging, Claude Code

## Elevator pitch
Chrome DevTools MCP now lets coding agents connect directly to active browser sessions, enabling agents to debug authenticated features and investigate issues identified during live developer sessions without requiring separate login flows.

## Takeaways
- Coding agents can now attach to existing browser sessions, eliminating the need for repeated sign-ins when debugging authenticated features
- Available in Chrome M144 (beta) with remote debugging enabled at `chrome://inspect/#remote-debugging`
- Configured with `--autoConnect` flag; Chrome shows permission dialog and "controlled by automated software" banner for each connection
- Two primary use cases: reusing authenticated sessions for testing, and handing off DevTools investigations to AI agents
- Security model requires explicit user permission per connection, with visible indicators during agent control

## Synthesis
Chrome's DevTools MCP integration represents a significant practical advance in how AI coding agents can assist with browser debugging. Previously, agents interacting with web applications faced a fundamental limitation: they operated in fresh browser contexts without the authentication state, cookies, and accumulated session data that characterize real user environments. Debugging an authentication-protected feature required either exposing credentials to the agent or building elaborate session setup automation.

The session reuse capability eliminates this friction by allowing the agent to attach to an existing authenticated browser session. A developer can sign in normally, navigate to the area they want to debug, then hand control to their coding agent without any credential sharing or session setup automation. The agent inherits the full browser state including cookies, localStorage, IndexedDB, and any dynamic session tokens.

The second capability—handing off DevTools investigations to AI agents—addresses a different workflow. When a developer identifies a problem through manual DevTools exploration (a failed network request, an unexpected element state, a JavaScript error), they can show the agent exactly what they found and ask it to investigate further. The agent can then use the same DevTools capabilities the developer was using—network inspection, DOM querying, console execution—to build a more comprehensive picture of the problem.

The security design reflects appropriate caution. Each agent connection requires an explicit permission dialog, and an always-visible banner indicates when the browser is under automated control. These mechanisms ensure the developer remains aware of and consenting to AI access to their browser session. The opt-in configuration (remote debugging must be explicitly enabled) means the capability is not active by default and requires deliberate developer choice to activate.

The Chrome M144 beta timing indicates this is early-stage tooling, but the underlying integration pattern—coding agents as first-class participants in the browser debugging workflow—represents a durable architectural direction for web development tooling.
