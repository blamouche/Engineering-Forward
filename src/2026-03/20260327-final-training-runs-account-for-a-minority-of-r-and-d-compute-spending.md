# Final training runs account for a minority of R&D compute spending
**Source**: https://epochai.substack.com/p/final-training-runs-account-for-a
**Date**: March 27, 2026
**Author**: Epoch AI
**Keywords**: AI compute, R&D spending, training runs, model development, benchmarking

## Elevator pitch
Epoch AI argues that the headline cost of a frontier model’s final training run hides the bulk of compute spend, which is dominated by experimentation, data generation, and failed runs during R&D.

## Takeaways
- The final training run is only the last step in a long R&D pipeline with heavy compute usage.
- OpenAI’s 2024 spending suggests only ~10% of R&D compute went to final training runs.
- IPO disclosures from MiniMax and Z.ai show similar patterns despite smaller budgets.
- Differences in training-to-R&D ratios may reflect how close a firm is to the frontier.
- Low GPU utilization during experimentation means spending and FLOP usage can diverge.

## Synthesis
This Epoch AI Gradient Updates post challenges the common mental model that AI compute spend is mostly about a single, massive training run. It argues that a model with a public name represents the end of a long and expensive R&D journey that includes multiple exploratory training runs, synthetic data generation, iterations on model architecture, and experiments that never ship. As a result, the final run—what most people cite when discussing training costs or compute thresholds—captures only a minority of real compute expenditure.

The piece grounds this claim with recent data. Epoch AI previously estimated that OpenAI spent roughly $5B on R&D compute in 2024, and only about $500M (around 10%) went to the final training runs behind released models. To test whether this was idiosyncratic to a frontier lab, the authors look at two smaller Chinese firms, MiniMax and Z.ai, which disclosed R&D compute spending in IPO filings. By pairing the reported R&D windows with models released a quarter later, and estimating training run compute from Epoch’s model database, they derive comparable ratios: 22.6% for MiniMax and 12.3% for Z.ai. The pattern holds across companies with different scales, locations, and business models: the final training run is a minority share of compute spend.

The methodology matters because the estimates rely on assumptions about GPU peak FLOP/s, model FLOP utilization (MFU), and price per GPU-hour. The authors propagate uncertainty via Monte Carlo simulation, and note that R&D workloads tend to have lower MFU than final training runs because experimentation includes idle time, failed jobs, and debugging. This means two activities with similar spending can represent very different amounts of effective compute. The analysis therefore focuses on spending shares rather than precise FLOP totals, and flags the uncertainties explicitly.

A key implication is about catch-up dynamics. If frontier companies must explore many possible research directions, they should spend more on experimentation, pushing their training-to-R&D ratio down. Firms further from the frontier can learn from public results, skip some exploratory work, and devote more of their compute budget to actual training runs. MiniMax’s higher ratio is consistent with that idea. Z.ai’s ratio, however, looks closer to OpenAI’s, which complicates the story. With only three data points and wide confidence intervals, the post cautions against drawing strong conclusions about the drivers of these differences.

Overall, the post reframes how to interpret compute numbers. Focusing only on the final training run can understate total R&D investment and overstate the cost advantage of replication. The bulk of compute spend is often in the experiments and iterations that precede a model’s public release. If this generalizes, policy discussions and competitive analyses should account for the full R&D pipeline rather than only the headline training run. The authors note that better disclosure—via IPO documents or future public filings—will be essential to refine these estimates and understand how compute spending patterns evolve as the industry matures.
