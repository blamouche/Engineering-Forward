# List Agent

This agent reads `LIST.md` and processes each URL using the article synthesis agent.

## Usage

```
/list-agent
```

## Instructions

When the user runs `/list-agent`:

1. **Open `LIST.md`** in the project root.

2. **Process URLs in order**:
   - Read URLs top to bottom.
   - Always start with the first URL in the file.
   - Ignore empty lines.

3. **For each URL**:
   - Run the article synthesis agent: `/article-synthesis-agent <url>`
   - Wait for it to complete.
   - Remove the processed URL line from `LIST.md` immediately after completion.
   - Save `LIST.md` after each removal.

4. **Finish**:
   - Continue until no URLs remain.
   - When complete, `LIST.md` must be empty.

## Notes

- If an URL fails to process, stop and report the error before modifying the list.
- Do not reorder URLs.
