# How Grab is Using AI Agents to Boost Team Productivity
**Source**: https://blog.bytebytego.com/p/how-grab-is-using-ai-agents-to-boost
**Date**: May 18, 2026
**Author**: ByteByteGo
**Keywords**: Grab, AI agents, multi-agent, data engineering, LangGraph, FastAPI, agent orchestration, production AI

## Elevator pitch
Grab's data engineering team built a multi-agent AI system to automate investigating data questions that consumed two days per week of senior engineer time — and discovered six things that broke when it hit production.

## Takeaways
- Grab's ADW team manages 15,000+ tables queried by ~1,000 people monthly; senior engineers spent 2 days/week answering quick questions that each required hours of investigation.
- The multi-agent architecture separates "brain" (LLM reasoning) from "hands" (specialized agents), with five agents: Classifier, Data Agent, Code Search Agent, On-call Agent, and Summarizer.
- Two distinct pathways: investigation (read-only, fully automated) and enhancement (write operations, semi-automated with mandatory human review).
- Tech stack: FastAPI, LangGraph for stateful multi-agent workflows, Redis for caching, PostgreSQL for memory, pulling data from three internal platforms (Hubble, Genchi, Lighthouse).
- Production exposed six failure modes: context window limits on complex questions, agent coordination breakdowns, guardrail bypasses, inconsistent output formats, latency issues, and user trust problems.
- Key design lesson: specialized agents beat monolithic models for maintainability and debuggability, even at the cost of coordination complexity.

## Synthesis
ByteByteGo's analysis of Grab's multi-agent AI system provides one of the most detailed public case studies of production AI agent deployment in a large enterprise. Grab, Southeast Asia's super-app handling rides, food delivery, and payments, faced a classic scaling problem: their Analytics Data Warehouse (ADW) team's best engineers were spending two full days every week answering ad-hoc data questions from colleagues across the company.

The pattern was consistent enough to automate. While every question was different, the investigation process was identical: search data catalogs, trace lineage, validate with SQL, check pipeline logs. Grab built a five-agent system (Classifier, Data Agent, Code Search Agent, On-call Agent, Summarizer) that mirrors the steps a human engineer would follow, separating the "brain" (LLM reasoning) from the "hands" (specialized tool agents).

The architecture's most important design decision was splitting work into two pathways based on risk profile. Read-only investigation questions (like "why does this data look wrong?") are fully automated through four collaborating agents. Write operations (like "add a column to this table") route through a single Enhancement Agent that generates merge requests — but every stage requires human review. This separation of concerns acknowledges that code changes to production pipelines require judgment that AI cannot yet reliably provide.

The tech stack is notably pragmatic: FastAPI for request handling, LangGraph for managing the complex stateful logic of multi-agent collaboration (where agents need to loop back, ask for more information, or hand off tasks), Redis for caching, and PostgreSQL for persistent memory. The agents interface with three internal platforms — Hubble (data catalog), Genchi (data quality observability), and Lighthouse (pipeline status).

What makes this case study especially valuable is what happened in production. Six things broke: context windows filled up on complex multi-turn conversations, agents stepped on each other's findings, users found ways around guardrails, output formats were inconsistent, latency exceeded user patience, and trust eroded when answers were wrong. The lesson: building agents is the easy part; making them reliable at scale with real users is where the real engineering begins.
