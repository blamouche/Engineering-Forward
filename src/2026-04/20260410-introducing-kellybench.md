# Introducing KellyBench

**Source**: https://www.gr.inc/releases/introducing-kellybench
**Date**: Unknown
**Author**: Unknown
**Keywords**: models, season, adapt, betting, claude, failing

## Elevator pitch
Language models are saturating benchmarks for procedural tasks with narrow objectives.

## Takeaways
- But they are increasingly being deployed in long-horizon, non-stationary environments with open-ended goals.
- Most existing evaluations do not measure capabilities in these settings.
- Today we are releasing KellyBench, a long-horizon environment for evaluating sequential decision-making in sports betting markets.
- Agents are placed in a simulated market for the 2023–24 English Premier League season and asked to maximise their long-term bankroll growth.
- They are given detailed historical data - advanced statistics, lineups, past results, and public odds - and must build machine learning models, identify edge in betting markets, size bets, manage risk, and adapt as the season unfolds.

## Synthesis
Language models are saturating benchmarks for procedural tasks with narrow objectives. But they are increasingly being deployed in long-horizon, non-stationary environments with open-ended goals. Most existing evaluations do not measure capabilities in these settings. Today we are releasing KellyBench, a long-horizon environment for evaluating sequential decision-making in sports betting markets. Agents are placed in a simulated market for the 2023–24 English Premier League season and asked to maximise their long-term bankroll growth. They are given detailed historical data - advanced statistics, lineups, past results, and public odds - and must build machine learning models, identify edge in betting markets, size bets, manage risk, and adapt as the season unfolds. Every frontier model we evaluated lost money over the season and many experienced ruin. The best-performing model, Claude Opus 4.6, finished with an average return of −11% over three seeds.
