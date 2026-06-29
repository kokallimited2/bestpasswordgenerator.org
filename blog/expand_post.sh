#!/bin/bash
# expand_post.sh - Expand a thin blog post to 1200+ words
# Usage: expand_post.sh <file.html> <topic_description>

FILE="$1"
TOPIC="$2"
BASEDIR="/home/khan/github-projects/bestpasswordgenerator-org/blog"

if [ ! -f "$FILE" ]; then
  echo "File not found: $FILE"
  exit 1
fi

echo "=== Processing $FILE ==="

# Extract existing body content (between meta div close and CTA div)
BODY=$(sed -n '/<\/div>$/,/<div style="text-align:center">/p' "$FILE" | head -n -1 | tail -n +2 | grep -v '^$' | grep -v '^\s*$' | tr '\n' ' ')

echo "Existing content: ${#BODY} chars"

# Use Claude CLI to generate expansion content
echo "Generating expansion content with Claude CLI..."
EXPANSION=$(claude -p "Write approximately 600-800 additional words to expand this blog post to 1200+ total words. The post is about: $TOPIC.

Existing content already in the post:
\"$BODY\"

Output ONLY new HTML content with <h2>, <p>, <ul> tags. No markdown, no code fences, no explanations. Just raw HTML that I can insert directly into the page." --dangerously-skip-permissions --output-format text 2>/dev/null)

echo "Generated expansion: ${#EXPANSION} chars"

# Save expansion to temp file
echo "$EXPANSION" > /tmp/expansion.html

# Find the insertion point - after the last content paragraph before the CTA div
INSERT_AFTER=$(grep -n '<div style="text-align:center"' "$FILE" | head -1 | cut -d: -f1)
INSERT_AFTER=$((INSERT_AFTER - 1))

echo "Insert point: line $INSERT_AFTER"

# Read file, split at insertion point, insert content
head -n $INSERT_AFTER "$FILE" > /tmp/part1.html
tail -n +$((INSERT_AFTER + 1)) "$FILE" > /tmp/part2.html

# Insert the expansion content between part1 and part2
cat /tmp/part1.html /tmp/expansion.html /tmp/part2.html > /tmp/expanded.html

# Replace original
cp /tmp/expanded.html "$FILE"

# Count new words
NEW_WORDS=$(wc -w < "$FILE")
echo "New word count: $NEW_WORDS"

# Update wordCount in JSON-LD
# Find the wordCount line and update it
sed -i "s/\"wordCount\": \"[0-9]*\"/\"wordCount\": \"$NEW_WORDS\"/g" "$FILE"

# Also update the meta div reading time
# Calculate min read (roughly 200 words per minute)
MIN_READ=$((NEW_WORDS / 200))
if [ $MIN_READ -lt 1 ]; then MIN_READ=1; fi
sed -i "s/[0-9]* min read/$MIN_READ min read/g" "$FILE"

echo "=== Done processing $FILE ($NEW_WORDS words, ~${MIN_READ} min read) ==="
