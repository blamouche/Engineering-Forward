# Todo — veille-ia-extraire-urls-gmail

## Context
- Scheduled daily run from cron on 2026-04-11 20:02:02 Europe/Paris.
- Goal: search Gmail label `0---veille-ia`, extract AI/app-dev article URLs, sync and clean `LIST.md`, trash processed emails, then report counts.

## Plan
- [x] Load `.prompt-hub/lessons.md`, `.prompt-hub/memory.md`, `.prompt-hub/releases.md`.
- [x] Search Gmail label `0---veille-ia`.
- [x] Inspect repo state and `LIST.md`.
- [x] Apply add-url workflow if URLs are found; otherwise record no-op.
- [x] Update prompt-hub tracking files, commit, and push.

## Review
- Gmail label `0---veille-ia` returned 0 message.
- Repo was already clean/synced aside from the new task log.
- `LIST.md` stayed empty.
- Result: 0 URL added, 0 URL removed, 0 email trashed.
