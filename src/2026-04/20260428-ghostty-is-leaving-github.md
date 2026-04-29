# Ghostty Is Leaving GitHub

**Source**: https://mitchellh.com/writing/ghostty-leaving-github
**Date**: April 28, 2026
**Author**: Mitchell Hashimoto
**Keywords**: GitHub, Ghostty, open source hosting, developer productivity, platform reliability

## Elevator pitch
Mitchell Hashimoto's decision to move Ghostty off GitHub turns general frustration with outages and product drift into a concrete signal that infrastructure reliability, not just ideology, can now justify leaving the default home of open source.

## Takeaways
- Hashimoto frames the move as the result of sustained operational pain, not a symbolic protest timed to a single outage.
- The argument centers on developer productivity, with GitHub increasingly described as an obstacle to review and shipping work.
- Ghostty will move incrementally while keeping a read-only mirror on GitHub during the transition.
- The post suggests that dissatisfaction with GitHub has reached maintainers with substantial project visibility and influence.
- The deeper issue is not Git itself but dependence on the centralized collaboration layer around issues, pull requests, and Actions.

## Synthesis
This post is significant less for its procedural details than for what it reveals about changing sentiment among prominent open-source maintainers. Mitchell Hashimoto describes leaving GitHub as emotionally difficult because the platform has been central to his work, identity, and professional life for nearly two decades. That personal framing matters. It signals that the decision is not driven by fashion or ideological posturing. It is a reluctant response to accumulated operational frustration.

The core complaint is reliability. Hashimoto says GitHub outages and degraded service have repeatedly interfered with core maintainer work such as pull-request review and software release processes. The issue is not simply that the platform occasionally fails. It is that these failures have become frequent enough to undermine confidence that serious work can depend on the service day after day. When a maintainer sees the main collaboration surface as a recurring blocker, the cost of staying begins to exceed the coordination cost of moving.

The post also matters because of who is saying it. Hashimoto is not a marginal or occasional open-source participant. He is a long-time builder whose projects helped define significant parts of cloud and infrastructure tooling. A move by Ghostty therefore functions as a signal to the broader ecosystem. It suggests that exiting GitHub is becoming imaginable for projects with real visibility, not just for communities already committed to alternative forges. Even if only a minority follow, the symbolic effect is strong because it lowers the social barrier to considering alternatives.

Notably, the article is careful about scope. Hashimoto is not announcing an immediate full departure from GitHub for everything, and he explicitly plans a read-only mirror for Ghostty. That reflects how sticky GitHub's surrounding infrastructure remains. The difficult part is not moving a Git repository, but replacing the network of issues, PRs, automation, and community habits built around it. In that sense, the post reinforces a broader market lesson: the moat is not version control, but workflow gravity.

Overall, the article reads as an early marker of possible platform dispersion in open source. If reliability and product direction continue to frustrate maintainers, more projects may decide that the operational risk of remaining concentrated on GitHub now outweighs the social cost of moving somewhere else. The post does not prove a mass migration is underway, but it shows that the question has become practical rather than hypothetical for influential maintainers.