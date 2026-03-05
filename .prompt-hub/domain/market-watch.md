# Market Watch

Point d'entree unique contenant toutes les consignes des agents.

## Usage
```bash
/agents <agent> [arguments]
```

## Registre
- `article-synthesis`
- `add-url`
- `scan-list`
- `monthly-synthesis`
- `substack-post-monthly`
- `newsletter`
- `update-stats`
- `substack-post-recents`
- `weekly-recap`

## Routage Market Watch
1. Verifier que `<agent>` existe dans le registre.
2. Appliquer uniquement la section de consignes correspondante.
3. Utiliser directement les chemins/fichiers definis dans chaque consigne.
4. Si l'agent est inconnu, retourner la liste du registre.

## Agent: article-synthesis
### Usage
```bash
/article-synthesis <url>
```

### Consignes
1. Fetch article via WebFetch.
2. Extract metadata: Title, Date, Author, Keywords.
3. Create file at `src/YYYY-MM/YYYYMMDD-<title-slug>.md` (YYYYMMDD = date de publication si dispo, sinon date du jour):
```markdown
# [Title]
**Source**: [URL]
**Date**: [Date or "Unknown"]
**Author**: [Author or "Unknown"]
**Keywords**: [Inferred if needed]

## Elevator pitch
[One sentence summary]

## Takeaways
- [5 key points]

## Synthesis
[500-word synthesis: main arguments, insights, conclusions]
```
4. Update `README.md`: add link under `## Articles > ### YYYY > #### Month` (newest first).
5. Run `/update-stats` to update statistics.
6. Commit and push:
   - `git fetch origin && git pull --rebase origin <branch>` if behind
   - Commit message: `Add synthesis: [Title]`

### Notes
- Create directories if needed.
- Maintain chronological order (newest first).
- Synthesis should be objective.

## Agent: add-url
### Usage
```bash
/add-url <url1> [url2] [url3] ...
```

### Consignes
1. Sync (must be clean):
   - `git status --porcelain` must be empty
   - `git pull --rebase`
2. Normalize + append URLs in `LIST.md`:
   - Ensure file exists
   - One URL per line
   - Remove blank lines
   - De-duplicate exact duplicate URLs (preserve order)
3. Verify before committing:
   - `grep -Fqx -- "<url>" LIST.md` for each URL intended.
4. Commit + push only if changes:
   - `git add LIST.md`
   - if staged diff empty: stop
   - commit message: `Add URL(s) to processing queue`
5. Verify HEAD contains URLs:
   - `git show HEAD:LIST.md | grep -Fqx -- "<url>"`

### Notes
- Avoid fragile shell escaping with URLs.
- Keep `LIST.md` plain text, one URL per line.

## Agent: scan-list
### Usage
```bash
/scan-list
```

### Consignes
1. Open `LIST.md` and note timestamp for batch recap.
2. For each URL (top to bottom, ignore empty lines):
   - Nettoyer l'URL (retirer `utm_*`, `ref`, `fbclid`, `gclid`, `mc_cid`, `mc_eid`, etc.)
   - Run `/article-synthesis <url-nettoyee>`
   - Extract title and elevator pitch from created file
   - Remove processed URL from `LIST.md`
   - Commit: `Process article: [Title]`
3. Create batch recap at `synthesis/YYYY-MM-DD - HHmmss - batch recap.md`:
```markdown
# Batch Recap - YYYY-MM-DD HH:mm:ss

Article Title 1
Elevator pitch.
Synthese: https://url1

Article Title 2
Elevator pitch.
Synthese: https://url2
```
4. In recap:
   - Un bloc par article, separe par une ligne vide
   - `https://urlX` = lien GitHub vers la synthese (`blob/main/src/...`)
   - Ne pas inclure de tracking params
5. Commit recap: `Add batch recap: YYYY-MM-DD HHmmss`

### Notes
- Stop on error before modifying list.
- `LIST.md` must be empty when complete.
- Use 24h format `HHmmss` for filename.

## Agent: monthly-synthesis
### Usage
```bash
/monthly-synthesis <YYYY-MM>
```

### Consignes
1. Read articles from `src/YYYY-MM/` (stop if folder empty/missing).
2. Extract from each: Title, Source URL, Elevator pitch, Takeaways, Synthesis.
3. Consult previous syntheses (2-3 prior months).
4. Create `synthesis/YYYY-MM.md`:
```markdown
# Synthesis YYYY-MM

## Summary
[Up to 4 paragraphs on monthly trends in AI work and required adaptations]

## Selected links
- [Title](Source URL)
[15 links prioritizing AI work, enterprise usage, organization, skills]
```
5. Update `README.md`: add synthesis link near month header.
6. Commit and push:
   - fetch/pull if behind
   - commit message: `Add monthly synthesis for YYYY-MM`

### Notes
- Write in English.
- Factual editorial style, max 4 paragraphs.
- Avoid hyperbolic words.
- ASCII filenames preferred.

## Agent: substack-post-monthly
### Usage
```bash
/substack-post-monthly YYYY-MM
```

