# Running a Software Factory Efficiently at Uber Scale
**Source**: https://www.uber.com/gb/en/blog/efficient-software-factory/
**Date**: August 27, 2026
**Author**: Uday Kiran Medisetty
**Keywords**: software factory, AI agents, cost optimization, engineering productivity, observability

## Elevator pitch
Uber describes a software factory in which agent adoption is measured alongside quality and unit economics, then optimized across models, sessions, prompts, and workflows.

## Takeaways
- More than 70% of Uber pull requests are attributed to local or cloud agents.
- Costs should be decomposed into adoption, engagement, input workload, and output workload.
- Outcome-based metrics connect spend to merged pull requests, reviews, alerts, and reliability.
- Model routing, caching, and fewer unproductive turns can improve unit economics.
- Quality signals such as revert rate and MTTR must accompany cost reduction.

## Synthesis
Uber's account is unusually concrete about the operational side of widespread agent use. It reports that agents now touch more than 70% of pull requests, with thousands of skills and tens of thousands of daily skill executions. That scale turns AI development from a collection of individual subscriptions into a portfolio-management problem. The company therefore treats sessions, models, tokens, requests, and managed-agent outcomes as measurable components of a software factory.

The key idea is a cost equation rather than a headline spend number. Total cost changes because more people use a tool, each user issues more requests, requests contain more input or output tokens, or models and prices change. Separating those effects lets teams see whether a saving is a genuine efficiency improvement or merely a shift in workload. Uber also tracks unit metrics such as cost per thousand requests, per session, and per active session hour, then relates managed agents to outcomes like reviews completed, incidents triaged, or pull requests merged.

This avoids a false choice between adoption and discipline. The company describes substantial usage growth while holding model choice constant to measure lower cost per request and session. The transferable lesson is to optimize the unnecessary work an agent does around a user request: planning, retries, context size, and poor routing. But savings are incomplete without quality measures. A cheaper review agent that increases reverts or slows incident response has not improved the factory. Effective governance therefore couples financial telemetry to reliability and business outcomes.
