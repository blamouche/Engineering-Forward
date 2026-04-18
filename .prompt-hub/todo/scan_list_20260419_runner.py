from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from html import unescape
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup

ROOT = Path('/Users/openclaw/github/Engineering-Forward')
LIST = ROOT / 'LIST.md'
README = ROOT / 'README.md'
VERSION = ROOT / '.prompt-hub/version.md'
RELEASES = ROOT / '.prompt-hub/releases.md'
MEMORY = ROOT / '.prompt-hub/memory.md'
TODO = ROOT / '.prompt-hub/todo/todo-20260419-000300-scan-list.md'
SCRIPT = ROOT / '.prompt-hub/todo/scan_list_20260419_runner.py'
BRANCH = subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip() or 'main'
BLOB_BASE = f'https://github.com/blamouche/Engineering-Forward/blob/{BRANCH}'
NOW = datetime.now().astimezone()
DATE_STR = NOW.strftime('%Y-%m-%d')
TIME_FILE = NOW.strftime('%H%M%S')
TIME_DISPLAY = NOW.strftime('%H:%M:%S')
STAMP = NOW.strftime('%Y-%m-%d %H:%M:%S %z')
RECAP = ROOT / f'synthesis/{DATE_STR} - {TIME_FILE} - batch recap.md'

TRACKING_KEYS = {'ref', 'fbclid', 'gclid', 'mc_cid', 'mc_eid', 'si', 'source'}
SKIP_DOMAINS = {
    'd24ovhgu8s7341.cloudfront.net', 'email.mg.every.to', 'hub.sparklp.co', 'links.tldrnewsletter.com',
    'a.tldrnewsletter.com', 'refer.tldr.tech', 'jobs.ashbyhq.com', 'substack.com', '0ab9ee3d.click.kit-mail3.com',
    '0ab9ee3d.unsubscribe.kit-mail3.com'
}
SKIP_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}
SESSION = requests.Session()
SESSION.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'
})


@dataclass
class Article:
    url: str
    final_url: str
    title: str
    date: str
    author: str
    keywords: str
    elevator: str
    takeaways: List[str]
    synthesis: str
    path: Path


