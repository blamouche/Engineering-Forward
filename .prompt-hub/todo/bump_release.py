from pathlib import Path
import sys
version_path = Path('.prompt-hub/version.md')
releases_path = Path('.prompt-hub/releases.md')
msg = sys.argv[1]
cur = version_path.read_text().strip()
parts = cur.split('.')
parts[-1] = str(int(parts[-1]) + 1)
new = '.'.join(parts)
version_path.write_text(new)
releases = releases_path.read_text()
entry = f'## {new} - 2026-04-08\n- {msg}\n\n'
if releases.startswith('# Releases\n\n'):
    releases = '# Releases\n\n' + entry + releases[len('# Releases\n\n'):]
else:
    releases = entry + releases
releases_path.write_text(releases)
print(new)
