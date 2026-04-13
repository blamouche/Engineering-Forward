# The Linux kernel now allows AI-written code, but you're on the hook for it

**Source**: https://www.xda-developers.com/linux-kernel-now-allows-ai-written-code
**Date**: April 11, 2026
**Author**: Simon Batt
**Keywords**: Linux kernel, AI-generated code, open source, DCO, software review, governance

## Elevator pitch
XDA reports that Linux maintainers are permitting AI-generated contributions, but only under a strict human-accountability model where contributors—not the tool—certify provenance, licensing, and correctness.

## Takeaways
- The Linux kernel documentation now permits AI-generated code contributions under existing submission rules.
- AI tools may not add Signed-off-by tags because only humans can certify the Developer Certificate of Origin.
- Maintainers are treating AI output as the submitter’s own work for responsibility and review purposes.
- The policy is permissive about tooling but conservative about accountability, provenance, and licensing.
- This creates a pragmatic governance precedent for other open-source projects trying to absorb AI-assisted development.

## Synthesis
The notable thing about the Linux kernel’s stance is not that it now allows AI-generated code, but how it allows it. The project is effectively saying that tooling is acceptable while accountability remains fully human. Contributors can use an assistant to draft code, but they cannot outsource review, legal certification, or blame. That is a much more grounded response than either blanket bans or naive acceptance.

The Signed-off-by requirement is the clearest expression of that philosophy. Since the Developer Certificate of Origin is a legal and social commitment, only a human can make it. That means AI assistance is treated like any other tool in the workflow: useful for drafting or accelerating work, but irrelevant to the question of who actually owns the submission. If the code is buggy, improperly licensed, or otherwise non-compliant, the submitter carries the consequences.

This matters beyond Linux because open-source communities have been searching for governance norms around AI-assisted coding. The kernel’s model offers a practical template: permit the use of AI, require explicit human review, and preserve existing provenance mechanisms instead of inventing a parallel lane for machine-authored code. That keeps standards stable while acknowledging that the tools are already widespread.

The broader implication is that mature engineering cultures may converge on “AI allowed, excuses not allowed.” In other words, the presence of an AI assistant does not dilute professional responsibility. If anything, it increases the need for disciplined review, because the speed and confidence of generated code can make subtle defects easier to smuggle into serious systems.
