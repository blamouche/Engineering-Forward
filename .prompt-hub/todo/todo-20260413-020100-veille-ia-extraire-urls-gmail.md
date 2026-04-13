# Task: Daily veille IA — extraire URLs Gmail

## Context
- Scheduled cron run at 2026-04-13 02:01 Europe/Paris.
- Goal: search Gmail label `0---veille-ia`, extract article URLs, update `LIST.md` via add-url workflow, remove non-AI/app-dev URLs, trash processed emails, and report counts.

## Plan
- [x] Read prompt-hub lessons, memory, and releases.
- [x] Create this task file.
- [x] Check Gmail access and repo state.
- [x] If repo is dirty, commit/push all local unsynced changes to restore a clean synced state.
- [x] Extract relevant URLs from Gmail and update `LIST.md` with dedupe.
- [x] Remove non-AI/app-dev URLs from `LIST.md`.
- [x] Trash processed emails.
- [x] Update prompt-hub memory/version/releases.
- [x] Commit and push final repo state.
- [x] Write review summary with counts.

## Review
- `gog gmail messages search 'label:0---veille-ia' --max 100 --json --include-body --no-input` failed with `oauth2: invalid_grant`.
- Repo state before cleanup only contained the new scheduled todo file; no content changes were needed in `LIST.md`.
- Result: 0 email read, 0 URL added, 0 URL removed, 0 email trashed.
- Follow-up: re-authenticate Gmail for `gog`, then rerun this sequence.
