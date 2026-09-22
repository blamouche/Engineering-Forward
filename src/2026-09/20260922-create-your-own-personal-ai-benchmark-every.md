# How to Create Your Own Personal AI Benchmark
**Source**: Every (hello@every.to) — https://every.to/essays/personal-ai-benchmark
**Date**: 2026-09-21
**Author**: Mike Taylor (Every)
**Keywords**: AI benchmarks, MMLU, personal benchmarks, model evaluation, Claude, GPT, model selection, evals, back-pocket evals, AI testing, model comparison, Dan Shipper

## Elevator pitch
Wharton professor Ethan Mollick argues that standard benchmarks like MMLU-Pro measure trivia, not job fitness — so Every's head of evals Mike Taylor built a three-level framework for creating personal AI benchmarks: collect your AI failures, run them across models in parallel, and teach AI your taste through voice-mode feedback.

## Takeaways
- **Standard benchmarks don't answer the real question**: MMLU-Pro asks models about the cranial capacity of Homo erectus and the place named in Cheap Trick's 1979 live album — scores are directionally useful but don't tell you if the model can do your job.
- **"Back-pocket evals" — collect tasks where AI failed you**: Steve Yegge's practice: whenever a model can't complete a project, add it to a personal eval list. When a new model makes progress on previously-failed tasks, you know it's worth adopting.
- **Level 1: Fill your back pocket with failures**: Review the past month's work, identify 10 tasks where AI required extensive back-and-forth or was abandoned. Capture all context: reference files, advice you'd give an intern doing the work.
- **Level 2: Turn your taste into tests**: Run all 10 tasks in parallel across multiple models using Claude Code, build an HTML eval viewer for side-by-side comparison. Compare large vs. small models, different providers, and same-model variance.
- **Level 3: Teach AI your preferences**: Use voice mode to dictate what you liked or disliked about each output. This creates a preference dataset that can be used to systematically evaluate whether outputs meet your standards.
- **Model selection is the largest cost lever**: For Every's consulting workload, model choice dominates cost, with context management a distant second — making systematic evaluation directly impact the bottom line.
- **The "surfed" benchmark problem**: When models get too good at a benchmark, it becomes "saturated" — the models are getting it right every time, so it no longer differentiates. Dan Shipper calls this the challenge of keeping benchmarks relevant as models improve.

## Synthesis
Mike Taylor's article addresses the gap that haunts every AI practitioner: you know which model "feels" better, but you can't defend the choice to a budget owner without data. The article bridges that gap with a process that's rigorous enough to produce defensible comparisons but lightweight enough that a busy practitioner will actually do it.

The framework's three levels map to increasing investment in evaluation maturity. Level 1 (back-pocket evals) requires only collecting tasks where AI failed — the lowest-effort, highest-signal starting point because failed tasks are where model improvements are most visible. Level 2 (parallel comparison) requires setting up infrastructure to run tasks across models simultaneously, but the investment pays off because it converts subjective impressions into systematic comparison. Level 3 (teaching preferences) is the most ambitious — using voice mode to build a preference dataset that could eventually be used for automated evaluation.

The most provocative insight comes from Dan Shipper's observation about "saturated" benchmarks. When all models pass a benchmark, it stops differentiating — which means personal benchmarks need to evolve as models improve. The tasks that differentiate Claude Fable 5 from GPT-5.6 Sol today won't differentiate their successors next year. This means personal benchmarking isn't a one-time setup but an ongoing practice of adding harder tasks and retiring solved ones.

The practical workflow is accessible: ask your desktop AI to search local session history for tasks that required extensive back-and-forth or were abandoned, collect the full context (reference files, intern-level advice), then run all tasks in parallel across models using Claude Code. Build an HTML viewer for side-by-side comparison. The article's screenshots show concrete examples — an NPS dashboard built by GPT-5.6 Sol vs. Claude Fable 5 — where Sol chose a title and description forming a useful narrative while Fable's was plain. These are the kinds of qualitative differences that personal benchmarks surface but public benchmarks can't.

The article's underlying argument is that model intelligence is becoming commoditized faster than model evaluation. As Dan Shipper notes, "Models are getting better every day. To get the most from them, we have to keep up." The organizations that build systematic evaluation practices will navigate the frontier pace of model releases with confidence; those that rely on vibes will oscillate between hype and disappointment without knowing why.