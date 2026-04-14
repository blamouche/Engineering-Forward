# Task: Daily veille IA — extraire URLs Gmail

## Context
Scheduled cron run on 2026-04-14 16:01 Europe/Paris.

## Plan
- [x] Load Gmail messages from label `0---veille-ia` and extract candidate article URLs.
- [x] Ensure repo is synced cleanly per `add-url` workflow requirements.
- [x] Normalize/dedupe relevant AI/app-dev URLs into `LIST.md`.
- [x] Remove non-AI/non-app-dev URLs from `LIST.md`.
- [x] Trash processed Gmail messages.
- [x] Update prompt-hub memory/version/releases, commit, and push.

## Review
- Added 12 URLs, removed 0 URLs, trashed 2 emails, and pushed the queue update.
