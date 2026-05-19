# Agent Evaluation: A Detailed Guide
**Source**: https://cameronrwolfe.substack.com/p/agent-evals
**Date**: 2026-05-18
**Author**: Cameron R. Wolfe, Ph.D.
**Keywords**: AI agents, evaluation, benchmarks, tool calling, reasoning models, agentic loop, ReAct, multi-agent systems

## Elevator pitch
A comprehensive guide to evaluating AI agents, covering fundamentals of agent systems through practical evaluation frameworks with real-world case studies.

## Takeaways
- Agent evaluation is fundamentally harder than LLM evaluation because agents operate over long time horizons, interact with environments, and must recover from errors autonomously
- The three core components of an agent system are: the underlying LLM (or reasoning model), tools for interaction, and clear instructions
- Tool calling evaluation spans multiple dimensions: invocation accuracy, selection accuracy, structural validity, trajectory accuracy, and outcome-oriented metrics
- Multi-agent systems should only be adopted after exhausting single-agent optimization — single agents are easier to evaluate and maintain
- The ReAct framework (Reasoning + Action) remains a foundational pattern: agents observe, reason, take action, and repeat until a terminal state

## Synthesis
Cameron Wolfe provides an exhaustive walkthrough of agent evaluation methodology, starting from first principles. The piece distinguishes between conventional LLM evaluation (static benchmarks, short conversations) and agent evaluation (long-horizon tasks, tool use, environmental interaction). This distinction matters because agents introduce failure modes — wrong tool calls, context decay over long runs, cascading errors — that don't appear in standard LLM benchmarks.

The article breaks down agent architecture into three components: the underlying model, the tool layer, and the instruction layer. Wolfe explains how tool calling is handled natively in token streams (using special tokens like Qwen3's XML-style tags), and walks through the specific metrics used to evaluate tool-calling performance. The treatment of reasoning models is particularly relevant — reasoning models that generate long thinking traces before answering are better suited to agentic tasks because they can decompose problems and self-reflect.

A key practical insight is the recommendation to start with single-agent designs and optimize before reaching for multi-agent orchestration. Wolfe notes that multi-agent systems compound evaluation complexity and maintenance burden. The piece also covers the ReAct framework in detail, showing how structured think-act-observe loops provide both rigor and interpretability. Finally, Wolfe offers a practical roadmap for building custom agent evaluations, emphasizing that rigorous measurement beats anecdotal checks for rapidly improving agent capabilities.
