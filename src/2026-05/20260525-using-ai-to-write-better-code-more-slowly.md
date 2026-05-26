# Using AI to write better code more slowly
**Source**: https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/
**Date**: May 25, 2026
**Author**: Nolan Lawson
**Keywords**: AI coding, code review, LLM agents, software quality, Claude, Codex, bug finding, multi-model review

## Elevator pitch
Nolan Lawson makes the case that AI coding tools aren't just for spewing slop at high velocity — they can be used just as effectively to write better code more slowly, by running multiple models as bug-finding reviewers in a careful, methodical loop.

## Takeaways
- The same LLMs that produce "slop cannon" PRs can be redirected to find bugs with near-zero false positives when multiple models are combined
- Lawson's review skill runs Claude, Codex, and Cursor Bugbot in parallel against a PR, then the main agent collates results and rules out false positives
- The technique consistently finds so many bugs that you'll be "bored senseless" — ranging from critical security issues to misleading comments
- Clearing context between review sweeps is essential to avoid influence bias from the first result
- The workflow often surfaces pre-existing bugs, leading to tangential side-quests that improve overall codebase health rather than raw velocity

## Synthesis
Nolan Lawson, a seasoned software engineer, pushes back against the dominant narrative that AI coding tools are exclusively for generating low-quality code at maximum speed. In a post that quickly gained traction on Hacker News, he argues that LLMs are flexible enough to be used for the exact opposite purpose: writing better code more slowly through rigorous multi-model review.

His core technique is a Claude skill that orchestrates parallel bug reviews. It dispatches sub-agents running Claude, Codex, and Cursor Bugbot independently against a pull request, each ranking findings as critical, high, medium, or low. Once all three return, the main agent collates results, performs its own research to eliminate false positives, and produces a final consolidated report. The false positive rate, Lawson reports, is "near zero" — a striking claim validated by the multi-model triangulation approach that a Milvus blog post originally demonstrated.

The results are both impressive and overwhelming. Reviews consistently uncover bugs ranging from critical security or correctness flaws to medium-level performance issues to low-priority misleading comments. Lawson's typical workflow: have an agent fix all criticals and highs with guidance, skip issues where the juice isn't worth the squeeze, and occasionally abandon a PR entirely when the review reveals the whole approach was misguided.

Critically, this technique does not increase velocity. It often decreases it, because reviews surface pre-existing bugs that predate the PR, sending Lawson on tangential side-quests writing unit tests and fixing subtle flaws. This is the opposite of the "10x productivity" narrative, but Lawson finds it deeply satisfying — it improves overall codebase health while teaching developers about failure modes and odd corners of complex architectures.

The approach reflects a philosophy that predates LLMs: careful, methodical, quality-obsessed programming focused on making things better for the next developer. AI, in Lawson's framing, doesn't replace that philosophy — it superpowers it. The post is particularly notable as a counterweight to the emerging industry narrative that AI coding's unit economics are broken because tools are too expensive and too low-quality. Lawson's response is that the quality problem is a workflow problem, not a tool problem.
