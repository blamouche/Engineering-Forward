# How Vercel Cut Build Wait Times From 90 Seconds to 5
**Source**: https://blog.bytebytego.com/p/how-vercel-cut-build-wait-times-from
**Date**: 2026-05-26
**Author**: ByteByteGo
**Keywords**: Vercel, build infrastructure, Firecracker, microVMs, multi-tenancy, Hive, build optimization, container isolation, platform engineering

## Elevator pitch
ByteByteGo dissects Vercel's internal build platform "Hive," which cut build provisioning from 90 seconds to 5 by accepting the harder constraint of hostile multi-tenancy, building on Firecracker microVMs, and layering three optimizations: cached container images, warm pools, and millisecond VM boot times.

## Takeaways
- Hive treats every customer build as potentially malicious ("hostile multi-tenancy"), a foundational assumption driving the entire architecture away from standard container orchestration.
- Firecracker microVMs provide VM-level isolation (separate kernels, CPU-enforced boundaries) at container-level speed — boot in ~125ms, use few MB of memory.
- Each build runs in a dedicated "cell" (microVM + container) that is destroyed after completion, eliminating cross-tenant state leakage risk.
- The 18x speedup comes from three layers: local container image caching (saved ~45s), warm cell pools (instant provisioning for common case), and Firecracker's baseline millisecond boot time.
- Overall build performance improved 30%, cold-path builds dropped 40%, with provisioning specifically going from 90s to 5s.

## Synthesis
ByteByteGo's deep dive into Vercel's Hive platform is a masterclass in infrastructure engineering where the constraints drive the architecture, not the other way around. The core insight is that Vercel accepted a harder problem — running untrusted third-party code on shared hardware — and that adversarial assumption cascaded through every design decision.

Standard Kubernetes would have been the lazy answer, but containers share a kernel, and one kernel exploit in a malicious build could compromise every tenant on the machine. Vercel needed VM-level isolation without VM-level overhead. Firecracker, AWS's open-source microVM engine (battle-tested on Lambda at millions of concurrent functions), provided exactly that: millisecond boot times, hardware-enforced isolation via CPU virtualization features, and minimal memory footprint.

The naming scheme (Hive → Box → Cell) maps cleanly to physical and logical boundaries. A Hive is a regional cluster with multiple Hives per region for failure isolation. A Box is a physical machine. A Cell is a Firecracker microVM with a container inside — each Cell handles exactly one build and is destroyed afterward, closing the door on cross-tenant state leakage.

The 90-to-5 second improvement isn't one breakthrough but three compounding optimizations. First, cold-start optimization: caching the build container image locally (instead of pulling from a remote registry) saved ~45 seconds, and block device snapshotting let new cells start from a saved clean state. Second, warm pools: pre-booted idle cells handle most builds with zero provisioning wait, with the 5-second figure only applying when the pool is empty. Third, Firecracker's baseline speed made warm pools viable in the first place — traditional VMs booting in 30-60 seconds would require an impossibly large pool.

The article is a reminder that the hardest infrastructure problems aren't about making things fast — they're about accepting a constraint (hostile multi-tenancy) that makes everything else harder, then building upward from that constraint. Hive is faster because it's more secure, not despite it.
