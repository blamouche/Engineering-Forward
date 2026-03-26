# We Tested MiniMax M2.7 Against Claude Opus 4.6
**Source**: https://blog.kilo.ai/p/we-tested-minimax-m27-against-claude
**Date**: March 26, 2026
**Author**: Unknown
**Keywords**: MiniMax M2.7, Claude Opus 4.6, benchmarking, coding agents, cost-performance

## Elevator pitch
Kilo’s hands-on benchmark finds MiniMax M2.7 matches Claude Opus 4.6 on bug and vulnerability detection while delivering most of the fix quality at a tiny fraction of the cost.

## Takeaways
- MiniMax M2.7 is priced around $0.30/$1.20 per million tokens versus Claude Opus 4.6 at $5/$25, a 17–21x difference.
- In three coding tasks, both models found all bugs and vulnerabilities, but Claude delivered more robust fixes and better testing.
- MiniMax achieved roughly 90% of the fix quality for about 7% of the total cost in Kilo’s tests.
- Claude’s strengths were architecture, modularity, and integration testing depth.
- MiniMax’s fixes were often simpler yet effective, with a few cases showing stronger technical choices.

## Synthesis
Kilo’s evaluation of MiniMax M2.7 versus Claude Opus 4.6 presents a pragmatic view of frontier versus open-weight model tradeoffs in real coding scenarios. The benchmark covered three tasks: building a full-stack event processing system from a spec, diagnosing production bugs from symptoms and logs, and conducting a security audit with planted vulnerabilities. In each task, both models detected all issues, but Claude consistently delivered more complete fixes and more thorough tests. The headline, however, is cost: MiniMax achieved close to Claude-level results at a fraction of the price.

In the build-from-spec test, both models implemented the required components, yet Claude’s output was more modular and production-ready. Its architecture separated routing, pipeline management, and WebSocket handling, and it introduced operational considerations like graceful shutdown. Claude also produced a large suite of integration tests that hit the API end-to-end. MiniMax’s output was simpler—fewer files, more consolidated logic—and it emphasized unit tests on handler functions. This choice made MiniMax faster and cheaper to run but left more integration risk. The difference reflects a broader pattern: Claude invests in structure and test coverage, while MiniMax prioritizes quick functional coverage.

In the bug investigation scenario, both models found the same six root causes. MiniMax occasionally made strong technical calls, such as switching to integer arithmetic (cents) to eliminate floating-point drift in price calculations. Claude, on the other hand, layered in operational safeguards like rollback logic for partial failures. The contrast shows the models’ biases: MiniMax resolves the bug; Claude also anticipates the follow-on failure modes. For production teams, this can translate to reduced downstream work with Claude, even if MiniMax is highly cost-efficient.

The security audit produced a similar pattern. Both models identified and categorized all vulnerabilities, but Claude’s fixes were more robust and comprehensive. For example, Claude applied safer password hashing, added broader SSRF validation, and implemented more consistent rate-limiting across endpoints. MiniMax’s fixes tended to be narrower and sometimes opted for disabling features rather than re-architecting them. That tradeoff can be acceptable for teams under time pressure or with limited security maturity, but it signals higher long-term remediation costs.

The test results suggest that the gap between open-weight models and frontier models is shrinking in detection ability but remains meaningful in fix quality and engineering discipline. For organizations that need high-quality output with fewer follow-on iterations, Claude still looks superior. For cost-sensitive workflows and high-volume tasks, MiniMax M2.7’s economics are hard to ignore. The takeaway is not that one model wins across the board, but that the “best” model depends on the workflow’s tolerance for quality variance, the cost envelope, and whether the team can absorb the extra cleanup work that cheaper models may require.