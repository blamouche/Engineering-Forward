# Veille IA Gmail extraction — 2026-04-15 22:01:00

## Objective
Run the scheduled veille IA sequence:
1. Search Gmail label(s) for veille IA messages
2. Extract article URLs
3. Sync repo cleanly and update LIST.md via add-url workflow
4. Remove non-AI/app-dev URLs from LIST.md
5. Trash processed emails

## Checklist
- [x] Load prompt-hub context
- [x] Create this task log
- [x] Inspect Gmail messages and extract candidate URLs
- [x] Restore clean synced repo state if needed
- [x] Update LIST.md with dedupe/filtering
- [x] Trash processed Gmail messages
- [x] Update prompt-hub version/releases/memory
- [x] Commit and push all pending changes

## Review
- Gmail search matched 6 messages in label `0 - Veille/IA`.
- Kept only AI / agent / app-dev relevant URLs and resolved newsletter tracking links to canonical article URLs where possible.
- `LIST.md` was rebuilt from empty with the filtered queue.
- Trashed the 6 processed Gmail messages, bumped prompt-hub tracking, and prepared the final commit/push.
