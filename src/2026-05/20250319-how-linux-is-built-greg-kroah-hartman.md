# How Linux Is Built with Greg Kroah-Hartman
**Source**: https://newsletter.pragmaticengineer.com/p/how-linux-is-built-with-greg-kroah
**Date**: March 19, 2025
**Author**: Gergely Orosz
**Keywords**: Linux, kernel, open source, Greg Kroah-Hartman, kernel development, Rust, git, maintainer

## Elevator pitch
Greg Kroah-Hartman, a 25-year Linux kernel maintainer and one of three Linux Kernel Foundation Fellows, reveals how the world's most widespread OS is built by 4,000 yearly contributors using only email and git with zero project managers and a strict 9-week release cadence.

## Takeaways
- Linux runs on 4 billion Android devices and is inside iPhones (Qualcomm 5G modem firmware), making it the most widespread OS globally
- 4,000 developers contribute yearly through a hierarchical maintainer trust model — changes flow up chains of maintainers until reaching Linus Torvalds
- The kernel has practically no meetings, no project managers, uses only email and git — project management happens outside the kernel
- 80% of kernel contributors are paid by employers because contributing is cheaper than building their own OS
- Linux won because "selfish" dev contributions solved common problems: embedded vendors made Linux more efficient, which later made it perfect for Android

## Synthesis
In this episode of The Pragmatic Engineer, Gergely Orosz interviews Greg Kroah-Hartman, who has served as a Linux kernel maintainer for 25 years and is one of only three Linux Kernel Foundation Fellows alongside Linus Torvalds and Shuah Khan. Greg manages the kernel's stable releases and maintains multiple kernel subsystems, making him one of the foremost authorities on how the world's most widespread operating system is actually built.

The scale of Linux's deployment is staggering and often underappreciated. Four billion Android devices run Linux — compared to which everything else is, as Greg puts it, "a rounding error." Beyond Android, it dominates servers and embedded devices, powers air traffic control systems, runs on the International Space Station, and even lives inside iPhones as the firmware for Qualcomm 5G modems. The kernel itself is approximately 40 million lines of code, though the core kernel every platform runs is only about 5% of that; the vast majority supports diverse hardware, drivers, and architectures.

The development process operates on a strict 9-week cadence with a two-week merge window where maintainers submit new features, followed by seven weeks of stabilization where only bug fixes and reverts are accepted. This discipline — no exceptions, no feature creep during stabilization — is a key reason the kernel maintains quality at its scale. The governance model is hierarchical: changes flow from individual developers to subsystem maintainers, then up the chain, ultimately reaching Linus Torvalds for the mainline kernel. Trust is the central currency: when a maintainer accepts code, they take personal responsibility for it, including if the original contributor disappears.

Perhaps the most counterintuitive aspect of Linux development is its extreme minimalism in process. A project with 4,000 yearly contributors operates with practically no meetings, no project managers, and just two tools: email and git. This works because project management happens outside the kernel — contributors arrive with completed work rather than requiring coordination. Heavy investment in automation (Linux Next for continuous integration, KernelCI for hardware testing, the "zero-day bot" for patch testing) substitutes for management overhead. Greg explicitly notes this model would not work for Linux distributions like Red Hat or Debian, which face fundamentally different coordination challenges.

The economic model is equally distinctive: 80% of contributors are paid by their employers. Companies invest in Linux because contributing features upstream is far cheaper than building and maintaining a custom operating system. The "selfish" motivation model — developers solving their own problems — paradoxically produces a general-purpose OS because many developers share the same problems. Embedded device vendors, for example, drove efficiency improvements that later made Linux the obvious choice for Android. Rust adoption is progressing with about 25,000 lines already in the kernel, driven by memory safety concerns and government mandates, though resistance from some core developers who prefer a single-language codebase remains. Greg's career advice is practical: contributing even a single patch to Linux demonstrates real-world collaboration skills and makes a resume stand out in a way that personal projects rarely match.
