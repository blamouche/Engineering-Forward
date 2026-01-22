# Weekly Recap Agent

This agent generates a thematic synthesis of articles published in the last 7 days.

## Usage

```
/weekly-recap-agent <theme>
```

## Instructions

When the user provides a theme:

1. **Calculate the date range**:
   - Determine today's date
   - Calculate the date 7 days ago
   - Only articles with a `**Date**` within this 7-day window will be considered

2. **Scan all article files**:
   - Read all Markdown files in `src/YYYY-MM/` directories (current and previous month if needed)
   - Extract the `**Date**` field from each article
   - Parse the date (format: `Month DD, YYYY`, e.g., `January 19, 2026`)
   - Filter out any article older than 7 days

3. **Filter by theme**:
   - From the articles within the date range, select those relevant to the provided theme
   - Use the article's title, keywords, elevator pitch, and synthesis to determine relevance
   - Prioritize articles with strong thematic alignment

4. **Select up to 10 articles**:
   - Choose a maximum of 10 articles that best match the theme
   - If fewer than 10 relevant articles exist, include all that match
   - Order by relevance to the theme (most relevant first)

5. **Generate the output**:
   - For each selected article, produce:
     - One paragraph executive summary (synthesize the key insight and relevance to the theme)
     - A link to the original source URL (from `**Source**` field)
   - Do NOT include article titles
   - Use this exact format:

```markdown
[Executive summary paragraph explaining the article's key insight and its relevance to the theme.]

[Source URL]

---

[Next article summary...]

[Source URL]

---
```

6. **Display the result**:
   - Output the synthesis directly to the user
   - Do NOT create a file
   - Do NOT commit anything

## Example

Input: `/weekly-recap-agent AI coding assistants`

Output:
```
A recent analysis explores how AI coding tools are reshaping developer workflows, arguing that the fundamental distinction between developers who understand systems deeply versus those who treat code as black boxes remains unchanged. The tools accelerate work but do not replace the need for foundational knowledge.

https://notes.eatonphil.com/2026-01-19-llms-and-your-career.html

---

An enterprise case study demonstrates measurable productivity gains from AI-assisted development, with teams reporting 40% faster code review cycles and improved documentation quality when integrating LLM tools into their existing workflows.

https://example.com/ai-coding-enterprise-adoption

---
```

## Notes

- Only articles from the last 7 days are considered (strict filtering)
- The theme matching should be flexible (synonyms, related concepts)
- Executive summaries should be original, not copied from the article
- Focus on the article's relevance to the specified theme
- If no articles match the theme within the date range, report that clearly
- If the date cannot be parsed, skip that article with a warning
