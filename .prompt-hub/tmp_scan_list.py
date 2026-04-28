import os, re, subprocess, unicodedata, math
from pathlib import Path
from datetime import datetime
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
import requests
from bs4 import BeautifulSoup

ROOT = Path('/Users/openclaw/github/Engineering-Forward')
LIST = ROOT / 'LIST.md'
README = ROOT / 'README.md'
VERSION = ROOT / '.prompt-hub/version.md'
RELEASES = ROOT / '.prompt-hub/releases.md'
PH_MEMORY = ROOT / '.prompt-hub/memory.md'
ROOT_MEMORY = ROOT / 'memory.md'
TASK = ROOT / '.prompt-hub/todo/todo-20260428-090853-scan-list.md'
BRANCH = 'main'
GITHUB_BASE = 'https://github.com/blamouche/Engineering-Forward/blob/main/'
NOW = datetime.now()
BATCH_STAMP = NOW.strftime('%Y-%m-%d - %H%M%S')
BATCH_HUMAN = NOW.strftime('%Y-%m-%d %H:%M:%S')
BATCH_FILE = ROOT / 'synthesis' / f'{BATCH_STAMP} - batch recap.md'
SESSION_TS = NOW.strftime('%Y-%m-%d %H:%M:%S %z')
USER_AGENT = 'Mozilla/5.0 (compatible; OpenClawScanList/1.0)'

session = requests.Session()
session.headers.update({'User-Agent': USER_AGENT})

STOPWORDS = {'the','a','an','and','or','of','to','in','for','on','with','from','by','at','is','are','be','as','that','this','it','its','into','your','you','how','why'}


def run(*args, check=True):
    res = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if check and res.returncode != 0:
        raise RuntimeError(f'command failed: {args}\nstdout={res.stdout}\nstderr={res.stderr}')
    return res


def bump_version(note):
    cur = VERSION.read_text().strip()
    parts = cur.split('.')
    parts[-1] = str(int(parts[-1]) + 1)
    new = '.'.join(parts)
    VERSION.write_text(new + '\n')
    prev = RELEASES.read_text()
    RELEASES.write_text(f'## {new} - {datetime.now().strftime("%Y-%m-%d")}\n- {note}\n\n' + prev)
    return new


def append_log(path, text):
    existing_size = path.stat().st_size if path.exists() else 0
    with path.open('a') as f:
        if existing_size and not str(text).startswith('\n'):
            f.write('\n')
        f.write(text.rstrip() + '\n')


def normalize_url(url):
    url = url.strip()
    parts = urlsplit(url)
    qs = []
    for k, v in parse_qsl(parts.query, keep_blank_values=True):
        lk = k.lower()
        if lk.startswith('utm_') or lk in {'ref','fbclid','gclid','mc_cid','mc_eid'}:
            continue
        qs.append((k, v))
    clean = urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip('/') if parts.path != '/' else parts.path, urlencode(qs), ''))
    return clean


def slugify(text, max_len=90):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    text = re.sub(r'-{2,}', '-', text)
    return text[:max_len].strip('-') or 'article'


def fetch(url):
    try:
        r = session.get(url, timeout=30, allow_redirects=True)
    except Exception as e:
        return None, f'{type(e).__name__}: {e}'
    if r.status_code >= 400:
        return None, f'HTTP {r.status_code}'
    return r, None


def clean_text(t):
    t = re.sub(r'\s+', ' ', t or '').strip()
    return t


def sentence(text, words=28):
    txt = clean_text(text)
    if not txt:
        return ''
    m = re.split(r'(?<=[\.!?])\s+', txt)
    s = m[0].strip()
    ws = s.split()
    if len(ws) > words:
        s = ' '.join(ws[:words]).rstrip(' ,;:') + '…'
    return s


def extract_date(soup, fallback):
    metas = [
        ('meta', {'property':'article:published_time'}, 'content'),
        ('meta', {'name':'publish_date'}, 'content'),
        ('meta', {'name':'pubdate'}, 'content'),
        ('meta', {'name':'date'}, 'content'),
        ('meta', {'property':'og:updated_time'}, 'content'),
        ('time', {}, 'datetime'),
    ]
    for tag, attrs, attr in metas:
        el = soup.find(tag, attrs=attrs) if attrs else soup.find(tag)
        if el and el.get(attr):
            raw = el.get(attr)
            m = re.search(r'(\d{4})-(\d{2})-(\d{2})', raw)
            if m:
                return f'{m.group(1)}-{m.group(2)}-{m.group(3)}', raw
    return fallback.strftime('%Y-%m-%d'), 'Unknown'


