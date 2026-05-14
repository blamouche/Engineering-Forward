# How will AI change operating systems? Part 1: Ubuntu and Linux
**Source**: https://newsletter.pragmaticengineer.com/p/ubuntu-and-ai
**Date**: 2026-04-28
**Author**: Gergely Orosz (with Jon Seager, Canonical VP of Engineering)
**Keywords**: Ubuntu, Linux, operating systems, AI hardware, NPUs, DPUs, GPUs, local LLMs, CUDA, NVIDIA, AMD, Intel, agentic workflows

## Elevator pitch
Canonical is betting on hardware enablement and local-first LLMs as its AI strategy for Ubuntu, with deep partnerships across NVIDIA, AMD, and Intel yielding day-one support for next-generation AI accelerators.

## Takeaways
- Ubuntu's AI strategy focuses on hardware enablement rather than embedding AI features into the OS itself
- The OS now supports GPUs, NPUs, and DPUs, with simplified CUDA toolkit installation via a single apt command
- NVIDIA has abandoned its custom DGX OS in favor of vanilla Ubuntu, now shipping DGX Spark on ARM64 with Ubuntu
- Canonical is exploring OS-level support for agentic workflows and local model inference via "inference snaps"
- Other distros take varying approaches: Arch DIY, Omarchy simplified installs, and RHEL integrated AI into the CLI

## Synthesis
This deepdive investigates how AI is reshaping operating systems, starting with Linux and Ubuntu before a planned follow-up on Windows. Gergely Orosz interviews Jon Seager, VP of Engineering at Canonical, who articulates a deliberately restrained vision: rather than blurring the line between OS and application features, Ubuntu's most powerful contribution to AI is hardware enablement—ensuring that when users power on machines with AI accelerators, the hardware performs at its full potential.

The hardware landscape covered is comprehensive. GPUs, now predominantly used for AI training and inference rather than gaming, come from NVIDIA (dominating discrete GPU and data center markets with Blackwell) and AMD (Instinct series). NPUs, dedicated AI inference blocks on modern SoCs, have appeared since 2022 in Apple M-series, Intel Core Ultra, AMD Ryzen AI, and Qualcomm Snapdragon chips, promising low-power local inference for tasks like speech-to-text and video processing. DPUs, found in data centers, handle massive data movement—NVIDIA BlueField is the most widespread, with competition from AMD Pensando and Intel IPU cards.

Canonical's partnership strategy has yielded concrete results. The CUDA toolkit is now packaged directly in Ubuntu repositories, collapsing what was a multi-step manual installation into a single apt install—solving the notorious "dance" of matching Python versions, CUDA versions, and drivers. NVIDIA's confidence in this approach is demonstrated by discontinuing its custom DGX OS (a modified Ubuntu maintained for years) in favor of vanilla Ubuntu, with the $4,000 DGX Spark AI workstation shipping Ubuntu as its only supported OS. At CES 2026, Canonical announced day-one support for NVIDIA's Vera Rubin NVL72 rack-scale architecture in Ubuntu 26.04 LTS, with 15 years of enterprise support. Canonical maintains neutrality with similar partnerships across Intel, AMD, Qualcomm, and MediaTek, with Ubuntu 26.04 LTS becoming the first major distribution to natively package all three GPU compute stacks (NVIDIA CUDA, AMD ROCm, Intel OpenVINO).

Beyond hardware, Canonical is exploring a local-first AI future with "inference snaps" that help users select the right model and quantization level, and early exploration of OS-level agentic workflow support. Canonical's engineering culture has evolved from skepticism toward AI to one of encouraged experimentation—notably without targets for token usage or AI-generated code percentages. The article also surveys other Linux distributions: Arch Linux takes a "DIY your AI setup" approach, Omarchy simplifies AI tool installation, and Red Hat Enterprise Linux ships with AI-integrated command-line tools and accelerator support.
