# List Add Agent

This agent adds one or more URLs to the LIST.md queue for later processing.

## Usage

```
/list-add-agent <url1> [url2] [url3] ...
```

## Instructions

When the user provides one or more URLs:

1. **Sync with repository**:
   - Run `git fetch origin` to get the latest remote state
   - Check if there are upstream changes with `git status`
   - If the branch is behind, pull the latest changes with `git pull --rebase origin main`

2. **Read LIST.md**:
   - Open the `LIST.md` file at the project root
   - If the file doesn't exist, create it

3. **Add URLs**:
   - Add each URL on a new line at the end of the document
   - Maintain one URL per line
   - Preserve any existing content in the file
   - If the file ends without a newline, add one before appending

4. **Commit and push changes**:
   - Stage the updated LIST.md
   - Commit with message: `Add URL(s) to processing queue`
   - Push to the remote repository

## Example

Input: `/list-add-agent https://example.com/article-1 https://example.com/article-2`

Before:
```
https://existing-url.com/article
```

After:
```
https://existing-url.com/article
https://example.com/article-1
https://example.com/article-2
```

## Notes

- URLs are added in the order provided
- Each URL must be on its own line
- No validation is performed on URL format
- The list-agent will process URLs from top to bottom