### Consignes
1. Get all articles for `YYYY-MM` from `src/YYYY-MM/`.
2. Analyze corpus: themes, patterns, narrative arc.
3. Craft title in sentence case.
4. Craft subtitle: compelling sentence <150 chars, italic.
5. Write article (1500-2000 words) in English unless explicit user request:
   - Opening hook (1-2 para)
   - Big picture (2-3 para)
   - Deep dive (4-6 para)
   - Tensions/nuances (2-3 para)
   - Looking ahead (1-2 para)
6. Format:
```markdown
# [TITLE]

*[Subtitle]*

[Article body - no bullets in main text, 2-3 subheadings max]

---

## Sources
1. [Title](source-url)
[list all articles from the month]
```
7. Save to `substack/YYYYMMDD-post-<slug>.md`.
8. Copy to `substack/latest.md`.
9. Commit and push:
   - fetch/pull if behind
   - commit message: `Add substack post YYYY-MM: [TITLE]`

### Style
- Confident editorial voice for intelligent non-technical readers.
- Specific examples over abstract claims.
- Clear narrative arc and stance.
- Attribute insights to source articles.
- Avoid cliches/superlatives.

## Agent: newsletter
### Usage
```bash
/newsletter <YYYY-MM>
```

### Consignes
1. Section 1: Latest from lamouche.fr/notebook
   - WebFetch `https://lamouche.fr/notebook/`
   - Extract 10 most recent articles (title + URL)
2. Section 2: Technical Watch Synthesis
   - Read all files in `src/YYYY-MM/`
   - Extract: Title, Source, Elevator pitch, Takeaways
   - Write 2-3 paragraph synthesis
3. Section 3: Worth Watching
   - Select 10 most impactful articles from month
   - Use elevator pitch as description
4. Output in `newsletter/YYYY-MM.md`:
```markdown
# Newsletter YYYY-MM

==intro text==

## My latest articles from the notebook

**[Title](https://lamouche.fr/notebook/posts/...)**
Brief description
[repeat 10x]

---

## What's hot today ?

[2-3 paragraphs: themes, trends, practical implications]

---

## Worth watching

Elevator pitch text.
[Link](Source URL)
[repeat 10x]

---

## Cartography for noobs

**🧭 Want to understand how maps really work?**

This newsletter explains, step by step, the foundations of modern cartography: data, projections, use cases, and key challenges simply, with no prior knowledge required.

[Subscribe](https://subscribepage.io/ylAON7)
```

### Notes
- Section 1: lamouche.fr URLs.
- Sections 2-3: external Source URLs.
- English, factual editorial tone.
- Focus on engineering and future of work.

## Agent: substack-post-recents
### Usage
```bash
/substack-post-recents
```

### Consignes
1. Get 15 most recent articles from `README.md` section `## Articles`, read each file.
2. Analyze corpus: themes, patterns, central insight.
3. Craft title in sentence case.
4. Craft subtitle: compelling sentence <150 chars, italic.
5. Write article (1500-2000 words) in English unless explicit user request:
   - Opening hook (1-2 para)
   - Big picture (2-3 para)
   - Deep dive (4-6 para)
   - Tensions/nuances (2-3 para)
   - Looking ahead (1-2 para)
6. Format:
```markdown
# [TITLE]

*[Subtitle]*

[Article body - no bullets in main text, 2-3 subheadings max]

---

## Sources
1. [Title](source-url)
[list all 15]
```
7. Save to `substack/YYYYMMDD-post-<slug>.md`.
8. Copy to `substack/latest.md`.
9. Commit and push:
   - fetch/pull if behind
   - commit message: `Add substack post: [TITLE]`

### Style
- Confident editorial voice.
- Specific examples.
- Clear stance and narrative arc.
- Attribute insights.
- Avoid cliches and superlatives.
- Quality over exhaustive coverage.

## Agent: update-stats
### Usage
```bash
/update-stats
```

### Consignes
1. Parse `README.md`: count articles per month (lines starting with `- [` under `#### Month`).
2. Generate statistics chart after title, before Articles section:
```text
## Statistics

Articles per month:

2026-01 | ████████ 46<br>
2026-02 | ██ 3
```
   - Each `█` = 3 articles (round up)
   - Chronological order (oldest first)
   - `<br>` after each line except last
   - Only months with articles
3. Update month headers: `#### January (5 articles)` (singular if 1).
4. Commit/push only when called directly (not from another agent):
   - fetch/pull if behind
   - commit message: `Update statistics`

### Notes
- Update existing Statistics section, do not duplicate.
- Preserve links and content.

## Agent: weekly-recap
### Usage
```bash
/weekly-recap <theme>
```

### Consignes
1. Calculate date range: today minus 7 days.
2. Scan articles in `src/YYYY-MM/`:
   - Extract `**Date**` field (`Month DD, YYYY`)
   - Filter to last 7 days
3. Filter by theme using title, keywords, elevator pitch, synthesis.
4. Select up to 10 most relevant articles.
5. Create file at `recap/YYYY-MM-DD-<theme-slug>.md`:
```markdown
[Executive summary: key insight and relevance to theme]

[Source URL]

---

[Next article...]
```
6. Commit and push:
   - fetch/pull if behind
   - commit message: `Add weekly recap: <theme>`

### Notes
- Strict 7-day filtering.
- Flexible theme matching.
- Original summaries only.
- Skip unparseable dates with warning.
- Report if no matching articles.
