# Todo - Daily veille IA extraire URLs

## Context
- Timestamp: 2026-04-30 04:01:00 Europe/Paris
- Objective: search Gmail label `0---veille-ia`, extract article URLs, sync/clean the repo, update `LIST.md` with dedupe, remove off-topic URLs, trash processed emails, commit and push all resulting changes.

## Plan
- [x] Inspect repo state and restore a clean synced baseline if needed.
- [x] Fetch Gmail messages from label `0---veille-ia` and extract candidate URLs.
- [x] Update `LIST.md` with relevant AI/app-dev URLs only, deduped and normalized. (No new URLs found.)
- [x] Remove off-topic URLs from `LIST.md`. (No URLs present.)
- [x] Trash processed emails. (No emails to trash.)
- [x] Update prompt-hub trace files, commit, and push.

## Notes
- Follow `agents.md` add-url workflow requirements.
- If repo is dirty, commit/push all local unsynced changes first to get back to a clean state.

## Review
- Gmail label `0---veille-ia` returned 0 message(s).
- `LIST.md` remained empty.
- Added URLs: 0.
- Removed off-topic URLs: 0.
- Trashed emails: 0.
- Repo restored to a clean synced state before the Gmail check.
