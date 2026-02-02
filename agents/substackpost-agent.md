# Substack Post Agent

Generates a journalistic article from the 15 most recent technical watch articles.

## Usage
```
/substackpost-agent
```

## Instructions

1. **Get 15 most recent articles** from README.md `## Articles` section, read each file

2. **Analyze corpus**: Identify themes, patterns, connections, and central insight

3. **Craft title**: Specific, provocative, engaging (e.g., "The IDE Is Dead, Long Live the Agent")

4. **Craft subtitle**: One compelling sentence under 150 chars, italic format

5. **Write article** (1500-2000 words):
   - **Opening hook** (1-2 para): Compelling observation/question
   - **Big picture** (2-3 para): Broader context and significance
   - **Deep dive** (4-6 para): Key developments, weaving multiple articles
   - **Tensions/nuances** (2-3 para): Contrasting viewpoints
   - **Looking ahead** (1-2 para): Future implications, actionable insights

6. **Format**:
```markdown
# [TITLE]

*[Subtitle]*

[Article body - no bullets in main text, 2-3 subheadings max]

---

## Sources
1. [Title](source-url)
[list all 15]
```

7. **Save** to `substack/YYYYMMDD-post-<slug>.md`

8. **Commit and push**: `git fetch/pull` if behind, commit: `Add substack post: [TITLE]`

## Style Guidelines
- Confident editorial voice, write for intelligent non-technical readers
- Show don't tell: specific examples over abstract claims
- Find the narrative arc connecting developments
- Be opinionated, take a clear stance
- Attribute insights to source articles
- Avoid clichés ("rapidly changing world") and superlatives ("revolutionary", "groundbreaking")
- Quality over coverage: better to deeply explore 5-7 articles than superficially mention all
