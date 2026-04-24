# I am building a cloud

**Source**: https://crawshaw.io/blog/building-a-cloud
**Date**: April 22, 2026
**Author**: David Crawshaw
**Keywords**: cloud infrastructure, developer experience, NVMe, agents, abstractions, exe.dev

## Elevator pitch
David Crawshaw argues that today’s cloud abstractions are poorly shaped for modern software and AI-agent workflows, and presents exe.dev as an attempt to rebuild cloud primitives around directly managed compute, local NVMe storage, and lower-friction operations.

## Takeaways
- Crawshaw thinks the main problem with current cloud platforms is not just bad UX but the shape of their core abstractions.
- He argues that tying virtual machines to fixed instance bundles limits developers who really want programmable pools of CPU, memory, and disk.
- Remote block storage and hyperscaler networking economics are presented as especially outdated and expensive constraints.
- Kubernetes is framed less as a clean solution than as a coping layer over clouds that remain hard to use and hard to port.
- The rise of agents matters because cheaper software creation increases the need for simpler, more flexible places to run software.

## Synthesis
Crawshaw’s essay is a founder manifesto, but it is also a clear statement about how AI-era software changes infrastructure expectations. His core claim is that cloud platforms have normalized abstractions that are no longer well matched to how developers want to work. The complaint is not merely that hyperscaler interfaces are ugly or expensive, though he says both are true. It is that core primitives such as instance sizing, remote block storage, and managed networking were optimized around older operational assumptions and provider convenience rather than around the needs of people building software today.

The storage argument is especially sharp. Crawshaw notes that remote block devices made more sense when spinning disks dominated and network overhead was relatively modest compared with seek times. In an SSD and NVMe world, that tradeoff looks much worse. Local disks can be dramatically faster, yet mainstream cloud design still pushes developers toward slower, more abstracted storage layers because they simplify provider operations. He makes a similar case for networking and egress pricing, arguing that clouds turn technically straightforward capabilities into economic lock-in.

What makes the piece timely is the link to agents. If software becomes easier to produce, then the friction of deploying and operating it becomes more visible. Crawshaw’s point is that agents can drive painful APIs, but they cannot erase poor abstractions. In fact, bad abstractions consume agent context and increase the amount of machine effort needed to accomplish basic infrastructure work. That is an interesting inversion of the usual AI story. Rather than agents making current clouds good enough, he argues they raise the premium on simpler infrastructure because software creation will expand faster than operational complexity becomes tolerable.

Exe.dev is introduced as one answer: buy resources directly, run the VMs you want, keep storage local, and place systems behind sane networking defaults. Whether that specific product wins is less important than the diagnosis. The piece suggests that the infrastructure stack many teams accepted during the SaaS era may become a bigger bottleneck in an agentic era, when the volume of software rises and developers expect environments that feel closer to programmable computers than to provider-shaped service catalogs.
