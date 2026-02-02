# Month Synthesis Agent

Produces a monthly synthesis from articles in a given month.

## Usage
```
/month-synthesis-agent <YYYY-MM>
```

## Instructions

1. **Read articles** from `src/YYYY-MM/` (stop if folder empty/missing)

2. **Extract** from each: Title, Source URL, Elevator pitch, Takeaways, Synthesis

3. **Consult previous syntheses** (2-3 prior months) to avoid repetition and ensure continuity

4. **Create** `synthesis/YYYY-MM.md`:
```markdown
# Synthesis YYYY-MM

## Summary
[Up to 4 paragraphs on monthly trends in AI work and required adaptations]

## Selected links
- [Title](Source URL)
[15 links prioritizing AI work, enterprise usage, organization, skills]
```

5. **Update README**: Add synthesis link near month header:
   `#### January (15 articles) [Synthesis 2026-01](synthesis/2026-01.md)`

6. **Commit and push**: `git fetch/pull` if behind, commit: `Add monthly synthesis for YYYY-MM`

## Notes
- Write in English
- Factual, editorial style, max 4 paragraphs
- Avoid hyperbolic words (pivotal, groundbreaking, revolutionary, etc.)
- ASCII filenames preferred
