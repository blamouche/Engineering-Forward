# Todo - veille ia extraire urls gmail

- [x] Read `.prompt-hub/lessons.md`
- [x] Read `.prompt-hub/memory.md`
- [x] Read `.prompt-hub/releases.md`
- [x] Check repo state and sync / clean if needed
- [x] Search Gmail label and extract candidate URLs
- [ ] Filter non-AI/non-app-dev URLs
- [ ] Update `LIST.md` with dedupe
- [ ] Trash processed emails
- [x] Update prompt-hub logs/version/release notes
- [x] Commit and push all local changes

## Review
- Repo state: already clean; no local unsynced changes to flush.
- Gmail access: `gog gmail messages search 'label:0---veille-ia' --max 100 --json --account b.lamouche@gmail.com` failed with `oauth2: invalid_grant` (`Token has been expired or revoked.`).
- Browser fallback: unavailable for the logged-in Chrome profile because the host browser bridge could not attach (`DevToolsActivePort` missing in `/Users/openclaw/Library/Application Support/Google/Chrome`).
- Consequence: no email was read, no URL was extracted, `LIST.md` remained unchanged, and no email was moved to trash.
