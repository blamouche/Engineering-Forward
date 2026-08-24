#!/usr/bin/env python3
"""
Static site generator for Engineering-Forward veille.
Pure Python stdlib — no Node, no pip, no external dependencies.
Reads markdown articles from ../src/, generates HTML pages in dist/.
"""

import os
import re
import html
import glob
import json
import hashlib
from datetime import datetime, date, timedelta
from collections import defaultdict, OrderedDict, Counter
from html import escape

# ─── Paths ───────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)
SRC_DIR = os.path.join(REPO_DIR, "src")
DIST_DIR = SCRIPT_DIR  # Output directly to docs/ for GitHub Pages
TEMPLATE_DIR = os.path.join(SCRIPT_DIR, "templates")

# ─── Config ───────────────────────────────────────────────────────────────────
SITE_TITLE = "Engineering Forward"
SITE_SUBTITLE = "Veille ingénierie et software"
SITE_URL = "https://engineeringforward.fr"
SITE_DESCRIPTION = "Synthèses quotidiennes d'articles sur l'ingénierie logicielle, l'AI, le engineering management et le future of work"
SITE_LANG = "en"
SITE_AUTHOR = "Benoit Lamouche"
ARTICLES_PER_PAGE = 25

def plural(n, word):
    """English pluralization helper: plural(1, 'article') -> '1 article'."""
    return f"{n} {word}" if n == 1 else f"{n} {word}s"

# ─── Markdown parsing ─────────────────────────────────────────────────────────

