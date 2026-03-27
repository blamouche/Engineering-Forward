# A New Framework for Evaluating Voice Agents (EVA)
**Source**: https://huggingface.co/blog/ServiceNow-AI/eva
**Date**: Unknown
**Author**: Unknown
**Keywords**: voice agents, evaluation, benchmarks, speech, conversational AI

## Elevator pitch
ServiceNow releases EVA, an end‑to‑end benchmark that scores voice agents on both task accuracy and user experience through realistic bot‑to‑bot conversations.

## Takeaways
- EVA jointly measures task accuracy (EVA‑A) and conversational experience (EVA‑X).
- The framework simulates full voice workflows using a user simulator, tools, and validators.
- Initial dataset includes 50 airline scenarios with 15 tools and deterministic end states.
- Results show a consistent accuracy‑experience tradeoff across 20 systems.
- Named‑entity transcription errors are a dominant failure mode for voice agents.

## Synthesis
The EVA framework targets a core gap in voice‑agent evaluation: existing benchmarks often assess speech perception, turn‑taking, or tool use separately, but do not score full, multi‑turn task workflows that voice agents must handle in practice. EVA combines these dimensions by evaluating complete conversations and scoring both task success and user experience.

EVA uses a bot‑to‑bot architecture with five components: a user simulator that speaks via TTS, a voice agent built on Pipecat (supporting cascade and audio‑native models), a deterministic tool executor, validators that ensure the conversation is correctly simulated, and a metrics suite. This structure enables repeatable evaluations with no human annotation, while still capturing the realities of spoken interaction such as turn‑taking, speech fidelity, and conversational flow.

The dataset released with EVA focuses on airline support and includes 50 scenarios such as rebooking, cancellations, and vouchers. Each scenario comes with a structured goal, persona, database state, and expected end state so task completion can be verified deterministically. EVA reports both pass@k and pass^k to capture peak capability and consistency across repeated runs.

EVA defines two primary scores. EVA‑A (accuracy) measures task completion, faithfulness to policies and tool results, and speech fidelity of critical entities. EVA‑X (experience) measures conciseness, conversation progression, and turn‑taking quality. The framework also includes diagnostic metrics to highlight specific failure modes.

Benchmarking 20 systems reveals a persistent accuracy‑experience tradeoff: agents that complete tasks reliably often deliver worse conversational experiences, while those that sound natural tend to fail more often. The evaluation also surfaces named‑entity transcription as a common breakdown point, where a single error can derail authentication or booking workflows. Multi‑step tasks, such as rebooking with preserved ancillaries, are another consistent failure source.

Overall, EVA positions voice‑agent quality as a joint optimization problem rather than a single metric. By combining deterministic task checks with LLM‑as‑judge experience scoring, the benchmark offers a structured way to compare systems and diagnose weaknesses, and it provides a foundation for future domain datasets and robustness tests across languages, accents, and noisy environments.
