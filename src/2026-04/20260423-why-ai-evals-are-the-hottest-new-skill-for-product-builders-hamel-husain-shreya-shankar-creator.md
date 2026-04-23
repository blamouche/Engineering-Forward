# Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar (creators of the #1 eval course)

**Source**: https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill
**Date**: April 22, 2026
**Author**: Lenny Rachitsky
**Keywords**: AI evals, product management, Hamel Husain, Shreya Shankar, error analysis

## Elevator pitch
Hamel Husain and Shreya Shankar argue that evals are becoming the defining skill for AI product builders because prompts and models only matter if teams can systematically measure failure modes and improve against them.

## Takeaways
- The conversation emphasizes starting with error analysis, not with ready-made metrics.
- Good evals are described as living product requirements for AI systems.
- LLM-as-judge and code-based evals are useful, but only after humans identify what matters.
- The guests argue dogfooding alone is usually not enough for production AI quality.
- The practical message is that teams can maintain useful eval systems with moderate ongoing effort.

## Synthesis
This conversation captures why evals have moved from niche research topic to mainstream product skill. Hamel Husain and Shreya Shankar make a simple but important point: prompts, model choice, and tool integration are only part of the job. Without a disciplined way to understand how an AI system fails, teams are mostly steering by anecdote and taste. That can work for demos. It does not work reliably in production.

What stands out is their insistence on error analysis as the starting point. Instead of beginning with fashionable metrics like hallucination or toxicity, they recommend manually reviewing real traces and identifying the actual failure modes that matter in context. That is a strong product instinct. AI systems fail in domain-specific ways, and teams often do not know what quality means until they study those failures carefully.

The discussion also helps clarify the tooling stack around evals. Human review is necessary up front. Code-based checks are powerful where outcomes are verifiable. LLM-as-judge systems are scalable and practical once they are grounded in real examples and tested against human judgment. The key is that evaluation is not just a dashboard exercise. It is part of the product-development loop.

The phrase that evals are the new PRDs works because it captures their role as operationalized requirements. A good eval suite makes product expectations concrete, testable, and continuously visible. That matters more as AI products become more agentic and less deterministic. The broader takeaway is that strong AI teams will likely differentiate not only through better models or prompts, but through better discipline around seeing, measuring, and correcting what their systems actually do.
