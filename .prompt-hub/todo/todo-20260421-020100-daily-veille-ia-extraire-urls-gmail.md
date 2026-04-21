# Daily veille IA Extraire URLs Gmail

- [x] Read prompt-hub context and repo instructions
- [x] Inspect repo sync state and restore a clean synced tree if needed
- [x] Search Gmail veille label(s) and extract article URLs
- [x] Update LIST.md with normalized/deduped relevant URLs only
- [x] Remove queued URLs that are not AI or application-development related
- [x] Trash processed Gmail emails
- [x] Update prompt-hub tracking (memory, version, releases)
- [ ] Commit and push all pending changes

## Notes
- Cron run requested at 2026-04-21 02:01 Europe/Paris.
- Must commit/push all unsynced local changes first if repo is not clean.

## Review
- Repo cleaned and synced first via commit+push, then rebased on `origin/main`.
- Gmail labels `0---veille-ia` and `0 - Veille/IA` both returned 0 message.
- `LIST.md` was already empty, so 0 URL was added and 0 off-topic URL was removed.
- No email was trashed because nothing was found to process.
