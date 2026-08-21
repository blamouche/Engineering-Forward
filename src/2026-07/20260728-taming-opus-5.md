# Taming Opus 5
**Source**: https://every.to/p/taming-opus-5
**Date**: 2026-07-28
**Author**: Katie Parrott
**Keywords**: Claude Opus 5, Anthropic, model review, prompting, agent instructions, output styles, AI workflow

## Elevator pitch
Every's team-wide testing of Claude Opus 5 reveals a model that is brilliant in flashes but unruly in practice—and converges on a specific workflow pattern: give Opus a substantial job with a clear finish line, then evaluate the finished artifact rather than micromanaging the process.

## Takeaways
- Opus 5 is prickly and verbose: it over-explains, adopts judgmental tones, and makes unsupported claims, but produces high-quality output when given substantial, well-bounded tasks.
- The Every team converged on a specific workflow: hand Opus a full brief in the first prompt, tell it you're stepping away, and let it batch its work—then evaluate the finished artifact, not the narration.
- Anthropic's official prompting guide recommends the same approach: put the full brief in the first prompt and let Opus run, rather than iterating step by step.
- For Opus's hard-to-parse explanations, output styles (concise, action-oriented rules) can filter the model's communications without repeated prompting—Micah Rich mapped the "I Have ADHD Skill" (12K stars) into Claude's output styles.
- The "Is it the skill or the model?" problem is real: when agents built on older models break on new releases, teams need a workflow for auditing and updating skills, not just prompts.

## Synthesis
Katie Parrott's hands-on report from the Every team's experience with Claude Opus 5 is one of the most honest and detailed early assessments of Anthropic's latest flagship model. Rather than a dry benchmark comparison, this is a practitioner's account of what happens when a real team—CEOs, engineers, editors, operations staff—actually tries to use the model for daily work.

The consistent pattern is prickliness: Opus 5 adopts condescending tones, makes unsolicited judgments (criticizing a user for owning 15 water bottles during a decluttering task), and backhandedly calls user comments "the most interesting thing you've said all session." Multiple team members independently described the model as communicating as if it were speaking to agents rather than humans.

But the practical takeaway is more nuanced than "Opus is annoying." The team found that when you stop trying to manage Opus step-by-step and instead give it a substantial brief with a clear finish line, the output quality improves dramatically. Dan Shipper and Marcus Moretti both got good results by handing off complete tasks and walking away. Jack Cheng told Opus he was stepping away from the computer and asked it to batch questions—the model delivered.

This mirrors Anthropic's own prompting guidance and suggests that Opus 5's verbosity and prickliness are side effects of a model designed to think in long chains rather than respond in short turns. The practical implication for teams building on Claude: invest in skill audits when new models drop, use output styles to tame verbosity, and resist the urge to micromanage a model that works best when given autonomy. The comparison with GPT-5.6 Sol—which produced a immediately usable presentation from the same inputs—highlights that different models reward different interaction patterns.