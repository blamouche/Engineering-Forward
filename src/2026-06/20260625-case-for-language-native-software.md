# The Case for Language-Native Software
**Source**: https://robenglander.com/writing/the-case-for-language-native-software/
**Date**: 2026-06-25
**Author**: Robert Englander
**Keywords**: natural language interface, conversational software, agents, intent determination, deterministic execution, software architecture

## Elevator pitch
The industry learned the wrong lesson from ChatGPT — the revolution isn't conversation, it's that software can now understand human language as an interface, and the real shift is from users adapting to systems to systems adapting to users.

## Takeaways
- "Conversational software" and "language-native software" are fundamentally different: conversation treats dialogue as the interaction model, while language-native treats human language as the interface for expressing intent that gets resolved to deterministic execution
- The industry learned the wrong lesson from ChatGPT — the important part wasn't that you could talk to software, but that millions experienced software that could understand instructions in natural language
- The false choice between traditional software and autonomous agents misses the point: execution is often the easy part; the hard part is deciding which instruction should run in the first place
- Conversation is valuable only to the extent it helps resolve ambiguity; once intent is sufficiently understood, continued dialogue creates more risk than value and increases complexity without increasing certainty
- The interaction boundary between intent determination (ambiguity, probability, interpretation) and execution (correctness, predictability, accountability) must be kept crisp — blurring them makes systems harder to trust and govern

## Synthesis
Robert Englander's essay reframes the conversation around AI-native software in a way that cuts through the industry's chatbot-and-agent obsession. His central distinction is between "conversational software" — which treats dialogue as the interaction model — and "language-native software," which treats human language as the interface for expressing intent that the system resolves and executes deterministically.

The industry's misreading of ChatGPT is the starting point. When ChatGPT landed, people fixated on the ability to talk to software. Englander argues the important part was that millions of people experienced software that could understand instructions in natural language. Conversation is a mechanism; natural language understanding is a capability. The distinction gets clearer when you look at business intelligence: asking "show customer churn by region for the last four quarters" doesn't require a conversation — the system just needs to know what you mean and give you the answer.

The essay dismantles the false choice between traditional rigid software and autonomous agents. Agents are seductive — describe a goal, walk away, let software fill in the details. But this framing assumes execution is the hard part. In many domains, it isn't. Databases execute instructions remarkably well. Tax packages, schedulers, reporting engines all execute well. The hard part is deciding which instruction should run in the first place. Language models fill that gap — they connect what the user means to what deterministic software can execute.

Perhaps the most important architectural insight is the interaction boundary. Intent determination lives with ambiguity, probability, and interpretation. Execution lives with correctness, predictability, and accountability. These are fundamentally different concerns that require different engineering approaches. Blurring them makes systems harder to reason about and harder to govern. When something goes wrong, you need to know where: was it misunderstood intent, wrong operation chosen, or right operation with wrong execution? Those are different failures with different fixes.

The essay's historical framing is compelling. For decades, users learned the application's language — navigation, workflows, forms, commands. Natural language flips the relationship: for the first time, users can say what they want in a language they already speak. The translation burden moves from the user to the software. This inversion may ultimately prove more significant than any individual AI capability. The more flexible the front door, the more you need a locked-down back room — tax math demands precision regardless of how casually you asked the question. Language-native software requires the same design, testing, validation, and governance we apply to APIs and databases, applied to the intent determination layer.