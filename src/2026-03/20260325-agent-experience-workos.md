# Agent Experience: Build without leaving your terminal
**Source**: https://workos.com/blog/agent-experience
**Date**: March 25, 2026
**Author**: WorkOS
**Keywords**: WorkOS, CLI, agent workflows, configuration, AuthKit

## Elevator pitch
WorkOS launches “Agent Experience,” a set of CLI‑first upgrades so coding agents can configure, diagnose, and manage WorkOS environments without dashboard clicks.

## Takeaways
- WorkOS Skills ship with the CLI to give agents native knowledge.
- AuthKit can be tried without creating an account via an unclaimed environment.
- workos doctor provides diagnostic checks for misconfigurations.
- CLI commands now set redirect URIs and webhooks without dashboards.
- workos seed enables declarative environment setup via YAML.

## Synthesis
WorkOS’s “Agent Experience” announcement reframes its platform for coding‑agent workflows. The company argues that most infra tools still assume a human will complete UI‑based setup steps—creating redirect URIs, configuring webhooks, and debugging environments—breaking the agent loop. The new release aims to make WorkOS fully operable by agents from the terminal.

The launch bundles six upgrades. First, the WorkOS CLI now installs WorkOS Skills, giving agents a built‑in understanding of the platform’s concepts and integration steps. Second, developers can now try AuthKit without creating an account: the CLI spins up an unclaimed environment so an agent can scaffold and test an auth flow immediately. Third, `workos doctor` adds diagnostics that detect common configuration mismatches, such as inconsistent redirect URIs or environment variables.

Fourth, the CLI can now perform configuration tasks previously restricted to the dashboard—setting redirect URIs and managing webhook endpoints—keeping the entire integration loop in the terminal. Fifth, `workos seed` introduces declarative environment setup: a YAML file defines roles, permissions, organizations, and config, and the CLI applies it idempotently. This allows agents to maintain desired state without manual steps. Sixth, new resource commands expose live environment data (roles, permissions, audit logs, directories, users), enabling agents to verify system state instead of merely suggesting changes.

The post argues that these features together change the development rhythm. Instead of writing code and then manually configuring the dashboard, developers can define environment state as code, apply it via CLI, run diagnostics, and verify results—everything within the agent’s control loop. This is positioned as essential for agent‑driven development, where latency and context switches reduce productivity.

Overall, “Agent Experience” is less about a new product and more about making WorkOS agent‑native. By moving setup, configuration, and diagnostics into CLI workflows, WorkOS aims to become a platform that agents can reliably operate without human intervention, making integration faster and more reproducible.
