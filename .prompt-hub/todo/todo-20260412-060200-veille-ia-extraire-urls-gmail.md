# Todo — veille-ia-extraire-urls-gmail

- [x] Read .prompt-hub/lessons.md
- [x] Read .prompt-hub/memory.md
- [x] Read .prompt-hub/releases.md
- [x] Check Gmail access for label `0---veille-ia`
- [ ] Extract article URLs from Gmail messages
- [ ] Sync repo from a clean state and update `LIST.md`
- [ ] Remove non-AI/app-dev URLs from `LIST.md`
- [ ] Trash processed Gmail emails
- [x] Document blocked run and results

## Notes
- Scheduled cron run at 2026-04-12 06:02 Europe/Paris.
- `gog gmail messages search 'label:0---veille-ia' --max 100 --json --no-input` failed with `oauth2: "invalid_grant" "Token has been expired or revoked."`
- Because Gmail access failed, no emails could be read, no URLs could be extracted, `LIST.md` was not changed, and no emails were trashed.

## Review
- Outcome: failed
- Reason: Gmail OAuth token for `gog` is expired or revoked.
- Follow-up: re-authenticate `gog`, then rerun the scheduled veille IA extraction.
