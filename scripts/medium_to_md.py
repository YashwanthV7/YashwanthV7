import feedparser
from markdownify import markdownify as md
import os

MEDIUM_USERNAME = "yash1thvangala9"
FEED_URL = f"https://medium.com/feed/@{MEDIUM_USERNAME}"
OUTPUT_DIR = "CTF-Writeups/Medium-Posts"

feed = feedparser.parse(FEED_URL)
os.makedirs(OUTPUT_DIR, exist_ok=True)

for entry in feed.entries:
    title = entry.title.replace(" ", "_").replace("/", "_")
    filename = f"{OUTPUT_DIR}/{title}.md"
    content = md(entry.content[0].value)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {entry.title}\n\n")
        f.write(f"Published on: {entry.published}\n\n")
        f.write(content)
        f.write(f"\n\n[Original Article]({entry.link})")

