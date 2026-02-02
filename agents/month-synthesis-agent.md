# Month Synthesis Agent

This agent takes a month in `YYYY-MM` format and produces a monthly synthesis.

## Usage

```
/month-synthesis-agent <YYYY-MM>
```

## Instructions

When the user provides a month `YYYY-MM`:

1. **List the month's articles**:
   - Read all Markdown files in `src/YYYY-MM/`
   - If the folder does not exist or is empty, report it and stop

2. **Extract useful information** from each article:
   - Title (line `# ...`)
   - Source link (line `**Source**: ...`)
   - Key ideas (sections `## Elevator pitch`, `## Takeaways`, `## Synthesis`)

3. **Create the output file**:
   - Path: `synthesis/YYYY-MM.md`
   - Create the `synthesis/` folder if needed

4. **Write the synthesis** with this exact structure:

```markdown
# Synthesis YYYY-MM

## Summary

[Up to 10 paragraphs in English about monthly trends related to working with AI and the adaptations required]

## Selected links

- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
```

5. **Select the links**:
   - Pick 15 links from the month's articles
   - Prioritize articles about working with AI, enterprise usage, organization, and skills to develop
   - Use the `**Source**` URLs from each article

6. **Update the README**:
   - Add a link to `synthesis/YYYY-MM.md` in the matching month section
   - Place the link near the month's name
   - Suggested format:

```markdown
#### January (15 articles) [Synthesis 2026-01](synthesis/2026-01.md)
- [Article Title](src/2026-01/article.md)
```

7. **Commit and push changes**:
   - First, check if the local branch is up to date with the remote:
     - Run `git fetch origin` to get the latest remote state
     - Check if there are upstream changes with `git status`
     - If the branch is behind, pull the latest changes with `git pull --rebase origin <branch>`
   - Stage all changes (the new synthesis file and the updated README.md)
   - Commit with a message following this format: `Add monthly synthesis for YYYY-MM`
   - Push to the remote repository

## Notes

- Stay factual and concise
- Editorial style
- Maximum 4 paragraphs for the summary
- Prefer ASCII for file names
- **Avoid strong or hyperbolic words**: Do not use words like "pivotal", "groundbreaking", "revolutionary", "transformative", "game-changing", "unprecedented", or similar superlatives. Prefer neutral, descriptive language.
- **Consult previous syntheses before writing**: Before drafting the summary, read the syntheses from the 2-3 previous months (e.g., for 2026-03, read `synthesis/2026-02.md`, `synthesis/2026-01.md`, and `synthesis/2025-12.md` if they exist). This ensures:
  - No repetition of themes or insights already covered
  - Continuity and progression in the narrative across months
  - Focus on what is genuinely new or evolving in the current month
