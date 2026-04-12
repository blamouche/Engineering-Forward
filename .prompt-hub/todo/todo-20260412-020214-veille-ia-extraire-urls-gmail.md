# Task: veille IA extraire urls gmail

- Created: 2026-04-12 02:02:14 +0200
- Status: failed
- Trigger: cron `a36a0c71-7b2a-4321-b289-0100a1328f1e`

## Plan
- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this task file
- [x] Check Gmail access for `label:0---veille-ia`
- [ ] Extract article URLs from matching emails
- [ ] Sync repo in a clean state and update `LIST.md`
- [ ] Remove non-AI/app-dev URLs from `LIST.md`
- [ ] Trash processed emails
- [ ] Commit and push repo updates

## Notes
- `gog auth list` shows the Gmail account is configured, but Gmail API access failed immediately.
- `gog gmail messages search 'label:0---veille-ia' --max 50 --json --include-body --no-input` returned: `invalid_grant` / `Token has been expired or revoked`.
- Because Gmail access failed, no emails were read, no URLs were extracted, `LIST.md` was not modified, and no emails were trashed.

## Review
- Blocked by revoked/expired OAuth token for `gog` Gmail access.
- Safe outcome: repo content queue untouched; no destructive mail action performed.
