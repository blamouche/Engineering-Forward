# Newsletter Agent

This agent generates a monthly newsletter file containing three sections:
1. The 10 most recent articles from lamouche.fr/notebook
2. A synthesis of all technical watch articles from the current month
3. A "We're Watching" selection of 10 highlighted articles

## Usage

```
/newsletter-agent <YYYY-MM>
```

## Instructions

When the user provides a month `YYYY-MM`:

### Section 1: Latest Articles from lamouche.fr/notebook

1. **Fetch the website** https://lamouche.fr/notebook/:
   - Use WebFetch to retrieve the page content
   - Extract the 10 most recent articles with their titles and URLs
   - These are blog posts from the notebook, not the technical watch articles

2. **For each article from the website**:
   - Extract the article title
   - Extract the article URL (full URL from lamouche.fr/notebook/posts/...)
   - Note the publication date if available

### Section 2: Technical Watch Synthesis

3. **Read ALL articles from the current month** (`YYYY-MM`):
   - List all Markdown files in `src/YYYY-MM/`
   - If the folder does not exist or is empty, report it and stop

4. **For each article in `src/YYYY-MM/`**:
   - Read the corresponding Markdown file
   - Extract:
     - Title (line `# ...`)
     - Source link (line `**Source**: ...`)
     - Elevator pitch (section `## Elevator pitch`)
     - Key takeaways (section `## Takeaways`)

5. **Write a synthesis** (2-3 paragraphs) based on ALL articles from the month:
   - Identify the main themes and trends
   - Highlight important developments
   - Focus on practical implications for engineers

### Section 3: Worth watching

6. **Select 10 articles** from the current month's technical watch:
   - Choose the most impactful or interesting articles
   - For each article, use the elevator pitch as the description

### Newsletter Generation

7. **Create the newsletter file**:
   - Path: `newsletter/YYYY-MM.md`
   - Create the `newsletter/` folder if needed

8. **Write the newsletter** with this exact structure:

```markdown
# Newsletter YYYY-MM

==intro text==

## My latest articles from the notebook


**[Article Title](https://lamouche.fr/notebook/posts/...)**
Brief description or publication date


**[Article Title](https://lamouche.fr/notebook/posts/...)**
Brief description or publication date

[...continue for all 10 articles...]

---

## What's hot today ?

[2-3 paragraphs in English synthesizing the key themes, trends, and insights from ALL articles of the current month. Focus on:
- Main topics covered (AI agents, new tools, architectural patterns, etc.)
- Important developments or announcements
- Practical implications for engineers and developers
- Emerging trends or shifts in the industry]

---

## Worth watching


Elevator pitch text describing the article.
[Link](Source URL)


Elevator pitch text describing the article.
[Link](Source URL)


Elevator pitch text describing the article.
[Link](Source URL)


Elevator pitch text describing the article.
[Link](Source URL)


Elevator pitch text describing the article.
[Link](Source URL)

---

## Cartography for noobs

**🧭 Want to understand how maps really work?**

This newsletter explains, step by step, the foundations of modern cartography: data, projections, use cases, and key challenges — simply, with no prior knowledge required.

[Subscribe](https://subscribepage.io/ylAON7)


```

9. **Content guidelines**:
   - Section 1 uses URLs from lamouche.fr/notebook (fetched via WebFetch)
   - Section 2 synthesis is based on ALL articles from `src/YYYY-MM/`
   - Section 3 uses **Source** URLs from the markdown files (external URLs, not internal paths)
   - Elevator pitch provides the description for "We're Watching" articles
   - Synthesis should be concise (2-3 paragraphs)
   - Stay factual and editorial
   - Write in English
   - Focus on engineering, technical implications and futur of work
   - Avoid superlatives and demonstrative words (amazing, incredible, groundbreaking, revolutionary, game-changing, etc.) - keep the tone neutral, factual, and straight to the point

## Notes

- If WebFetch fails, report the error and ask the user to retry
- If unable to read a technical watch article, skip it and note the error
- Ensure all URLs are correct: lamouche.fr URLs for Section 1, external source URLs for Sections 2 and 3
- Keep descriptions concise
- The synthesis should provide strategic insights based on ALL articles of the month
- Select the 5 most impactful articles for the "We're Watching" section
