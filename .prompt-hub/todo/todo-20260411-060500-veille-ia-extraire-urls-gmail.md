# Todo — veille ia extraire urls gmail

## Context
- Timestamp: 2026-04-11 06:05:00 Europe/Paris
- Source: cron `Daily veille IA Extraire urls de gmail`
- Goal: search Gmail label `0---veille-ia`, extract AI/app-dev URLs, sync/update `LIST.md`, remove non-relevant URLs, trash processed emails, then log/version/commit/push.

## Plan
- [x] Read prompt-hub lessons, memory, releases
- [x] Inspect repo state and current `LIST.md`
- [x] Search Gmail label and extract candidate article URLs
- [x] Restore clean synced repo state if needed, then update `LIST.md` with dedupe/filter rules
- [x] Trash processed Gmail messages
- [x] Update prompt-hub memory/version/releases and finalize commit/push

## Review
- Gmail label `0---veille-ia` returned 0 message.
- Repo was not clean because two prompt-hub todo files were untracked.
- `LIST.md` was already empty, so 0 URL added, 0 URL removed, and 0 email trashed.
- Remaining work: log the run in prompt-hub metadata, then commit/push the cleanup state.
