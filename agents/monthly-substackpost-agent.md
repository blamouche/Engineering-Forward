# Monthly Substack Post Agent

Generates a journalistic article covering all technical watch articles from a given month.

## Usage
```
/monthly-substackpost-agent YYYY-MM
```

## Instructions

1. **Get all articles for YYYY-MM** from `src/YYYY-MM/`: list all files in that directory, read each one

2. **Analyze corpus**: Identify dominant themes, patterns, connections, and central narrative arc across all articles from the month

3. **Craft title**: Specific, provocative, engaging, in **sentence case** (only the first letter capitalized; e.g., "The IDE is dead, long live the agent")

4. **Craft subtitle**: One compelling sentence under 150 chars, italic format

5. **Write article** (1500-2000 words) in **English** (unless the user explicitly requests another language):
   - **Opening hook** (1-2 para): Compelling observation/question rooted in the month's events
   - **Big picture** (2-3 para): Broader context and significance of the month's themes
   - **Deep dive** (4-6 para): Key developments, weaving multiple articles together
   - **Tensions/nuances** (2-3 para): Contrasting viewpoints and competing narratives
   - **Looking ahead** (1-2 para): Future implications, actionable insights

6. **Format**:
```markdown
# [TITLE]

*[Subtitle]*

[Article body - no bullets in main text, 2-3 subheadings max]

---

## Sources
1. [Title](source-url)
[list all articles from the month]
```

7. **Save** to `substack/YYYYMMDD-post-<slug>.md` (use today's date as prefix)

8. **Copy to latest.md**: Create a copy of the file as `substack/latest.md` (replace if it already exists)

9. **Commit and push**: `git fetch/pull` if behind, commit: `Add substack post YYYY-MM: [TITLE]`

## Style Guidelines
- Confident editorial voice, write for intelligent non-technical readers
- Show don't tell: specific examples over abstract claims
- Find the narrative arc connecting the month's developments
- Be opinionated, take a clear stance
- Attribute insights to source articles
- Avoid clichés ("rapidly changing world") and superlatives ("revolutionary", "groundbreaking")
- Quality over coverage: synthesize themes rather than listing every article individually
