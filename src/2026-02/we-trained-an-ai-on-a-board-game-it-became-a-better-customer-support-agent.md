# We Trained an AI on a Board Game. It Became a Better Customer Support Agent.
**Source**: https://every.to/playtesting/we-trained-an-ai-on-a-board-game-it-became-a-better-customer-support-agent-299b5938-09dd-4881-803f-aea21f0d461f
**Date**: 2026-02-04
**Author**: Alex Duffy, Every
**Keywords**: reinforcement learning, Diplomacy, game AI, transfer learning, customer support, fine-tuning, AI training

## Elevator pitch
Fine-tuning the Qwen3-235B model on the strategy game Diplomacy yielded a 10%+ improvement on other games and — surprisingly — measurable gains on customer support and industrial operations benchmarks, suggesting game-based RL training develops transferable cognitive skills.

## Takeaways
- Fine-tuning Qwen3-235B on Diplomacy improved performance by over 10% on other games (Hanabi, Wordle) and also on non-game benchmarks
- The Diplomacy-trained model improved on Tau2 (customer support conversations) and AssetOpsBench (industrial operations) benchmarks
- Games reward specific behaviors — context-tracking, shifting priorities, strategic communication — that transfer to domains with incomplete information and shifting requests
- Reinforcement learning with clear scoring environments develops skills that static internet text training cannot: models learn to strategize, not just recall facts
- The future of AI training points toward less web scraping and more "learning by doing" in interactive environments

## Synthesis
Alex Duffy, cofounder and CEO of Good Start Labs, presents a compelling finding at the intersection of game-based training and real-world AI capabilities. His team fine-tuned the Qwen3-235B model — an open-source model from Alibaba Cloud — on thousands of rounds of Diplomacy, the strategy board game famous for requiring persuasion and strategy with no element of luck.

The expected result was improvement on other games, which materialized as a 10%+ gain on Hanabi and Wordle. The surprising result was that the Diplomacy-trained model also improved on entirely unrelated benchmarks: Tau2, which tests AI agent performance on customer support conversations, and IBM's AssetOpsBench, which measures industrial operations capabilities like equipment monitoring and maintenance.

The mechanism is intuitive once explained. Diplomacy trains specific cognitive behaviors: tracking shifting contexts, reprioritizing as situations evolve, and communicating strategically with incomplete information. Customer support requires the same capabilities — information is often incomplete, requests shift mid-conversation, and the agent must track context across multiple interactions. The game doesn't teach the model about airline reservations specifically; it teaches it how to think in dynamic, multi-party situations.

The article draws on Every team members' personal experiences with skill transfer from games. StarCraft taught one team member to coordinate parallel tasks with different timescales. Pokémon taught English before any classroom. Board game mechanics led to more systematic thinking about AI workflows. These anecdotes reinforce the paper's finding that games develop transferable cognitive structures.

The deeper insight concerns the future direction of AI training. Training on internet text teaches word prediction. Training in environments with goals and feedback teaches strategy. Reinforcement learning in game environments generates the kind of data and behavioral feedback that static text cannot provide. Duffy frames this as a directional shift in AI development: less scraping the web, more learning by doing.

This work points toward a future where game environments become standard components of AI training pipelines, not as curiosities but as efficient generators of the behavioral patterns that make models useful in real-world, dynamic situations.
