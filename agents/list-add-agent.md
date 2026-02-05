# List Add Agent

Adds URL(s) to `LIST.md` (processing queue) in a **reliable, verifiable** way.

## Usage
```
/list-add-agent <url1> [url2] [url3] ...
```

## Instructions

1) **Sync (must be clean)**
- `git status --porcelain` must be empty
- `git pull --rebase`

2) **Normalize + append URLs**
- Ensure `LIST.md` exists
- Append **one URL per line**
- Remove blank lines
- De-duplicate exact duplicate URLs (preserve order)

Recommended (safe with `?&=` etc.):
```bash
python3 - <<'PY'
from pathlib import Path
import sys

urls = [u.strip() for u in sys.argv[1:] if u.strip()]
if not urls:
    raise SystemExit('No URLs provided')

p = Path('LIST.md')
existing = []
if p.exists():
    existing = [ln.strip() for ln in p.read_text().splitlines() if ln.strip()]

# append + de-dupe preserving order
seen = set()
out = []
for ln in existing + urls:
    if ln in seen:
        continue
    seen.add(ln)
    out.append(ln)

p.write_text('\n'.join(out) + ('\n' if out else ''))
PY \
  "<url1>" "<url2>" "<url3>"
```

3) **Verify before committing**
- For each URL you intended to add:
  - `grep -Fqx -- "<url>" LIST.md`

4) **Commit + push (only if changes)**
```bash
git add LIST.md
if git diff --cached --quiet; then
  echo "No changes (URLs already present)."
  exit 0
fi
git commit -m "Add URL(s) to processing queue"
git push
```

5) **Verify HEAD contains the URLs**
- For each URL:
  - `git show HEAD:LIST.md | grep -Fqx -- "<url>"`

## Notes / Pitfalls
- Avoid fragile shell-escaping / nested quotes when handling URLs.
- Always verify with `grep -Fqx` (exact full-line match).
- Keep `LIST.md` as plain text: one URL per line, no bullets.
