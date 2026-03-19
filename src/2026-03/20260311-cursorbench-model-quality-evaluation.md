# How we compare model quality in Cursor
**Source**: https://cursor.com/blog/cursorbench
**Date**: 2026-03-11
**Author**: Naman Jain
**Keywords**: CursorBench, model evaluation, benchmarks, SWE-bench, agentic graders, real developer tasks, online-offline evaluation, data contamination

## Elevator pitch
CursorBench evaluates models on tasks sourced from actual Cursor sessions—tasks that have doubled in scope from public benchmarks and use agentic graders to handle underspecified developer requests—because public benchmarks systematically misrepresent what developers actually do.

## Takeaways
- Public benchmark limitations: misaligned with real workflows (focused on bug-fixing rather than complex multi-file tasks), flawed grading that penalizes valid alternatives, data contamination (OpenAI stopped reporting SWE-bench results after finding models reproduced training patches from memory).
- CursorBench sources tasks from actual Cursor sessions using "Cursor Blame" tracing for maximum real-world relevance.
- Tasks have doubled in scope since inception, involving substantially more code than public benchmarks.
- Agentic graders score underspecified, ambiguous developer requests—addressing the problem that real tasks rarely have single correct solutions.
- Hybrid online-offline evaluation: offline benchmarks supplemented with live A/B experiments to validate findings against real user behavior.
- Future challenge: adapting benchmarks for long-running agents on their own computers, requiring cheaper grading and reproducibility across external services.

## Synthesis
CursorBench represents a principled response to a problem that Anthropic's infrastructure noise research identified from a different angle: public benchmarks systematically misrepresent what they're supposed to measure. Cursor's complaint is different but related—public benchmarks measure capabilities that don't matter for their users, and at scales that don't represent real developer tasks.

The "Cursor Blame" tracing approach is methodologically elegant. Rather than constructing tasks that researchers believe represent real developer work, it samples directly from what developers actually did in Cursor sessions. This produces tasks with authentic complexity, authentic ambiguity, and authentic stakes—because they came from developers who were trying to accomplish real work.

The agentic grader requirement addresses a fundamental limitation of traditional benchmark design: real developer tasks rarely have single correct solutions. A developer asking Claude to "refactor this module to be more testable" has preferences but not a unique correct answer. Grading this automatically requires a grader that can evaluate solution quality rather than just check against a reference solution. This is harder and more expensive but necessary for measuring capabilities that matter.

The data contamination note about OpenAI and SWE-bench is significant. If models are memorizing and reproducing training patches rather than actually solving problems, the benchmark is measuring training data coverage rather than problem-solving capability. This is a form of benchmark gaming that's not intentional cheating but an emergent property of training on internet-scale data that includes publicly available benchmark tasks.
