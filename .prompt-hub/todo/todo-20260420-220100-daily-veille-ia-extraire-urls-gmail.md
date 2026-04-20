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
- [ ] Inspect repo status and restore clean synced state if needed
- [ ] Search Gmail veille label(s) and collect messages
- [ ] Extract, normalize, dedupe, and filter AI/app-dev URLs
- [ ] Update `LIST.md` and remove off-topic URLs
- [ ] Trash processed emails
- [ ] Update prompt-hub tracking files
- [ ] Commit and push all changes

## Notes
- Apply `add-url` constraints: clean sync first, then update `LIST.md`, verify, commit, push.
- If repo is dirty, commit/push all pending local changes before queue update.

## Review
- Pending.
