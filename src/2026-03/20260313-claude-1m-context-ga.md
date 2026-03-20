# 1M Context Is Now Generally Available for Opus 4.6 and Sonnet 4.6
**Source**: https://claude.com/blog/1m-context-ga
**Date**: 2026-03-13
**Author**: Anthropic
**Keywords**: Claude, 1M context, Opus 4.6, Sonnet 4.6, long context, pricing, rate limits, Claude Code, media

## Elevator pitch
Anthropic makes the full 1-million-token context window generally available for Claude Opus 4.6 and Sonnet 4.6 at standard pricing with no long-context premiums, expanding media support to 600 images or PDF pages per request.

## Takeaways
- Full 1M-token context now available at standard pricing ($5/$25 per million for Opus; $3/$15 for Sonnet) with no multipliers
- Standard rate limits apply at every context length—no throughput penalties for long-context requests
- Media support expanded from 100 to 600 images or PDF pages per request
- Existing API code works automatically for requests over 200K tokens; beta headers are ignored
- Claude Code Max/Team/Enterprise users gain automatic 1M context access with reduced mid-conversation compaction events

## Synthesis
Anthropic's decision to make 1-million-token context generally available at standard pricing is a significant strategic move that changes the economics of long-context AI applications. Previously, accessing extended context required either special arrangements or accepting premium pricing that made certain use cases economically unviable. Removing that premium removes the cost-based disincentive for developers to design applications around long-context capabilities.

The technical achievement underlying this announcement is substantial. Opus 4.6 achieves 78.3% accuracy on MRCR v2 benchmarks for long-context retrieval, maintaining consistent performance across the full million-token window. This matters because naive attention-based models show significant performance degradation on retrieval tasks as context length increases—the "lost in the middle" problem where content from the middle of long contexts is effectively invisible to the model. Maintaining reliable retrieval at 1M tokens requires architectural attention to this problem.

The practical implications differ across use case categories. For developers processing large codebases, the entire repository can now fit in a single context without chunking strategies that introduce their own complexity and retrieval errors. For document analysis, complete books, legal documents, and regulatory filings can be processed without lossy summarization. For research workflows, large document corpora can be analyzed holistically.

The expanded media support—600 images or PDF pages per request versus the previous 100—opens multimodal long-context applications that were previously impossible within API limits. A complete illustrated technical manual, a collection of architectural drawings, or a year's worth of financial reports with charts can now be processed in a single pass.

For Claude Code specifically, reducing mid-conversation compaction events is a quality-of-experience improvement that preserves codebase context across longer sessions. Every compaction introduces potential for context loss and forces the model to work from summaries rather than the actual code, reducing reliability. Automatic 1M context access eliminates this friction for the platforms where it matters most.
