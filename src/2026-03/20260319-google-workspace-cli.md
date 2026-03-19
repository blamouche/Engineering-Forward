# Google Workspace CLI (gws)
**Source**: https://github.com/googleworkspace/cli
**Date**: Unknown
**Author**: Google Workspace team
**Keywords**: CLI, Google Workspace, API, automation, AI agents, Drive, Gmail, Calendar, Sheets, Docs, open source

## Elevator pitch
A unified command-line interface that dynamically builds itself from Google's Discovery Service, enabling humans and AI agents to interact with all Google Workspace services through structured JSON outputs and agent skills—with zero boilerplate required.

## Takeaways
- Dynamic API Surface: Rather than shipping a static command list, gws reads Google's Discovery Service at runtime, automatically incorporating new API endpoints as they're released.
- Multiple Auth Flows: Supports interactive OAuth, service accounts, pre-obtained tokens, and credentials files—designed to work on laptops, in CI/CD pipelines, and on servers alike.
- AI-Ready Architecture: Every response outputs structured JSON; 100+ agent skills and Gemini extension support enable LLMs to manage Workspace without custom tooling.
- Helper Commands: Curated high-level commands (prefixed with `+`) handle common workflows like email replies, spreadsheet appends, and calendar agendas with intelligent defaults.
- Enterprise-Grade Security: Credentials encrypt at rest using AES-256-GCM with OS keyring storage; Model Armor integration scans responses for prompt injection risks.

## Synthesis
The gws CLI represents a paradigm shift in how developers and agents interact with enterprise platforms. Rather than maintaining a brittle SDK that falls out of sync with API changes, the tool embraces Google's own metadata layer—the Discovery Service—to stay perpetually current. This design eliminates the traditional friction of API onboarding: users don't memorize endpoint paths or parameter schemas; they ask the CLI for help and get intelligent guidance.

The authentication architecture reflects real-world complexity. Whether you're running commands on your workstation, scripting in GitHub Actions, or deploying to a server, gws accommodates your constraints. Encrypted local credentials, environment variable tokens, service account keys, and OAuth flows all coexist without conflict, prioritized sensibly so the most secure option (explicit token) wins if present.

For AI agents, the implications are profound. Existing tools force agents to parse unstructured text or reconstruct APIs from documentation. gws hands agents structured JSON and pre-built skills—domain knowledge about Gmail threading, Calendar timezones, or Sheets ranges—baked into the CLI itself. An agent can reason about data directly rather than fighting command syntax.

The helper commands deserve special attention. These aren't trivial wrappers; they encode months of design decisions about common patterns. The `+agenda` command, for instance, automatically fetches your Calendar timezone and respects it, eliminating the friction of manual timezone conversions. Similarly, `+reply` handles email threading transparently—a surprisingly complex detail that most tools punt to the user.

Security considerations run throughout. Credentials don't litter the filesystem as plaintext; they're locked with OS-native keyrings or AES encryption. Model Armor integration allows responses to be scanned for prompt injection before they reach an LLM, a critical safeguard for agent-driven workflows. These aren't afterthoughts—they're baked into the command lifecycle.

The project acknowledges its pre-1.0 status, signaling that the API surface may shift. This honesty is refreshing and reflects a commitment to stability over premature frozen design.

Ultimately, gws solves a fundamental problem: how to build a single tool that scales from individual developers on macOS to AI agents in production clusters, across dozens of APIs, without forcing users to master each service's quirks separately. By delegating to Google's own service metadata and bundling high-level skills, it achieves an elegant balance between flexibility and usability.
