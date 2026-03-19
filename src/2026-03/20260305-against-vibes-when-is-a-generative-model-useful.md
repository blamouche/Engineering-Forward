# Against Vibes: When is a Generative Model Useful
**Source**: https://www.williamjbowman.com/blog/2026/03/05/against-vibes-when-is-a-generative-model-useful/
**Date**: 2026-03-05
**Author**: William J. Bowman
**Keywords**: generative models, utility framework, encoding cost, verification cost, process dependency, AI criticism, rigor, LLM evaluation

## Elevator pitch
A structured framework for evaluating when generative models are genuinely useful: they excel when encoding cost is low, verification is cheap, and only the output matters—but fail systematically in complex, verification-heavy domains where "plausible doesn't mean useful."

## Takeaways
- Three factors determine generative model utility: encoding cost (effort to prompt vs. directly produce output), verification cost (effort to check generated output vs. checking traditional output), and process dependency (whether the output matters or the process creating it does).
- Encoding cost problem: for semantically dense code with tight requirements, manual creation often proves faster than iterative prompting.
- Verification cost warning: plausible-sounding outputs may conceal subtle errors, potentially increasing verification burden as models become more sophisticated—not decreasing it.
- Process dependency: tasks like education and research inherently require human engagement; others (like installing software) only need functional results.
- Central insight: "Plausible doesn't mean useful"—generative models excel narrowly when all three factors are favorable but fail systematically in complex, verification-heavy domains.

## Synthesis
The "against vibes" framing targets a real problem in AI tool adoption discourse: decisions about when to use AI are often made based on impressions from demos, social proof from thought leaders, or general enthusiasm rather than structured evaluation of whether the tool helps with the specific task. Bowman's framework provides a vocabulary for making those evaluations more rigorous.

The encoding cost insight is underappreciated. The narrative that AI tools reduce effort assumes prompting is faster than doing the work directly—an assumption that holds for some tasks and fails for others. For tasks requiring precise technical specifications, the effort required to write a prompt clear enough to get useful output is often comparable to the effort of writing the solution directly. The advantage of AI tools is not uniform across task types.

The verification cost point is the most important and potentially most dangerous observation. As models become more capable, their outputs become more sophisticated and more plausible. This makes errors harder to detect, not easier—a counterintuitive result that suggests capability improvements may actually increase verification burden in high-stakes domains. A naive SQL query from a 2022 model is obviously wrong; a sophisticated query from a 2026 model might be subtly wrong in ways that only appear in edge cases.

Process dependency identifies a category of tasks where AI tools create value by providing output but destroy value by providing it. Education is the clearest example: a student who gets AI to write their essay hasn't learned to write essays. Research is similar: the cognitive work of exploring sources and constructing arguments is where understanding is built. Automating the output removes the process that creates the value. Teams that use AI tools naively in these contexts optimize for the artifact while destroying the capability.
