# Todo — veille-ia-extraire-urls-gmail

- [x] Read prompt-hub context (`lessons.md`, `memory.md`, `releases.md`)
- [x] Check repo status
- [x] Attempt Gmail extraction from label `0---veille-ia`
- [x] Record blocker (`gog` OAuth `invalid_grant`)
- [x] Leave repo traceability updates for this failed run

## Review

- Gmail extraction failed immediately because `gog gmail messages search 'label:0---veille-ia' --max 100 --json --no-input` returned `oauth2: "invalid_grant" "Token has been expired or revoked."`
- No emails were read.
- `LIST.md` was left unchanged.
- No URLs were added.
- No URLs were removed.
- No emails were moved to trash.
- Browser fallback was not retried in this run because prior runs already showed the browser bridge was unavailable; the primary blocker remains Gmail re-authentication for `gog`.
