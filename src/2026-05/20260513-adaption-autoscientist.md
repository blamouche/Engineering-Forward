# Adaption Aims Big with AutoScientist, an AI Tool That Helps Models Train Themselves
**Source**: https://techcrunch.com/2026/05/13/adaption-aims-big-with-autoscientist-an-ai-tool-that-helps-models-train-themselves/
**Date**: 2026-05-13
**Author**: Russell Brandom
**Keywords**: Adaption, AutoScientist, AI training, fine-tuning, self-improving AI, Sara Hooker, Adaptive Data, neolabs, frontier AI

## Elevator pitch
Adaption, founded by former Cohere VP of AI research Sara Hooker, has launched AutoScientist—a tool that automates the fine-tuning process by co-optimizing both data and model simultaneously, potentially democratizing frontier-level AI training beyond the major labs.

## Takeaways
- AutoScientist co-optimizes both data and model simultaneously, learning the best approach for any target capability—a departure from traditional sequential fine-tuning workflows
- The tool builds on Adaption's existing Adaptive Data product, creating a pipeline where continuously improving datasets generate continuously improving models
- Adaption claims AutoScientist has more than doubled win rates across different models, though conventional benchmarks like SWE-Bench or ARC-AGI don't apply given its task-specific nature
- CEO Sara Hooker positions this as democratization, stating it "suggests we can finally allow for successful frontier AI trainings outside of these labs"
- The tool is being offered free for the first 30 days after release, betting that users will see enough value to convert to paid

## Synthesis

The promise of AI systems that can improve themselves has been a north star for the research community for years—the recursive self-improvement loop that could accelerate progress beyond human engineering bandwidth. Adaption's AutoScientist represents one of the most concrete steps toward operationalizing that vision, and it comes from a team with serious credentials.

Sara Hooker, Adaption's CEO and co-founder, previously led AI research at Cohere, one of the major enterprise-focused foundation model companies. Her bet—and the bet of investors backing a new generation of "neolabs"—is that the scaling race toward ever-larger models is giving way to a smarter race around training methodology. AutoScientist embodies this thesis: instead of brute-forcing capability through parameter count, it automates the discovery of optimal training recipes for specific capabilities.

The technical architecture is noteworthy. Traditional fine-tuning follows a sequential pattern: curate a dataset, train on it, evaluate, adjust the dataset, repeat. AutoScientist collapses this loop by co-optimizing both the data and the model parameters simultaneously. The system learns not just what the model should learn, but how it should learn—the optimal data mix, the most effective training schedule, the right hyperparameters for the target capability. This isn't just automation; it's meta-learning applied to the training process itself.

The claimed results—more than doubled win rates across different models—are striking but difficult to contextualize without standard benchmarks. Adaption argues this is inherent: since AutoScientist optimizes for specific, user-defined capabilities rather than general-purpose metrics, conventional evaluation suites don't apply. This is both a strength (the tool does something uniquely valuable) and a vulnerability (it's hard for potential users to compare against alternatives).

The strategic positioning is clear: democratize frontier AI training. Hooker explicitly frames AutoScientist as enabling successful frontier training "outside of these labs"—meaning outside the OpenAI/Anthropic/Google oligopoly that dominates foundation model development. If the tool delivers, it could meaningfully reshape the competitive landscape, allowing smaller labs and enterprise teams to produce highly capable, task-specific models without the billion-dollar infrastructure of the majors.

The free-for-30-days launch strategy is a confident bet on product quality. In a market saturated with AI tooling claims, Adaption is essentially saying: try it yourself, the results will speak louder than any benchmark. The parallel Hooker draws to code generation—"the same way that code generation unlocked a lot of tasks, this is going to unlock a lot of innovation at the frontier of different fields"—is ambitious but not unreasonable if AutoScientist genuinely automates a significant portion of the ML research workflow.

The bigger question is whether automated training optimization can compound. If AutoScientist can improve a model, and that improved model can then better operate AutoScientist to further improve itself, Adaption may have built more than a product—they may have built the first rung of a ladder toward genuinely recursive self-improvement.
