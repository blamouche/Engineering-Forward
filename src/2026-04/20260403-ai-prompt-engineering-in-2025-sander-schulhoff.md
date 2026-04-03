# AI Prompt Engineering in 2025: What Works and What Doesn't | Sander Schulhoff

**Source**: https://www.lennysnewsletter.com/p/ai-prompt-engineering-in-2025-sander-schulhoff
**Date**: Unknown
**Author**: Sander Schulhoff (Lenny's Newsletter interview)
**Keywords**: prompt engineering, few-shot prompting, prompt injection, AI security, role prompting, decomposition, HackAPrompt

## Elevator pitch
Sander Schulhoff, creator of the first prompt engineering guide, breaks down what actually works in 2025—few-shot prompting dominates, role prompting is largely ineffective, and prompt injection is an unsolved security threat that will only grow as AI agents proliferate.

## Takeaways
- Few-shot prompting (showing examples) remains one of the highest-leverage techniques, capable of improving accuracy from 0% to 90% on specific tasks
- Role prompting ("you are a math professor") has little effect on correctness despite its popularity—it may influence tone but not reasoning quality
- Decomposition (breaking problems into sub-problems) and self-criticism (asking models to critique their own answers) significantly improve performance on complex tasks
- Prompt injection is fundamentally unsolved: attackers can trick AI agents into taking unintended actions through malicious content in the environment
- Product/system prompts are distinct from conversational prompting—they run millions of times at scale and must be hardened like production code

## Synthesis
Sander Schulhoff has an unusual vantage point on prompt engineering: he wrote the first guide before ChatGPT launched, co-authored the most comprehensive study of prompting techniques (covering 1,500+ papers and 200+ techniques with OpenAI, Microsoft, Google, Princeton, and Stanford), and runs HackAPrompt, the largest AI red teaming competition. His Lenny's Newsletter interview separates what the research actually shows from the folklore that circulates on Twitter.

The most important distinction he draws is between conversational prompting and product prompting. Most people think about prompting as chatting with ChatGPT—how to phrase a one-time question better. But the real leverage is in system prompts inside products: these run at scale, millions of times, and drive user-facing features. They need to be optimized, tested, and hardened against adversarial inputs—treated like production code, not casual conversation.

The few-shot prompting finding is striking: providing examples of desired input-output pairs can transform task performance dramatically. Schulhoff describes a medical coding use case that went from complete failure to near-perfect output simply by adding a few example pairs. The underlying reason is that examples communicate intent more precisely than descriptions. "Format the output like this: [example]" is unambiguous in a way that "format it professionally" is not.

Role prompting—telling the model it's a domain expert—has become a widespread practice but the research doesn't support it for improving correctness. It can influence writing style and tone, but models don't actually become better reasoners by being told they're math professors. This is a useful correction for anyone who's been investing effort in elaborate role definitions.

The more sophisticated techniques that actually work: decomposition (explicitly breaking complex problems into sub-problems before solving them) and self-criticism (asking the model to critique and improve its own output). Both mirror effective human problem-solving strategies and appear to engage the model's reasoning capabilities more fully.

The security discussion is the most urgent. Prompt injection—where malicious content in the environment redirects an AI agent's behavior—is an unsolved problem that traditional security approaches can't fully address. As AI agents gain more capabilities and autonomy, the attack surface grows. An agent with access to email, web browsing, and code execution that encounters a malicious document with embedded instructions is genuinely dangerous. Schulhoff's HackAPrompt competition continuously surfaces new attack techniques that bypass current defenses.

The practical implication: any team deploying AI agents that interact with untrusted content needs explicit security thinking about prompt injection, not just capability design.
