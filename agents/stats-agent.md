# Stats Agent

Updates README.md with article statistics.

## Usage
```
/stats-agent
```

## Instructions

1. **Parse README.md**: Count articles per month (lines starting with `- [` under `#### Month`)

2. **Generate statistics chart** after title, before Articles section:
```
## Statistics

Articles per month:

2026-01 | ████████ 46<br>
2026-02 | ██ 3
```
   - Each `█` = 2 articles (round up)
   - Chronological order (oldest first)
   - `<br>` after each line except last
   - Only months with articles

3. **Update month headers**: `#### January (5 articles)` (singular if 1)

4. **Commit/push** (only when called directly, not from another agent):
   - `git fetch/pull` if behind
   - Commit: `Update statistics`

## Notes
- Update existing Statistics section, don't duplicate
- Preserve all links and content
