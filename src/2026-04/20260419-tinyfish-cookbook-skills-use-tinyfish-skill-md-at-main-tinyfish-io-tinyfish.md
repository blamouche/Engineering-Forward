# tinyfish-cookbook/skills/use-tinyfish/SKILL.md at main · tinyfish-io/tinyfish

**Source**: https://github.com/tinyfish-io/tinyfish-cookbook/blob/main/skills/use-tinyfish/SKILL.md
**Date**: April 19, 2026
**Author**: tinyfish-io
**Keywords**: github, tinyfish, cookbook, skills, skill, main

## Elevator pitch
A collection of sample apps and recipes built with the TinyFish web agent. Open-source examples for you to learn & build! - tinyfish-cookbook/skills/use-tinyfish/SKILL.md at main · tinyfish-io/tinyfish-cookbook.

## Takeaways
- tinyfish-io / tinyfish-cookbook Public Notifications You must be signed in to change notification settings Fork 258 Star 1.6k Files Expand file tree main / SKILL.md Copy path Blame More file actions Blame More file actions Latest commit History History History 196 lines (139 loc) · 6.64 KB main / SKILL.md Top File metadata and controls Preview Code Blame 196 lines (139 loc) · 6.64 KB Raw Copy raw file Download raw file Outline Edit and raw actions name use-tinyfish description Use TinyFish web agent to extract/scrape websites, extract data, and automate browser actions using natural language.
- Use when you need to extract/scrape data from websites, handle bot-protected sites, or automate web tasks.
- TinyFish CLI You have access to the TinyFish CLI ( tinyfish ) — a suite of web tools you can call from the terminal.
- If not installed: npm install -g @tiny-fish/cli If not authenticated: tinyfish auth login or set TINYFISH_API_KEY env var.
- Keys at https://agent.tinyfish.ai/api-keys Picking the Right Tool TinyFish has four tools.

## Synthesis
tinyfish-io / tinyfish-cookbook Public Notifications You must be signed in to change notification settings Fork 258 Star 1.6k Files Expand file tree main / SKILL.md Copy path Blame More file actions Blame More file actions Latest commit History History History 196 lines (139 loc) · 6.64 KB main / SKILL.md Top File metadata and controls Preview Code Blame 196 lines (139 loc) · 6.64 KB Raw Copy raw file Download raw file Outline Edit and raw actions name use-tinyfish description Use TinyFish web agent to extract/scrape websites, extract data, and automate browser actions using natural language. Use when you need to extract/scrape data from websites, handle bot-protected sites, or automate web tasks. TinyFish CLI You have access to the TinyFish CLI ( tinyfish ) — a suite of web tools you can call from the terminal. If not installed: npm install -g @tiny-fish/cli If not authenticated: tinyfish auth login or set TINYFISH_API_KEY env var. Keys at https://agent.tinyfish.ai/api-keys Picking the Right Tool TinyFish has four tools. Start with the lightest one that can do the job and escalate only when needed. search → fetch → agent → browser lightest heaviest Tool When to use Speed Cost search You need to find URLs or get a quick answer about a topic Fastest Lowest fetch You have URLs and need their clean content (articles, docs, product pages) Fast Low agent You need to interact with a page — click, fill forms, navigate, extract structured data from dynamic sites Slower Higher browser Agent isn't enough — you need raw programmatic browser control via CDP Slowest Highest Common Patterns Research: search → fetch Search for a topic, then fetch the best results to read their full content. Find URLs tinyfish search query " best React state management libraries 2026 " # 2. Read the top results tinyfish fetch content get --format markdown " https://result1.com " " https://result2.com " Deep extraction: search → agent Search to find the right site, then use agent to interact with it and extract structured data. Find the site tinyfish search query " Nike running shoes official store " # 2.
