# Clawpatch — Automated Code Review
**Source**: https://clawpatch.ai/
**Date**: Unknown (c. 2026-05)
**Author**: OpenClaw team
**Keywords**: automated code review, semantic analysis, AI patching, code quality, open source, Codex CLI

## Elevator pitch
An open-source automated code review tool that maps codebases into semantic feature slices, reviews them for bugs and quality issues, and records explicit fix attempts with validation.

## Takeaways
- Clawpatch goes beyond traditional linters by reviewing semantic "features" — routes, commands, packages, CLI scripts — rather than individual files
- The tool produces structured findings with severity, confidence scores, evidence snippets, and actionable recommendations
- Automated patching includes a full validation pipeline (format, type, lint, test checks) before any fix is applied
- Safety is a first-class concern: no implicit commits, clean worktree checks, and full audit trails in `.clawpatch/`
- Built on the local Codex CLI with strict JSON schemas for provider responses, ensuring deterministic tool behavior

## Synthesis
Clawpatch represents an evolution in automated code review: where traditional linters check for syntactic patterns, Clawpatch operates at the semantic feature level. It maps a repository into logical units — API routes, package entry points, CLI commands, test suites — and reviews each feature with the bounded context an AI reviewer needs. This is a significant departure from file-at-a-time scanning, which lacks the cross-file context that makes code review meaningful.

The tool's architecture supports a complete workflow: init, map, review, report, fix, and revalidate. Each step is idempotent and resumable, with state persisted in `.clawpatch/`. Findings include not just what's wrong but how confident the reviewer is, what evidence supports the finding, and what to do about it. The explicit fix loop — generate a patch, validate through the project's own format/lint/type/test pipeline, then present it for human review — is a thoughtful approach to AI code modification that preserves developer agency.

The safety guarantees are notable: Clawpatch never commits or pushes code, requires a clean worktree before applying fixes, and keeps an audit trail. Built on Codex CLI with strict JSON schemas, it avoids the non-deterministic behavior that plagues less constrained AI code tools. The project, released under MIT license by the OpenClaw team, is positioned as infrastructure for teams that want AI code review but need to maintain control over their repositories.
