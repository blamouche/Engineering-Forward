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

[Up to 4 paragraphs in English about monthly trends related to working with AI and the adaptations required]

## Selected links

- [Article title](Source URL)
- [Article title](Source URL)
- [Article title](Source URL)
```

5. **Select the links**:
   - Pick 3 to 6 links from the month's articles
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

## Notes

- Stay factual and concise
- Editorial style
- Maximum 4 paragraphs for the summary
- Prefer ASCII for file names
