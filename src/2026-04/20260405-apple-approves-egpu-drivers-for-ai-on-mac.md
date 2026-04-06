# Apple approves drivers that let AMD and Nvidia eGPUs run on Mac — software designed for AI, though, and not built for gaming

**Source**: https://www.tomshardware.com/pc-components/gpu-drivers/apple-approves-drivers-that-let-amd-and-nvidia-egpus-run-on-mac-software-designed-for-ai-though-and-not-built-for-gaming
**Date**: April 5, 2026
**Author**: Jowi Morales
**Keywords**: Apple, Mac, eGPU, AMD, Nvidia, AI workloads, drivers

## Elevator pitch
Apple has approved third-party drivers that let AMD and Nvidia external GPUs run on Macs for AI workloads, signaling a practical but narrow reopening of accelerated compute on Apple hardware.

## Takeaways
- Apple appears willing to support external GPU acceleration again on Macs, but only for software paths aimed at AI and compute workloads rather than gaming.
- The change matters because it gives developers a way to pair Apple laptops or desktops with stronger off-device acceleration without fully leaving the Mac environment.
- This is not a return to the old eGPU era on macOS: the support is constrained, workload-specific, and shaped by driver approvals rather than broad graphics compatibility.
- Tiny Corp’s work continues to show that the demand for AI-oriented hybrid setups is outpacing the platform assumptions of traditional PC and Mac product lines.
- The development reinforces a broader trend in AI infrastructure: users increasingly want flexible local inference setups that mix consumer devices with specialized accelerators.

## Synthesis
This story is interesting less because it revives eGPU nostalgia and more because it shows how AI workloads are changing the boundaries of hardware support. For years, Apple Silicon Macs have been positioned as vertically integrated systems where the GPU story is largely settled by Apple’s own chips. External GPUs, especially from Nvidia, seemed like a dead end on modern Macs. The approval of drivers that enable AMD and Nvidia eGPUs for AI-oriented software suggests that this boundary is becoming more negotiable when machine learning workloads are involved.

The distinction matters. The article does not describe a general reopening of gaming-class eGPU support on macOS. Instead, it points to a narrower path where third-party acceleration is tolerated because it serves a different market: developers and researchers running AI software. That reflects a larger industry reality. AI has created a new class of users who care less about traditional graphics pipelines and more about access to memory bandwidth, CUDA-class ecosystems, and local model execution. In that context, a Mac paired with an external accelerator becomes a productivity tool rather than a gaming rig.

There is also a strategic tension underneath this. Apple has invested heavily in presenting its own silicon as a complete hardware-software stack for AI, especially around on-device inference and tightly integrated performance. Allowing Nvidia or AMD eGPUs into part of that workflow could look like a concession. But it may be a practical one. Developers often choose tools based on where the models, frameworks, and performance options are best, not on platform purity. If Mac users want to stay in the Apple ecosystem while attaching external accelerators for specialized tasks, blocking that entirely risks pushing them toward Linux or Windows workstations instead.

The broader lesson is that AI infrastructure is making previously niche hardware configurations economically relevant again. External accelerators, USB4-attached GPUs, and mixed-device local setups used to feel like enthusiast territory. Now they are becoming part of the practical experimentation stack for people building and testing models locally. Apple’s approval does not mean the platform has embraced open-ended hardware modularity. But it does show that AI demand is strong enough to reopen doors that mainstream product strategy had largely closed.
