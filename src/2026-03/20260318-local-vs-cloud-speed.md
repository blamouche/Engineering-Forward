# The Robotic Tortoise & the Robotic Hare
**Source**: https://tomtunguz.com/local-vs-cloud-speed/
**Date**: 2026-03-18
**Author**: Tomasz Tunguz
**Keywords**: local AI models, cloud AI, inference speed, Qwen, Claude, developer productivity, feedback loops

## Elevator pitch
A side-by-side test reveals that a local 35B-parameter model completed a payment app build 3x faster than Claude Opus 4.5 despite scoring lower on benchmarks, showing that inference speed often matters more than raw model capability for iterative development.

## Takeaways
- Local Qwen 35B on a Mac finished a payment app in 2 minutes; Claude Opus 4.5 took 6+ minutes
- The local model scored 6.5/10 in Claude's own quality assessment vs. 4.5/10 for the cloud model
- Faster response times enable multiple refinement cycles within the time a single cloud response takes
- Raw benchmark scores do not reliably predict practical effectiveness in iterative development tasks
- The advantage reverses for complex agentic or reasoning-intensive workflows where model capability dominates

## Synthesis
Tomasz Tunguz conducted a practical experiment with significant implications for AI-assisted development: he built the same payment application using Stripe's Tempo blockchain platform twice—once with Qwen 35B running locally on a Mac, and once with Claude Opus 4.5 via API. The results challenged conventional assumptions about the relationship between model capability and practical value.

The local model finished in two minutes. Claude took over six. When Tunguz asked Claude to evaluate both outputs, it rated the local model's work at 6.5 out of 10 and its own output at 4.5—the supposedly inferior model produced the more competitive result. This outcome surprised him because Claude carries approximately 20% higher benchmark scores and is roughly 50 times larger in parameter count.

The explanation lies in iteration velocity. Software development is not a single-shot task; it requires continuous refinement based on observed results. When a model responds in 30-40 seconds rather than 2-3 minutes, a developer can complete five or six revision cycles in the same timeframe a single cloud response requires. Each cycle incorporates feedback, catches errors earlier, and compounds improvements. The faster system's lower ceiling per individual response is outweighed by its higher throughput of complete thought-action-observation loops.

Tunguz is careful to note where the calculus inverts. For complex reasoning tasks, multi-step planning, or long-horizon agentic workflows, the additional depth of a larger model justifies the wait. The "tortoise wins" heuristic applies specifically to development patterns characterized by many small, independent, iterative decisions—exactly the pattern most prevalent in daily software engineering. The broader lesson is that when choosing AI tools, latency deserves as much weight in the evaluation as benchmark scores, and the best model for a given workflow is the one optimized for that workflow's actual cycle time.
