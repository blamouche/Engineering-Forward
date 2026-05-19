#!/bin/bash
# Process scan-list URLs - this script handles one URL at a time
# Usage: ./process_url.sh <url> <workdir>

URL="$1"
WORKDIR="$2"

cd "$WORKDIR" || exit 1

# Normalize URL - remove tracking params
CLEAN_URL=$(echo "$URL" | sed -E 's/[?&](utm_[^&]+|ref=[^&]+|fbclid=[^&]+|gclid=[^&]+|mc_cid=[^&]+|mc_eid=[^&]+)//g' | sed 's/?&/\?/g' | sed 's/\?$//g')

echo "CLEAN_URL=$CLEAN_URL"
echo "ORIGINAL=$URL"
