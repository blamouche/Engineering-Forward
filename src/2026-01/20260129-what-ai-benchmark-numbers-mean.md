# What those AI benchmark numbers mean
**Source**: https://ngrok.com/blog/ai-benchmarks
**Date**: 2026-01-29
**Author**: Sam Rose
**Keywords**: AI benchmarks, SWE-bench, evaluation, model comparison, leaderboards, benchmark integrity, custom evals

## Elevator pitch
A guide to 14 commonly cited AI benchmarks that explains what each actually measures, what criticisms researchers have raised, and why benchmark scores often obscure more than they reveal.

## Takeaways
- Benchmark numbers require domain context: an 80.6% score on SWE-bench Verified means bug-fixing in specific Python repositories, not general coding competence across stacks or real-world complexity.
- Benchmarks span distinct domains: coding (SWE-bench), terminal tasks (Terminal-Bench 2.0), customer service (τ²), tool usage (MCP Atlas), computer interaction (OSWorld), reasoning (ARC-AGI), and domain knowledge (GPQA, MMMU, MMMLU).
- Data contamination is a recurring concern—SWE-bench's 500 tasks may already exist in training data, undermining generalization claims.
- Conflicts of interest are present in some evaluations: GDPVal and FrontierMath show publisher involvement in test construction.
- Benchmark quality itself varies: Humanity's Last Exam contained approximately 18% factually incorrect questions.
- The article recommends organizations develop custom evaluations for their specific use cases rather than relying solely on published leaderboard scores.

## Synthesis
AI benchmarks serve the same function for models that quarterly earnings reports serve for companies: they provide standardized numbers that allow comparison while potentially obscuring the factors that matter for any specific decision. Rose's survey makes clear that this analogy holds in its limitations too—the numbers are real, but what they measure is often narrower than how they get used.

The data contamination problem is structurally difficult. As training datasets expand, the probability that any publicly-available benchmark task appears in pre-training data increases. This creates a perverse incentive: benchmarks that remain useful over time must either be private (limiting community verification) or continuously regenerated (requiring significant ongoing resources). The industry has not resolved this tension.

Infrastructure noise adds another confound. Anthropic's research on Terminal-Bench 2.0 showed infrastructure configuration alone can shift scores by up to 6 percentage points—exceeding the gaps between many ranked models. Combined with training data leakage concerns, small leaderboard differences become nearly meaningless without standardized evaluation conditions.

The recommendation to build custom evaluations reflects where mature AI engineering is heading. Organizations deploying models in production increasingly understand that their actual task distribution bears limited resemblance to published benchmark tasks. A model that scores best on SWE-bench may underperform on their TypeScript monorepo with specific patterns, libraries, and failure modes. Custom evals are more expensive to build and maintain but produce actionable signal rather than marketing-grade comparisons.
