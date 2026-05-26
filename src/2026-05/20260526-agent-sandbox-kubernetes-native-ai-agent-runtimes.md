# Agent Sandbox: Kubernetes-native AI agent runtimes
**Source**: https://github.com/kubernetes-sigs/agent-sandbox
**Date**: May 26, 2026
**Author**: Kubernetes SIG Apps
**Keywords**: Kubernetes, agent sandbox, CRD, AI runtimes, container isolation, sandboxing, cloud-native

## Elevator pitch
Kubernetes SIG Apps introduces agent-sandbox, a Custom Resource Definition (CRD) and controller designed to manage isolated, stateful, singleton workloads — the ideal primitive for running AI agent sandboxes with stable identity, persistent storage, and hibernation.

## Takeaways
- agent-sandbox fills a gap in Kubernetes: Deployments are stateless, StatefulSets are numbered sets — neither fits long-running singleton workloads like AI agent runtimes
- Core Sandbox CRD provides stable identity, persistent storage, and lifecycle management (creation, scheduled deletion, pausing, resuming)
- Extensions include SandboxTemplate (reusable templates), SandboxClaim (template-based creation), and SandboxWarmPool (pre-warmed sandboxes for fast allocation)
- Targets AI agent runtimes, dev environments, notebooks, and stateful single-pod services
- Future roadmap: strong isolation (gVisor/Kata), deep hibernation, memory sharing, and programmable API consumption

## Synthesis
The Kubernetes SIG Apps community has released agent-sandbox, a project that introduces a new `Sandbox` Custom Resource Definition (CRD) and controller to Kubernetes. The motivation is straightforward: existing Kubernetes abstractions don't fit long-running, stateful, singleton workloads — the exact pattern needed for AI agent runtimes, development environments, and persistent single-container sessions.

The core `Sandbox` CRD manages a single, stateful pod with a stable hostname, persistent storage that survives restarts, and lifecycle operations including scheduled deletion, pausing, and resuming. This is deliberately designed as a lightweight, single-container VM experience built on Kubernetes primitives — filling the gap between stateless Deployments and numbered StatefulSets.

The extensions layer adds three additional CRDs. `SandboxTemplate` defines reusable configurations for creating sandboxes at scale. `SandboxClaim` abstracts creation details, letting users request sandboxes from templates without understanding the underlying configuration. `SandboxWarmPool` manages pre-warmed sandboxes that can be allocated instantly, addressing the cold-start problem that makes agent workflows feel sluggish.

The architecture follows the standard Kubernetes controller pattern: users create Sandbox custom resources, and the controller manages the underlying pods and runtimes. The Python SDK provides programmatic access for agents and applications to create and manage their own sandboxes.

The project's desired characteristics reveal ambitious long-term thinking. Strong isolation via gVisor or Kata Containers is planned for running untrusted code — critical for executing LLM-generated content safely. Deep hibernation would save state to persistent storage and potentially archive the Sandbox object. Memory sharing across sandboxes on the same host is being explored. Rich identity and connectivity features would provide dual user/sandbox identities and efficient traffic routing without requiring per-sandbox Services.

The project is community-driven under SIG Apps, with an experimental AI-assisted code review workflow using GitHub Copilot as a first-pass reviewer. The Python SDK, documentation site, and example configurations are already available, making this a production-ready tool for teams building agent infrastructure on Kubernetes.
