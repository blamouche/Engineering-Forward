# Use Fable Before You Know What to Ask
**Source**: https://every.to/context-window/use-fable-before-you-know-what-to-ask
**Date**: 2026-07-07
**Author**: Katie Parrott (Every)
**Keywords**: Claude Fable 5, AI workflow, unknown knowns, unknown unknowns, model selection, Anthropic, specialist models

## Elevator pitch
Anthropic's Claude Fable 5 earns its premium price not by doing bigger tasks, but by surfacing the questions and assumptions you didn't know you were making—a framework from Anthropic's Thariq Shihipar distinguishes "unknown knowns" from "unknown unknowns" to guide when to deploy the expensive model versus a cheaper one.

## Takeaways
- **Unknown knowns vs. unknown unknowns**: Tasks are hard either because they demand enormous execution (known knowns) or because the goal/constraints/standards are wrong from the start—the latter is where Fable excels
- **Fable's value is in discovery, not execution**: When Mike Taylor gave Fable his completed book manuscript, the model found a major omission he couldn't name in advance—an "unknown known"
- **Unknown unknowns surface mis-specified problems**: When Dan Shipper pointed Fable at five weeks of stalled copy-editing experiments, Fable identified that the team had been optimizing against a target nobody had validated
- **The cheaper specialist model won**: Researchers at Bridgewater AIA Labs fine-tuned Qwen3-235B to outperform every frontier model on six financial tasks at 13.8x lower cost—proof that for well-defined repeated work, specialization beats general capability
- **Workflow: expensive model creates instructions, cheap model executes**: Becky Isjwara's approach—give Fable the job and failed attempts, have it document the method, then test the instructions on Opus—is becoming a best practice

## Synthesis
Every's analysis of Claude Fable 5 reframes the question of when to use expensive AI models. The prevailing intuition is to reserve the most capable model for the biggest, most complex tasks. But Katie Parrott, drawing on a framework from Anthropic's Thariq Shihipar, argues that task complexity has two dimensions: execution complexity (the task is well-defined but hard to do) and uncertainty complexity (the task's definition, constraints, or success criteria are unclear).

For execution-heavy tasks—well-defined work that needs to be done reliably—cheaper specialist models like fine-tuned Qwen3-235B outperform frontier models at a fraction of the cost, as the Bridgewater AIA Labs result demonstrates. The specialist model beats GPT-5, Claude Opus, and Gemini on well-defined financial tasks because the problem space is narrow and the success criteria are clear.

For uncertainty-heavy tasks—where you don't know what you're missing—Fable's value proposition is different. The model surfaces assumptions you didn't know you were making, questions you didn't think to ask, and flaws in your problem specification that you hadn't validated. Dan Shipper's copy-editing example is instructive: five weeks of optimization against a 70% reproduction target for an editor's historical edits, but nobody had ever checked whether the editor herself would make the same edit twice. The target was never validated, and Fable found this flaw.

The practical takeaway for engineering teams is a triage framework: use cheaper models for tasks where the goal, constraints, and definition of good are settled. Reach for the expensive model when the map is still incomplete—when you need to discover what you don't know. And once Fable has done its discovery work, convert its method into instructions that cheaper models can follow. This create-once-execute-many pattern is emerging as the dominant cost optimization strategy for teams working with frontier AI.