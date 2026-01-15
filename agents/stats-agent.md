# Stats Agent

This agent calculates and displays statistics about articles in the README.

## Usage

```
/stats-agent
```

## Instructions

When invoked, this agent updates the README.md with statistics:

1. **Read the README.md** at the root of the project

2. **Count articles per month**:
   - Parse the README to find all month sections (e.g., `#### January`, `#### February`)
   - Count the number of article links (lines starting with `- [`) under each month
   - Store the count for each month with its year

3. **Generate the statistics chart**:
   - Create an ASCII bar chart showing article counts per month
   - Use this format:

```
## 📊 Statistics

Articles per month:

2026-01 | ████████████████ 5
```

   - Each `█` represents one article
   - Show months in chronological order (oldest to newest)
   - Only show months that have articles

4. **Update month headers with counts**:
   - Add the article count next to each month name
   - Format: `#### January (5 articles)` or `#### January (1 article)`
   - Use singular "article" when count is 1, plural "articles" otherwise

5. **Update the README.md**:
   - Add or update the Statistics section at the top (after the main title and description)
   - Update all month headers with their article counts
   - Preserve all existing content and links

6. **Commit and push changes** (only when called directly, not from another agent):
   - First, check if the local branch is up to date with the remote:
     - Run `git fetch origin` to get the latest remote state
     - Check if there are upstream changes with `git status`
     - If the branch is behind, pull the latest changes with `git pull --rebase origin <branch>`
   - Stage the updated README.md
   - Commit with message: `Update statistics`
   - Push to the remote repository
   - **Note**: When called from `/article-synthesis-agent`, skip this step as the parent agent will handle the commit

## Example

Before running `/stats-agent-agent`:

```markdown
# Engineering-Forward
Technical watch for engineering

## Articles

### 2026

#### January
- [Article 1](src/2026-01/article-1.md)
- [Article 2](src/2026-01/article-2.md)
- [Article 3](src/2026-01/article-3.md)
```

After running `/stats-agent-agent`:

```markdown
# Engineering-Forward
Technical watch for engineering

## 📊 Statistics

Articles per month:

2026-01 | ███ 3

## Articles

### 2026

#### January (3 articles)
- [Article 1](src/2026-01/article-1.md)
- [Article 2](src/2026-01/article-2.md)
- [Article 3](src/2026-01/article-3.md)
```

## Notes

- The chart uses Unicode block characters (█) for visual representation
- Months with 0 articles are not displayed in the chart
- The Statistics section is always placed after the project title/description and before the Articles section
- If a Statistics section already exists, update it rather than creating a duplicate
- Month counts in headers should be updated to reflect current totals