def parse_article(filepath):
    """Parse a markdown article file into a dict."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    data = {
        "filepath": filepath,
        "filename": os.path.basename(filepath),
        "title": "",
        "source": "",
        "date": "",
        "author": "",
        "keywords": "",
        "elevator_pitch": "",
        "takeaways": [],
        "synthesis": "",
        "raw": content,
    }

    # Extract title (first # heading)
    m = re.match(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        data["title"] = m.group(1).strip()

    # Extract metadata fields (**Source**: ..., **Date**: ..., etc.)
    for field in ["Source", "Date", "Author", "Keywords"]:
        m = re.search(rf"\*\*{field}\*\*:\s*(.+)$", content, re.MULTILINE)
        if m:
            val = m.group(1).strip()
            key = field.lower()
            if key == "source":
                data["source"] = val
            elif key == "date":
                data["date"] = val
            elif key == "author":
                data["author"] = val
            elif key == "keywords":
                data["keywords"] = val

    # Extract elevator pitch
    m = re.search(r"##\s*Elevator pitch\s*\n(.+?)(?=\n##|\Z)", content, re.DOTALL)
    if m:
        data["elevator_pitch"] = m.group(1).strip()

    # Extract takeaways
    m = re.search(r"##\s*Takeaways\s*\n(.+?)(?=\n##|\Z)", content, re.DOTALL)
    if m:
        takeaway_block = m.group(1).strip()
        data["takeaways"] = [
            line.lstrip("- ").strip()
            for line in takeaway_block.split("\n")
            if line.strip().startswith("-")
        ]

    # Extract synthesis
    m = re.search(r"##\s*Synthesis\s*\n(.+?)(?=\n##|\Z)", content, re.DOTALL)
    if m:
        data["synthesis"] = m.group(1).strip()

    # Extract date from filename if not in metadata: YYYYMMDD-slug.md
    fname = os.path.basename(filepath)
    m = re.match(r"(\d{4})(\d{2})(\d{2})-", fname)
    if m:
        data["date_sort"] = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        data["year"] = m.group(1)
        data["month"] = m.group(2)
        data["day"] = m.group(3)
    else:
        data["date_sort"] = data["date"] or "unknown"
        data["year"] = ""
        data["month"] = ""
        data["day"] = ""

    # Generate slug and URL path (relative to site root, no leading slash —
    # keeps the site browsable both via a web server and directly via file://)
    slug = fname.replace(".md", "")
    data["slug"] = slug
    if data["year"] and data["month"]:
        data["url"] = f"articles/{data['year']}-{data['month']}/{slug}.html"
    else:
        data["url"] = f"articles/{slug}.html"

    return data


def load_all_articles():
    """Load all articles from src/ directory, sorted by date descending."""
    articles = []
    for filepath in glob.glob(os.path.join(SRC_DIR, "**", "*.md"), recursive=True):
        try:
            data = parse_article(filepath)
            articles.append(data)
        except Exception as e:
            print(f"WARNING: Failed to parse {filepath}: {e}")
    articles.sort(key=lambda a: a["date_sort"], reverse=True)
    return articles


# ─── HTML helpers ─────────────────────────────────────────────────────────────

def md_to_html(text):
    """Minimal markdown to HTML: paragraphs, bold, italic, links, lists."""
    if not text:
        return ""
    lines = text.split("\n")
    html_lines = []
    in_list = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("")
            continue
        if stripped.startswith("- "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            item = stripped[2:]
            item = inline_md(item)
            html_lines.append(f"<li>{item}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<p>{inline_md(stripped)}</p>")
    if in_list:
        html_lines.append("</ul>")
    return "\n".join(html_lines)


def inline_md(text):
    """Convert inline markdown (bold, italic, links) to HTML."""
    # Links [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    # Bold **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic *text* (but not ** which is bold)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    # Escape remaining HTML
    # (we escape after, so links/bold tags survive)
    return text


def page_html(title, body, nav_active="", base=""):
    """Wrap content in full HTML page with CSS.

    `base` is the relative path prefix back to the site root (e.g. "" at the
    root, "../../" from articles/YYYY-MM/*.html). Using relative links
    throughout means the generated site works both served by a web server
    and opened directly via file://.
    """
    nav = f"""
<nav class="navbar">
    <div class="nav-brand">
        <a href="{base}index.html">{SITE_TITLE}</a>
    </div>
    <div class="nav-search">
        <input type="search" id="site-search" placeholder="Search articles…" autocomplete="off" aria-label="Search articles">
        <div id="search-results" class="search-results" hidden></div>
    </div>
    <div class="nav-links">
        <a href="{base}index.html" class="{ 'active' if nav_active == 'home' else '' }">Home</a>
        <a href="{base}archives.html" class="{ 'active' if nav_active == 'archives' else '' }">Archives</a>
        <a href="{base}feed.xml" class="{ 'active' if nav_active == 'rss' else '' }">RSS</a>
        <a href="https://engineeringforward.substack.com" target="_blank" rel="noopener">Substack</a>
        <a href="https://engineeringforward.substack.com/subscribe" target="_blank" rel="noopener" class="subscribe-btn">Subscribe</a>
    </div>
</nav>"""
    return f"""<!DOCTYPE html>
<html lang="{SITE_LANG}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(title)} — {SITE_TITLE}</title>
    <meta name="description" content="{escape(SITE_DESCRIPTION)}">
    <link rel="alternate" type="application/rss+xml" title="{SITE_TITLE}" href="{base}feed.xml">
    <link rel="stylesheet" href="{base}style.css">
    <script>window.SITE_BASE = "{base}";</script>
    <script src="{base}search.js" defer></script>
</head>
<body>
{nav}
<main>
{body}
</main>
<footer class="site-footer">
    <p>{SITE_TITLE} — {SITE_SUBTITLE}</p>
</footer>
</body>
</html>"""


# ─── Page generators ──────────────────────────────────────────────────────────

MONTH_NAMES_EN = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
MONTH_ABBR_EN = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}
DAY_NAMES_EN = {
    0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
    4: "Friday", 5: "Saturday", 6: "Sunday"
}


def generate_heatmap(articles):
    """Generate a GitHub-style contribution heatmap (articles per day, last 12 months).

    Pure HTML/CSS grid, no JavaScript — cell tooltips use the native `title`
    attribute, consistent with the rest of the site.
    """
    counts = Counter()
    for a in articles:
        if re.match(r"\d{4}-\d{2}-\d{2}", a["date_sort"]):
            counts[a["date_sort"]] += 1

    today = date.today()
    # Align the grid to full weeks (Sunday -> Saturday) covering the trailing year
    range_start = today - timedelta(days=364)
    range_start -= timedelta(days=(range_start.weekday() + 1) % 7)  # back up to Sunday
    range_end = today + timedelta(days=(5 - today.weekday()) % 7)  # forward to Saturday

    total_days = (range_end - range_start).days + 1
    weeks = total_days // 7

    def level_for(n):
        if n <= 0:
            return 0
        if n <= 2:
            return 1
        if n <= 4:
            return 2
        if n <= 7:
            return 3
        return 4

    month_cols = []  # (week_index, month_abbr)
    last_month = None
    cells = []
    for w in range(weeks):
        week_start = range_start + timedelta(days=w * 7)
        if week_start.month != last_month:
            month_cols.append((w, MONTH_ABBR_EN[week_start.month]))
            last_month = week_start.month
        for d_offset in range(7):
            cur = range_start + timedelta(days=w * 7 + d_offset)
            if cur > today:
                cells.append('<span class="heatmap-cell is-future" aria-hidden="true"></span>')
                continue
            n = counts.get(cur.isoformat(), 0)
            label = f"{plural(n, 'article')} on {DAY_NAMES_EN[cur.weekday()]}, {MONTH_NAMES_EN[cur.month]} {cur.day}, {cur.year}"
            cells.append(f'<span class="heatmap-cell level-{level_for(n)}" title="{escape(label)}" aria-label="{escape(label)}" role="img"></span>')

    month_labels_html = "".join(
        f'<span style="grid-column: {w + 1};">{name}</span>' for w, name in month_cols
    )

    return f"""
<section class="heatmap-section">
    <h2 class="heatmap-title">Activity over the last 12 months</h2>
    <div class="heatmap-scroll">
        <div class="heatmap" style="--weeks: {weeks};">
            <div class="heatmap-months">{month_labels_html}</div>
            <div class="heatmap-body">
                <div class="heatmap-daylabels">
                    <span></span><span>Mon</span><span></span><span>Wed</span><span></span><span>Fri</span><span></span>
                </div>
                <div class="heatmap-grid">{"".join(cells)}</div>
            </div>
        </div>
    </div>
    <div class="heatmap-legend">
        <span>Less</span>
        <span class="heatmap-cell level-0"></span>
        <span class="heatmap-cell level-1"></span>
        <span class="heatmap-cell level-2"></span>
        <span class="heatmap-cell level-3"></span>
        <span class="heatmap-cell level-4"></span>
        <span>More</span>
    </div>
</section>"""


def generate_index(articles):
    """Generate homepage with daily synthesis + recent articles."""
    # Group by date
    by_date = defaultdict(list)
    for a in articles:
        d = a["date_sort"]
        if re.match(r"\d{4}-\d{2}-\d{2}", d):
            by_date[d].append(a)

    # Sort dates descending
    sorted_dates = sorted(by_date.keys(), reverse=True)

    body_parts = []
    body_parts.append(f"""
<header class="hero">
    <h1>{SITE_TITLE}</h1>
    <p class="subtitle">{SITE_SUBTITLE}</p>
    <p class="stats">{plural(len(articles), 'article')} · {plural(len(sorted_dates), 'day')} of watch</p>
</header>""")

    body_parts.append(generate_heatmap(articles))

    # Daily synthesis sections (show last 7 days with content)
    days_shown = 0
    max_days = 7
    for dt in sorted_dates:
        if days_shown >= max_days:
            break
        day_articles = by_date[dt]
        # Format date nicely
        try:
            d = datetime.strptime(dt, "%Y-%m-%d")
            date_en = f"{DAY_NAMES_EN[d.weekday()]}, {MONTH_NAMES_EN[d.month]} {d.day}, {d.year}"
        except:
            date_en = dt

        day_id = dt.replace("-", "")
        body_parts.append(f"""
<section class="daily-synthesis" id="day-{day_id}">
    <h2 class="day-header">
        <time datetime="{dt}">{date_en}</time>
        <span class="article-count">{plural(len(day_articles), 'article')}</span>
    </h2>
    <div class="day-articles">""")

        for a in day_articles:
            takeaways_html = ""
            if a["takeaways"]:
                takeaways_html = f'<details class="takeaways"><summary>Key takeaways</summary><ul>{"".join(f"<li>{escape(t)}</li>" for t in a["takeaways"])}</ul></details>'

            source_link = ""
            if a["source"]:
                source_link = f'<a href="{escape(a["source"])}" target="_blank" rel="noopener" class="source-link">Source article</a>'

            body_parts.append(f"""
        <article class="article-card">
            <h3><a href="{a["url"]}">{escape(a["title"])}</a></h3>
            <p class="elevator-pitch">{escape(a["elevator_pitch"])}</p>
            {takeaways_html}
            <div class="article-meta">
                <span class="meta-date">{escape(a["date"])}</span>
                {f'<span class="meta-author">{escape(a["author"])}</span>' if a["author"] and a["author"] != "Unknown" else ''}
                {source_link}
            </div>
        </article>""")

        body_parts.append("""
    </div>
</section>""")
        days_shown += 1

    # Link to archives
    body_parts.append("""
<div class="archives-link">
    <a href="archives.html" class="btn">View all archives →</a>
</div>""")

    return page_html("Home", "\n".join(body_parts), nav_active="home")


def generate_article_page(article):
    """Generate individual article page (fiche de récap)."""
    # Articles live two levels deep (articles/YYYY-MM/slug.html) unless the
    # date couldn't be parsed from the filename, in which case they sit one
    # level deep (articles/slug.html).
    base = "../../" if (article["year"] and article["month"]) else "../"

    body_parts = []
    body_parts.append(f"""
<article class="article-full">
    <a href="{base}index.html" class="back-link">← Back home</a>
    <h1>{escape(article["title"])}</h1>
    <div class="article-meta-full">
        <span class="meta-date">{escape(article["date"])}</span>
        {f'<span class="meta-author">{escape(article["author"])}</span>' if article["author"] and article["author"] != "Unknown" else ''}
        {f'<span class="meta-keywords">{escape(article["keywords"])}</span>' if article["keywords"] and article["keywords"] != "Unknown" else ''}
    </div>""")

    if article["source"]:
        body_parts.append(f"""
    <a href="{escape(article["source"])}" target="_blank" rel="noopener" class="source-link-full">
        Read the source article
    </a>""")

    if article["elevator_pitch"]:
        body_parts.append(f"""
    <section class="elevator-pitch-section">
        <h2>Quick summary</h2>
        <p class="elevator-pitch">{escape(article["elevator_pitch"])}</p>
    </section>""")

    if article["takeaways"]:
        body_parts.append("""
    <section class="takeaways-section">
        <h2>Key takeaways</h2>
        <ul class="takeaways-list">""")
        for t in article["takeaways"]:
            body_parts.append(f"            <li>{escape(t)}</li>")
        body_parts.append("""        </ul>
    </section>""")

    if article["source"]:
        body_parts.append(f"""
    <a href="{escape(article["source"])}" target="_blank" rel="noopener" class="source-link-full">
        Read the full article on the source site
    </a>""")

    body_parts.append("""
</article>""")

    return page_html(article["title"], "\n".join(body_parts), base=base)


def generate_archives(articles):
    """Generate archives page grouped by year/month."""
    # Group by year-month
    by_month = defaultdict(list)
    for a in articles:
        if a["year"] and a["month"]:
            key = f"{a['year']}-{a['month']}"
            by_month[key].append(a)

    sorted_months = sorted(by_month.keys(), reverse=True)

    body_parts = []
    body_parts.append("""
<header class="page-header">
    <h1>Archives</h1>
    <p>All articles from the engineering watch</p>
</header>""")

    current_year = ""
    for ym in sorted_months:
        year, month = ym.split("-")
        if year != current_year:
            if current_year:
                body_parts.append("</div>")
            current_year = year
            body_parts.append(f"""
<div class="archive-year">
    <h2>{year}</h2>""")

        month_name = MONTH_NAMES_EN.get(int(month), month)
        month_articles = by_month[ym]

        body_parts.append(f"""
    <div class="archive-month">
        <h3>{month_name} ({plural(len(month_articles), 'article')})</h3>
        <ul class="archive-list">""")

        for a in month_articles:
            body_parts.append(f"""
            <li>
                <a href="{a["url"]}">{escape(a["title"])}</a>
                <span class="archive-date">{escape(a["date"])}</span>
            </li>""")

        body_parts.append("""
        </ul>
    </div>""")

    if current_year:
        body_parts.append("</div>")

    return page_html("Archives", "\n".join(body_parts), nav_active="archives")


def generate_rss(articles):
    """Generate RSS 2.0 feed."""
    parts = [f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>{escape(SITE_TITLE)}</title>
    <link>{SITE_URL}</link>
    <description>{escape(SITE_DESCRIPTION)}</description>
    <language>{SITE_LANG}</language>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
    <lastBuildDate>{datetime.now(tz=__import__('datetime').timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>"""]

    # Include last 50 articles
    for a in articles[:50]:
        title = escape(a["title"])
        link = f"{SITE_URL}/{a['url']}"
        desc_parts = []
        if a["elevator_pitch"]:
            desc_parts.append(a["elevator_pitch"])
        if a["takeaways"]:
            desc_parts.append("Key takeaways: " + " ; ".join(a["takeaways"]))
        if a["synthesis"]:
            # First 300 chars of synthesis
            desc_parts.append(a["synthesis"][:300] + "..." if len(a["synthesis"]) > 300 else a["synthesis"])
        description = " — ".join(desc_parts[:2]) if desc_parts else a["title"]
        description = escape(description)

        pub_date = ""
        if re.match(r"\d{4}-\d{2}-\d{2}", a["date_sort"]):
            try:
                d = datetime.strptime(a["date_sort"], "%Y-%m-%d")
                pub_date = d.strftime("%a, %d %b %Y %H:%M:%S +0000")
            except:
                pub_date = datetime.now(tz=__import__('datetime').timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
        else:
            pub_date = datetime.now(tz=__import__('datetime').timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

        parts.append(f"""
    <item>
        <title>{title}</title>
        <link>{link}</link>
        <guid isPermaLink="true">{link}</guid>
        <description>{description}</description>
        <pubDate>{pub_date}</pubDate>
    </item>""")

    parts.append("""
</channel>
</rss>""")
    return "\n".join(parts)


# ─── CSS ──────────────────────────────────────────────────────────────────────

CSS = """/* Engineering Forward — Static site stylesheet
   Sober and professional: flat surfaces, thin borders, one restrained accent.
   No gradients, no decorative shadows, no emoji glyphs in UI text. */
:root {
    --bg: #101316;
    --bg-card: #171b21;
    --bg-hover: #1d2229;
    --text: #dde3ea;
    --text-muted: #8b95a3;
    --accent: #5e86c2;
    --accent-hover: #7199d0;
    --border: #262c35;
    --border-soft: #1f252d;
    --radius: 4px;
    --max-width: 860px;
    --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}
@media (prefers-color-scheme: light) {
    :root {
        --bg: #f7f8f9;
        --bg-card: #ffffff;
        --bg-hover: #eef1f4;
        --text: #1f242b;
        --text-muted: #5f6873;
        --accent: #20568f;
        --accent-hover: #1a4573;
        --border: #d9dfe6;
        --border-soft: #e5eaf0;
    }
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: var(--font-sans);
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    font-size: 16px;
}
a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--accent-hover); text-decoration: underline; }
::selection { background: var(--accent); color: #fff; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
h1, h2, h3 { line-height: 1.3; font-weight: 700; }

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.85rem 2rem;
    background: var(--bg-card);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
}
.nav-brand a {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text);
}
.nav-brand a:hover { text-decoration: none; color: var(--text); }
.nav-links { display: flex; gap: 1.4rem; }
.nav-links a {
    color: var(--text-muted);
    font-size: 0.92rem;
    font-weight: 500;
    padding-bottom: 2px;
    border-bottom: 2px solid transparent;
}
.nav-links a:hover, .nav-links a.active {
    color: var(--text);
    text-decoration: none;
    border-bottom-color: var(--accent);
}
.nav-links a.subscribe-btn {
    background: var(--accent);
    color: var(--bg);
    padding: 0.3rem 0.9rem;
    border-radius: 6px;
    font-weight: 600;
    text-decoration: none;
    border-bottom: none;
    transition: opacity 0.2s;
}
.nav-links a.subscribe-btn:hover {
    opacity: 0.85;
    color: var(--bg);
    border-bottom: none;
}
.nav-search { position: relative; }
#site-search {
    width: 190px;
    padding: 0.4rem 0.7rem;
    font-size: 0.9rem;
    font-family: var(--font-sans);
    color: var(--text);
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    outline: none;
}
#site-search::placeholder { color: var(--text-muted); }
#site-search:focus { border-color: var(--accent); }
.search-results {
    position: absolute;
    top: calc(100% + 6px);
    right: 0;
    min-width: 320px;
    max-width: 420px;
    max-height: 60vh;
    overflow-y: auto;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    z-index: 200;
}
.search-results a {
    display: block;
    padding: 0.55rem 0.8rem;
    color: var(--text);
    font-size: 0.9rem;
    line-height: 1.35;
    border-bottom: 1px solid var(--border-soft);
}
.search-results a:last-child { border-bottom: none; }
.search-results a:hover { background: var(--bg-hover); text-decoration: none; }
.search-results .search-date {
    display: block;
    color: var(--text-muted);
    font-size: 0.78rem;
    margin-top: 0.15rem;
}
.search-results .search-empty {
    padding: 0.7rem 0.8rem;
    color: var(--text-muted);
    font-size: 0.9rem;
}

