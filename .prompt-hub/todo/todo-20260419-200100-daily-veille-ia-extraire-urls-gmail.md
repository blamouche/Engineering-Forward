# Daily veille IA Extraire URLs Gmail

- [x] Load prompt-hub context (lessons, memory, releases)
- [x] Restore a clean synced repo state
- [x] Extract article URLs from Gmail label `0---veille-ia`
- [x] Update `LIST.md` with dedupe and off-topic cleanup
- [x] Trash processed emails
- [x] Update prompt-hub logs/versioning, commit, and push

## Notes
- Cron run requested on 2026-04-19 20:01 Europe/Paris.
- Repo had pending local prompt-hub files, so they were committed/pushed before the Gmail check.
- Gmail labels `0---veille-ia` and `0 - Veille/IA` both returned 0 messages.

## Review
- No new Gmail newsletters were waiting.
- `LIST.md` remained empty after relevance cleanup.
- Effective result: 0 URL added, 0 URL removed, 0 email trashed.
