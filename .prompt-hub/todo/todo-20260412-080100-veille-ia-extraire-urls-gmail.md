# Todo — veille IA extraire urls gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Create this task file
- [x] Check repo status / sync preconditions
- [x] Search Gmail label `0---veille-ia`
- [ ] Extract article URLs
- [ ] Update `LIST.md` via add-url workflow
- [ ] Remove non-AI/app-dev URLs from `LIST.md`
- [ ] Trash processed emails
- [ ] Commit and push any resulting changes

## Plan
1. Verify the repo is clean enough for add-url sync.
2. Read Gmail messages from label `0---veille-ia` and extract article URLs.
3. Normalize/dedupe/filter the queue, then trash processed emails.
4. Update prompt-hub tracking, commit, and push.

## Notes
- Gmail access failed immediately: `gog gmail messages search 'label:0---veille-ia' --max 50 --json --include-body --no-input`
- Error: `oauth2: "invalid_grant" "Token has been expired or revoked."`
- Repo was already clean (`git status --short --branch` showed only `## main...origin/main`).
- No Gmail messages were read, so no URLs could be extracted or filtered and no emails were trashed.

## Review
- Outcome: blocked by Gmail OAuth failure.
- URLs added: 0
- URLs removed: 0
- Emails trashed: 0
- Follow-up: re-authenticate `gog`, then rerun this scheduled workflow.