/* Main */
main {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 2rem 1.25rem 4rem;
}

/* Hero */
.hero { text-align: center; padding: 3rem 1rem 2rem; }
.hero h1 { font-size: 2.1rem; margin-bottom: 0.6rem; font-weight: 700; }
.subtitle { color: var(--text-muted); font-size: 1.05rem; }
.stats {
    color: var(--text-muted);
    font-size: 0.88rem;
    margin-top: 0.9rem;
    display: inline-flex;
    gap: 0.5rem;
    align-items: center;
    flex-wrap: wrap;
    justify-content: center;
}
.stats::before, .stats::after { content: ""; }

/* Activity heatmap */
.heatmap-section {
    margin: 0 0 3rem;
    padding: 1.2rem 1.25rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
}
.heatmap-title {
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-muted);
    margin-bottom: 1rem;
    text-align: center;
}
.heatmap-scroll { overflow-x: auto; padding-bottom: 0.25rem; }
.heatmap { display: flex; flex-direction: column; gap: 0.3rem; width: 100%; --hcg: 3px; }
.heatmap-months {
    display: grid;
    grid-template-columns: repeat(var(--weeks), minmax(0, 1fr));
    gap: var(--hcg);
    margin-left: 28px;
    font-size: 0.7rem;
    color: var(--text-muted);
}
.heatmap-body { display: flex; gap: 4px; align-items: stretch; }
.heatmap-daylabels {
    display: grid;
    grid-template-rows: repeat(7, 1fr);
    gap: var(--hcg);
    width: 24px;
    font-size: 0.65rem;
    color: var(--text-muted);
    text-align: right;
    line-height: 1;
}
.heatmap-grid {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(var(--weeks), minmax(0, 1fr));
    grid-template-rows: repeat(7, auto);
    grid-auto-flow: column;
    gap: var(--hcg);
}
.heatmap-cell {
    width: 100%;
    aspect-ratio: 1 / 1;
    border-radius: 2px;
    border: 1px solid var(--border-soft);
    background: var(--bg-hover);
}
.heatmap-cell.level-1 { background: color-mix(in srgb, var(--accent) 28%, var(--bg-card)); border-color: transparent; }
.heatmap-cell.level-2 { background: color-mix(in srgb, var(--accent) 52%, var(--bg-card)); border-color: transparent; }
.heatmap-cell.level-3 { background: color-mix(in srgb, var(--accent) 76%, var(--bg-card)); border-color: transparent; }
.heatmap-cell.level-4 { background: var(--accent); border-color: transparent; }
.heatmap-cell.is-future { background: transparent; border-color: transparent; }
.heatmap-legend {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.35rem;
    margin-top: 0.8rem;
    font-size: 0.75rem;
    color: var(--text-muted);
}
.heatmap-legend .heatmap-cell { width: 11px; height: 11px; }

