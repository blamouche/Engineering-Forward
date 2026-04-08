# Todo — veille-ia-extraire-urls-gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo status and restore a clean synced state if needed
- [x] Search Gmail label `0---veille-ia`
- [x] Extract article URLs and filter to AI/app-dev only
- [x] Update `LIST.md` with dedupe and remove non-relevant URLs
- [x] Trash processed Gmail emails
- [x] Update prompt-hub logs/versioning and push

## Notes
- Cron run requested: daily veille IA URL extraction + LIST.md cleanup.
- If repo is dirty, commit/push all unsynced local changes first to restore a clean state before add-url workflow.

## Review
- Gmail label `0---veille-ia` returned 0 messages.
- Repo had only this new todo file pending; no `LIST.md` content to add/remove.
- `LIST.md` stayed empty, so 0 URL added, 0 removed, 0 email trashed.
- Run logged in prompt-hub memory/releases and pushed to `origin/main`.
