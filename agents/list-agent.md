# List Agent

Processes all URLs in LIST.md using the article synthesis agent.

## Usage
```
/list-agent
```

## Instructions

1. **Open LIST.md** and note timestamp for batch recap

2. **For each URL** (top to bottom, ignore empty lines):
   - Run `/article-synthesis-agent <url>`
   - Extract title and elevator pitch from created file
   - Remove processed URL from LIST.md
   - Commit: `Process article: [Title]`

2b. **Nettoyer l’URL avant traitement** (important)
   - Avant d’appeler l’agent, nettoie l’URL pour retirer les paramètres de tracking inutiles (ex: `utm_*`, `ref`, `fbclid`, `gclid`, `mc_cid`, `mc_eid`, etc.).
   - Utilise l’URL nettoyée pour `/article-synthesis-agent`.

3. **Create batch recap** at `synthesis/YYYY-MM-DD - HHmmss - batch recap.md`:
```markdown
# Batch Recap - YYYY-MM-DD HH:mm:ss

Article Title 1 Elevator pitch. URL to the synthesys https://url1
Article Title 2 Elevator pitch. URL to the synthesys https://url2
```
   Notes:
   - Une ligne par article.
   - `https://urlX` doit être le **lien GitHub vers la synthèse** (blob/main/src/...).
   - Ne pas inclure de paramètres de tracking dans les URLs (pas de `?utm_...`).

   - Commit: `Add batch recap: YYYY-MM-DD HHmmss`

## Notes
- Stop on error before modifying list
- LIST.md must be empty when complete
- Use 24h format (HHmmss) for filename
