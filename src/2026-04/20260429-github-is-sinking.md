# GitHub is sinking

**Source**: https://dbushell.com/2026/04/29/github-is-sinking
**Date**: April 29, 2026
**Author**: David Bushell
**Keywords**: github, developer-tools, open-source, forgejo, git

## Elevator pitch
David Bushell argues that GitHub's reliability, incentives, and product direction have degraded enough that developers should actively plan their exit to other Git forges or self-hosted options.

## Takeaways
- The post ties GitHub's decline to Microsoft-era reliability problems, product sprawl, and AI-driven clutter.
- Bushell emphasizes that Git is distributed infrastructure and should not be conflated with GitHub as a hosted service.
- He argues that network effects and CI convenience are weaker defenses than developers assume.
- The recommended alternatives range from Codeberg and Forgejo to GitLab, Gitea, and self-hosting.
- The core advice is to maintain an exit plan before platform dependence becomes too costly.

## Synthesis
David Bushell's essay is a blunt critique of GitHub's trajectory and a broader reminder about infrastructure dependency in developer workflows. He argues that GitHub has become less reliable, more cluttered, and more shaped by Microsoft's incentives, especially around AI-related product bloat and the erosion of the focused experience that made the platform attractive in the first place. The most useful part of the piece is not the rant itself but the reframing: GitHub is not Git. Git remains open, distributed, and portable, while GitHub is only one centralized service layered on top of it. That distinction matters because many teams now treat GitHub as synonymous with source control, which makes migration feel harder and riskier than it really is. Bushell also pushes back on common lock-in arguments, especially around network effects and GitHub Actions, arguing that these are conveniences rather than irreplaceable foundations. His proposed alternatives include community-run forges, commercial platforms, and self-hosted setups. The deeper point is that code collaboration platforms are becoming strategic dependencies, and teams should think about resilience, governance, and exit options before quality or policy shifts force a rushed move.