/* Daily synthesis */
.daily-synthesis {
    margin-bottom: 2.5rem;
    border-bottom: 1px solid var(--border-soft);
    padding-bottom: 2rem;
}
.day-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 1.25rem;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.day-header h2 { font-size: 1.25rem; font-weight: 700; }
.day-header h2 time { color: var(--text); }
.article-count {
    color: var(--text-muted);
    font-size: 0.85rem;
    font-weight: 500;
    white-space: nowrap;
}

/* Article card */
.article-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem 1.35rem;
    margin-bottom: 0.75rem;
}
.article-card:hover { border-color: var(--accent); }
.article-card h3 { margin-bottom: 0.45rem; font-size: 1.05rem; font-weight: 600; }
.article-card h3 a { color: var(--text); }
.article-card h3 a:hover { color: var(--accent); text-decoration: none; }
.elevator-pitch { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 0.7rem; }
.article-meta {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    align-items: center;
    font-size: 0.82rem;
    color: var(--text-muted);
}
.article-meta .meta-date { font-variant-numeric: tabular-nums; }
.source-link { font-weight: 600; }
.source-link::before { content: "↗ "; }

/* Takeaways (inline) */
details.takeaways {
    margin: 0.75rem 0;
    font-size: 0.9rem;
    padding: 0.55rem 0.8rem;
    background: var(--bg-hover);
    border-radius: var(--radius);
    border: 1px solid var(--border-soft);
}
details.takeaways summary {
    cursor: pointer;
    color: var(--accent);
    font-weight: 600;
    list-style: none;
}
details.takeaways summary::-webkit-details-marker { display: none; }
details.takeaways summary::before { content: "▸ "; transition: transform 0.15s ease; display: inline-block; }
details.takeaways[open] summary::before { transform: rotate(90deg); }
details.takeaways ul { margin-top: 0.5rem; padding-left: 1.3rem; }
details.takeaways li { color: var(--text-muted); margin-bottom: 0.3rem; }

