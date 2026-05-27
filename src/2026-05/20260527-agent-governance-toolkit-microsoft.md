# Agent Governance Toolkit (Microsoft)
**Source**: https://github.com/microsoft/agent-governance-toolkit
**Date**: May 27, 2026
**Author**: Microsoft
**Keywords**: AI agents, governance, policy enforcement, zero-trust, sandboxing, OWASP, agentic security, Microsoft, open source, Claude Code, Copilot

## Elevator pitch
Microsoft's open-source Agent Governance Toolkit provides policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents, covering 10/10 OWASP Agentic Top 10 risks with SDKs in Python, TypeScript, Rust, Go, .NET, and integrations for Claude Code and Copilot CLI.

## Takeaways
- Comprehensive agent governance covering policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for production AI agents.
- Full coverage of the OWASP Agentic Top 10 — the first major toolkit to claim 10/10 coverage.
- Multi-language SDKs: Python, TypeScript, Rust, Go, .NET, plus dedicated integrations for Claude Code and Copilot CLI.
- Includes a CLI tool (antigravity) for governance operations, fuzz testing via ClusterFuzzLite, and Docker Compose deployment.
- Ships with pre-commit hooks, shellcheck, gitleaks, and safety policies — governance tooling eating its own dogfood.

## Synthesis
Microsoft has released the Agent Governance Toolkit as an open-source project (MIT license) addressing the rapidly emerging need for production-grade safety infrastructure around autonomous AI agents. The toolkit positions itself at the intersection of policy enforcement, identity, and execution control — three pillars that become critical when agents operate with real permissions in production environments.

The project's headline claim is comprehensive coverage of the OWASP Agentic Top 10, the emerging standard for agentic security risks. It provides language-specific SDKs across Python, TypeScript, Rust, Go, and .NET, alongside pre-built integrations for high-profile agent platforms: Claude Code (Anthropic) and GitHub Copilot CLI. This multi-platform approach suggests Microsoft is targeting governance as a horizontal layer that should work across different agent ecosystems, not just its own.

Under the hood, the toolkit bundles identity management (zero-trust principles), execution sandboxing, policy enforcement, and reliability engineering. A dedicated CLI tool ("antigravity") handles governance operations, while fuzz testing via ClusterFuzzLite and Docker Compose deployment indicate production-readiness. The project's own governance is notable — it includes pre-commit hooks, shellcheck, gitleaks, and safety policies, demonstrating that the governance toolkit itself follows the practices it enforces. With 14 contributors and active community engagement, this represents a significant open-source investment by Microsoft in the agent safety infrastructure layer.
