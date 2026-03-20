# OpenReview: Open-Source AI Code Review Bot by Vercel
**Source**: https://github.com/vercel-labs/openreview
**Date**: 2026-03-20
**Author**: Vercel Labs
**Keywords**: code review, AI, Claude, GitHub, Vercel, sandbox, open source, self-hosted, Next.js

## Elevator pitch
OpenReview is a self-hosted AI code review bot that integrates with GitHub via @mentions in pull requests, delivers line-level inline suggestions using Claude in isolated Vercel Sandbox environments, and supports extensible custom skills via YAML.

## Takeaways
- Triggered by `@openreview` mentions in GitHub PR comments; delivers line-level inline suggestions with native GitHub suggestion blocks
- Runs in isolated Vercel Sandbox environments with full repository access; durable execution via Vercel Workflow
- Reaction-based approval workflow: 👍/❤️ applies suggestions, 👎/😕 skips them—keeping humans in control
- Extensible via custom skills in `.agents/skills/` as YAML-frontmatter markdown files defining when each skill applies
- Built on Next.js, Claude (Anthropic), AI SDK, and Vercel Workflow; currently in beta

## Synthesis
OpenReview addresses the practical integration problem for AI code review: most AI coding tools require developers to change their workflow, but PR review already happens in GitHub where the code, context, and collaborators are all co-located. By triggering through a GitHub mention and delivering suggestions as native GitHub suggestion blocks, OpenReview meets reviewers in their existing workflow rather than requiring context switching.

The isolated sandbox execution model is the key technical differentiator. Code review often requires understanding what code actually does, not just what it says—which means executing tests, running linters, and sometimes exploring runtime behavior. By running in Vercel Sandbox environments with full repository access, OpenReview can perform more thorough analysis than tools that only parse static code. The isolated environment ensures this exploration cannot affect production systems regardless of what the code under review contains.

The reaction-based approval system reflects mature thinking about human-AI collaboration in review. Automatic application of every suggestion would undermine developer ownership of their code and create trust issues when suggestions are wrong. Automatic rejection of all suggestions defeats the purpose. The emoji reaction model creates a lightweight, in-context decision interface that keeps humans in final control without requiring them to leave the review context to act on AI suggestions.

The extensible skill system is the feature most likely to drive long-term adoption. Built-in skills covering Next.js patterns, React optimization, and design guidelines address common review scenarios. But every codebase has its own patterns, conventions, and review priorities. YAML-based custom skill definitions in a `.agents/skills/` directory allow teams to encode organizational knowledge into their review bot—gradually building a review system that reflects how their specific team thinks about code quality, rather than generic best practices. This institutional customization is what transforms a generic tool into a trusted team member.
