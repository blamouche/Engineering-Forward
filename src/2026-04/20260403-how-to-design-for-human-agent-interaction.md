# How to Design for Human-agent Interaction

**Source**: https://every.to/thesis/how-to-design-for-human-agent-interaction
**Date**: April 3, 2026
**Author**: Karri Saarinen
**Keywords**: human-agent interaction, design, Linear, transparency, accountability, AI interfaces

## Elevator pitch
Karri Saarinen argues that AI unreliability is primarily an interface problem and proposes six principles for designing products where humans and agents can work together safely and legibly.

## Takeaways
- Chat is a useful bootstrap interface but a poor default for repeatable, high-stakes work.
- Agents should disclose themselves clearly and act through the same native product patterns humans already understand.
- Users need immediate feedback and visibility into agent state, reasoning, and progress to build trust.
- Stopping an agent must be a real control, not a polite suggestion.
- Accountability ultimately belongs to the human who deploys the agent inside a well-designed system, not to the agent itself.

## Synthesis
Karri Saarinen’s essay is valuable because it relocates the AI reliability problem from model evaluation to product design. When an agent behaves unpredictably, the instinct is to blame the underlying model. Saarinen’s argument is that many failures are actually interface failures: the product does not expose enough structure, state, or control for people to use non-deterministic systems safely. That reframing is useful because it gives designers and product teams concrete agency instead of waiting passively for smarter models.

His critique of chat as the default interface is persuasive. Chat works for exploration because it is flexible and familiar, but it is a weak medium for repeated operational work. Everything becomes a stream of text. Outputs are hard to compare, context is easy to lose, and small prompt differences can produce radically different results. For serious use, teams need interfaces that impose structure without destroying flexibility. That is the larger design agenda behind agent-native software.

The six principles he proposes are pragmatic. Agents should identify themselves clearly, use native product affordances, provide immediate feedback, expose internal state, obey disengagement requests, and exist within a clear accountability model. None of that makes the model smarter. It makes the surrounding system more legible. That distinction matters because trust in AI is often less about absolute accuracy than about whether users understand what the system is doing and what recourse they have when it goes wrong.

The essay also gestures toward a maturing discipline. Human-computer interaction was built around deterministic tools manipulated directly by users. Human-agent interaction requires designing for semi-autonomous actors that operate inside shared systems. Saarinen’s framework is still early, but it gives product teams a way to think beyond chatbot novelty and toward durable collaboration patterns between people and software agents.
