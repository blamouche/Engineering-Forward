# I built a programming language using Claude Code
**Source**: https://ankursethi.com/blog/programming-language-claude-code/
**Date**: 2026-03-10
**Author**: Ankur Sethi
**Keywords**: Claude Code, agentic engineering, programming language, Cutlet, LLM-assisted development, software craftsmanship, test-driven development

## Elevator pitch
Building Cutlet, a dynamic programming language, entirely through Claude Code over four weeks demonstrates that agentic engineering requires more planning and discipline—not less—than traditional development.

## Takeaways
- Sethi built a complete dynamic programming language (Cutlet) with arrays, vectorized operations, functions, and a REPL using Claude Code over four weeks, running on macOS and Linux.
- Problem selection matters: the key question is whether a challenge suits LLM solutions—specifically, whether success can be automated and whether the domain is well-represented in training data.
- Clear formal specifications outperform vague prompts: detailed plans require upfront cognitive investment but dramatically improve agent output quality.
- Environmental setup is critical: comprehensive test suites, linters, sanitizers, and introspection tools help agents maximize effectiveness and catch their own errors.
- Loop optimization: identifying agent inefficiencies and converting repeated patterns into reusable scripts compounds productivity over a multi-week project.

## Synthesis
The Cutlet project is a useful data point against two opposing oversimplifications. The first oversimplification is that AI coding tools require minimal skill—just describe what you want and the code appears. Sethi's account is explicit that this project required careful upfront planning, disciplined communication, and sustained engineering judgment throughout. The second oversimplification is that AI coding tools produce low-quality output that real engineers wouldn't ship. A complete, working programming language with a REPL contradicts that.

The problem selection insight gets at something underappreciated: not all programming tasks are equally suited to agentic approaches. A domain well-covered in training data (programming language implementation has enormous prior art) with automatable success criteria (does the test suite pass?) is significantly more tractable than a domain with novel requirements or fuzzy success criteria. Teams that apply agentic approaches indiscriminately will get worse results than teams that deliberately select the highest-leverage tasks.

The environmental setup recommendation reflects a key insight about how agents fail. When agents lack good tooling—test runners they can invoke, linters that catch errors immediately, sanitizers that surface undefined behavior—they operate with delayed feedback that creates feedback loops with long cycle times. Investing in tooling before starting an agentic project changes the agent's error correction rate throughout the entire project.

The loop optimization concept addresses a meta-level inefficiency: agents often repeat the same mistakes or go through the same unproductive patterns. Recognizing these patterns and converting them into scripts—standard fixes that can be invoked directly—is a form of prompt engineering at the workflow level rather than the individual prompt level.
