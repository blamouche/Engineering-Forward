# LiteLLM Agent Platform — Self-Hosted Agent Infrastructure with Sandboxes and Vault Proxy
**Source**: https://github.com/BerriAI/litellm-agent-platform
**Date**: 2026-05
**Author**: BerriAI
**Keywords**: agent platform, self-hosted, sandbox, Claude Code, Codex, Hermes, coding agents, credential vault, Kubernetes, agent infrastructure

## Elevator pitch
LiteLLM Agent Platform provides self-hosted infrastructure for running coding agents (Claude Code, Codex, Hermes) inside isolated Kubernetes sandboxes with a credential vault that swaps stub credentials for real keys, so agents never see your actual secrets.

## Takeaways
- Agents run with bypass-permissions in sandbox pods that contain only stub credentials — the vault swaps them for real keys on every outbound TLS connection
- The `lap` CLI attaches your local terminal to a Kubernetes pod's TTY over WebSocket, giving a native terminal experience with 24-hour session persistence
- Supports multiple harnesses (Claude Code, Codex, Hermes) with a unified web UI, CLI, and REST API for agent management
- Self-hosting uses kind for local dev or AWS EKS for production, with a one-click Render Blueprint for web and worker components
- Architecture separates web UI (:3000), worker processes, Postgres, and sandbox pods on Kubernetes with agent-sandbox CRD

## Synthesis
As coding agents proliferate, the infrastructure challenge shifts from "can I run an agent?" to "can I run agents securely at scale?" LiteLLM Agent Platform addresses this by providing a complete self-hosted platform where agents execute inside isolated Kubernetes sandboxes with a credential vault proxy. The vault is the key architectural innovation: agent pods contain only stub credentials (e.g., GITHUB_TOKEN=stub_github_a8f1), and the vault swaps them for real keys on every outbound TLS connection. Agents run with bypass-permissions enabled but never touch actual secrets.

The developer experience centers on the `lap` CLI, which connects a local terminal to a sandbox pod over WebSocket, giving the same experience as running Claude Code or Codex locally — but with the security guarantees of pod isolation. Sessions persist for 24 hours after detach. The platform also offers a web UI for agent creation and management, plus a REST API for programmatic control.

Local development uses kind (Kubernetes in Docker) with a single `bin/kind-up.sh` script that provisions the cluster, installs the agent-sandbox controller, and loads harness images. Production deployment targets AWS EKS for sandbox clusters with Render for web and worker components. The platform supports Claude Code, Codex, and Hermes as harnesses, with agent templates for quick configuration.

Built by the team behind LiteLLM (the popular AI gateway), the platform reflects a growing understanding that agent infrastructure needs to solve for credential management, sandboxing, and multi-agent orchestration as table stakes — not afterthoughts. At 431 stars and 41 forks, it's gaining traction in the self-hosted agent platform space.
