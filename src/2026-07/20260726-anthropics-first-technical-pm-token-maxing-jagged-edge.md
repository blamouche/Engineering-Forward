# Anthropic's First Technical PM on Token Maxing, the Jagged Edge, and Living in the Future
**Source**: https://www.lennysnewsletter.com/p/anthropics-first-technical-pm-on
**Date**: 2026-07-26
**Author**: Lenny Rachitsky (interview with Dianne Penn)
**Keywords**: Anthropic, Claude, product management, AI products, eval-driven development, Dianne Penn

## Elevator pitch
Dianne Penn, Anthropic's first technical PM and now Head of Product for AI Research and Labs, shares how eval-driven development, the "jagged edge" of model capability, and learning from Claude's own users shaped Anthropic's path from underdog to the fastest-growing company in history.

## Takeaways
- Dianne Penn joined Anthropic in 2023 as its first technical PM when the entire product team was five engineers; she helped ship every model from Claude 2 through Fable.
- Eval-driven development is Anthropic's core loop: define evaluations that capture the behavior you want, then train the model to pass those evaluations — replacing intuition with measurable criteria.
- The "jagged edge" describes how frontier models have vastly different capabilities across similar tasks: they can write production code but fail at simple arithmetic, making product decisions about what to ship extremely hard.
- Penn helped incubate Claude Code, MCP, Skills, computer use, tool use, and reasoning — key pieces of Anthropic's developer-facing infrastructure.
- Anthropic's willingness to have Claude "push back" on user instructions is a deliberate product choice reflecting the company's safety philosophy, even when it frustrates users.

## Synthesis
Dianne Penn's trajectory from Anthropic's first technical PM to Head of Product for AI Research and Labs offers a window into how Anthropic built its product stack from scratch. When she joined in 2023, the product team was just five engineers. Her background — Alexa AI at Amazon and high-yield bond trading at JPMorgan — gave her both technical depth and a tolerance for ambiguity that building AI products demands.

The central methodological insight is eval-driven development. Rather than relying on product intuition or user anecdotes, Anthropic defines concrete evaluations that measure whether a model behaves as intended, then trains the model to pass those evaluations. This loop replaces subjective "does this feel right?" with objective "does this pass the eval?" It's a discipline that becomes more important as models get more capable, because the jagged edge — the uneven boundary between what a model can and can't do — makes it impossible to reason about capability from general impressions alone.

Penn's work incubating Claude Code, MCP (Model Context Protocol), Skills, and tool use reflects a shift from building a single chat interface to building an ecosystem of composable developer tools. Each of these products was shaped by Anthropic eating its own cooking: the team uses Claude to build Claude, which surfaces real problems faster than any external feedback loop.

The discussion of Claude's tendency to "push back" on user instructions is perhaps the most interesting product philosophy point. Anthropic deliberately chose a model personality that doesn't always comply, reflecting a safety-first approach that treats refusal and pushback as features rather than bugs. This creates a real tension in product development — the same behavior that makes Claude safer in adversarial scenarios makes it more frustrating in everyday use. Penn's framing is that this is a tradeoff the company continues to navigate, not a bug to be fixed.

For engineering teams building on Claude, the key takeaway is that the eval-driven loop applies beyond model training. Define what good looks like in measurable terms, test against those evaluations systematically, and treat the jagged edge as a feature of the landscape rather than a surprise.