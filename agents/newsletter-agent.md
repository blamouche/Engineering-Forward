# Newsletter Agent

This agent generates a monthly newsletter file containing the 10 most recent articles and a summary of the current month's content.

## Usage

```
/newsletter-agent <YYYY-MM>
```

## Instructions

When the user provides a month `YYYY-MM`:

1. **Read the README.md** to get the list of articles:
   - Extract all article entries from the README
   - Take the first 10 articles from the list (most recent)

2. **For each of the 10 articles**:
   - Read the corresponding Markdown file in `src/YYYY-MM/`
   - Extract:
     - Title (line `# ...`)
     - Source link (line `**Source**: ...`)
     - Elevator pitch (section `## Elevator pitch`)

3. **Read all articles from the current month** (`YYYY-MM`):
   - List all Markdown files in `src/YYYY-MM/`
   - If the folder does not exist or is empty, report it and stop
   - Extract key information from each article:
     - Title
     - Elevator pitch
     - Takeaways
     - Main synthesis points

4. **Create the newsletter file**:
   - Path: `newsletter/YYYY-MM.md`
   - Create the `newsletter/` folder if needed

5. **Write the newsletter** with this exact structure:

```markdown
# Newsletter YYYY-MM

## Latest Articles

*The 10 most recent articles published on lamouche.fr/notebook:*

1. **[Article Title](Source URL)**
   Description from elevator pitch

2. **[Article Title](Source URL)**
   Description from elevator pitch

[...continue for all 10 articles...]

## Worth Knowing

[2-3 paragraphs in English summarizing the key themes, trends, and insights from this month's articles. Focus on:
- Main topics covered this month (AI agents, new tools, architectural patterns, etc.)
- Important developments or announcements
- Practical implications for engineers and developers
- Emerging trends or shifts in the industry]
```

6. **Content guidelines**:
   - Use article's **Source** URLs (not internal markdown paths)
   - Elevator pitch provides the description
   - "Worth Knowing" section should be concise (2-3 paragraphs)
   - Stay factual and editorial
   - Write in English
   - Focus on engineering and technical implications

## Notes

- If unable to read an article, skip it and note the error
- Ensure all URLs are external source URLs, not internal paths
- Keep descriptions concise (1-2 sentences from elevator pitch)
- The "Worth Knowing" section should provide strategic insights about the month's content
