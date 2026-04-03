# Things I Learned at OpenAI
**Source**: https://semaphore.substack.com/p/things-i-learned-at-openai
**Date**: March 28, 2026
**Author**: Karina Nguyen
**Keywords**: OpenAI, Anthropic, AI research, evaluations, post-training, product development, alignment, organizational culture

## Elevator pitch
Karina Nguyen reflects on lessons from building AI at both Anthropic and OpenAI, arguing that creating the right evaluation is often more impactful than building the model that scores well on it, and that product design and training data form a bidirectional feedback loop.

## Takeaways
- Designing effective evaluations is harder than it appears and often more impactful than the model itself
- Product shapes training data; training data shapes the model; the model shapes what the product can become — a bidirectional cycle
- Post-training is the frontier for subjective capabilities like emotional intelligence and creative judgment
- Greater model capability correlates with better alignment — more sophisticated models understand deception's costs
- Organizational misalignment and internal politics present core bottlenecks to AGI progress, not technical barriers

## Synthesis
Nguyen's reflections carry weight because they come from someone who has operated at the research frontier at both Anthropic and OpenAI — two organizations with different cultures and approaches that share the same technical frontier. The lessons she draws are not technical breakthroughs but organizational and methodological insights about how progress actually happens.

The evaluation primacy argument is counterintuitive but defensible. Benchmarks create incentives: research teams, companies, and the broader community orient effort toward improving benchmark scores. A well-designed benchmark that measures something genuinely important can therefore direct enormous aggregate effort toward solving a real problem. MMLU shaped years of LLM development; SWE-bench is currently shaping coding capability investment. The creator of a benchmark that proves predictive of real-world capability has more downstream impact than the team that achieves the first high score on it.

The bidirectional product-data-model cycle is a systems-level insight about how AI products and models co-evolve. It explains why companies with large deployments have sustainable advantages: the product generates the data that trains the model that enables the product to improve. Breaking into this cycle requires either exceptional research talent (to make training-time improvements independent of product data) or acquiring the product scale to start the flywheel. It also explains why post-training — which is most directly connected to product behavior and user interaction data — has become the competitive frontier.

The alignment-capability correlation claim is the most contrarian element. The conventional safety concern frames capability and alignment as potentially in tension. Nguyen argues the opposite: more capable models better understand the social and institutional costs of deception, making them more reliably aligned. This is not universally accepted, but it reflects an empirically grounded observation about current model behavior that has policy implications — the case for delaying capability improvements on safety grounds weakens if the correlation holds.

The organizational bottleneck observation is the most practically relevant for anyone building AI teams. The technical problems in AI are difficult but tractable; the challenges of coordinating large organizations of talented, opinionated people around a shared mission may be harder.
