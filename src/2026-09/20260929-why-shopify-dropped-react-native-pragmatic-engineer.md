# Why Has Shopify Dropped React Native?
**Source**: The Pragmatic Engineer (pragmaticengineer+deepdives@substack.com)
**Date**: 2026-09-29
**Author**: Gergely Orosz
**Keywords**: Shopify, React Native, native mobile development, AI agents, Kotlin Multiplatform, KMP, Airbnb, Clubhouse, Notion, mobile engineering, cross-platform

## Elevator pitch
The Pragmatic Engineer deep-dives Shopify's decision to abandon React Native and go back to native mobile development — a reversal of its 2020 bet — driven by AI agents making native codebase rewrites fast enough that React Native's cross-platform abstraction is no longer worth the performance cost.

## Takeaways
- Shopify announced that "native is now the future of mobile development," reversing its 2020 all-in bet on React Native — triggering a community reaction on the scale of the original RN adoption
- In 2020, Shopify chose React Native because Android apps took too long to build, and having consistent iOS/Android apps was valuable — 71% of buyers purchased on mobile
- The 2026 reversal is driven by AI: coding agents are now good enough at writing mobile and backend code that Shopify rewrote its Shop app to native in just 12 weeks — an effort that would have taken many months before AI
- React Native adds abstractions that native does not, and with AI lowering the cost of maintaining separate iOS/Android codebases, the abstraction tax is no longer justified
- Airbnb followed the same pattern: adopted React Native in 2016, moved back to native in 2018 — the underlying reason was the same: performance
- Notion has been migrating to native since 2019 and is still at it seven years later — raising the question of whether a native editor actually slows web iteration speed, with or without AI
- Kotlin Multiplatform (KMP) offers a middle path: shared business logic in Kotlin across iOS/Android while each platform stays native — could become more popular with AI assistance
- The Clubhouse story is a cautionary tale: the live-conversations app was iOS-only for 14 months, couldn't ship Android fast enough, and by the time it did, usage had peaked and declined

## Synthesis
Shopify's React Native reversal is the first major architectural decision publicly attributed to AI coding capability. The 12-week native rewrite of Shop is the number that matters: it collapses the core tradeoff that made cross-platform frameworks attractive. When maintaining two native codebases required two full teams and double the engineering time, the abstraction tax of React Native — performance overhead, bridge latency, platform-feature lag — was worth paying. AI agents have effectively halved the cost of native development, and the abstraction tax is no longer worth it.

The deeper implication is that AI doesn't just make existing codebases faster to write — it changes which architectural tradeoffs make sense. Cross-platform frameworks exist to amortise human engineering effort across platforms. If AI reduces that effort by 50-80%, the amortisation value shrinks proportionally. KMP, which shares logic but keeps UI native, may be the sweet spot: it's the framework that preserves the most platform-specific control while still deduplicating non-UI code. The Notion seven-year migration is the warning: native transitions are expensive, and even with AI, the cost of being mid-migration — straddling web and native — can itself become a competitive drag.