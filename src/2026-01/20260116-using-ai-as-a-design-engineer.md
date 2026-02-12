# Using AI as a Design Engineer

**Source**: https://jakub.kr/work/using-ai-as-a-design-engineer

**Date**: January 2026

**Author**: Jakub Krehel

**Keywords**: AI workflow, design engineering, Cursor, Claude, code quality, Figma MCP, developer tools, AI-assisted development

## Elevator pitch

A design engineer shares practical strategies for integrating AI into development workflows while emphasizing that AI should accelerate execution, not replace thinking, and that design quality will become the ultimate differentiator.

## Takeaways

- AI should accelerate workflow execution rather than replace creative thinking—blindly following AI suggestions without understanding the output undermines quality and ownership
- Establishing explicit codebase rules (animation performance, design systems, code utilities) in dedicated files helps AI produce consistent, project-aligned code
- Always assume AI has zero context when starting conversations—treat each interaction independently and provide necessary background explicitly
- Custom commands like `/deslop` help remove AI-generated redundancies and maintain code quality by catching the verbose patterns AI tends to produce
- As AI commoditizes implementation, design and user experience will become the product—human judgment on quality and craftsmanship remains irreplaceable

## Synthesis

Jakub Krehel's article provides a practitioner's perspective on integrating AI tools into design engineering work. Rather than presenting AI as a revolutionary force, he frames it as a sophisticated acceleration layer that requires careful management to produce quality outcomes.

The core philosophy is pragmatic restraint. Krehel uses AI to speed up execution—UI scaffolding, refactoring, migrations, code reviews—but explicitly avoids using it for ideation. This distinction matters because it preserves human ownership over creative decisions while delegating mechanical implementation tasks. The warning against blindly following AI suggestions underscores that effective AI use requires active engagement and understanding.

The setup practices he describes have emerged from real project experience. Maintaining explicit rule files for animations, design systems, and code patterns gives AI consistent guidance aligned with project standards. These aren't generic best practices but project-specific constraints that channel AI output toward acceptable solutions. The practice of assuming zero context—treating each AI interaction as a fresh start requiring explicit background—prevents the compound errors that arise when AI makes incorrect assumptions based on partial information.

His tooling choices reflect current best-in-class options for design engineering. Cursor provides the primary development environment. Claude Opus 4.5 delivers the speed and reliability needed for frequent interactions. The Figma MCP integration represents a significant productivity gain by connecting design source files directly to implementation workflows. Additional MCPs like context7 address the documentation freshness problem by fetching current references rather than relying on potentially stale training data.

The custom `/deslop` command deserves attention as a practical pattern. AI-generated code tends toward verbosity and redundancy—patterns that pass functional tests but accumulate into maintenance burdens. Having an explicit cleanup mechanism acknowledges this tendency and builds correction into the workflow rather than hoping the problem won't occur.

Krehel's concluding argument frames the strategic implications: as AI commoditizes implementation, differentiation shifts entirely to design and user experience. This isn't a threat to design engineers but an elevation of their importance. The skills that matter increasingly aren't raw coding speed but taste, judgment, and the ability to translate user needs into elegant solutions. AI handles the mechanical translation; humans handle the decisions about what to build and why.

The article implicitly argues for a mature relationship with AI tools—neither dismissive skepticism nor uncritical enthusiasm, but informed integration that maximizes benefits while maintaining quality standards and human agency over creative direction.
