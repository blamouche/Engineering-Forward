# Branching (version control)

**Source**: https://en.wikipedia.org/wiki/Branching_(version_control)
**Date**: 2026
**Author**: Wikipedia contributors
**Keywords**: branching, version control, trunk, merge, software configuration management

## Elevator pitch
The article is a general refresher on why branches exist in version control, how they relate to trunks and merges, and the organizational tradeoffs behind parallel development.

## Takeaways
- Branching isolates work so teams can develop fixes, features, and releases in parallel.
- The trunk/mainline concept remains the central baseline from which many workflows branch.
- Branching strategies are deeply tied to release policy and team coordination, not just tooling.
- Distributed VCS changed the practical cost and ubiquity of branching.
- It is basic reference material, but still useful context when comparing branching philosophies.

## Synthesis
On its own this is just a reference page, but in the context of the Spotify release articles it becomes a nice baseline. Branching is easy to explain mechanically and much harder to optimize organizationally. The Wikipedia article reminds us that branches are simply a way to create parallel lines of change and eventually merge them. The interesting part is always the policy wrapped around that capability: long-lived feature branches, release branches, trunk-based development, vendor branches, and so on. In practice, branching debates are rarely about Git mechanics; they are about how teams want to manage risk, integration cost, and release cadence.
