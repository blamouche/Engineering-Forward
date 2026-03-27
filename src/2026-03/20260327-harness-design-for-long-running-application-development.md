# Harness design for long-running application development
**Source**: https://www.anthropic.com/engineering/harness-design-long-running-apps
**Date**: Unknown
**Author**: Prithvi Rajasekaran
**Keywords**: agent harness, multi-agent, long-running tasks, evaluation, autonomy

## Elevator pitch
Anthropic details a three‑agent harness (planner, generator, evaluator) that improves long‑running autonomous app development by separating creation from critique and using structured handoffs to sustain quality over hours‑long builds.

## Takeaways
- Long‑running agent performance degrades without context resets or structured handoffs.
- Self‑evaluation is weak; a separate evaluator agent yields more reliable critique.
- A generator‑evaluator loop, inspired by GANs, improves subjective quality and bug detection.
- Sprint contracts and Playwright‑based QA help keep work aligned with product specs.
- Harness complexity should be trimmed as models improve; components must earn their cost.

## Synthesis
Prithvi Rajasekaran describes a new harness design for long‑running autonomous application development, motivated by two persistent problems: agents drift as tasks stretch over time, and models are poor judges of their own output. Earlier Anthropic work used task decomposition and context handoffs to keep agents on track, but performance still plateaued, especially for subjective work like UI design and for longer, multi‑hour builds.

The core improvement is a GAN‑inspired separation between a generator and an evaluator. Instead of asking the model to both create and grade its own work, the harness assigns critique to a distinct evaluator agent. This separation matters because LLMs are consistently generous when evaluating their own outputs, while a tuned evaluator can be made skeptical. The evaluator gains leverage when its feedback is concrete, testable, and tied to explicit criteria, giving the generator a real target to iterate against.

Rajasekaran first applies this loop to frontend design. The evaluator grades against four criteria—design quality, originality, craft, and functionality—with heavier weight on design quality and originality to push the model away from generic “AI slop.” The loop runs multiple iterations, with the evaluator using Playwright to inspect the live UI rather than a static screenshot. Over time, scores improved and the generator took bolder aesthetic risks, including unexpected creative pivots. The experiment shows that clear grading rubrics and external critique can push models beyond safe, template‑like defaults.

The same pattern then scales to full‑stack coding. The resulting harness uses three agents: a planner that expands a short prompt into a product spec, a generator that implements features in sprints, and an evaluator that QA‑tests the running app through Playwright. Each sprint begins with a “contract” that defines what done looks like; the evaluator uses that contract as the test suite. In a retro game maker example, the evaluator found concrete bugs in feature behavior and API routing that a single‑agent build missed. The harness was expensive and slow but produced noticeably more complete and functional applications.

The post also emphasizes that harnesses should evolve as models improve. With Opus 4.6, the team could remove some scaffolding (like strict sprint decomposition) while keeping the planner and evaluator. The evaluator’s value becomes contingent on task difficulty: when tasks fall within the model’s solo capabilities, the evaluator is overhead; when tasks sit at the edge, it remains critical. In a later Digital Audio Workstation (DAW) build, QA still uncovered missing core interactions even after model improvements, showing why external evaluation remains useful for ambitious projects.

Overall, the piece argues that long‑running autonomy isn’t just about bigger context windows. It is about orchestration: clean handoffs, explicit criteria, and structured evaluation loops that keep a model honest over hours‑long builds. As models advance, the optimal harness will shift, but the need for principled structure—especially for complex, multi‑stage work—remains.
