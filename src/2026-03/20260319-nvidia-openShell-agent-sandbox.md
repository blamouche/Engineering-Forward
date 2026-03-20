# OpenShell: Safe, Private Runtime for Autonomous AI Agents
**Source**: https://github.com/NVIDIA/OpenShell
**Date**: 2026-03-19
**Author**: NVIDIA
**Keywords**: NVIDIA, OpenShell, AI agents, sandbox, security, Kubernetes, policy enforcement, Claude, Codex

## Elevator pitch
NVIDIA OpenShell is an Apache-2.0 containerized sandbox platform that enforces YAML-declared policies over AI agent actions—governing filesystem, network, process, and inference layers—for developers running Claude, OpenCode, and Codex locally.

## Takeaways
- Enforces declarative YAML security policies across four protection layers: filesystem, network, process, and inference
- Runs as a Kubernetes cluster (K3s) inside a single Docker container, enabling single-command setup without Kubernetes expertise
- Hot-reloadable network policies allow updating security rules without restarting running agents
- GPU passthrough enables local inference workloads within the sandbox
- Alpha software for individual developers (single-player mode); Apache 2.0 licensed; 2.5K stars

## Synthesis
OpenShell reflects NVIDIA's recognition that the AI agent security problem requires purpose-built infrastructure rather than repurposed general-purpose tools. Traditional sandboxing solutions (Docker containers, virtual machines) provide isolation but not the fine-grained behavioral policy enforcement that AI agents require. An AI agent can be fully containerized yet still make problematic network calls, access sensitive files, or execute unexpected processes—because containers restrict capabilities but don't enforce intent-based policies.

The four-layer policy architecture addresses this. Filesystem policies control which paths agents can read and write. Network policies specify which hosts, protocols, and methods are permitted. Process policies govern which commands can be executed and with what privileges. Inference policies—the most novel layer—control how the agent can interact with AI model APIs, including rate limiting, input filtering, and output inspection. Together these layers enable developers to express "this agent should be able to read source files, write to a specific output directory, call the OpenAI API, and nothing else" in a way that is actually enforced rather than merely intended.

The K3s-in-Docker implementation makes this functionality accessible to individual developers who lack Kubernetes expertise. Running a production-grade container orchestration system would normally require substantial infrastructure knowledge. By wrapping K3s inside a single Docker container, OpenShell reduces the setup complexity to a single command, enabling developers to benefit from Kubernetes-grade policy enforcement without operating a Kubernetes cluster.

Hot-reloadable network policies are a significant operational quality of life feature. Security policies need to evolve as agent tasks change—a research agent needs different network access than a code-writing agent. Without hot reload, updating policies requires restarting containers and losing agent state. Hot reload enables policy adjustment without interrupting running sessions.

The alpha/single-player designation is an honest acknowledgment of current scope. Multi-tenant environments with multiple users running agents against shared infrastructure require additional isolation and audit capabilities that OpenShell doesn't yet provide. The current target—individual developers running agents on their own machines—is the right initial scope for gathering feedback before addressing the harder multi-tenant problem.
