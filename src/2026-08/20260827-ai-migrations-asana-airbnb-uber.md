# We Need to Talk About Migrations with AI
**Source**: https://newsletter.pragmaticengineer.com/p/we-need-to-talk-about-migrations
**Date**: 2026-08-27
**Author**: The Pragmatic Engineer (Gergely Orosz)
**Keywords**: AI migrations, LLM-assisted refactoring, Enzyme to React Testing Library, Codex, test migration, JUnit migration, Bun migration, engineering productivity

## Elevator pitch
AI-assisted migrations are turning multi-year, multi-million-dollar engineering tasks into two-week projects, as demonstrated by Asana, Airbnb, Uber, and Bun—making previously impractical migrations finally doable.

## Takeaways
- Asana migrated 4,000+ Enzyme test files to React Testing Library in two weeks using OpenAI Codex, costing ~$12K instead of the estimated $6M and five years of manual work
- Airbnb migrated 3,500 Enzyme test files in six weeks with LLMs (Claude 3.7 Sonnet); 75% of files were migrated in just four hours once retry loops were built, reaching 97% automated completion in four days
- Uber migrated 600,000 JUnit 4 tests spanning 15 million lines of code to JUnit 5 in four months with two engineers and AI, modifying 1.25M lines of code
- Bun migrated 530,000 lines of code from Zig to Rust in two weeks for $165K in API costs
- Engineers must still plan migrations, design verification loops, and be involved throughout—the AI does the grunt work but not the orchestration
- The biggest benefit is shortening the window where both old and new libraries must be supported simultaneously

## Synthesis
OpenAI published a case study claiming Asana cleared five years of engineering work in two weeks using Codex, migrating from Enzyme to React Testing Library for about $12K. The $6M estimate was a back-of-envelope calculation: estimate time per file, multiply by 3,000+ outstanding files, multiply by engineer hourly rate. The real context, clarified by Asana's Dan Ubilla, is that this was an opportunistic, low-priority migration that had been ongoing for two years—the five-year estimate was when it would have finished at its current priority level, not a dedicated team working nonstop.

The broader pattern is clear across multiple companies. Airbnb built multi-phase retry loops that migrated 75% of 3,500 test files in four hours, then a more sophisticated pipeline handled the remaining 25% over four days, with engineers finishing the last 3% in a week. Uber's JUnit 4 to JUnit 5 migration was even larger: 600,000 tests, 15M lines of code, eight engineering months of effort plus AI costs. Bun's Zig-to-Rust migration cost $165K in API calls for 530K lines in two weeks.

The key insight is that these migrations were all previously impractical—not impossible, but too long and distracting to justify. Pre-AI, Sentry's JavaScript-to-TypeScript migration took 1.5 years with 10 engineers for 95,000 lines. The shared characteristic of AI-assisted migrations is that engineers still needed to plan, design verification loops, and remain involved throughout. The AI handles the repetitive transformation work, but human judgment governs the strategy. The biggest practical benefit is shortening the dual-support window: the painful period where both the old and new library must be maintained simultaneously. As models continue to improve beyond GPT-5.6 Sol and Claude Fable 5, expect long-avoided migrations to finally happen, and expect cost optimization to bring the $12K price tags even lower.