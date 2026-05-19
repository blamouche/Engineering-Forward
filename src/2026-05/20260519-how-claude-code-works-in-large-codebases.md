# How Claude Code Works in Large Codebases: Best Practices and Where to Start
**Source**: https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
**Date**: Unknown (c. 2026-05)
**Author**: Anthropic
**Keywords**: Claude Code, large codebases, best practices, code navigation, AI coding, Anthropic

## Elevator pitch
Anthropic's guide to using Claude Code effectively in large, complex codebases, with strategies for context management and getting started.

## Takeaways
- Claude Code uses intelligent context selection to work with large codebases without needing the entire repo loaded — it targets relevant files and symbols
- Starting with focused, well-scoped tasks produces better results than broad, open-ended instructions when working with large codebases
- Providing clear context about the codebase structure (architecture docs, README, conventions) significantly improves Claude Code's effectiveness
- Iterative refinement — reviewing, testing, and giving feedback on Claude Code's output — is essential for quality results in complex codebases
- Breaking large changes into smaller, sequential steps helps Claude Code maintain context and avoid errors

## Synthesis
Anthropic's blog post addresses one of the most common friction points with AI coding tools: using them effectively in repositories that are too large to fit entirely in context. The guide explains that Claude Code doesn't need to load the entire codebase at once; instead, it uses targeted file selection based on the task at hand, pulling in relevant source files, test files, and configuration as needed.

The post recommends starting with well-defined, bounded tasks rather than attempting sweeping changes. This aligns with the broader industry understanding that AI coding agents perform best when their work is scoped and verifiable. The guidance to provide structural documentation — README files, architecture descriptions, coding conventions — reflects that Claude Code benefits from the same artifacts that help human developers onboard to a codebase.

A core theme is the importance of the human-in-the-loop workflow: review Claude Code's output, test it, provide feedback, and iterate. The tool amplifies developer productivity but doesn't replace engineering judgment. The recommendation to break large changes into sequential small steps addresses a fundamental limitation: long agent sessions risk context decay and error propagation, so decomposing work into discrete, verifiable chunks is both a practical necessity and a best practice for quality.
