# What Salesforce Learned from 20,000 Enterprise Agent Deployments

**Source**: https://blog.bytebytego.com/p/what-salesforce-learned-from-20000
**Date**: June 9, 2026
**Author**: ByteByteGo (interview with John Kucera, Salesforce CPO of Agentforce)
**Keywords**: enterprise-agents, Agentforce, Salesforce, agent-deployment, guardrails, feedback-loops, anti-patterns, multi-agent-orchestration, deterministic-workflows, KPIs, context-engineering

## Elevator pitch
Salesforce's experience deploying AI agents across 20,000 enterprise customers — with their support agent alone handling over three million conversations — reveals that 90% of the work happens after launch, and the teams that succeed are those that build tight feedback loops, encode policies in code rather than prompts, and keep their context lean.

## Takeaways
- The effort distribution for AI agents is the inverse of traditional software: 90% of work happens post-launch, not pre-launch
- Every agent needs a concrete KPI tied to a real business outcome — Salesforce's support agent uses containment rate (cases fully resolved without human follow-up)
- Agentic Work Units (AWUs) provide a standardized way to measure actual task completion beyond raw activity or interaction counts
- Trust architecture requires both input guardrails (secure data retrieval, zero data retention, trust-boundary hosting) and output guardrails (tool validation, grounding checks, content filtering)
- Data masking should not be the default for agents — it strips the context the agent needs for reasoning
- Three anti-patterns consistently degrade performance: over-reliance on LLM reasoning where code is better, prompting harder instead of encoding policies, and poor context engineering
- Agent Script (Salesforce's TypeScript-based deterministic scripting framework) lets you define control flow alongside LLM reasoning — if you can write the logic as a flowchart, it should probably be code
- The future is multi-agent orchestration (parent agents coordinating specialized sub-agents three levels deep) and agents that work beyond the chat window across channels

## Synthesis
The article draws on an interview with John Kucera, Salesforce's CPO of Agentforce, to distill lessons from deploying AI agents across 20,000 enterprise customers. The central insight reframes the software lifecycle: while traditional software puts 90% of effort before launch, AI agents flip this ratio — 90% of the work happens after the agent goes live. This is because LLMs are non-deterministic, and real users ask things the demo never anticipated.

The pre-launch foundations are scoped around three pillars. First, start small and focused — agent capabilities are evolving fast, and a focused use case gives production learnings without overcommitting. Second, tie the agent to a measurable KPI. Salesforce's own support agent uses containment rate (percentage of cases fully resolved without human follow-up), complemented by Agentic Work Units (AWUs) that quantify work completed per interaction. Third, build the trust layer: input guardrails protect data before it reaches the LLM (secure retrieval, zero data retention, trust-boundary hosting), while output guardrails validate responses (tool validation prevents hallucinated actions, grounding checks prevent fabricated facts, content filtering catches harmful output).

The post-launch section details a four-category feedback loop for triage: tone and brand alignment (fix in system prompt), logic errors (check tool configurations, consider deterministic scripting), data quality (route to data owners), and coverage gaps (expand scope or build escalation paths). The speed of this feedback loop turned out to be the gate to scaling — teams with fast loops gained KPI confidence and expanded; teams with slow loops stayed stuck in pilot mode.

Three anti-patterns emerged across 20,000 deployments. Over-reliance on LLM reasoning where deterministic code is better led Salesforce to build Agent Script, a TypeScript framework for specifying control flow alongside LLM reasoning. Prompting harder instead of encoding policies fails because LLMs don't respond to emphasis — business rules should be explicit structured policies, not natural-language instructions. Poor context engineering — passing full unfiltered API responses (one e-commerce company's get_orders returned 100K tokens by default) — hurts both accuracy and latency; trimming to relevant fields (2K tokens) improved both simultaneously.

Looking forward, Salesforce sees multi-agent orchestration going three levels deep, agents expanding beyond the chat window to multi-session and background tasks, and the pace of change continuing to accelerate. But the core engineering disciplines — start small, measure what matters, build tight feedback loops, encode policies in code, keep context lean — are model-agnostic and durable.