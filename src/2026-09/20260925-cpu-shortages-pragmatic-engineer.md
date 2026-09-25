# The Pulse: A New Trend of CPU Shortages
**Source**: The Pragmatic Engineer (pragmaticengineer+the-pulse@substack.com)
**Date**: 2026-09-25
**Author**: Gergely Orosz (The Pragmatic Engineer)
**Keywords**: CPU shortage, cloud providers, spot pricing, AI agents, reinforcement learning, capacity planning, TSMC, HBM, DRAM, turbopuffer, Anthropic, Opus 5.5

## Elevator pitch
After GPU and memory shortages driven by AI, a new bottleneck has emerged: CPUs. Cloud providers have effectively killed spot pricing, reservations need months of advance planning, and even large inference providers are being turned down despite having cash to spend. The root cause is AI agents running tools, compiling code, and executing tests — all CPU-heavy workloads that shift the data center ratio from 1:8 (CPU:GPU) toward 1:1.

## Takeaways
- **Spot pricing has vanished**: CPUs that used to cost 90% less on spot instances are no longer available — there's no excess capacity.
- **Reservations require months of advance planning**: Cloud providers are turning down reservations because they don't have enough CPUs or the right types.
- **Even big players are blocked**: A VP of Engineering at a large inference provider reports being at the limit of GPU and CPU capacity they can buy, despite having cash and willingness to accept long leases.
- **RL and agents drive CPU demand**: Reinforcement learning training needs CPUs to run software. General-purpose agents run tools, compile code, run tests — all CPU-heavy. The data center CPU:GPU ratio has shifted from 1:8 to 1:4, heading toward 1:1.
- **Supply chain squeeze on both sides**: At TSMC, GPUs compete with CPUs for production lines. DRAM manufacturers (SK Hynix, Samsung, Micron) are producing HBM instead of regular DRAM, making CPU memory more expensive.
- **Server orders now take ~6 months**: Previously 1-2 weeks. Prices up 10-20%.
- **Capacity planning is now mandatory for CPUs**: Katelyn Lesse (Anthropic) warns that teams who never planned CPU capacity must now forecast 12 months ahead.
- **Some cloud regions reject new tenants**: All CPU capacity is leased. Customers are paying today for capacity that comes online in December.
- **Opus 5.5 released**: 40% the cost of Fable 5.1 with superior coding capability.
- **Code reviews may vanish**: AWS Distinguished Engineer Marc Brooker believes humans will have no role in routinely reviewing code by hand.

## Synthesis
The CPU shortage is the most underreported infrastructure story of the AI era. While GPU scarcity has dominated headlines, the cascade effect on CPUs is arguably more disruptive for the broader engineering community. Most companies don't run GPU clusters, but every company uses CPUs — and the spot pricing model that enabled cost-efficient scaling for a decade is gone.

Simon Eskildsen's explanation from turbopuffer is the clearest articulation of the demand shift: reinforcement learning requires CPUs to run the software that models learn to use, and general-purpose agents need CPUs to execute tools, compile code, and run tests. This is not a temporary spike — it's a structural change in the compute mix. The ratio shift from 1:8 to potentially 1:1 CPU:GPU in AI data centers means the total silicon demand has fundamentally changed.

The supply chain analysis from Katelyn Lesse reveals a double squeeze: TSMC's production lines are constrained by GPU demand (which is more profitable per wafer), and memory manufacturers have shifted capacity to HBM (also more profitable). AMD, which doesn't own fabs, is particularly exposed. The implication is that CPU supply won't normalize for multiple quarters, and companies that haven't started capacity planning are already behind.

The note about Opus 5.5 — 40% of Fable 5.1's cost with superior coding — and Marc Brooker's prediction about the end of human code reviews suggest that the demand side will only intensify. More capable models at lower cost means more agents doing more work, which means more CPU consumption.