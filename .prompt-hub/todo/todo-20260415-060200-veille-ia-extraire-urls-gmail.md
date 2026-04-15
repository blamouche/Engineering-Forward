# Todo — veille IA extraire urls gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Read `agents.md`
- [x] Check repo cleanliness / sync strategy
- [x] Search Gmail veille labels and extract article URLs
- [x] Update `LIST.md` with normalized, deduped relevant URLs only
- [x] Remove off-topic URLs from `LIST.md`
- [x] Trash processed Gmail messages
- [x] Update prompt-hub trace files (`memory.md`, `version.md`, `releases.md`)
- [x] Commit and push required changes

## Notes
- Scheduled daily veille IA extraction run.
- Need to honor `add-url`: clean sync, dedupe, verify URLs in `LIST.md`, commit/push.

## Review
- Repo was initially clean except for this task log after creation.
- Gmail labels `0---veille-ia` and `0 - Veille/IA` both returned 0 messages.
- `LIST.md` was already empty, so no URL was added or removed.
- No processed email existed to move to trash.
- Prompt-hub tracking files were updated and the no-op trace was prepared for commit/push.
