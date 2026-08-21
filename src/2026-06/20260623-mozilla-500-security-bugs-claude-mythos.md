# How Mozilla Fixed 500 Security Bugs with Claude Mythos
**Source**: https://www.chatprd.ai/how-i-ai/how-mozilla-fixed-500-security-bugs-with-mythos
**Date**: 2026-06-22
**Author**: Brian Grinstead (Mozilla), presented by Claire Vo
**Keywords**: Mozilla, Firefox, Claude Mythos, security, agent harness, LLM judge, bug hunting, verification

## Elevator pitch
Mozilla shipped 423 security fixes in one month not by using a magical model, but by building a tightly engineered agentic harness that gives an agent real tools, forces it to prove its claims with reproducible crashes, and routes every result through independent verification and human review.

## Takeaways
- The breakthrough wasn't just a better model—it was a custom harness: Mozilla gives the agent a Firefox checkout, terminal access, build commands, and browser evaluators tied to existing fuzzing infrastructure, so findings must trigger actual crashes to count.
- The pipeline has three connected jobs: rank which files deserve attention (LLM judge), search for reproducible vulnerabilities inside those files (bug-hunting loop), and independently verify both the exploit and the proposed patch (verifier + patching agents).
- Agents are relentless in a way humans can't be: one bug required 14 attempts before the agent generated a reproducing test case; cognitive energy declines in humans but not in agents.
- The verification loop eliminates false positives through a two-stage process: first, the agent must trigger an actual crash in an AddressSanitizer-instrumented build (crystal-clear signal), then a verifier subagent checks the bug report for legitimacy and rejects test-only configurations or agent-manufactured vulnerabilities.
- The harness can be built in an afternoon using vendor SDKs (Claude Agent SDK, OpenAI Agent SDK); Brian recommends using vendor-provided harnesses because models are likely post-trained to work best with their own infrastructure, and the same pattern applies to performance optimization, tech debt, and UX analysis—not just security.

## Synthesis
Mozilla Distinguished Engineer Brian Grinstead breaks down how his team used AI agents to ship nearly 500 Firefox security fixes in a single month, a dramatic spike from the typical ~20 per month. The viral narrative was that Anthropic's Mythos model found the bugs, but Grinstead's more interesting argument is that the breakthrough came from engineering the orchestration around the model, not from the model alone.

The system is built around three phases. First, a lightweight LLM judge scores each Firefox source file on two dimensions—likelihood of containing a memory-safety issue and accessibility from a webpage—producing a prioritized queue. This scoring is intentionally simple: ask the model to act like a security reviewer and assign rough risk scores. Second, the bug-hunting loop gives the top-ranked files to an agent running via the Claude Agent SDK with shell access, build commands, and a Firefox build instrumented with AddressSanitizer. The agent generates HTML test cases designed to trigger vulnerabilities, runs them, and iterates on failures—sometimes trying 14+ times before succeeding. Third, a verifier agent checks for shortcuts (modified source code, unrealistic settings, manufactured vulnerabilities) before a separate patching agent proposes fixes.

The key architectural insight is that the harness provides ground truth. Without AddressSanitizer and reproducible crash evidence, the system would produce noise. With it, repeated agent attempts become useful engineering work. The model supplies persistence and pattern matching; the harness supplies the measurable signal that turns speculation into evidence.

Grinstead emphasizes that this pattern extends far beyond security. Any domain where you can score and prioritize targets, give an agent a constrained goal with verification criteria, and plug results into an existing pipeline can benefit: performance optimization, tech debt reduction, and UX quality reviews all fit the same structure. The harness can be built in an afternoon using vendor SDKs, and multiple models should be run because different models spike on different vulnerability types—attackers will use whatever model finds bugs, so defenders need to scan with multiple approaches.