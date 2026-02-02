# List Agent

This agent reads `LIST.md` and processes each URL using the article synthesis agent.

## Usage

```
/list-agent
```

## Instructions

When the user runs `/list-agent`:

1. **Open `LIST.md`** in the project root.

2. **Initialize batch tracking**:
   - Create an empty list to store processed articles (title, elevator pitch, URL).
   - Note the current timestamp for the batch recap filename.

3. **Process URLs in order**:
   - Read URLs top to bottom.
   - Always start with the first URL in the file.
   - Ignore empty lines.

4. **For each URL**:
   - Run the article synthesis agent: `/article-synthesis-agent <url>`
   - Wait for it to complete.
   - Extract the article title and elevator pitch from the created synthesis file.
   - Add to the batch tracking list: title, elevator pitch, and URL.
   - Remove the processed URL line from `LIST.md` immediately after completion.
   - Save `LIST.md` after each removal.
   - Commit and push with message: `Process article: [Article Title]`

5. **Create batch recap**:
   - When all URLs are processed, create `synthesis/YYYY-MM-DD - HHmmss - batch recap.md`
   - Use the timestamp noted at the start of processing.
   - Format:
     ```markdown
     # Batch Recap - YYYY-MM-DD HH:mm:ss

     **Article Title 1**
     One sentence elevator pitch summary.
     https://example.com/article1

     **Article Title 2**
     One sentence elevator pitch summary.
     https://example.com/article2
     ```
   - Commit and push with message: `Add batch recap: YYYY-MM-DD HHmmss`

6. **Finish**:
   - When complete, `LIST.md` must be empty.

## Notes

- If a URL fails to process, stop and report the error before modifying the list.
- Do not reorder URLs.
- The batch recap file uses 24-hour time format (HHmmss) without colons for filename compatibility.
