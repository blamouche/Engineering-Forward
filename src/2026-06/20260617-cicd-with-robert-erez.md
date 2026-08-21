# CI/CD with Robert Erez

**Source**: https://newsletter.pragmaticengineer.com/p/cicd-with-robert-erez
**Date**: 2026-06-17
**Author**: Gergely Orosz
**Keywords**: cicd, devops, kubernetes, gitops, deployment, progressive-delivery, platform-engineering

## Elevator pitch

Robert Erez of Octopus Deploy shares hard-won lessons on CI/CD, GitOps, progressive delivery, and how AI is shifting the calculus from speed to risk—making the case that continuous delivery beats continuous deployment and feature flags trump rollbacks.

## Takeaways

- Roll forward, never backward: when a system has state (databases), rolling back to v1 can leave code talking to an out-of-sync schema—pushing v3 with the fix is safer and faster.
- GitOps isn't actually about Git: none of the four pillars (declarative, versioned and immutable, pulled not pushed, continuously reconciled) require Git—yet the term has made the industry dogmatic about cramming secrets into repos where they don't belong.
- Continuous delivery is more practical than continuous deployment: shipping every change to prod automatically isn't as necessary as many think; the real value is validating that the deployment process works, then choosing when to push.
- Feature toggles are a better safety net than rollbacks: switching off a broken feature stops the bleeding instantly, which is less nerve-wracking than forcing a midnight redeployment.
- AI shifts the CI/CD calculus from speed to risk: when an agent babysits a slow pipeline without context-switching, the priority becomes running more thorough (and slower) tests to reduce the risk of an agent shipping bugs to production.

## Synthesis

Gergely Orosz's conversation with Robert Erez—a principal engineer at Octopus Deploy and veteran of Skype's web team—cuts through the hype around modern deployment practices with practical, experience-backed observations. The episode covers Kubernetes, GitOps, platform engineering, progressive delivery, feature flags, cloud development environments, and AI's growing role in CI/CD workflows.

The most immediately actionable insight is the roll-forward principle. When a deployment fails and the system has state—which means almost every production system with a database—rolling back to the previous version can create a dangerous mismatch between code and schema. Erez's advice: treat a v2 failure as an opportunity to push v3 with the fix, not a reason to retreat to v1. This is a mental model shift that eliminates the need for complex rollback machinery.

Erez's critique of GitOps is similarly grounded. The four pillars that define GitOps—declarative configuration, versioned and immutable state, pull-based reconciliation, and continuous reconciliation—don't actually require Git. Yet the industry has conflated the methodology with the tool, leading teams to store secrets in repositories and accept Git-based bottlenecks at scale. When thousands of Kubernetes clusters pull state from a single repo, throttling becomes a real constraint. The insight: use the principles, question the tooling orthodoxy.

The continuous delivery versus continuous deployment distinction matters more than most teams realize. Continuous deployment—shipping every change to production automatically—sounds rigorous but isn't always necessary. Continuous delivery—ensuring every change flows through testing and that the deployment process itself is validated—gives teams the option to push when ready, which is often weekly rather than continuously.

Feature flags emerge as the superior safety mechanism. Rather than rolling back a deployment at 3 AM, a feature toggle lets you switch off the offending functionality instantly while you diagnose. The caveat: flags are addictive, and teams must treat flag cleanup as regular gardening.

The AI observation may be the most forward-looking. Today, shaving minutes off CI build times matters because humans context-switch during long waits. When an AI agent is babysitting the pipeline, that urgency disappears. The new priority becomes thoroughness: running more tests, including slower ones, to reduce the risk of an agent shipping bugs. This inverts the traditional CI/CD optimization narrative—speed for humans, safety for agents.