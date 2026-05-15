# Context Makes the Coworker: Glean vs. Off-the-Shelf MCP
**Source**: https://www.glean.com/blog/cowork-mcp-eval
**Date**: 2026-05-13
**Author**: Neil Dhruva, Karthik Rajkumar, Chenhao Yang, Julie Mills (Glean)
**Keywords**: MCP, context layer, enterprise AI, federated search, centralized indexing, token costs, Claude Cowork, AI coworkers

## Elevator pitch
Glean benchmarked its centralized indexing against off-the-shelf MCP tools using Claude Cowork and found that better context layers deliver ~2.5x higher preference rates while consuming 30% fewer tokens — proving that the economics of enterprise AI hinge on context quality, not just model capability.

## Takeaways
- Glean was preferred ~2.5x as often as off-the-shelf MCP tools across ~175 enterprise queries when benchmarked with Claude Cowork as the common harness
- Off-the-shelf MCP tools consumed ~30% more tokens on average; to win on correctness, they had to brute-force with nearly double the token usage (83k vs 43k)
- The advantage of centralized context grows with task complexity: Glean's win rate rose from 66% on simple tasks to 73% on complex, multi-step queries
- Federated search carries a "token tax" — models compensate for poor retrieval by over-fetching data and running multiple reasoning loops
- As frontier model pricing rises and consumption accelerates, the economics of the context layer become a direct driver of enterprise AI costs

## Synthesis
Glean's engineering team conducted a rigorous benchmark designed to isolate the impact of the context layer on AI coworker performance. Using Claude Cowork as the constant harness and Claude Sonnet 4.6 as the model, they compared their own remote MCP server — backed by centralized indexes and a cross-application knowledge graph — against off-the-shelf MCP servers for tools like Google Drive, Gmail, Slack, Salesforce, and Atlassian across approximately 175 queries.

The results are striking: Glean was preferred ~2.5x as often when evaluators scored responses on a 5-point preference scale across four dimensions: utility (how work-ready is the output?), correctness (are claims backed by verified sources?), completeness (did it finish the task end-to-end?), and tool fidelity (did it use tools correctly without errors or interruptions?).

The token economics tell an even sharper story. Off-the-shelf MCP tools used 30% more tokens on average. When they managed to produce correct answers, the token gap widened dramatically — roughly 83,000 tokens versus Glean's 43,000. The pattern is revealing: achieving correctness with federated tools required brute-force search, more tool calls, and more reasoning loops. It was a workaround, not efficiency. Glean's token usage, by contrast, remained stable within a narrow ~42k–44k band regardless of outcome.

The article makes a compelling case that MCP, while a valuable standardization layer for connectivity, does not standardize quality. Two MCP servers can expose identical interfaces but deliver vastly different results depending on their underlying retrieval architecture. This is the difference between federation (querying each system independently with its native search) and centralized indexing (normalizing all data into a single layer with cross-application ranking signals).

The implications extend beyond immediate quality metrics. As AI coworkers take on longer-running, multi-step work, retrieval errors compound — each missed signal can cascade into incorrect write actions or flawed analysis. And as frontier model pricing increases (with companies like Uber and ServiceNow reportedly burning through annual AI coding budgets in months), the token tax of poor context becomes a genuine financial liability.

For enterprise AI buyers, the message is clear: the context layer is not a commodity. It is a first-order determinant of both quality and cost, and its importance grows as tasks become more ambitious and autonomous.