/* Article full page */
.article-full { padding: 1rem 0; }
.back-link {
    display: inline-block;
    margin-bottom: 1.4rem;
    font-size: 0.88rem;
    color: var(--text-muted);
}
.back-link:hover { color: var(--accent); }
.article-full h1 {
    font-size: 1.9rem;
    margin-bottom: 0.9rem;
    line-height: 1.25;
    font-weight: 700;
}
.article-meta-full {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    color: var(--text-muted);
    font-size: 0.88rem;
    margin-bottom: 1.4rem;
}
.source-link-full {
    display: inline-block;
    background: var(--accent);
    color: #fff !important;
    padding: 0.6rem 1.4rem;
    border-radius: var(--radius);
    font-weight: 600;
    margin: 0.9rem 0 1.8rem;
}
.source-link-full:hover { background: var(--accent-hover); text-decoration: none; }

.elevator-pitch-section, .takeaways-section, .synthesis-section { margin-bottom: 2rem; }
.elevator-pitch-section h2, .takeaways-section h2, .synthesis-section h2 {
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 0.9rem;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid var(--border);
}
.elevator-pitch-section .elevator-pitch {
    font-size: 1.1rem;
    color: var(--text);
    font-style: italic;
    line-height: 1.6;
    padding: 0.2rem 0;
}
.takeaways-list { padding-left: 1.3rem; }
.takeaways-list li { margin-bottom: 0.5rem; line-height: 1.55; }
.takeaways-list li::marker { color: var(--accent); }
.synthesis-content p { margin-bottom: 1.1rem; }
.synthesis-content ul { padding-left: 1.5rem; margin-bottom: 1.1rem; }
.synthesis-content li { margin-bottom: 0.4rem; }
.synthesis-content strong { color: var(--text); }

