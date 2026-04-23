# The Pulse: ‘Tokenmaxxing’ as a weird new trend

**Source**: https://newsletter.pragmaticengineer.com/p/the-pulse-tokenmaxxing-as-a-weird-6b2
**Date**: April 23, 2026
**Author**: Gergely Orosz
**Keywords**: AI tooling, engineering productivity, token usage, management metrics, developer incentives

## Elevator pitch
Gergely Orosz shows how internal token leaderboards at Meta, Microsoft, and Salesforce turn AI usage into a vanity metric that encourages wasteful prompting instead of better engineering outcomes.

## Takeaways
- Token leaderboards can quickly turn AI usage into a status game rather than a productivity tool.
- Developers respond to measured token usage by inflating prompts, running agents unnecessarily, and generating throwaway work.
- The costs of tokenmaxxing are not just financial, because they can also degrade code quality and slow down execution.
- Shopify avoided the worst behaviors by reframing the leaderboard as a usage dashboard and adding circuit breakers for runaway spend.
- A useful management signal is business value created with AI, not raw token volume consumed.

## Synthesis
This piece is really about a classic management failure wearing new AI clothes. Once companies start measuring token consumption, employees quickly infer that more tokens means stronger adoption, stronger adoption means better optics, and better optics may matter more than shipping better software. The result is predictable. Engineers optimize for the visible metric, not for product quality, engineering speed, or cost discipline.

Orosz reports that Meta’s internal leaderboard became a public ranking of AI superusers, encouraging developers to burn tokens through sprawling agent sessions and disposable experiments. Engineers described wasteful prompting, low-value code generation, and even incidents where AI-assisted changes appeared to contribute to SEVs. Whether the original objective was signaling AI-native behavior or collecting training traces, the mechanism produced the same effect: more usage, more spend, and more noise.

The Microsoft and Salesforce examples are useful because they show how quickly a soft cultural nudge becomes an implicit performance metric. Once dashboards expose token usage and people worry about being seen as below average, the rational response is defensive overuse. Developers ask AI things they already know, prototype features they never intend to build, or run agent flows they could complete faster by hand. In other words, token spend stops being a byproduct of useful work and becomes performative compliance.

The Shopify comparison is the most practical part of the article. Its leadership treated high usage as something to inspect, not something to blindly reward, and added circuit breakers to stop runaway agents. That distinction matters. If the goal is learning how teams can use AI effectively, managers need observability around cost spikes and a habit of reviewing high-spend patterns for business value. If the goal is simply to make usage graphs go up, organizations should expect gaming.

The deeper lesson is that token count is shaping up to be this era’s lines-of-code metric. It is easy to capture, easy to compare, and easy to game. The best engineers will not necessarily be the ones who consume the most model output. They will be the ones who apply these tools with judgment, control costs, and solve real problems faster. Companies that forget that will spend a fortune teaching people to look busy with AI.
