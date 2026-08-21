# AI Could Do Anything. Then It Met PowerPoint.
**Source**: https://every.to/also-true-for-humans/ai-could-do-anything-then-it-met-powerpoint
**Date**: 2026-06-29
**Author**: Mike Taylor
**Keywords**: AI, PowerPoint, automation, Claude Code, consulting, quality control

## Elevator pitch
Creating high-quality presentations with AI requires far more engineering investment than most teams expect—only at scale does custom automation justify the cost.

## Takeaways
- Claude's official PowerPoint skill has 59 files and 16 Python scripts, yet still struggles with company templates and spatial layout in .pptx files.
- An AI-generated deck that's 80% right is often worse than one built manually, because reviewing for hidden errors takes longer than starting from scratch.
- Every's consulting team built a 24-skill, 11-phase PowerPoint plugin costing $62 per deck in tokens, achieving near-zero defect rate through massive orchestration.
- The blueprint-first approach—planning slide structure before generating—was the single biggest quality improvement, allowing human review before expensive token spend.
- For most teams, automating what you can and waiting for model improvements is better than building custom automation at current quality levels.

## Synthesis
Mike Taylor, head of tech consulting at Every, provides a refreshingly honest account of attempting to automate PowerPoint creation with AI. The piece is valuable precisely because it documents failure alongside success, and because it sets a realistic bar for when custom AI automation is worth the investment.

The journey starts with Claude's out-of-the-box PowerPoint capabilities, which produce impressive results from scratch but fail when matching existing company templates. The .pptx file format, never designed with agents in mind, is "messy, token-inefficient, and hard to manipulate reliably." An AI-generated deck that's 80% correct is worse than no AI at all, because the review process for catching subtle errors in a polished-looking presentation is more time-consuming than building it correctly from the start.

The breakthrough came from Nityesh Agarwal's adaptation: a blueprint-first approach where Claudie (Every's AI assistant) first creates a plan for slide structure and visual direction, then waits for human approval before generating. This human-in-the-loop checkpoint saved significant token waste. Combined with Opus 4.7, this workflow produced one of the best AI-generated slide decks the team had seen—though Opus still invented a new brand style because it decided theirs wasn't good enough.

The real production test came when Every partnered with a company creating 25 sales decks per week. The initial vibe-coded adaptation was a mess: slides out of place, text overlapping, headshots labeled with wrong names. Claude had written evaluation metrics that verified content but not appearance. After three weeks of micromanaged iteration, the result was a 24-skill, 11-phase plugin with 18 Python scripts, costing 28.9 million tokens and $62 per deck. This level of investment only makes sense at the scale of hundreds of similar decks per month.

The article's most pragmatic conclusion: don't fire your analyst. Automation becomes genuinely useful only when it approaches a zero-percent defect rate. Below that threshold, you're creating more work reviewing AI output than you save generating it. The alternative of moving to HTML slides—where Claude is far more competent—is presented as a viable path for teams willing to leave the .pptx format behind. The deeper lesson is about process design: designing workflows where AI is a primary contributor from day one, rather than grafting AI onto human-scaled processes.