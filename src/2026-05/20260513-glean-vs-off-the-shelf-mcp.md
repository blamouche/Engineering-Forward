# Glean vs. Off-the-Shelf MCP: How the Right AI Context Layer Reduces Token Costs and Drives Better Results
**Source**: https://www.glean.com/blog/cowork-mcp-eval
**Date**: May 13, 2026
**Author**: Neil Dhruva, Karthik Rajkumar, Chenhao Yang, Julie Mills (Glean)
**Keywords**: MCP, Model Context Protocol, Glean, AI context, token costs, enterprise AI, federated search, centralized indexing, Claude Cowork, agent frameworks

## Elevator pitch
Glean benchmarked its centralized context layer against off-the-shelf MCP tools using Claude Cowork and found it was preferred 2.5x more often while consuming 30% fewer tokens, demonstrating that context architecture—not just model quality—determines the economics and effectiveness of enterprise AI coworkers.

## Takeaways
- Glean was preferred ~2.5x as often as off-the-shelf MCP tools when using Claude Cowork as the constant harness across ~175 enterprise queries
- Off-the-shelf MCP tools consumed 30% more tokens on average; when they did produce correct answers, they used nearly double the tokens (83k vs Glean's 43k) via brute-force multi-loop reasoning
- Federated search imposes a "token tax" because each MCP tool requires individual API calls and the model must normalize, aggregate, and re-reason over inconsistently retrieved data
- Centralized indexing (Glean's approach) normalizes data across sources into a single layer, enabling cross-application ranking signals that federated approaches miss
- Context quality becomes more important as task complexity increases—Glean's win rate rose from 66% on simple tasks to 73% on complex multi-step queries

## Synthesis
Glean's engineering team conducted a rigorous benchmark comparing their centralized context layer against off-the-shelf MCP servers, holding Claude Cowork (with Claude Sonnet 4.6) constant as the execution harness. The results make a compelling case that the context architecture underlying AI coworkers is at least as important as the model itself when it comes to enterprise-grade reliability and cost efficiency.

The fundamental architectural divide is between federation and indexing. Off-the-shelf MCP tools embody a federated approach: each connector (Google Drive, Gmail, Slack, Salesforce, Atlassian) provides its own search, and the model must call each tool independently, then synthesize results across inconsistent retrieval strategies. Glean's centralized indexing takes the opposite approach—ingesting and normalizing all enterprise data into a unified knowledge graph with consistent ranking, cross-application authority signals, and up-to-date linkage information.

The token economics are striking. Off-the-shelf MCP tools consumed 30% more tokens on average. More revealingly, when those tools did manage to produce correct answers, they achieved it through brute force—nearly double the token consumption (83k vs 43k), reflecting additional tool calls, reasoning loops, and over-fetching to compensate for poor initial retrieval. Glean's token usage remained stable in the 42-44k range regardless of outcome quality, indicating a fundamentally more efficient retrieval pattern.

The benchmark evaluated responses on utility (work-readiness), correctness, completeness, and tool fidelity. Glean outperformed across every category. The gap widened with task complexity—from 66% preference on simple queries to 73% on multi-step tasks requiring coordination across multiple data sources. This suggests that as AI coworkers take on more ambitious autonomous work, the context layer becomes a compounding advantage or liability.

The practical implications are significant for enterprise AI budgets. As frontier model token prices rise and engineering teams at companies like Uber and ServiceNow report burning through annual AI coding budgets within months, optimizing the context layer becomes a direct cost-control lever. Prompt caching—widely underutilized per the Datadog report—is one approach, but Glean's results suggest that architectural decisions about indexing versus federation may be the higher-order optimization.
