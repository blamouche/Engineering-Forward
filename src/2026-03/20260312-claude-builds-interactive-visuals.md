# Claude now creates interactive charts, diagrams and visualizations
**Source**: https://claude.com/blog/claude-builds-visuals
**Date**: 2026-03-12
**Author**: Anthropic
**Keywords**: Claude, generative UI, interactive visualizations, charts, diagrams, artifacts, conversational rendering, Anthropic

## Elevator pitch
Claude now generates interactive charts, diagrams, and visualizations inline during conversations—temporary pedagogical tools that adjust as topics evolve, distinct from permanent shareable artifacts.

## Takeaways
- Interactive visualizations appear inline in conversations rather than in side panels; users can request adjustments as discussions develop.
- Distinct from Claude Artifacts: visualizations serve temporary pedagogical purposes and adjust or disappear as conversation topics shift; artifacts are permanent, polished, shareable outputs.
- Claude autonomously decides when visualizations would enhance understanding—not just when users explicitly request them.
- Examples: interactive compound interest curves, clickable periodic table with on-demand element details.
- Enabled by default across all Claude subscription tiers; complements integrations with Figma, Canva, and Slack.

## Synthesis
The artifact/visualization distinction reveals a thoughtful design decision about what role AI-generated visual content should play in conversations. Artifacts are designed for persistence and sharing—the user wants to produce something that outlasts the conversation. Visualizations are designed for explanation and understanding—they're useful for the duration of a question but don't need to persist beyond it. Conflating these use cases would produce either persistent clutter or insufficient capabilities for generating lasting deliverables.

The autonomous visualization decision is the most significant capability. Users explicitly requesting charts is useful; a model that recognizes when a visualization would clarify a concept before the user thinks to ask is more powerful. This requires the model to reason about pedagogical effectiveness—to identify when abstract description can be replaced by concrete visual representation that produces better understanding. This is a form of pragmatic reasoning about communication rather than just content generation.

The implementation details uncovered by Livshits's reverse engineering (separate article) are relevant context: Claude uses a `show_widget` tool call injecting HTML directly into the DOM with CSP restrictions on CDN sources. This architecture enables streaming-friendly rendering (styles first, scripts last; no gradients that flash during DOM updates) while maintaining security through content restrictions. The design choices reflect production deployment constraints rather than demo optimization.

The inline placement is an interaction design choice with real consequences. Side panels create cognitive context switching—users have to visually shift between conversation and visualization. Inline placement keeps the visual in context with the discussion, reducing the cognitive overhead of connecting text explanation to visual representation.
