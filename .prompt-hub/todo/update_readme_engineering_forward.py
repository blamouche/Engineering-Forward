from pathlib import Path
import re, sys

readme = Path('README.md')
article_path = Path(sys.argv[1])
text = readme.read_text()
article = article_path.read_text()
title = re.search(r'^#\s+(.+)$', article, re.M).group(1).strip()
date = re.search(r'\*\*Date\*\*:\s+([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})', article).groups()
month_name, _day, year = date
month_map = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
month_num = month_map[month_name]
link = f'- [{title}]({article_path.as_posix()})'
month_heading = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}[month_num]
header = f'#### {month_heading} ('
if link not in text:
    idx = text.index(header)
    line_end = text.index('\n', idx)
    text = text[:line_end+1] + link + '\n' + text[line_end+1:]
links = re.findall(r'^- \[(.+?)\]\((src/([^/]+)/[^)]+)\)$', text, re.M)
counts = {}
for _title, _path, month in links:
    counts[month] = counts.get(month, 0) + 1
stats_pattern = re.compile(r'(## Statistics\n\nArticles per month:\n\n)(.*?)(\n## Articles)', re.S)
stats_lines = []
for m in sorted(counts):
    stats_lines.append(f"{m} | {'█' * counts[m]} {counts[m]}<br>")
stats_body = '\n'.join(stats_lines)
text = stats_pattern.sub(lambda m: m.group(1) + stats_body + m.group(3), text)
for m, c in counts.items():
    mo = m.split('-')[1]
    month_heading = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}[mo]
    text = re.sub(rf'^(#### {month_heading}) \(\d+ articles\)$', rf'\1 ({c} articles)', text, flags=re.M)
readme.write_text(text)
