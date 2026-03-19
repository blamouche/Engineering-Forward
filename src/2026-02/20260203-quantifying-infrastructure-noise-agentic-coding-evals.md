# Quantifying Infrastructure Noise in Agentic Coding Evals
**Source**: https://www.anthropic.com/engineering/infrastructure-noise
**Date**: 2026-02-03
**Author**: Gian Segato, Nicholas Carlini, Jeremy Hadfield, Mike Merrill, Alex Shaw
**Keywords**: benchmarks, evaluation, infrastructure noise, agentic coding, Terminal-Bench, resource allocation, leaderboards

## Elevator pitch
Infrastructure configuration can shift agentic coding benchmark scores by up to 6 percentage points—sometimes exceeding the gaps between top-ranked models—making resource allocation a critical but underreported variable in evaluation methodology.

## Takeaways
- Agentic evals are environment-dependent: unlike static benchmarks, they involve runtime environments where models write code, run tests, and iterate, making infrastructure a meaningful experimental variable.
- Infrastructure error rates ranged from 5.8% under strict resource enforcement to 0.5% with uncapped resources on Terminal-Bench 2.0.
- Success rates jumped approximately 4 percentage points between 3x and uncapped resource allocations—a difference that would meaningfully alter model rankings on current leaderboards.
- Different resource limits reward different strategies: tight constraints favor efficient approaches, generous allocations enable heavyweight methods.
- Recommended practice: specify guaranteed resource allocations and kill thresholds separately; a 3x ceiling above specified minimums balances stability with meaningful constraints.
- Small leaderboard differences below 3 percentage points warrant skepticism without documented, standardized infrastructure configurations.

## Synthesis
This paper from Anthropic's engineering team identifies a confound in agentic benchmark methodology that the field has largely ignored: the machines running the evaluation matter, and they matter more than most assume. While static benchmarks like MMLU or GPQA present the same task regardless of hardware, agentic evals spin up real execution environments where resource constraints actively shape what solutions are possible.

The finding has practical implications beyond academic benchmarking. Any organization running internal agentic evals to compare models or measure progress needs consistent infrastructure across evaluation runs. If resource allocation changes between runs—because of cloud instance availability, cost optimization, or environment upgrades—observed score changes conflate genuine capability differences with infrastructure variation.

The 3x ceiling recommendation is useful engineering guidance. Completely uncapped resources produce artificially clean results that don't reflect deployment conditions; excessively tight limits introduce noise that drowns signal. A 3x buffer above specified minimums appears to hit the practical optimum, reducing infrastructure-induced errors while still creating meaningful constraints that differentiate efficient from inefficient strategies.

The broader implication for leaderboard consumers is sobering. Many prominent model comparisons show differences of 1-3 percentage points presented as evidence of meaningful capability gaps. This paper suggests those differences may be entirely explained by infrastructure variation between evaluation runs. The field needs standardized evaluation infrastructure specifications reported alongside results—analogous to how experimental physics reports equipment specifications—before small leaderboard differences can be interpreted as meaningful.
