# Weekly Recap Agent

Generates a thematic synthesis of articles from the last 7 days.

## Usage
```
/weekly-recap-agent <theme>
```

## Instructions

1. **Calculate date range**: Today minus 7 days

2. **Scan articles** in `src/YYYY-MM/` directories:
   - Extract `**Date**` field (format: `Month DD, YYYY`)
   - Filter to last 7 days only

3. **Filter by theme**: Select relevant articles using title, keywords, elevator pitch, synthesis

4. **Select up to 10** most relevant articles

5. **Create file** at `recap/YYYY-MM-DD-<theme-slug>.md`:
```markdown
[Executive summary: key insight and relevance to theme]

[Source URL]

---

[Next article...]
```

6. **Commit and push**: `git fetch/pull` if behind, commit: `Add weekly recap: <theme>`

## Notes
- Strict 7-day filtering
- Flexible theme matching (synonyms, related concepts)
- Original summaries, not copied from article
- Skip unparseable dates with warning
- Report if no matching articles found
