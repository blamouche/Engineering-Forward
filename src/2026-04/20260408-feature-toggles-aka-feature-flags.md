# Feature Toggles (aka Feature Flags)

**Source**: https://martinfowler.com/articles/feature-toggles.html
**Date**: 2017
**Author**: Martin Fowler
**Keywords**: feature flags, release toggles, canary release, a/b testing, trunk-based development

## Elevator pitch
Martin Fowler’s classic feature-toggle essay explains how flags let teams keep shipping from trunk while separating deploy from exposure, canarying risky changes, and experimenting safely.

## Takeaways
- Feature flags are presented as a core enabling pattern for continuous delivery and trunk-based development.
- The article distinguishes different kinds of toggles with different lifetimes and operational needs.
- Toggle routers can evolve from simple config checks to per-request dynamic decisions.
- Canary releases and A/B tests become far easier when feature exposure is decoupled from deployment.
- The biggest caution is that toggle systems create complexity unless actively managed.

## Synthesis
This remains one of the clearest explanations of why feature flags matter beyond “turn things on and off.” Fowler frames them as a control mechanism for delivering incomplete or risky code safely, which is exactly why they pair so naturally with trunk-based development and staged rollouts. The examples still feel current because modern product teams use flags for the same reasons: testing, internal exposure, canaries, experimentation, and operational fallback. The important nuance is that flags are not free. They buy release flexibility at the cost of runtime and codepath complexity. Teams that internalize both sides of that trade tend to use flags well; teams that do not end up with permanent conditional archaeology.
