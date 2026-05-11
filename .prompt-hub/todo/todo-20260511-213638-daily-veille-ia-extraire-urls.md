# Daily veille IA extraire URLs

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Read `agents.md`
- [x] Check repo status and restore a clean synced state if needed
- [x] Search Gmail label `0---veille-ia`
- [x] Extract, normalize, and filter relevant AI/app-dev article URLs
- [x] Update `LIST.md` with dedupe and remove off-topic URLs
- [x] Trash processed emails
- [x] Update prompt-hub memory/version/releases, commit, and push

## Notes
- Cron run requested on 2026-05-11 21:36 Europe/Paris.
- If repo is dirty, commit/push all pending local changes first so add-url rules can run from a clean synced state.

## Review
- Repo cleaned and synced before extraction.
- Gmail veille backlog processed and moved to trash.
- `LIST.md` rebuilt with relevant AI/app-dev URLs only.