/* Archives */
.page-header { text-align: center; padding: 2.5rem 0 2.5rem; }
.page-header h1 { font-size: 1.9rem; font-weight: 700; }
.page-header p { color: var(--text-muted); margin-top: 0.5rem; font-size: 1rem; }
.archive-year { margin-bottom: 2.5rem; }
.archive-year h2 { font-size: 1.4rem; margin-bottom: 0.9rem; font-weight: 700; }
.archive-month {
    margin-bottom: 1.2rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0.9rem 1.1rem;
}
.archive-month h3 {
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
    color: var(--text-muted);
    font-weight: 600;
}
.archive-list { list-style: none; }
.archive-list li {
    padding: 0.5rem 0;
    border-bottom: 1px solid var(--border-soft);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
}
.archive-list li:last-child { border-bottom: none; }
.archive-list li a { flex: 1; color: var(--text); }
.archive-list li a:hover { color: var(--accent); text-decoration: none; }
.archive-date {
    color: var(--text-muted);
    font-size: 0.82rem;
    white-space: nowrap;
    font-variant-numeric: tabular-nums;
}

/* Buttons */
.btn {
    display: inline-block;
    background: var(--accent);
    color: #fff !important;
    padding: 0.65rem 1.6rem;
    border-radius: var(--radius);
    font-weight: 600;
}
.btn:hover { background: var(--accent-hover); text-decoration: none; }
.archives-link { text-align: center; margin: 3rem 0 1rem; }

