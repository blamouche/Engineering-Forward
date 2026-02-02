# List Add Agent

Adds URLs to LIST.md queue for later processing.

## Usage
```
/list-add-agent <url1> [url2] [url3] ...
```

## Instructions

1. **Sync**: `git fetch origin && git pull --rebase origin main` if behind

2. **Update LIST.md**: Append each URL on a new line (create file if needed)

3. **Commit and push**: Message: `Add URL(s) to processing queue`

## Notes
- One URL per line
- Preserves existing content
- No URL validation performed
