#!/usr/bin/env python3
"""
Research Cleaner - Clean and classify research markdown files.
Usage:
  python research_cleaner.py <input.md>
  python research_cleaner.py --inbox
  python research_cleaner.py --stats
"""

import os, re, sys, argparse
from pathlib import Path
from datetime import datetime

VAULT = Path(r"H:\转录")
INBOX = VAULT / "00-Inbox" / "Downloaded"
CLEANED = VAULT / "00-Inbox" / "Cleaned"
RESEARCH = VAULT / "04-Research"

DOMAIN_MAP = {
    "arxiv.org": "AI/Research",
    "github.com": "Programming/Tools",
    "youtube.com": "AI/Information-Sources",
    "openai.com": "AI/Models",
    "anthropic.com": "AI/Models",
    "huggingface.co": "AI/Models",
    "medium.com": "AI/Information-Sources",
    "twitter.com": "AI/Information-Sources",
    "coingecko.com": "Crypto/Market",
    "finance.yahoo.com": "US-Stocks/Market",
}


def extract_title(content):
    for line in content.split("\n"):
        s = line.strip()
        if s.startswith("# ") and not s.startswith("## "):
            return s[2:].strip()
    return "Untitled"


def extract_urls(content):
    return list(set(re.findall(r"https?://[^\s<>\"']+", content)))


def classify(urls):
    for url in urls:
        for domain, area in DOMAIN_MAP.items():
            if domain in url.lower():
                return area
    return None


def clean(content):
    """Clean markdown. Preserve all original content."""
    return content.strip()


def safe_filename(title):
    safe = re.sub(r'[\\/*?:"<>|]', "", title)
    return safe.strip()[:80] + ".md"


def build_frontmatter(title, urls, area):
    tags = "type/research, source/web, status/cleaned"
    date = datetime.now().strftime("%Y-%m-%d")
    src = urls[0] if urls else ""
    return f"---\ntitle: \"{title}\"\ndate: {date}\nsource: \"{src}\"\ntags: [{tags}]\n---\n\n"


def process_file(filepath, output_dir=None):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    title = extract_title(content)
    urls = extract_urls(content)
    area = classify(urls)
    frontmatter = build_frontmatter(title, urls, area)

    output = frontmatter + clean(content) + "\n"
    name = safe_filename(title)

    if output_dir:
        out = Path(output_dir)
    elif area:
        out = RESEARCH / area
    else:
        out = CLEANED

    os.makedirs(out, exist_ok=True)
    outfile = out / name
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"  OK: {filepath.name} -> {outfile}")
    return outfile


def main():
    parser = argparse.ArgumentParser(description="Research Cleaner")
    parser.add_argument("input", nargs="?", help="Input file")
    parser.add_argument("--inbox", action="store_true", help="Process Inbox/Downloaded")
    parser.add_argument("--output-dir", help="Output directory")
    parser.add_argument("--stats", action="store_true", help="Show statistics")
    args = parser.parse_args()

    if args.stats:
        dl = len(list(INBOX.glob("*.md"))) if INBOX.exists() else 0
        cd = len(list(CLEANED.glob("*.md"))) if CLEANED.exists() else 0
        total = sum(len(list(p.glob("*.md"))) for p in RESEARCH.rglob("*") if p.is_dir())
        print(f"Inbox/Downloaded: {dl}")
        print(f"Inbox/Cleaned: {cd}")
        print(f"04-Research: {total}")
        return

    if args.inbox:
        files = list(INBOX.glob("*.md"))
        if not files:
            print("No files in Inbox/Downloaded")
            return
        for f in files:
            process_file(f, args.output_dir)
    elif args.input:
        process_file(Path(args.input), args.output_dir)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
