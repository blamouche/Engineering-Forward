# How Will AI Change Operating Systems? Part 2: Windows
**Source**: The Pragmatic Engineer (pragmaticengineer+deepdives@substack.com)
**Date**: 2026-09-22
**Author**: Gergely Orosz (The Pragmatic Engineer)
**Keywords**: Windows, Microsoft, AI agents, operating systems, MCP, WindowsML, MXC, agent isolation, local models, WSL, ARM, developer experience

## Elevator pitch
Microsoft reveals its plan to make Windows an agent-native operating system — with built-in agent identity, MCP tool registries, sandboxed execution containers, local model inference, and a renewed push to win back developers who abandoned the platform.

## Takeaways
- **Agent identity and discovery built into the OS**: Windows ships with agent identification via Entra ID, where agents appear as separate users in Task Manager, and the On Device Agent Registry (ODR) provides a centralized MCP server registry for tool discovery.
- **Microsoft Execution Containers (MXC) for agent isolation**: A new containment technology lets developers spawn agentic tools in isolated sandboxes with configurable levels — process, session, WSL containers, Hyper-V, or full VMs — balancing speed against blast radius.
- **WindowsML: DirectX for AI**: A hardware-agnostic abstraction layer running on ONNX runtime that supports GPUs, NPUs, and CPUs from all vendors, eliminating the driver-update bottleneck that plagued DirectML.
- **Embedded small language models in the OS**: SLMs like Aion-1.0-Instruct are built into Edge, enabling apps to use LLM-powered features (sentiment analysis, etc.) without cloud calls or per-token costs.
- **Windows developer share is declining**: Surveys suggest macOS may overtake Windows as the most-used standalone developer OS, with Linux also gaining — Microsoft needs to win back developer goodwill.
- **WSL is the strategic bridge**: Windows Subsystem for Linux is proving popular with developers, and Microsoft's embrace of Linux within Windows may be the counterintuitive strategy to reclaim developers from both native Linux and macOS.
- **ARM on Windows finally viable**: Windows on ARM is looking like a real alternative, with upcoming NVIDIA collaborations and a Surface laptop demo running Qwen locally at ~40 tokens per second.

## Synthesis
This is one of the most detailed public looks at how a major operating system is being rearchitected for the age of AI agents. Microsoft's approach is comprehensive and opinionated: agents are not just applications but first-class OS citizens with identities, registries, isolation boundaries, and local compute resources. The On Device Agent Registry (ODR) acting as a proxy between MCP clients and servers is particularly significant — it gives Windows an inspection choke point for all agent-tool interactions, enabling security monitoring without breaking the MCP protocol.

The MXC isolation framework is the piece most relevant to engineering teams building agents today. The idea that an agent's tools should run in containers with policy-defined network, filesystem, and UI restrictions — with the containment level adjustable to the sensitivity of the operation — is exactly the architecture that production agent deployments need. The fact that MXC already runs on Windows, Linux, and macOS, and that OpenClaw is cited as one of the first agents to adopt it, suggests this could become a cross-platform standard.

WindowsML as "DirectX for AI" is an apt analogy. Just as DirectX abstracted graphics hardware complexity and enabled a generation of games to run across diverse GPU vendors, WindowsML aims to do the same for AI inference. The ONNX-based approach with vendor-specific execution providers is technically sound, and the elimination of the six-month driver-update bottleneck is a meaningful improvement over DirectML. The embedded SLM strategy — where the OS ships with models that apps can call like any local library — could fundamentally change the economics of AI-powered features in desktop applications.

The developer share data is the strategic context for all of this. Microsoft is not building agent-native Windows out of pure innovation enthusiasm — it's fighting to remain relevant to developers who have drifted to macOS and Linux. The WSL-ARM-local-model combination is a credible strategy: give developers Linux tools, ARM performance, local AI inference, and agent-native primitives, all in one machine. Whether it's enough to reverse the trend depends on execution, but the ambition is genuine.