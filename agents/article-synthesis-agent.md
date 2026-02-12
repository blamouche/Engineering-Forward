# Article Synthesis Agent

Creates a synthesis note from a URL.

## Usage
```
/article-synthesis-agent <url>
```

## Instructions

1. **Fetch article** via WebFetch

2. **Extract metadata**: Title, Date, Author, Keywords

3. **Create file** at `src/YYYY-MM/YYYYMMDD-<title-slug>.md` (YYYYMMDD = date de publication si dispo, sinon date du jour):
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

4. **Update README.md**: Add link under `## Articles > ### YYYY > #### Month` (newest first)

5. **Run `/stats-agent`** to update statistics

6. **Commit and push**:
   - `git fetch origin && git pull --rebase origin <branch>` if behind
   - Stage changes, commit: `Add synthesis: [Title]`
   - Push

## Notes
- Create directories if needed
- Maintain chronological order (newest first)
- Synthesis should be objective
