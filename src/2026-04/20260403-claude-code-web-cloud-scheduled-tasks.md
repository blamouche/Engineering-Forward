# Schedule Tasks on the Web: Claude Code Cloud Scheduled Tasks
**Source**: https://code.claude.com/docs/en/web-scheduled-tasks
**Date**: April 3, 2026
**Author**: Anthropic
**Keywords**: Claude Code, scheduled tasks, cloud, automation, GitHub, recurring tasks, CI, MCP connectors

## Elevator pitch
Claude Code now supports cloud-hosted scheduled tasks that run recurring prompts on Anthropic-managed infrastructure — even when your computer is off — with GitHub integration, MCP connectors, and configurable environments.

## Takeaways
- Cloud scheduled tasks run on Anthropic infrastructure with no requirement for the user's machine to be on
- Three scheduling options: cloud (Anthropic-managed), desktop (local machine), and /loop (session-scoped)
- Tasks clone GitHub repositories at each run, work in claude/-prefixed branches, and can create pull requests
- MCP connectors enable access to external services (Slack, Linear, Google Drive) during each run
- Minimum interval 1 hour; configurable environments support API keys, setup scripts, and network access controls

## Synthesis
Cloud scheduled tasks represent a meaningful expansion of Claude Code's operational model: from a tool that requires active human sessions to infrastructure that can operate autonomously on recurring schedules. The practical applications described — reviewing open pull requests each morning, analyzing CI failures overnight, syncing documentation after PRs merge, running dependency audits weekly — are tasks that currently require either human discipline to perform regularly or custom automation scripts to run without human involvement.

The architecture reflects deliberate constraints. Cloud tasks clone repositories fresh at each run and work in claude/-prefixed branches rather than pushing directly to main branches. This design prevents scheduled tasks from making unreviewable changes to production code, maintaining human oversight as a structural property rather than a policy. The default restriction to claude/-prefixed branches means developers must actively choose to grant broader push permissions rather than discovering unexpected changes in protected branches.

The three scheduling modes offer a useful spectrum. Session-scoped /loop polling is appropriate for quick feedback during active development. Desktop scheduled tasks suit workflows that need local file access and can tolerate machine availability requirements. Cloud tasks handle the persistent automation use case — work that must run reliably regardless of the developer's machine state.

MCP connector integration is the feature that makes cloud tasks genuinely useful for complex workflows. A task that needs to read from Slack, create issues in Linear, and commit changes to GitHub requires integration with multiple external services. By inheriting the user's connected MCP connectors, cloud tasks can perform these multi-service workflows without requiring custom integration code.

The configurable environment system — API keys, setup scripts, network access controls — addresses the practical reality that most automated tasks need access to external services and infrastructure. A dependency audit task needs npm registry access; a documentation sync needs documentation API credentials. The environment abstraction provides these without requiring hardcoded secrets in task prompts.

For teams looking to reduce the human overhead of maintaining engineering hygiene, cloud scheduled tasks provide a low-integration-cost path to automating tasks that are important but not urgent enough to reliably receive manual attention.
