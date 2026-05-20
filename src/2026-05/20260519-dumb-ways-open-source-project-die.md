# Dumb Ways for an Open Source Project to Die
**Source**: https://nesbitt.io/2026/05/19/dumb-ways-for-an-open-source-project-to-die.html
**Date**: May 19, 2026
**Author**: Andrew Nesbitt
**Keywords**: open-source, maintainers, supply-chain, dependencies, security, sustainability, burnout

## Elevator pitch
Andrew Nesbitt catalogs the many ways open source projects die — from ghost maintainers and corporate orphans to sabotage, platform obsolescence, and toxic gatekeeping — showing that a package resolving from a registry tells you nothing about whether it's actually alive.

## Takeaways
- Ghost maintainers (last human commit years ago, unanswered issues) are the most common death mode, indistinguishable from a long holiday until too many issues pile up
- Corporate orphans occur when a company builds and open-sources a project, then pivots or lays off the team — often nobody at the company even knows the project is theirs anymore
- "Benevolent zombies" are projects with solid green contribution graphs maintained entirely by bots (Dependabot, auto-merge, coding agents) — every recency-based health score rates them fine
- Captured maintainers (xz, event-stream) look healthier than before during the capture because the attacker is the one putting in the work
- About 1.7% of npm and 4% of Packagist packages point at a repo that no longer exists — and a fair number are still being installed

## Synthesis
Building on his earlier "Weekend at Bernie's" post that revealed how many critical open source packages are dead, Andrew Nesbitt provides a comprehensive taxonomy of failure modes. The piece reads like a field guide for dependency auditors, organized into broad categories: maintainers who left, maintainers who are still there but shouldn't be, sabotage and capture, broken release pipelines, force majeure events, obsolescence, and community fractures.

The most alarming category is "the maintainer is still there" — because these projects pass every automated health check. Benevolent zombies are maintained entirely by bots: Dependabot bumps trigger auto-merge rules, which trigger automated releases, and recency-based scores show perfect health. Toxic gatekeepers drive away every potential contributor through bruising code reviews, maintaining a bus factor of one while looking productive on every metric. Burnout plateaus produce just enough activity — typo fixes, "thanks, will look at this" — to deter forks without ever actually shipping.

The sabotage section is particularly sobering in light of xz. Captured maintainers are a worst-case scenario because the project appears healthier than before: the attacker is the one putting in work, responding to issues, shipping features. The legitimate maintainer handing over to a helpful volunteer is indistinguishable from a social engineering campaign until it's too late. Nesbitt also highlights protestware (colors, faker, node-ipc, left-pad) where the legitimate maintainer deliberately breaks their own package — a different failure mode but the same downstream impact.

The registry orphan statistics are striking: 1.7% of npm and 4% of Packagist packages reference a repo that no longer exists. These packages still resolve, still install, and there's no way to verify the tarball matches anything that was ever in source control. The piece ends with the recursive insight that every failure mode listed is also a way to kill the things that depend on you — transitive death through the supply chain. As Nesbitt concludes: your lockfile will keep wheeling the dead project around "for as long as nobody checks too closely."
