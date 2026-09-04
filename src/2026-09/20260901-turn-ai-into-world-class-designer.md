# How to Turn Your AI Into a World-Class Designer
**Source**: https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world
**Date**: 2026-09-01
**Author**: Anshu Chimala (Lenny's Newsletter guest post)
**Keywords**: AI design, Claude, Fable 5, Opus 5, GPT-5.6 Sol, Double Diamond, seed strings, subagents, design critic, image generation, video generation, AI creativity

## Elevator pitch
A former Apple design and engineering leader shares a seven-technique process for tapping into AI's hidden creative potential — from seed strings that inject true randomness, to subagent feedback loops with a "design critic," to image and video generation that enrich designs beyond what code alone can produce.

## Takeaways
- LLMs are poor designers by default because they predict the most likely token at every step — producing "design-by-committee" blandness, the opposite of great design
- Seed strings (inspired by Sakana AI's String Seed of Thought) inject true randomness by generating a random alphanumeric string and using it as design inspiration
- Ambitious prompts with specific creative visions (pixel art, isometric cities, asymmetric layouts) give the model a clear direction instead of letting it default to familiar patterns
- Subagent feedback loops: use a cheap model for implementation and an expensive model (like Fable 5) as a "design critic" that evaluates screenshots independently — costing less than 10% of total tokens
- Image generation via OpenAI/Gemini APIs adds personality that gradients and shapes cannot — the biggest giveaway of AI-generated design
- Video generation models create animated graphics (looping clips with chroma key) and fluid transitions between UI states that respond to scrolling
- The most important polishing technique is removal: AI loves to add more, but restraint immediately looks premium and tasteful
- "Save the prompts that don't work, and test them again when newer models come out" — you'll know you're taking full advantage of new capabilities

## Synthesis
Anshu Chimala, who led software engineering and design teams at Apple for 12 years focusing on AI products, argues that most people only see 1% of AI's creative potential. The problem is structural: LLMs are next-token predictors that make the most predictable choice at every step — the exact opposite of great design, which bends rules and creates emotional responses through unexpected choices.

The article presents a three-phase process loosely inspired by the Double Diamond design model, reimagined for AI agents. In the "Discover" phase, two techniques push models beyond their comfort zone. Seed strings (from Sakana AI's String Seed of Thought) generate a random alphanumeric string that serves as design inspiration — because models can't inherently act randomly, only predict the most likely token. Ambitious prompts with specific creative visions give the model direction rather than letting it default to purplish gradients and text-on-left layouts.

In the "Define" phase, three techniques deepen the design. Subagent feedback loops use a cheap model for implementation and an expensive model (like Fable 5) as a "design critic" that evaluates screenshots in a fresh context — accounting for less than 10% of output tokens while dramatically improving quality. Image generation via OpenAI or Gemini APIs adds personality that code-based alternatives (gradients, shapes) cannot. Video generation models create animated graphics with chroma key background removal and fluid transitions between UI states that respond to user scrolling.

In the "Deliver" phase, the key technique is restraint. AI loves to add more but rarely takes away — one of the biggest signs a design is AI-generated. The author's calorie tracking app went from cluttered gradients and custom buttons to a clean, Apple-native grid simply by removing elements that didn't add value. The practical advice: "putting less on the screen communicates more." The article concludes with a reminder to save failed prompts and retest them with newer models, as capabilities improve faster than expectations adjust.