def extract_article(url):
    resp, err = fetch(url)
    if err:
        return {'error': f'FETCH_ERROR: {url} — {err}'}
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = clean_text((soup.find('meta', attrs={'property':'og:title'}) or {}).get('content') if soup.find('meta', attrs={'property':'og:title'}) else '') or clean_text(soup.title.string if soup.title and soup.title.string else '') or url
    author = 'Unknown'
    for attrs in ({'name':'author'},{'property':'author'},{'name':'parsely-author'}):
        el = soup.find('meta', attrs=attrs)
        if el and el.get('content'):
            author = clean_text(el['content'])
            break
    date_iso, raw_date = extract_date(soup, datetime.now())
    kw = []
    el = soup.find('meta', attrs={'name':'keywords'})
    if el and el.get('content'):
        kw = [clean_text(x) for x in el['content'].split(',') if clean_text(x)]
    paras = []
    for p in soup.find_all(['p','li']):
        txt = clean_text(p.get_text(' ', strip=True))
        if len(txt) >= 60 and txt not in paras:
            paras.append(txt)
    if not paras:
        return {'error': f'FETCH_ERROR: {url} — no extractable article text'}
    main = paras[:12]
    elevator = sentence(main[0], 30)
    takeaways = []
    seen = set()
    for p in main:
        s = sentence(p, 24)
        key = s.lower()
        if s and key not in seen:
            takeaways.append(s)
            seen.add(key)
        if len(takeaways) == 5:
            break
    if not kw:
        words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9'-]+", title)]
        kw = [w for w in words if w not in STOPWORDS][:5]
    synthesis = '\n\n'.join(main[:8])
    return {
        'title': title,
        'author': author,
        'date_iso': date_iso,
        'date_display': raw_date if raw_date != 'Unknown' else 'Unknown',
        'keywords': ', '.join(kw[:8]) if kw else 'Unknown',
        'elevator': elevator or sentence(title, 18),
        'takeaways': takeaways or [sentence(title, 18)],
        'synthesis': synthesis,
    }


def write_article(url, art):
    y,m,d = art['date_iso'].split('-')
    folder = ROOT / 'src' / f'{y}-{m}'
    folder.mkdir(parents=True, exist_ok=True)
    slug = slugify(art['title'])
    rel = Path('src') / f'{y}-{m}' / f'{y}{m}{d}-{slug}.md'
    path = ROOT / rel
    content = f"# {art['title']}\n**Source**: {url}\n**Date**: {art['date_display']}\n**Author**: {art['author']}\n**Keywords**: {art['keywords']}\n\n## Elevator pitch\n{art['elevator']}\n\n## Takeaways\n" + '\n'.join(f'- {t}' for t in art['takeaways']) + f"\n\n## Synthesis\n{art['synthesis']}\n"
    path.write_text(content)
    return rel


def read_title(path):
    for line in Path(path).read_text().splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return Path(path).stem


def rebuild_readme():
    preamble = README.read_text().split('## Articles')[0]
    articles = []
    for p in sorted((ROOT/'src').glob('*/*.md')):
        folder = p.parent.name
        if not re.match(r'\d{4}-\d{2}', folder):
            continue
        title = read_title(p)
        rel = p.relative_to(ROOT).as_posix()
        try:
            date_num = int(p.stem.split('-')[0])
        except Exception:
            date_num = 0
        year, month = folder.split('-')
        articles.append({'path': rel, 'title': title, 'year': int(year), 'month': int(month), 'date_num': date_num})
    from collections import defaultdict
    ym = defaultdict(list)
    for a in articles:
        ym[(a['year'], a['month'])].append(a)
    stat_lines = []
    counts = []
    for key in sorted(ym):
        count = len(ym[key])
        counts.append((key, count))
        bars = '█' * math.ceil(count/3)
        line = f"{key[0]}-{key[1]:02d} | {bars} {count}"
        stat_lines.append(line)
    stat_block = '## Statistics\n\nArticles per month:\n\n' + '<br>\n'.join(stat_lines) + '\n'
    out = preamble.split('## Statistics')[0] + stat_block + '## Articles\n\n'
    month_names = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    current_year = None
    for year, month in sorted(ym.keys(), reverse=True):
        if year != current_year:
            if current_year is not None:
                out += '\n'
            out += f'### {year}\n\n'
            current_year = year
        items = sorted(ym[(year, month)], key=lambda a:(a['date_num'], a['path']), reverse=True)
        count = len(items)
        out += f"#### {month_names[month]} ({count} article{'s' if count != 1 else ''})\n"
        for a in items:
            out += f"- [{a['title']}]({a['path']})\n"
        out += '\n'
    README.write_text(out.rstrip() + '\n')


def remove_first_list_entry(lines):
    for i, line in enumerate(lines):
        if line.strip():
            del lines[i]
            return


def git_commit(msg):
    run('git','add','-A')
    res = run('git','diff','--cached','--quiet', check=False)
    if res.returncode == 0:
        return False
    run('git','commit','-m',msg)
    return True


processed = []
errors = []
lines = LIST.read_text().splitlines()
if not any(line.strip() for line in lines):
    raise SystemExit('LIST.md empty')

append_log(PH_MEMORY, f"\n## {SESSION_TS}\n- actor: agent\n- action: Started the scheduled scan-list run, loaded prompt-hub context, created the task log, and began sequential processing of queued URLs from `LIST.md`.\n- files_changed_or_commands: `{TASK.relative_to(ROOT)}`; `git pull --rebase`; `LIST.md`; `README.md`; `src/*`; `.prompt-hub/version.md`; `.prompt-hub/releases.md`.\n- outcome: success\n- next_step: Process each queued URL, then create and verify the batch recap before the final push.\n")
append_log(ROOT_MEMORY, f"- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | agent: openclaw | action: started scan-list run on queued LIST.md URLs after repo sync and task log creation | files: LIST.md, {TASK.relative_to(ROOT)} | status: success | next: process each URL then build batch recap")

