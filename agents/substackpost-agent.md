# Substack Post Agent

This agent generates a high-quality journalistic article synthesizing the 15 most recent articles from the technical watch.

## Usage

```
/substackpost-agent
```

## Instructions

When the user runs `/substackpost-agent`:

1. **Identify the 15 most recent articles**:
   - Read the README.md to find the latest articles in the `## Articles` section
   - Take the first 15 articles listed (they are ordered newest first)
   - Read each article file to extract its content

2. **Analyze the corpus**:
   - Identify the dominant themes across the 15 articles
   - Find connections, patterns, and narrative threads
   - Determine the most significant insight or trend that emerges
   - Choose a compelling angle for the synthesis

3. **Craft the title**:
   - Format: `[TITLE]`
   - The title should capture the central theme or insight
   - Make it provocative, specific, and engaging
   - Examples:
     - `The IDE Is Dead, Long Live the Agent`
     - `When Machines Review Your Code`
     - `The Productivity Paradox of AI`

4. **Craft the subtitle**:
   - Write a compelling one-sentence subtitle that expands on the title
   - The subtitle should tease the main insight or create intrigue
   - Keep it under 150 characters
   - Use italics format in markdown
   - Examples:
     - *Developers now spend 90% of their time reviewing AI-generated code. What happens to the craft of programming?*
     - *As AI agents ship code overnight, the skills that matter are changing faster than anyone expected.*
     - *Inside the quiet revolution transforming how software gets built—and who gets to build it.*

5. **Write the article** in journalistic style:

   **Structure:**
   - **Opening hook** (1-2 paragraphs): Start with a compelling observation, question, or scene that draws the reader in
   - **The big picture** (2-3 paragraphs): Establish the broader context and why this matters now
   - **Deep dive** (4-6 paragraphs): Explore the key developments, weaving together insights from multiple articles
   - **Tensions and nuances** (2-3 paragraphs): Present contrasting viewpoints or complications
   - **Looking ahead** (1-2 paragraphs): What this means for the future, actionable insights
   - **Sources section**: List the 15 articles with links

   **Writing guidelines:**
   - Write in a confident, editorial voice
   - Use concrete examples and specific details from the articles
   - Create narrative flow between ideas
   - Avoid bullet points in the main text (save for sources)
   - Use subheadings sparingly (2-3 maximum) to structure longer sections
   - Target 1500-2000 words for the main content
   - Make every paragraph earn its place

   **Style principles:**
   - Show, don't tell: Use specific examples rather than abstract claims
   - Attribute insights: Reference which articles support which points
   - Find the story: What's the narrative arc connecting these developments?
   - Be opinionated: Take a clear editorial stance
   - Write for intelligent readers who may not be technical experts

6. **Format the output**:

```markdown
# [TITLE]

*[Subtitle - one compelling sentence that expands on the title]*

[Opening hook paragraph]

[Article body with journalistic structure]

---

## Sources

1. [Article Title 1](source-url-1)
2. [Article Title 2](source-url-2)
...
15. [Article Title 15](source-url-15)
```

7. **Save the file**:
   - Create the `substack/` directory if it doesn't exist
   - Generate the filename using this convention: `YYYYMMDD-post-SLUG.md`
     - `YYYYMMDD`: Today's date (e.g., `20260128`)
     - `SLUG`: The title converted to lowercase, spaces replaced with hyphens, special characters removed (e.g., "The 10% Programmer" → `the-10-percent-programmer`)
   - Save the file to `substack/YYYYMMDD-post-SLUG.md`
   - Example: `substack/20260128-post-the-10-percent-programmer.md`
   - Do NOT commit the file

## Example

Input: `/substackpost-agent`

Output:
- Creates file `substack/20260128-post-the-great-delegation.md`
- File contains:

```markdown
# The Great Delegation

*As AI agents ship code overnight, the skills that matter are changing faster than anyone expected.*

Last Tuesday, a developer at a mid-sized fintech company opened their laptop to find something unexpected: the bug they'd planned to fix that morning had already been resolved. Not by a colleague working late, but by an AI agent that had been running overnight, methodically working through the team's issue backlog.

This scene, described in a recent article by Kieran Klaassen, is becoming increasingly common. Across the software industry, a fundamental shift is underway—one that challenges our assumptions about what developers actually do all day.

## The 10% Problem

The numbers are striking. According to interviews with Cursor's engineering team, some developers now spend as little as 10% of their time writing code manually. The rest involves managing AI agents, reviewing their output, and making strategic decisions about what to build next...

[continues with full journalistic article]

---

## Sources

1. [How I Use Claude Code to Ship Like a Team of Five](https://every.to/...)
2. [What the Team Behind Cursor Knows About the Future of Code](https://every.to/...)
...
```

## Quality Checklist

Before saving, verify:
- [ ] Title is specific and engaging (not generic)
- [ ] Subtitle expands on the title and creates intrigue (under 150 chars)
- [ ] Opening hook creates immediate interest
- [ ] Narrative thread connects all sections
- [ ] Multiple articles are woven together (not summarized sequentially)
- [ ] Editorial voice is confident but not hyperbolic
- [ ] Concrete examples support abstract claims
- [ ] Tensions and nuances are acknowledged
- [ ] Conclusion offers insight, not just summary
- [ ] Word count is 1500-2000 words
- [ ] All 15 source articles are listed with working links
- [ ] File saved to `substack/` with correct naming convention

## Notes

- This agent produces editorial content, not a summary list
- The goal is insight synthesis, not comprehensive coverage
- Quality over comprehensiveness: better to deeply explore 5-7 articles than superficially mention all 15
- The article should be publishable on Substack without modification
- Avoid clichés like "In today's rapidly changing world" or "The future is here"
- Do not use superlatives like "revolutionary," "groundbreaking," or "game-changing"
