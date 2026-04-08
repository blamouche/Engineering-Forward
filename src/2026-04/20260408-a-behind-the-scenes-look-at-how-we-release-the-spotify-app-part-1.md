# A Behind-the-Scenes Look at How We Release the Spotify App (Part 1)

**Source**: https://engineering.atspotify.com/2025/04/how-we-release-the-spotify-app-part-1
**Date**: April 2025
**Author**: Spotify Engineering
**Keywords**: release management, trunk-based development, staged rollout, mobile releases, spotify

## Elevator pitch
Spotify details the human and process side of its weekly mobile release machine, from nightly internal builds through branch cut, regression testing, store submission, and gradual rollout.

## Takeaways
- The release team balances short merge-to-user time against strict quality thresholds.
- Major launches are isolated through coordination and backend flags rather than long-lived branches.
- The process relies on constant telemetry, bug triage, and explicit release-blocker handling.
- Manual regression remains selective and focused, not a blanket ritual for every team.
- The article makes clear that disciplined process still matters even with strong tooling.

## Synthesis
Part 1 is valuable because it shows the socio-technical layer of release engineering. The mechanics are familiar—nightly builds, branch cut, testing, rollout—but the interesting detail is the release manager’s role in prioritization, coordination, and deciding what risk is acceptable now versus next week. Spotify’s weekly cadence works because the process narrows what must be perfect in the current release and defers the rest. That is a strong argument for frequent shipping: a shorter cycle lets teams classify more issues as “next release” without losing responsiveness. The feature-flag examples also underline how product rollout planning and release engineering are inseparable at scale.
