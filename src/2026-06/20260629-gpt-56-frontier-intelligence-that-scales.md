# GPT-5.6: Frontier Intelligence That Scales with Your Ambition
**Source**: https://openai.com/index/gpt-5-6/
**Date**: 2026-06-29
**Author**: OpenAI
**Keywords**: GPT-5.6, OpenAI, Sol, Terra, Luna, LLM, model launch, coding benchmarks

## Elevator pitch
OpenAI launches the GPT-5.6 family—flagship Sol, balanced Terra, and cost-efficient Luna—setting new benchmarks in coding, cybersecurity, and knowledge work while introducing multi-agent "ultra" mode and programmatic tool calling.

## Takeaways
- GPT-5.6 comes in three tiers: Sol (flagship, $5/$30 per 1M tokens), Terra (balanced, $2.50/$15), and Luna (cost-efficient, $1/$6), all sharing a 1.05M token context window and 128K output.
- Sol achieves 80 on the Artificial Analysis Coding Agent Index (2.8 points above Fable 5) with less than half the output tokens and roughly one-third the cost.
- New "ultra" mode coordinates four agents in parallel for demanding tasks, while "Programmatic Tool Calling" lets the model write and run lightweight programs that coordinate tools in-memory.
- On cybersecurity benchmarks, Sol scores 73.5% on ExploitBench (vs. GPT-5.5's 47.9%) and nearly doubles GPT-5.5's peak pass rate on ExploitGym.
- The model was subject to a government-coordinated limited preview before general availability, with safety evaluations including human red teaming and large-scale automated testing.

## Synthesis
OpenAI's GPT-5.6 launch represents both a technical milestone and a shifting landscape in the frontier model competition. The three-tier naming convention (Sol, Terra, Luna replacing the old pro/mini/nano pattern) signals an attempt to make model selection more intuitive, while the performance-per-dollar framing positions each tier against specific competitors: Sol vs. Fable 5, Terra vs. Fable 5 at lower cost, Luna vs. Opus 4.8 at roughly one-quarter the cost.

The coding benchmarks are the headline numbers. Sol's 80 on the Artificial Analysis Coding Agent Index edges past Fable 5's 77.2 with significantly better efficiency. On Terminal-Bench 2.1 and DeepSWE—evaluations that test real-world engineering workflows—GPT-5.6 also sets new state-of-the-art results. The cybersecurity improvements are dramatic: nearly doubling GPT-5.5's ExploitGym pass rate (24.9% vs. 15.1% under two hours, 33.7% with six hours), though these capabilities are gated behind OpenAI's Daybreak Trusted Access program.

Two architectural innovations stand out. Programmatic Tool Calling allows the model to write and execute lightweight programs that coordinate tools, filter intermediate data, and adapt workflows—reducing the need for developers to script every step or pass every tool response back through the model. The multi-agent "ultra" mode coordinates four parallel agents, trading higher token use for faster time-to-result on complex tasks, with a 16-agent configuration available for specific evaluations.

The launch also carries geopolitical weight. OpenAI conducted a government-coordinated limited preview at the request of the US administration, restricting access to a small group of vetted partners during evaluation of cyber and biology capabilities. OpenAI explicitly stated this is not their preferred long-term model, framing it as a short-term measure while working on a repeatable process for future releases. The 13-day preview period and the explicit government coordination represent a new phase in frontier model deployment, one where national security considerations directly shape product availability timelines.

For engineering teams, the practical implications are straightforward: Terra is the default migration target from GPT-5.5 (comparable quality at half the price via a model-string change), Sol is reserved for tasks where peak capability matters, and Luna handles high-volume classification and routing. The expanded prompt caching with explicit cache breakpoints and a 30-minute minimum cache life makes cost management more predictable for production workloads.