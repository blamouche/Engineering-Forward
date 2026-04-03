# Improve coding agents' performance with Gemini API Docs MCP and Agent Skills
**Source**: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-docsmcp-agent-skills/
**Date**: April 1, 2026
**Author**: Trey Nguyen
**Keywords**: Gemini API, coding agents, Model Context Protocol, MCP, Agent Skills, API documentation, SDK patterns, developer tools

## Elevator pitch
Google introduces two tools — Gemini API Docs MCP and Agent Skills — that together achieve a 96.3% pass rate on coding evals with 63% fewer tokens by keeping AI coding agents current with up-to-date API documentation.

## Takeaways
- Coding agents often generate outdated Gemini API code because training data has an expiration date
- Gemini API Docs MCP connects agents to current documentation via the Model Context Protocol
- Agent Skills provides best-practice instructions and SDK patterns to guide agents toward current APIs
- Combined, the tools achieve 96.3% pass rate on eval set with 63% fewer tokens per correct answer
- Available at ai.google.dev/gemini-api/docs/coding-agents

## Synthesis
A persistent problem with AI coding assistants is the temporal gap between their training cutoff and the current state of any given API. As APIs evolve — adding new methods, deprecating old ones, changing recommended patterns — models trained on older snapshots of documentation continue generating code that references outdated interfaces. For rapidly evolving APIs like Gemini's, this creates a compounding problem: the more actively an API is developed, the less useful AI coding assistance becomes for it.

Google's two-part response addresses this from complementary angles. The Gemini API Docs MCP leverages the Model Context Protocol to provide coding agents with live access to current documentation and SDKs. Rather than relying on training-time knowledge, agents can query the MCP server to retrieve up-to-date API specifications, usage examples, and configuration parameters at inference time. This is a retrieval-augmented approach applied specifically to the documentation problem.

The Gemini API Agent Skills component provides a higher-level complement: instead of just raw documentation, it supplies structured best-practice instructions, resource links, and patterns that guide agents toward current SDK idioms. Where the MCP handles the factual currency problem, Agent Skills handles the pattern and idiom problem — ensuring that agents don't just know what methods exist, but know how to use them in the way that Google currently recommends.

The performance numbers are striking: a 96.3% pass rate on their evaluation set, with 63% fewer tokens per correct answer compared to vanilla prompting. The token reduction is particularly meaningful in production contexts where token count directly translates to cost and latency. It suggests that providing structured, current context enables agents to reach the correct answer more directly, without the exploratory token generation that occurs when an agent is uncertain about current API state.

This approach generalizes beyond Gemini: it illustrates a pattern for any API provider that wants to maintain AI coding assistant quality as their API evolves. Rather than waiting for model providers to incorporate updated documentation in future training runs, the MCP architecture enables API providers to serve current documentation directly to agents at inference time. The implication for developers is that the combination of retrieval-augmented documentation and structured skill definitions may become a standard pattern for maintaining AI coding assistant relevance across any actively developed API.
