# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Engineering-Forward is a technical watch repository that synthesizes articles about AI, engineering practices, and the future of work. Content is organized chronologically with automated agents that handle article processing, statistics, and newsletter generation.

## Repository Structure

```
Engineering-Forward/
├── src/YYYY-MM/          # Monthly article syntheses (markdown files)
├── synthesis/YYYY-MM.md  # Monthly trend summaries
├── newsletter/YYYY-MM.md # Monthly newsletters
├── agents/               # Agent instructions for automation
├── LIST.md              # Queue of URLs to process
└── README.md            # Main index with statistics and article links
```

## Key Workflows

### Processing Articles

Articles are processed through specialized agents that follow a specific workflow:

1. **Single article**: `/article-synthesis-agent <url>`
   - Fetches article content via WebFetch
   - Creates `src/YYYY-MM/article-slug.md` with structured synthesis
   - Updates README.md with article link
   - Calls `/stats-agent` to update statistics
   - Commits and pushes with message: `Add synthesis: [Article Title]`

2. **Batch processing**: `/list-agent`
   - Processes URLs from LIST.md sequentially (top to bottom)
   - Removes each URL from LIST.md after successful processing
   - LIST.md should be empty when complete

3. **Statistics update**: `/stats-agent`
   - Counts articles per month from README.md
   - Generates ASCII bar chart
   - Updates month headers with article counts
   - When called directly (not from article-synthesis-agent), commits and pushes changes

4. **Monthly synthesis**: `/month-synthesis-agent <YYYY-MM>`
   - Reads all articles from `src/YYYY-MM/`
   - Writes 2-4 paragraph trend analysis to `synthesis/YYYY-MM.md`
   - Selects 3-6 key articles focused on working with AI
   - Updates README.md with synthesis link

5. **Newsletter generation**: `/newsletter-agent <YYYY-MM>`
   - Section 1: Fetches 10 latest articles from lamouche.fr/notebook
   - Section 2: Synthesizes all technical watch articles from the month
   - Section 3: Highlights 10 impactful articles with elevator pitches
   - Creates `newsletter/YYYY-MM.md`

### Git Workflow

All agents that commit changes follow this pattern:
```bash
git fetch origin
git status  # Check for upstream changes
git pull --rebase origin <branch>  # If behind
git add <files>
git commit -m "Message"
git push
```

## Article Structure

Every article synthesis follows this exact format:

```markdown
# [Article Title]

**Source**: [Original URL]
**Date**: [Publication date]
**Author**: [Author name]
**Keywords**: [Comma-separated keywords]

## Elevator pitch
[One sentence summary]

## Takeaways
- [Key point 1]
- [Key point 2]
- [Key point 3]
- [Key point 4]
- [Key point 5]

## Synthesis
[500-word synthesis of main arguments and insights]
```

## Content Guidelines

- **Synthesis tone**: Factual, editorial, concise
- **Avoid**: Superlatives (amazing, groundbreaking, revolutionary), demonstrative words
- **Focus**: Working with AI, enterprise adoption, engineering practices, skills development
- **Language**: English for syntheses and newsletters
- **Unknown values**: Mark as "Unknown" if metadata cannot be extracted
- **Keywords**: Infer from content if not explicitly provided

## File Naming

- **Article files**: `src/YYYY-MM/article-title-as-slug.md`
  - Lowercase, hyphens instead of spaces, no special characters
- **Monthly syntheses**: `synthesis/YYYY-MM.md`
- **Newsletters**: `newsletter/YYYY-MM.md`

## Important Notes

- Create `src/YYYY-MM/` directory if it doesn't exist
- Maintain chronological order in README.md (newest first)
- LIST.md processes URLs top-to-bottom, removing each after completion
- Stats agent is called automatically by article-synthesis-agent (no separate commit)
- Newsletter folder is in .gitignore (not tracked)
- Use WebFetch tool for retrieving article content
- External source URLs (not internal file paths) are used in syntheses and newsletters
