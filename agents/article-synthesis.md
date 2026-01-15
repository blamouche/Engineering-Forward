# Article Synthesis Agent

This agent takes a URL as input and creates a synthesis note in a new markdown file.

## Usage

```
/article-synthesis <url>
```

## Instructions

When the user provides a URL:

1. **Fetch the article** using WebFetch tool to retrieve the content from the provided URL

2. **Extract metadata** from the article:
   - Title
   - Publication date
   - Author name
   - Keywords/tags

3. **Create the output file**:
   - Directory: `src/YYYY-MM/` where YYYY is the current year and MM is the current month
   - Filename: Convert the article title to a slug (lowercase, hyphens instead of spaces, no special characters) and append `.md`
   - Example: `src/2026-01/how-to-build-better-apis.md`

4. **Generate the content** with this exact structure:

```markdown
# [Article Title]

**Date**: [Publication date of the article]
**Author**: [Author name]
**Keywords**: [Comma-separated keywords]

## Takeaways

- [Key point 1]
- [Key point 2]
- [Key point 3]
- [Key point 4]
- [Key point 5]

## Synthesis

[A 500-word synthesis of the article covering the main arguments, key insights, and conclusions]
```

## Example

Input: `/article-synthesis https://example.com/article-about-ai`

Output: Creates file `src/2026-01/article-about-ai.md` with the synthesis content.

## Notes

- If the article date or author cannot be found, mark as "Unknown"
- Keywords should be inferred from the content if not explicitly provided
- The synthesis should be objective and capture the essence of the article
- Create the `src/YYYY-MM/` directory if it doesn't exist
