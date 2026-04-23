# Beyond vibe checks: A PM’s complete guide to evals

**Source**: https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete
**Date**: April 22, 2026
**Author**: Aman Khan
**Keywords**: AI evals, product managers, AI PM, metrics, evaluation

## Elevator pitch
Aman Khan argues that AI PMs need to move beyond intuition and vibe checks by treating evals as the practical way to measure whether an AI system is actually useful, safe, and improving.

## Takeaways
- The article positions evals as a core product-management skill in the AI era.
- It distinguishes human evals, code-based evals, and LLM-based evals with different strengths and weaknesses.
- The framework emphasizes evaluating each step in an agent system rather than only the final output.
- It argues that subjective AI quality can still be measured with disciplined methods.
- The post pushes PMs to think in terms of regression protection and explicit quality criteria.

## Synthesis
Aman Khan’s guide is effective because it translates evaluation from a research-sounding concept into day-to-day product work. His central claim is that AI PMs who focus only on prompts and models are missing the real control surface. Evals are what let a team break a system into parts, define what good looks like, and understand whether a change actually improved anything. Without that, teams are mostly doing taste-based iteration.

The examples are especially useful for PM audiences because they make the problem concrete. A trip-planning agent may look good in manual tests and still fail badly in production if it books the wrong city or ignores user constraints. The point of evals is to catch those failures before launch and to localize where they originate. That is much closer to product quality assurance than to abstract model science.

Khan also does a good job separating evaluation methods. Human feedback is valuable but sparse and expensive. Code-based checks are fast and cheap where outcomes are objective. LLM-based judges scale better to open-ended tasks but need calibration and validation. Rather than treating one approach as universal, he presents them as complementary tools for different layers of the system.

The broader lesson is that AI product management requires more explicit quality thinking than classic software in some areas, not less. Because outputs are probabilistic and often open-ended, teams need stronger habits around defining success, testing edge cases, and preventing regressions. “Beyond vibe checks” is a good phrase for that shift. It captures the move from intuition-led iteration to disciplined evaluation without pretending the work becomes fully mechanical.
