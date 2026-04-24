# Todo - daily-veille-ia-extraire-urls

## Objective
Run the daily Gmail veille IA workflow: extract relevant article URLs from label `0---veille-ia`, sync and clean `LIST.md`, remove off-topic URLs, trash processed emails, and leave the repo clean/synced.

## Plan
- [x] Check repo cleanliness and sync requirements
- [x] Fetch Gmail messages from label `0---veille-ia`
- [x] Extract, normalize, dedupe, and relevance-filter article URLs
- [x] Update `LIST.md` and remove off-topic entries
- [x] Trash processed emails
- [x] Update prompt-hub tracking, commit, and push

## Notes
- Timestamp: 2026-04-24 22:02:31 Europe/Paris
- Agent route: `add-url` rules applied for `LIST.md`
- Gmail returned 1 message; 1 relevant article URL extracted.

## Review
- Repo was first restored to a clean synced state with a dedicated cleanup commit.
- Added 1 new relevant URL to `LIST.md` after dedupe/normalization checks.
- Removed 0 off-topic URLs from `LIST.md`.
- Trashed 1 processed Gmail message.