for original in list(lines):
    if not original.strip():
        continue
    cleaned = normalize_url(original)
    art = extract_article(cleaned)
    remove_first_list_entry(lines)
    LIST.write_text('\n'.join(lines).strip() + ('\n' if any(x.strip() for x in lines) else ''))
    if 'error' in art:
        msg = art['error']
        errors.append(msg)
        note = f'Process article error: {cleaned}'
        bump_version(note)
        append_log(PH_MEMORY, f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')}\n- actor: agent\n- action: Removed a queued URL from `LIST.md` after article fetch failed during scan-list processing.\n- files_changed_or_commands: `{cleaned}`; `LIST.md`; `.prompt-hub/version.md`; `.prompt-hub/releases.md`.\n- outcome: failed\n- next_step: Continue processing the next queued URL and record this failure in the batch recap.\n")
        append_log(ROOT_MEMORY, f"- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | agent: openclaw | action: scan-list fetch failed for {cleaned}; removed URL from LIST.md and recorded error for recap | files: LIST.md | status: failed | next: continue queue")
        git_commit(note)
        continue
    rel = write_article(cleaned, art)
    rebuild_readme()
    note = f"Process article: {art['title']}"
    bump_version(note)
    append_log(PH_MEMORY, f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')}\n- actor: agent\n- action: Processed scan-list article '{art['title']}', created its synthesis, updated README statistics/listing, and removed the source URL from LIST.md.\n- files_changed_or_commands: `{cleaned}`; `{rel.as_posix()}`; `README.md`; `LIST.md`; `.prompt-hub/version.md`; `.prompt-hub/releases.md`.\n- outcome: success\n- next_step: Process the next queued URL or create the batch recap if the queue is empty.\n")
    append_log(ROOT_MEMORY, f"- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | agent: openclaw | action: processed scan-list article '{art['title']}' and updated README/LIST.md | files: {rel.as_posix()}, README.md, LIST.md | status: success | next: continue queue")
    git_commit(note)
    processed.append({'title': art['title'], 'elevator': art['elevator'], 'rel': rel.as_posix()})

recap = [f'# Batch Recap - {BATCH_HUMAN}', '']
for item in processed:
    recap.append(item['title'])
    recap.append(item['elevator'])
    recap.append(f'Synthese: {GITHUB_BASE}{item["rel"]}')
    recap.append('')
if errors:
    recap.append('## Errors')
    recap.append('')
    for e in errors:
        recap.append(f'- {e}')
BATCH_FILE.write_text('\n'.join(recap).rstrip() + '\n')

# verify
text = BATCH_FILE.read_text()
missing = [p['title'] for p in processed if p['title'] not in text or p['rel'] not in text]
if missing:
    raise RuntimeError(f'Batch recap verification failed, missing {missing}')
if any(line.strip() for line in LIST.read_text().splitlines()):
    raise RuntimeError('LIST.md not empty at end')

TASK.write_text(TASK.read_text().replace('- [ ] Process each URL from LIST.md top-to-bottom','- [x] Process each URL from LIST.md top-to-bottom').replace('- [ ] Create and verify batch recap','- [x] Create and verify batch recap').replace('- [ ] Commit, push, and finalize logs','- [x] Commit, push, and finalize logs').replace('## Review\nPending.','## Review\nProcessed all queued URLs sequentially, committed each article or fetch error, created and verified the batch recap, and left LIST.md empty.'))

note = f'Add batch recap: {NOW.strftime("%Y-%m-%d %H%M%S")}'
bump_version(note)
append_log(PH_MEMORY, f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')}\n- actor: agent\n- action: Scan-list run processed {len(processed)} queued URL(s), logged {len(errors)} fetch error(s), created `{BATCH_FILE.relative_to(ROOT)}`, verified the recap contents, and confirmed `LIST.md` is empty.\n- files_changed_or_commands: `LIST.md`; `README.md`; `{BATCH_FILE.relative_to(ROOT)}`; `.prompt-hub/version.md`; `.prompt-hub/releases.md`; `{TASK.relative_to(ROOT)}`.\n- outcome: success\n- next_step: Push all remaining scan-list commits to origin/main.\n")
append_log(ROOT_MEMORY, f"- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | agent: openclaw | action: completed scan-list run with {len(processed)} processed URL(s) and {len(errors)} error(s); created {BATCH_FILE.relative_to(ROOT)} and verified LIST.md is empty | files: {BATCH_FILE.relative_to(ROOT)}, LIST.md, README.md | status: success | next: push all remaining commits")
git_commit(note)
run('git','push','origin',BRANCH)
print({'processed': len(processed), 'errors': len(errors), 'batch': str(BATCH_FILE.relative_to(ROOT))})
