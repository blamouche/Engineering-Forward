# My AI Had Already Fixed the Code Before I Saw It

**Source**: https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it-f4a29a07-ea95-409f-bcb2-487a970bed4a

**Date**: January 27, 2026

**Author**: Kieran Klaassen

**Keywords**: compounding engineering, AI development, Claude, persistent memory, code review, self-improving systems, CLAUDE.md

## Elevator pitch

Compounding engineering builds self-improving development systems where each iteration teaches the AI through persistent memory, so every bug fix and code review becomes a permanent lesson that strengthens future work.

## Takeaways

- Compounding engineering creates systems with persistent memory rather than delivering short-term speed gains that reset each cycle
- Every code review becomes a permanent lesson embedded in system behavior, shifting focus from daily problem-solving to architectural teaching
- Documenting workflows in CLAUDE.md files enables scaling development without human intervention by preserving context across sessions
- Running validation multiple times catches edge cases like hedged language that single test runs miss
- Claude can autonomously apply months of prior code review feedback without being asked, demonstrating the compound effect of accumulated learning

## Synthesis

Kieran Klaassen introduces the concept of compounding engineering—building development systems where each iteration teaches the AI, making future work progressively faster and better. This represents a shift from standard AI engineering that delivers short-term speed gains to systems that accumulate knowledge persistently.

The distinction matters practically. Traditional AI-assisted development starts fresh each session. Developers explain context, provide guidance, and correct mistakes that the AI will make again tomorrow. Compounding engineering inverts this: "Every time we fix something, the system learns" rather than starting from scratch each cycle. The investment in teaching compounds over time.

Klaassen demonstrates the approach through a practical example: building a frustration detection feature. Rather than manually coding detection logic, he created a sample conversation showing frustration, had Claude generate tests first, and iterated prompts until tests passed. He then ran validation 10 times to catch edge cases, discovering subtle issues like hedged language that single test runs missed. The workflow was documented in a CLAUDE.md file for reuse.

The breakthrough moment came when Claude autonomously applied three months of prior code review feedback without being asked, citing specific pull requests. This behavior emerged from accumulated context, not explicit instruction. The AI had internalized patterns from past corrections and applied them proactively.

Several practices enable compounding returns. Documenting workflows in CLAUDE.md files preserves context across sessions, allowing AI agents to pick up where previous sessions left off. Running validation multiple times surfaces edge cases that single passes miss. Treating every code review as a teachable moment embeds lessons in system behavior rather than letting them evaporate after the immediate fix.

The upfront investment is modest—roughly 10 minutes to teach a tool or document a workflow—but the returns accumulate. Each bug fix strengthens the pipeline. Each code review improves future output. The mindset shift involves treating development as architectural teaching rather than daily problem-solving. Over time, the system becomes capable of handling tasks that previously required explicit guidance.

This approach represents a different relationship with AI development tools. Instead of using AI to accelerate existing workflows, compounding engineering restructures the workflow itself to capture and preserve learning.
