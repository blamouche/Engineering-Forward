# Todo - daily veille ia extraire urls gmail

## Context
- Timestamp: 2026-04-20 22:01:00 Europe/Paris
- Trigger: cron daily veille IA
- Goal: extract relevant URLs from Gmail label(s), sync and clean LIST.md, trash processed emails, then commit and push all repo updates.

## Plan
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Read `agents.md`
- [x] Create this task file
- [x] Inspect repo status and restore clean synced state if needed
- [x] Search Gmail veille label(s) and collect messages
- [x] Extract, normalize, dedupe, and filter AI/app-dev URLs
- [x] Update `LIST.md` and remove off-topic URLs
- [x] Trash processed emails
- [x] Update prompt-hub tracking files
- [ ] Commit and push all changes

## Notes
- Apply `add-url` constraints: clean sync first, then update `LIST.md`, verify, commit, push.
- If repo is dirty, commit/push all pending local changes before queue update.

## Review
- Added 14 URL(s) to `LIST.md`.
- Removed 0 off-topic URL(s) from `LIST.md`.
- Trashed 2 Gmail message(s) from veille labels.
- Pending final commit/push for `LIST.md` + prompt-hub tracking.
