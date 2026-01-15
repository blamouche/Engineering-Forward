# Article Synthesis Agent

This agent takes a URL as input and creates a synthesis note in a new markdown file.

## Usage

```
/article-synthesis-agent <url>
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

**Source**: [URL of the original article]

**Date**: [Publication date of the article]

**Author**: [Author name]

**Keywords**: [Comma-separated keywords]

## Elevator pitch

[One sentence summary capturing the essence of the article]

## Takeaways

- [Key point 1]
- [Key point 2]
- [Key point 3]
- [Key point 4]
- [Key point 5]

## Synthesis

[A 500-word synthesis of the article covering the main arguments, key insights, and conclusions]
```

5. **Update the README.md** at the root of the project:
   - Add a link to the newly created file
   - Organize links by year and month in descending order (most recent first)
   - Use this format:

```markdown
## Articles

### 2026

#### January
- [Article Title](src/2026-01/article-slug.md)

#### February
- [Another Article](src/2026-02/another-article.md)

### 2025

#### December
- [Old Article](src/2025-12/old-article.md)
```

6. **Update statistics**:
   - Call the `/stats-agent` agent to update the statistics in the README.md
   - This will add/update the statistics chart and article counts per month
   - Wait for the stats agent to complete before proceeding to the next step

7. **Commit and push changes**:
   - First, check if the local branch is up to date with the remote:
     - Run `git fetch origin` to get the latest remote state
     - Check if there are upstream changes with `git status`
     - If the branch is behind, pull the latest changes with `git pull --rebase origin <branch>`
   - Stage all changes (the new synthesis file and the updated README.md)
   - Commit with a message following this format: `Add synthesis: [Article Title]`
   - Push to the remote repository

## Example

Input: `/article-synthesis-agent https://example.com/article-about-ai`

Output:
1. Creates file `src/2026-01/article-about-ai.md` with the synthesis content
2. Updates `README.md` with a link to the new file under the appropriate year/month section
3. Runs `/stats-agent` to update the statistics chart and article counts
4. Commits and pushes with message: `Add synthesis: Article About AI`

## Notes

- If the article date or author cannot be found, mark as "Unknown"
- Keywords should be inferred from the content if not explicitly provided
- The synthesis should be objective and capture the essence of the article
- Create the `src/YYYY-MM/` directory if it doesn't exist
- Create the README.md if it doesn't exist
- When adding to README, maintain chronological order (newest first)
