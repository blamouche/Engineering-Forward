import json, os, re, subprocess, sys, urllib.parse, html
from pathlib import Path

repo = Path('/Users/openclaw/github/Engineering-Forward')
os.chdir(repo)

def sh(cmd, check=True, capture=True):
    res = subprocess.run(cmd, shell=True, text=True, capture_output=capture)
    if check and res.returncode != 0:
        if res.stdout:
            print(res.stdout)
        if res.stderr:
            print(res.stderr, file=sys.stderr)
        raise SystemExit(res.returncode)
    return res

status = sh('git status --porcelain').stdout.strip()
if status:
    sh('git add -A')
    diff_cached = subprocess.run('git diff --cached --quiet', shell=True)
    if diff_cached.returncode != 0:
        sh('git commit -m "chore: sync pending local changes before veille IA"', capture=False)
        sh('git push origin main', capture=False)
sh('git pull --rebase origin main', capture=False)

queries = ['label:0---veille-ia', 'label:"0 - Veille/IA"']
messages = []
seen_ids = set()
for q in queries:
    res = sh(f"gog gmail messages search {json.dumps(q)} --max 100 --json --include-body --no-input", check=False)
    if res.returncode != 0:
        if res.stdout:
            print(res.stdout)
        if res.stderr:
            print(res.stderr, file=sys.stderr)
        raise SystemExit(res.returncode)
    payload = json.loads(res.stdout or '{}')
    if isinstance(payload, dict):
        data = payload.get('messages') or []
    elif isinstance(payload, list):
        data = payload
    else:
        data = []
    for m in data:
        mid = str(m.get('id') or m.get('messageId') or '')
        if mid and mid not in seen_ids:
            seen_ids.add(mid)
            messages.append(m)

url_re = re.compile(r"https?://[^\s<>()\[\]{}\"'“”]+", re.I)
tracking_params = {
    'utm_source','utm_medium','utm_campaign','utm_term','utm_content','utm_id','utm_name','utm_cid',
    'fbclid','gclid','mc_cid','mc_eid','ref','ref_src','ref_url','source','sr_share','s','si',
    'trk','trkCampaign','trkEmail','mkt_tok','igshid','cmpid','guccounter','guce_referrer','guce_referrer_sig'
}
blocked_hosts = {
    'tldr.tech','a.tldrnewsletter.com','links.tldrnewsletter.com','refer.tldr.tech',
    'every.to','email.mg.every.to','d24ovhgu8s7341.cloudfront.net','substack.com',
    'hub.sparklp.co','kit.com','kit-mail3.com','unsubscribe.kit-mail3.com',
}
blocked_schemes = {'mailto'}
blocked_exact_patterns = ['/subscribe','/unsubscribe','/manage','/preferences','/events','/podcast']
allowed_keywords = [
    'ai','agent','agents','llm','gpt','claude','openai','anthropic','gemini','copilot','cursor',
    'developer','development','engineering','software','programming','code','coding','app','apps',
    'mcp','rag','notebooklm','benchmark','inference','model','models','robotics','database','cloud',
    'api','apis','terminal','cli','security','devtools','productivity'
]
blocked_keywords = [
    'unsubscribe','subscribe','feedback','rating','linkedin.com','x.com/','twitter.com/','instagram.com',
    'facebook.com','youtube.com','podcast','event','conference','jobs.ashbyhq.com','careers','privacy',
    'terms','support','help/','mailto:'
]

def canonicalize(raw):
    raw = html.unescape(raw.strip().strip(').,;\"\''))
    if not raw:
        return None
    parsed = urllib.parse.urlparse(raw)
    if parsed.scheme.lower() in blocked_schemes:
        return None
    if not parsed.scheme.startswith('http'):
        return None
    host = parsed.netloc.lower()
    host_cmp = host[4:] if host.startswith('www.') else host
    if host_cmp in blocked_hosts:
        return None
    path = parsed.path or '/'
    path_lower = path.lower()
    full_lower = raw.lower()
    if any(p in path_lower for p in blocked_exact_patterns):
        return None
    if any(k in full_lower for k in blocked_keywords):
        return None
    q = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    q = [(k, v) for (k, v) in q if k not in tracking_params and not k.startswith('utm_')]
    new = parsed._replace(fragment='', query=urllib.parse.urlencode(q, doseq=True))
    url = urllib.parse.urlunparse(new)
    if url.endswith('/') and path != '/':
        url = url[:-1]
    return url

def is_relevant(url):
    lower = url.lower()
    if any(k in lower for k in blocked_keywords):
        return False
    return any(k in lower for k in allowed_keywords)

extracted = []
for m in messages:
    blobs = []
    for key in ('body','snippet','text','htmlBody','subject'):
        val = m.get(key)
        if isinstance(val, str):
            blobs.append(val)
    blob = '\n'.join(blobs)
    for found in url_re.findall(blob):
        url = canonicalize(found)
        if url and is_relevant(url):
            extracted.append(url)

new_urls = []
seen = set()
for u in extracted:
    if u not in seen:
        seen.add(u)
        new_urls.append(u)

list_path = repo / 'LIST.md'
existing = [line.strip() for line in list_path.read_text().splitlines() if line.strip()] if list_path.exists() else []
clean_existing = []
removed_existing = []
seen2 = set()
for u in existing:
    cu = canonicalize(u) or u.strip()
    if cu and is_relevant(cu) and cu not in seen2:
        clean_existing.append(cu)
        seen2.add(cu)
    elif u.strip():
        removed_existing.append(u.strip())
final = []
seen3 = set()
for u in clean_existing + new_urls:
    if u not in seen3:
        final.append(u)
        seen3.add(u)
list_path.write_text(('\n'.join(final) + '\n') if final else '')

added = [u for u in final if u not in clean_existing]

if messages:
    ids = ' '.join(str(m.get('id') or m.get('messageId')) for m in messages if (m.get('id') or m.get('messageId')))
    if ids:
        sh(f'gog gmail batch modify {ids} --add TRASH --no-input --force', capture=False)

summary = {
    'messages': len(messages),
    'added': len(added),
    'removed': len(removed_existing),
    'final_total': len(final),
    'added_urls': added,
    'removed_urls': removed_existing,
}
Path('/tmp/veille_ia_summary.json').write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
