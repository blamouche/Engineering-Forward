#!/bin/bash
set -euo pipefail
cd /Users/openclaw/github/Engineering-Forward

BATCH_TS="2026-05-16 180500"
BATCH_FILE="synthesis/2026-05-16 - 180500 - batch recap.md"
ERRORS=""
RECAPS=""

# Clean URL function
clean_url() {
  echo "$1" | sed -E 's/[?&](utm_[^=&]+|ref|fbclid|gclid|mc_cid|mc_eid)=[^&]*//g' | sed 's/?$//'
}

process_url() {
  local raw="$1"
  local url
  url=$(clean_url "$raw")
  
  echo "PROCESSING: $url"
  
  # Fetch article
  FETCH_OUT=$(curl -s --max-time 30 -o /tmp/article-fetch.html -w "%{http_code}" "$url" 2>/dev/null || echo "000")
  
  if [ "$FETCH_OUT" != "200" ] && [ "$FETCH_OUT" != "200" ]; then
    echo "FETCH_ERROR: $url — HTTP $FETCH_OUT"
    echo "FETCH_ERROR: $url — HTTP $FETCH_OUT" >> /tmp/scan-errors.txt
    return 1
  fi
  
  # Try text extraction from HTML
  python3 -c "
import sys, re
with open('/tmp/article-fetch.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()
# Remove scripts and styles
html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL|re.IGNORECASE)
html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL|re.IGNORECASE)
# Get text
text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\s+', ' ', text).strip()
# Extract title
title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL|re.IGNORECASE)
title = title_match.group(1).strip() if title_match else 'Unknown Title'
print('TITLE:' + title[:200])
print('TEXT:' + text[:5000])
" > /tmp/article-parsed.txt 2>/dev/null || true
  
  TITLE=$(grep '^TITLE:' /tmp/article-parsed.txt | sed 's/^TITLE://' | head -1)
  TEXT_BODY=$(grep '^TEXT:' /tmp/article-parsed.txt | sed 's/^TEXT://')
  
  if [ -z "$TITLE" ] || [ "$TITLE" = "Unknown Title" ]; then
    echo "FETCH_ERROR: $url — Could not extract title"
    echo "FETCH_ERROR: $url — Could not extract title" >> /tmp/scan-errors.txt
    return 1
  fi
  
  echo "TITLE: $TITLE"
  echo "$TITLE" > /tmp/article-title.txt
  echo "$TEXT_BODY" > /tmp/article-body.txt
  echo "$url" > /tmp/article-url.txt
  
  return 0
}

# Process each URL
TOTAL=0
ERROR_COUNT=0

while IFS= read -r line; do
  [ -z "$line" ] && continue
  TOTAL=$((TOTAL + 1))
  
  if process_url "$line"; then
    echo "SUCCESS: $(cat /tmp/article-title.txt)"
  else
    ERROR_COUNT=$((ERROR_COUNT + 1))
  fi
  echo "---"
done < LIST.md

echo "TOTAL_URLS=$TOTAL"
echo "ERRORS=$ERROR_COUNT"