/* Footer */
.site-footer {
    text-align: center;
    padding: 2rem 2rem;
    border-top: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 0.83rem;
}
.site-footer p { margin: 0.25rem 0; }
.site-footer a { color: var(--accent); font-weight: 500; }

/* Responsive */
@media (max-width: 768px) {
    .navbar { flex-direction: column; gap: 0.6rem; padding: 1rem; }
    .nav-links { gap: 1.1rem; flex-wrap: wrap; justify-content: center; }
    .nav-search { width: 100%; }
    #site-search { width: 100%; }
    .search-results { left: 0; right: 0; min-width: 0; max-width: none; }
    .hero { padding: 2.2rem 1rem 1.5rem; }
    .hero h1 { font-size: 1.6rem; }
    .day-header { flex-direction: column; align-items: flex-start; gap: 0.35rem; }
    .article-card { padding: 1.05rem; }
    .article-full h1 { font-size: 1.45rem; }
    .archive-list li { flex-direction: column; align-items: flex-start; gap: 0.2rem; }
    .heatmap-scroll { margin: 0 -1.25rem; padding: 0 1.25rem 0.25rem; }
    .heatmap { --hcg: 2px; }
    .heatmap-section { padding: 1rem 0.6rem; }
}
@media (max-width: 560px) {
    .heatmap { --hcg: 1px; }
}
@media (prefers-reduced-motion: reduce) {
    * { transition: none !important; }
}"""


# ─── Main build ───────────────────────────────────────────────────────────────

def main():
    print("Loading articles...")
    articles = load_all_articles()
    print(f"  Found {len(articles)} articles")

    # Clean generated files (preserve build_site.py, README.md, .gitignore)
    import shutil
    preserve = {"build_site.py", "README.md", ".gitignore", "__pycache__"}
    if os.path.exists(DIST_DIR):
        for item in os.listdir(DIST_DIR):
            if item in preserve:
                continue
            item_path = os.path.join(DIST_DIR, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

    # Write CSS
    with open(os.path.join(DIST_DIR, "style.css"), "w") as f:
        f.write(CSS)
    print("  ✓ style.css")

    # Generate index.html
    index_html = generate_index(articles)
    with open(os.path.join(DIST_DIR, "index.html"), "w") as f:
        f.write(index_html)
    print("  ✓ index.html")

    # Generate article pages
    articles_dir = os.path.join(DIST_DIR, "articles")
    os.makedirs(articles_dir)
    for a in articles:
        # Create year-month subdirectory
        if a["year"] and a["month"]:
            subdir = os.path.join(articles_dir, f"{a['year']}-{a['month']}")
        else:
            subdir = articles_dir
        os.makedirs(subdir, exist_ok=True)
        html_path = os.path.join(subdir, f"{a['slug']}.html")
        with open(html_path, "w") as f:
            f.write(generate_article_page(a))
    print(f"  ✓ {len(articles)} article pages")

    # Generate archives.html
    archives_html = generate_archives(articles)
    with open(os.path.join(DIST_DIR, "archives.html"), "w") as f:
        f.write(archives_html)
    print("  ✓ archives.html")

    # Generate RSS feed
    rss = generate_rss(articles)
    with open(os.path.join(DIST_DIR, "feed.xml"), "w") as f:
        f.write(rss)
    print("  ✓ feed.xml")

    # Generate a JSON manifest (useful for integrations)
    manifest = {
        "site": SITE_TITLE,
        "url": SITE_URL,
        "generated": datetime.now().isoformat(),
        "article_count": len(articles),
        "articles": [
            {
                "title": a["title"],
                "url": f"{SITE_URL}/{a['url']}",
                "date": a["date"],
                "source": a["source"],
                "author": a["author"],
                "keywords": a["keywords"],
                "elevator_pitch": a["elevator_pitch"],
            }
            for a in articles
        ],
    }
    with open(os.path.join(DIST_DIR, "manifest.json"), "w") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("  ✓ manifest.json")

    # Generate a lean search index (relative URLs so it works on any host)
    search_index = [
        {
            "title": a["title"],
            "url": a["url"],
            "date": a["date"],
            "keywords": a["keywords"],
            "elevator_pitch": a["elevator_pitch"],
        }
        for a in articles
    ]
    with open(os.path.join(DIST_DIR, "search-index.json"), "w") as f:
        json.dump(search_index, f, ensure_ascii=False)
    print("  ✓ search-index.json")

    # Client-side search (vanilla JS, no dependencies)
    search_js = r"""/* Site search: filters search-index.json as you type. */
