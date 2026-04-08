# How We Release the Spotify App: A Look Under the Hood (Part 2)

**Source**: https://engineering.atspotify.com/2026/2/how-we-release-the-spotify-app-part-2
**Date**: February 2026
**Author**: Spotify Engineering
**Keywords**: release dashboard, backstage, state machine, automation, release tooling

## Elevator pitch
Part 2 focuses on the tooling behind Spotify’s release process: a Backstage-based dashboard, a unifying backend, and a “Robot” state machine that advances releases when conditions are met.

## Takeaways
- Spotify built the Release Manager Dashboard to reduce context switching across many data sources.
- Caching and pre-aggregation were necessary to make the dashboard operationally cheap and fast.
- The release process is modeled as an explicit state machine with advancement conditions.
- Automation removed hours of delay caused by waiting for a human to click the next step.
- This is a strong example of tooling evolving directly from observed process bottlenecks.

## Synthesis
Part 2 is the more reusable engineering story because it translates release operations into productized internal tooling. The dashboard is not just a UI convenience; it is a way to collapse fragmented release evidence into a single operational view. More interestingly, Spotify used the resulting time-series data to identify that some delays were pure coordination waste, then encoded the workflow as a state machine and automated it. That progression—observe, centralize, measure, automate—is exactly how mature platform teams should attack operational toil. It is a nice reminder that the best internal tools usually start as relief valves for specific human pain.
