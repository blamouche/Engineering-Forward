# Advanced Evals: How to Find (and Fix) Hidden AI Failures in Your Product
**Source**: Lenny's Newsletter (lenny@substack.com)
**Date**: 2026-09-22
**Author**: Hamel Husain & Shreya Shankar (via Lenny's Newsletter)
**Keywords**: evals, AI evaluation, error discovery, traces, coding agents, criteria drift, active learning, AI product management, annotation

## Elevator pitch
Hamel Husain and Shreya Shanker present an advanced guide to AI product evaluation, arguing that most teams skip the critical "error discovery" phase and jump straight to writing metrics — measuring the wrong things. They offer a 30-minute workflow using coding agents to find the failures that actually matter.

## Takeaways
- **Error discovery is the eval equivalent of product discovery**: Just as product discovery identifies which problems are worth solving, error discovery reveals which AI failures are worth measuring — and skipping it means building dashboards around the wrong metrics.
- **Criteria drift is the core challenge**: Your definition of "good" changes as you review examples, and you often only discover what your criteria should be after seeing failures — a process that can't be fully automated.
- **Agents are good at obvious failures, bad at product judgment**: In a study of 100 production traces, agents caught trace-internal contradictions but missed failures requiring product context (objection handling, formatting, missed handoffs) and introduced noise by flagging good responses as failures.
- **A 3-step workflow with coding agents**: Start with traces (instrument your app to log complete session records), review and annotate with a custom-built review app (10+ traces minimum, 100 recommended), then turn failure modes into prioritized product issues.
- **The evals skills plugin**: `npx skills add https://github.com/ai-evals-course/evals-skills` installs a plugin that reads your trace schema, builds a customized review interface, clusters traces for diverse sampling, and learns from your annotations to suggest additional issues.
- **Evals are now a defining PM skill**: Mike Krieger (Anthropic CPO) calls evals "the most important thing we can teach product people," and Garry Tan (YC CEO) says "evals are emerging as the real moat for AI startups."
- **Real-world impact**: Shopify's eval-guided AI workflow builder was 2.2x faster and 68% cheaper; Cursor reduced costs 41% with eval-driven routing; Ramp went from 35% to 83% accuracy on receipt collection after investing in evals.

## Synthesis
This article is the most practically useful piece on AI evaluation published in 2026. The central argument — that error discovery precedes metric writing, and that most teams get this backwards — reframes the eval conversation from "how do we measure" to "what should we measure." The distinction matters because the industry is flooding with eval tools, frameworks, and benchmarks, but very little guidance on how to decide what actually matters for your specific product.

The concept of "criteria drift" is the article's most important intellectual contribution. It explains why fully automated eval discovery fails: you don't know your criteria until you've reviewed enough failures to understand what "good" means for your product. This is a deeply human process — it requires product judgment, domain knowledge, and the willingness to change your mind as you see more data. The article's honest assessment that agents "are far less reliable when a failure depends on your definition of a good product experience" is a crucial corrective to the hype around AI-powered eval automation.

The workflow itself is well-designed. Starting with traces (complete session records including system prompts, tool calls, and outputs) is the right foundation — you can't evaluate what you can't reconstruct. The review app that the skills plugin generates, customized to your data schema, solves a real problem: generic eval tools force your data into their format, while a custom-built interface can render conversations, code, or documents the way users actually see them. The recommendation to annotate 100 traces before trusting agent suggestions is conservative but wise — it ensures sufficient human signal before ceding judgment to automation.

The real-world case studies — Shopify, Cursor, Ramp, Harvey — demonstrate that evals are not a theoretical exercise but a competitive advantage. The specific numbers (2.2x faster, 68% cheaper, 35%→83% accuracy) are the kind of evidence that moves evals from "nice to have" to "board-level priority." The article's timing is perfect: as AI products proliferate and model changes accelerate, the teams that invest in eval infrastructure now will compound their advantage over teams that don't.