(function () {
    var input = document.getElementById("site-search");
    if (!input) return;
    var results = document.getElementById("search-results");
    var index = null;
    var base = window.SITE_BASE || "";

    fetch(base + "search-index.json")
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (data) { index = data; })
        .catch(function () { input.hidden = true; });

    function matches(article, tokens) {
        var hay = (article.title + " " + article.keywords + " " +
                   article.date + " " + article.elevator_pitch).toLowerCase();
        return tokens.every(function (t) { return hay.indexOf(t) !== -1; });
    }

    function render() {
        var q = input.value.trim();
        if (!q || !index) { results.hidden = true; return; }
        var tokens = q.toLowerCase().split(/\s+/);
        var hits = [];
        for (var i = 0; i < index.length && hits.length < 8; i++) {
            if (matches(index[i], tokens)) hits.push(index[i]);
        }
        if (!hits.length) {
            results.innerHTML = '<div class="search-empty">No results for "' +
                q.replace(/"/g, "&quot;") + '"</div>';
        } else {
            results.innerHTML = hits.map(function (a) {
                return '<a href="' + base + a.url + '">' + a.title +
                    '<span class="search-date">' + a.date + "</span></a>";
            }).join("");
        }
        results.hidden = false;
    }

    var timer = null;
    input.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(render, 150);
    });
    input.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            var first = results.querySelector("a");
            if (first) { window.location.href = first.getAttribute("href"); }
        } else if (e.key === "Escape") {
            results.hidden = true;
            input.blur();
        }
    });
    document.addEventListener("click", function (e) {
        if (!e.target.closest(".nav-search")) results.hidden = true;
    });
})();
"""
    with open(os.path.join(DIST_DIR, "search.js"), "w") as f:
        f.write(search_js)
    print("  ✓ search.js")

    print(f"\nDone! Site generated in {DIST_DIR}")
    print(f"Open with: python3 -m http.server -d {DIST_DIR} 8000")


if __name__ == "__main__":
    main()