# From Doing to Tending: GPT-5.6 Sol, Tend Framework, and Grok 4.5 Vibe Check
**Source**: https://every.to/essays/from-doing-to-tending
**Date**: 2026-07-12
**Author**: Every (Dan Shipper, Katie Parrott, Ashwin Sharma)
**Keywords**: gpt-5.6, sol, tend, grok-4.5, ai-agents, knowledge-work, model-evaluation, efficiencymaxxing

## Elevator pitch
Every's newsletter introduces "Tend," an open-source framework for building AI loops that handle knowledge work while humans make key decisions, reviews Grok 4.5 as an Opus-level model at a fraction of the cost, and argues AI scribes in medicine risk dangerous cognitive off-loading.

## Takeaways
- GPT-5.6 Sol is the Every team's preferred daily model—fast, resourceful, easy to steer—while Fable still gets the biggest, loosest assignments; Sol runs $5/$30 per million tokens
- Tend is an open-source prompt and repository for building loops where AI gathers information, proposes decisions, and carries out approved ones—the thesis is that GPT-5.6 is the first model that can run a complete knowledge-work loop
- Grok 4.5 (jointly trained by SpaceXAI and Cursor) benchmarks at Opus 4.8 level with $2/$6 per million token pricing and ~80 tokens/second—it's not SOTA but earns a slot for long, multi-step assignments where cost and speed matter
- "Efficiencymaxxing" is replacing "tokenmaxxing"—as labs pull back subsidies, people compete on output per token rather than raw token volume; OpenRouter enables stacking cheaper models for tasks that don't need frontier ones
- AI scribes in medicine carry the same risk as autopilot in aviation: cognitive off-loading that atrophies manual skills; the proposed solution is mandated simulation training for complex cases while letting AI handle routine documentation

## Synthesis
This issue of Every's Context Window newsletter packages three distinct but connected ideas under the umbrella of the shift from doing work to tending the systems that do work.

The first is the Tend framework, open-sourced alongside Dan Shipper's argument that GPT-5.6 is the first model capable of running a complete knowledge-work loop. Tend is a prompt-plus-repository that sets up loops where the AI gathers information, proposes decisions, and executes approved ones while the human makes the key calls. The mental model shifts from "AI as assistant" to "AI as autonomous loop that you supervise"—the human tends the loop rather than performing the work. The framework is model-agnostic but calibrated for Sol's particular strengths in speed, file-finding, and multi-turn context retention.

The second is a vibe check of Grok 4.5, the first model born from SpaceXAI's acquisition of Cursor. The verdict: Opus-level performance at dramatically lower cost. Mike Taylor's benchmarks put it slightly above Claude Opus 4.8 in completeness and follow-through, while Kieran Klaassen placed it in the Opus 4.5-4.6 range for practical coding tasks. At $2/$6 per million tokens and ~80 tokens/second, it's not replacing anyone's daily driver but earns a slot for long multi-step assignments where cost and speed outweigh marginal quality differences. Its PowerPoint creation tested at Opus 4.6-4.7 level, and its writing avoids Claude's tics but defaults to short, sharp sentences.

The third is a shorter essay on AI scribes and cognitive off-loading, drawing a direct parallel to aviation's autopilot problem. Dr. Helen Ouyang argues in the New York Times that writing clinical notes forces doctors to synthesize information and arrive at sound judgment—the same kind of manual cognitive exercise that autopilot atrophies in pilots. The answer isn't to ban AI scribes but to follow aviation's lead: mandate simulation training for complex cases while letting AI handle routine documentation. The broader implication applies to any knowledge worker: the more cognitive load you offload, the more deliberate you need to be about maintaining the skills you're no longer exercising daily.