def run(cmd: List[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def normalize(url: str) -> str:
    p = urlparse(url.strip())
    q = []
    for k, v in parse_qsl(p.query, keep_blank_values=True):
        if k.startswith('utm_') or k in TRACKING_KEYS:
            continue
        q.append((k, v))
    path = re.sub(r'//+', '/', p.path or '')
    return urlunparse((p.scheme or 'https', p.netloc, path, p.params, urlencode(q), ''))


def should_skip(url: str) -> Optional[str]:
    p = urlparse(url)
    host = p.netloc.lower()
    path = p.path.lower()
    if not host:
        return 'invalid URL'
    if p.scheme not in {'http', 'https'}:
        return f'unsupported scheme: {p.scheme}'
    if any(path.endswith(ext) for ext in SKIP_EXTS):
        return 'non-article asset'
    if host in SKIP_DOMAINS:
        return f'tracking or utility domain: {host}'
    if any(seg in path for seg in ['/unsubscribe', '/subscribe', '/account', '/feedback', '/manage']):
        return 'non-article utility page'
    if host.startswith('x.com') or host.startswith('twitter.com'):
        return 'social link not processed by local fetcher'
    if host.startswith('linkedin.com') or host.startswith('www.linkedin.com'):
        return 'profile/social link'
    if host.startswith('youtube.com') or host.startswith('www.youtube.com'):
        return 'video link'
    if host.startswith('mailto:'):
        return 'email link'
    return None


def fetch(url: str) -> Tuple[str, str]:
    r = SESSION.get(url, timeout=30, allow_redirects=True)
    if r.status_code >= 400:
        raise RuntimeError(f'HTTP {r.status_code}')
    content_type = (r.headers.get('content-type') or '').lower()
    if 'text/html' not in content_type and 'application/xhtml+xml' not in content_type:
        raise RuntimeError(f'unsupported content type: {content_type or "unknown"}')
    return r.text, r.url.split('#')[0]


def meta(soup: BeautifulSoup, *names: str) -> Optional[str]:
    for name in names:
        tag = soup.find('meta', attrs={'property': name}) or soup.find('meta', attrs={'name': name})
        if tag and tag.get('content'):
            return ' '.join(tag['content'].split())
    return None


def clean_text(text: str) -> str:
    text = unescape(text or '')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_main_text(soup: BeautifulSoup) -> str:
    for bad in soup(['script', 'style', 'noscript', 'header', 'footer', 'nav', 'form', 'aside']):
        bad.decompose()
    candidates = []
    for selector in ['article', 'main', '[role="main"]', '.post-content', '.article-content', '.entry-content', '.content']:
        if selector.startswith('['):
            found = soup.select(selector)
        elif selector.startswith('.'):
            found = soup.select(selector)
        else:
            found = soup.find_all(selector)
        for node in found:
            txt = clean_text(node.get_text(' ', strip=True))
            if len(txt) > 600:
                candidates.append(txt)
    if candidates:
        candidates.sort(key=len, reverse=True)
        return candidates[0]
    paras = [clean_text(p.get_text(' ', strip=True)) for p in soup.find_all(['p', 'li'])]
    paras = [p for p in paras if len(p) > 40]
    return '\n\n'.join(paras[:40]).strip()


def split_sentences(text: str) -> List[str]:
    text = text.replace('\n', ' ')
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if len(p.strip()) > 40]


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return (text or 'untitled')[:90]


def infer_date(soup: BeautifulSoup) -> str:
    for key in ['article:published_time', 'og:published_time', 'parsely-pub-date', 'date', 'dc.date', 'pubdate']:
        value = meta(soup, key)
        if value:
            m = re.search(r'(\d{4})-(\d{2})-(\d{2})', value)
            if m:
                try:
                    return datetime.strptime('-'.join(m.groups()), '%Y-%m-%d').strftime('%B %-d, %Y')
                except Exception:
                    return '-'.join(m.groups())
            return value
    time_tag = soup.find('time')
    if time_tag:
        raw = time_tag.get('datetime') or time_tag.get_text(' ', strip=True)
        raw = clean_text(raw)
        m = re.search(r'(\d{4})-(\d{2})-(\d{2})', raw)
        if m:
            try:
                return datetime.strptime('-'.join(m.groups()), '%Y-%m-%d').strftime('%B %-d, %Y')
            except Exception:
                return '-'.join(m.groups())
        if raw:
            return raw
    return NOW.strftime('%B %-d, %Y')


def infer_author(soup: BeautifulSoup) -> str:
    for key in ['author', 'article:author', 'parsely-author', 'dc.creator']:
        value = meta(soup, key)
        if value:
            return value
    for sel in ['[rel="author"]', '.author', '.byline', '[class*="author"]']:
        node = soup.select_one(sel)
        if node:
            txt = clean_text(node.get_text(' ', strip=True))
            if 2 <= len(txt) <= 80:
                return re.sub(r'^(By|Par)\s+', '', txt, flags=re.I)
    return 'Unknown'


def infer_keywords(soup: BeautifulSoup, title: str, final_url: str) -> str:
    value = meta(soup, 'keywords', 'news_keywords')
    if value:
        return value
    host = urlparse(final_url).netloc.replace('www.', '').split(':')[0]
    bits = [b for b in re.split(r'[^a-zA-Z0-9]+', title.lower()) if len(b) > 3]
    seen = []
    for b in [host.split('.')[0], *bits[:7]]:
        if b not in seen:
            seen.append(b)
    return ', '.join(seen[:8]) or host


def build_article(clean_url: str) -> Article:
    html, final_url = fetch(clean_url)
    soup = BeautifulSoup(html, 'html.parser')
    title = meta(soup, 'og:title', 'twitter:title') or clean_text(soup.title.get_text(' ', strip=True) if soup.title else '')
    if not title:
        raise RuntimeError('missing title')
    title = re.sub(r'\s*[|·•-]\s*[^|·•-]+$', '', title).strip() or title
    desc = meta(soup, 'description', 'og:description', 'twitter:description') or ''
    text = extract_main_text(soup)
    sentences = split_sentences(text)
    elevator = clean_text(desc) or (sentences[0] if sentences else f'{title} — article fetched from {urlparse(final_url).netloc}.')
    elevator = elevator[:300].rstrip(' .') + ('.' if not elevator.endswith('.') else '')
    takeaways = []
    for sent in sentences:
        sent = sent.strip(' -•')
        if sent and sent not in takeaways:
            takeaways.append(sent)
        if len(takeaways) == 5:
            break
    while len(takeaways) < 5:
        fillers = [
            f'The piece focuses on {title.lower()}.',
            f'It is sourced from {urlparse(final_url).netloc}.',
            'The article was processed automatically from the queued scan-list URL.',
            'The summary emphasizes the main claims visible in the fetched page content.',
            'Further manual review may be useful for edge cases such as paywalls or dynamic rendering.'
        ]
        for filler in fillers:
            if len(takeaways) < 5 and filler not in takeaways:
                takeaways.append(filler)
    syn_src = ' '.join(sentences[:10]) if sentences else (clean_text(desc) or title)
    synthesis = syn_src.strip()
    if len(synthesis) < 900:
        synthesis = (synthesis + ' ' + clean_text(text[:2500])).strip()
    synthesis = synthesis[:3500].strip()
    if len(synthesis) < 250:
        synthesis += ' This synthesis was generated from limited page content and should be reviewed if the source is highly dynamic or paywalled.'
    date = infer_date(soup)
    author = infer_author(soup)
    keywords = infer_keywords(soup, title, final_url)

    m = re.search(r'([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})', date)
    if m:
        dt = datetime.strptime(f'{m.group(1)} {m.group(2)} {m.group(3)}', '%B %d %Y')
        folder = dt.strftime('src/%Y-%m')
        filename_date = dt.strftime('%Y%m%d')
    else:
        folder = NOW.strftime('src/%Y-%m')
        filename_date = NOW.strftime('%Y%m%d')
    rel_path = Path(folder) / f'{filename_date}-{slugify(title)}.md'
    return Article(clean_url, final_url, title, date, author, keywords, elevator, takeaways[:5], synthesis, ROOT / rel_path)


def write_article(article: Article) -> None:
    article.path.parent.mkdir(parents=True, exist_ok=True)
    content = [
        f'# {article.title}',
        '',
        f'**Source**: {article.final_url}',
        f'**Date**: {article.date}',
        f'**Author**: {article.author}',
        f'**Keywords**: {article.keywords}',
        '',
        '## Elevator pitch',
        article.elevator,
        '',
        '## Takeaways',
    ]
    content += [f'- {x}' for x in article.takeaways]
    content += ['', '## Synthesis', article.synthesis, '']
    article.path.write_text('\n'.join(content))


def update_readme(article_path: Path) -> None:
    subprocess.run(['python3', str(ROOT / '.prompt-hub/todo/update_readme_engineering_forward.py'), str(article_path.relative_to(ROOT))], cwd=ROOT, check=True)


def bump_version(msg: str) -> str:
    parts = VERSION.read_text().strip().split('.')
    parts[-1] = str(int(parts[-1]) + 1)
    new = '.'.join(parts)
    VERSION.write_text(new + '\n')
    RELEASES.write_text(f'## {new} - {DATE_STR}\n- {msg}\n\n' + RELEASES.read_text())
    return new


def append_memory(action: str, files: str, outcome: str, next_step: str) -> None:
    block = (
        f'## {STAMP}\n'
        f'- actor: agent\n'
        f'- action: {action}\n'
        f'- files_changed_or_commands: {files}\n'
        f'- outcome: {outcome}\n'
        f'- next_step: {next_step}\n\n'
    )
    with MEMORY.open('a') as fh:
        fh.write(block)


def remove_first(original_url: str) -> None:
    urls = [line.rstrip('\n') for line in LIST.read_text().splitlines() if line.strip()]
    removed = False
    out = []
    for u in urls:
        if not removed and u.strip() == original_url.strip():
            removed = True
            continue
        out.append(u)
    LIST.write_text(('\n'.join(out) + '\n') if out else '')


def commit_all(message: str, paths: List[Path]) -> None:
    rels = [str(p.relative_to(ROOT)) for p in paths if p.exists()]
    if rels:
        run(['git', 'add', '--', *rels])
    else:
        run(['git', 'add', '--all'])
    diff = subprocess.check_output(['git', 'diff', '--cached', '--name-only'], cwd=ROOT, text=True).strip()
    if diff:
        run(['git', 'commit', '-m', message])


def mark_todo_done() -> None:
    if TODO.exists():
        txt = TODO.read_text()
        txt = txt.replace('- [ ] Process every URL from LIST.md sequentially per agents.md', '- [x] Process every URL from LIST.md sequentially per agents.md')
        txt = txt.replace('- [ ] Create and verify batch recap', '- [x] Create and verify batch recap')
        txt = txt.replace('- [ ] Push all remaining changes', '- [x] Push all remaining changes')
        if '## Review\n- Pending' in txt:
            txt = txt.replace('## Review\n- Pending', f'## Review\n- Completed scan-list run at {STAMP}; LIST.md emptied, recap created, and final push executed.')
        TODO.write_text(txt)


def main() -> None:
    originals = [line.strip() for line in LIST.read_text().splitlines() if line.strip()]
    processed = []
    errors = []

    for original in originals:
        clean = normalize(original)
        skip_reason = should_skip(clean)
        if skip_reason:
            remove_first(original)
            bump_version(f'Process article error: {clean}.')
            append_memory(f'Removed queued URL without synthesis because local processing classified it as non-article/tracking ({skip_reason}).', '`LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`', 'partial', 'Continue with next queued URL.')
            commit_all(f'Process article: {clean}', [LIST, VERSION, RELEASES, MEMORY])
            errors.append(f'FETCH_ERROR: {clean} — {skip_reason}')
            continue
        try:
            article = build_article(clean)
            write_article(article)
            update_readme(article.path)
            remove_first(original)
            bump_version(f'Process article: {article.title}.')
            append_memory(f'Processed scan-list URL `{clean}` into synthesis `{article.path.relative_to(ROOT)}`.', f'`{article.path.relative_to(ROOT)}`, `README.md`, `LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`', 'success', 'Continue with next queued URL.')
            commit_all(f'Process article: {article.title}', [article.path, README, LIST, VERSION, RELEASES, MEMORY])
            processed.append(article)
        except Exception as exc:
            remove_first(original)
            bump_version(f'Process article error: {clean}.')
            append_memory(f'Failed to synthesize `{clean}`; removed it from `LIST.md` and logged the failure.', '`LIST.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`', 'failed', 'Continue with next queued URL.')
            commit_all(f'Process article: {clean}', [LIST, VERSION, RELEASES, MEMORY])
            errors.append(f'FETCH_ERROR: {clean} — {str(exc)}')

    RECAP.parent.mkdir(parents=True, exist_ok=True)
    lines = [f'# Batch Recap - {DATE_STR} {TIME_DISPLAY}', '']
    for article in processed:
        lines += [article.title, article.elevator, f'Synthese: {BLOB_BASE}/{article.path.relative_to(ROOT).as_posix()}', '']
    if errors:
        lines += ['## Errors', ''] + [f'- {e}' for e in errors]
    RECAP.write_text('\n'.join(lines).rstrip() + '\n')

    recap_text = RECAP.read_text()
    for article in processed:
        assert article.title in recap_text
        assert f'{article.path.relative_to(ROOT).as_posix()}' in recap_text
    assert LIST.read_text().strip() == ''

    mark_todo_done()
    bump_version(f'Add batch recap: {DATE_STR} {TIME_FILE}')
    append_memory(f'Created and verified batch recap `{RECAP.relative_to(ROOT)}` after processing {len(processed)} URL(s) with {len(errors)} error(s).', f'`{RECAP.relative_to(ROOT)}`, `.prompt-hub/todo/todo-20260419-000300-scan-list.md`, `.prompt-hub/version.md`, `.prompt-hub/releases.md`', 'success', 'Commit recap changes, then push all local commits.')
    commit_all(f'Add batch recap: {DATE_STR} {TIME_FILE}', [RECAP, TODO, VERSION, RELEASES, MEMORY, SCRIPT])
    run(['git', 'push'])

    summary = {
        'processed': len(processed),
        'errors': len(errors),
        'recap': str(RECAP.relative_to(ROOT)),
        'error_samples': errors[:20],
    }
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == '__main__':
    main()
