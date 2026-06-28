#!/usr/bin/env python3
"""
Topic Analyzer - Analyze research content for topic discovery.
Usage: python topic_analyzer.py
"""

import os, re
from pathlib import Path
from collections import Counter

VAULT = Path(r"H:\转录")
RESEARCH = VAULT / "04-Research"

TOPIC_KEYWORDS = {
    "codex": ["topic/codex", "topic/ai"],
    "claude": ["topic/claude-code", "topic/ai"],
    "prompt": ["topic/prompt", "topic/ai"],
    "workflow": ["topic/workflow", "topic/automation"],
    "agent": ["topic/agent", "topic/ai"],
    "mcp": ["topic/mcp", "topic/protocol"],
    "obsidian": ["topic/obsidian", "topic/tool"],
    "github": ["topic/github", "topic/devops"],
    "python": ["topic/python", "topic/programming"],
    "gpt": ["topic/gpt", "topic/llm", "topic/ai"],
    "llm": ["topic/llm", "topic/ai"],
    "rag": ["topic/rag", "topic/ai"],
    "bitcoin": ["topic/bitcoin", "topic/crypto"],
    "ethereum": ["topic/ethereum", "topic/crypto"],
    "defi": ["topic/defi", "topic/crypto"],
    "seo": ["topic/seo", "topic/marketing"],
}


def scan():
    files = []
    for root, dirs, _ in os.walk(RESEARCH):
        for f in Path(root).glob("*.md"):
            try:
                content = f.read_text(encoding="utf-8", errors="replace")
                files.append({"path": f.relative_to(VAULT), "content": content,
                             "dir": str(f.parent.relative_to(VAULT))})
            except Exception as e:
                print(f"  Skip {f}: {e}")
    return files


def suggest_tags(title, content):
    text = f"{title} {content}".lower()
    suggested = []
    seen = set()
    for keyword, tags in TOPIC_KEYWORDS.items():
        if keyword in text:
            for tag in tags:
                if tag not in seen:
                    seen.add(tag)
                    suggested.append(tag)
    return suggested


def main():
    print("Scanning 04-Research...")
    files = scan()
    print(f"Found {len(files)} files\n")

    # Keyword frequency
    word_counter = Counter()
    for f in files:
        words = re.findall(r"\b[a-zA-Z]{4,}\b", f["content"].lower())
        word_counter.update(words)

    print("Top keyword topics (suggesting new Hubs):")
    top = [w for w, c in word_counter.most_common(20)
           if w in TOPIC_KEYWORDS]
    for w in top:
        print(f"  - {w} -> {', '.join(TOPIC_KEYWORDS[w])}")

    print("\nFiles needing tags:")
    untagged = [f for f in files if "tags:" not in f["content"][:200]]
    if untagged:
        for f in untagged[:10]:
            tags = suggest_tags(f["path"].stem, f["content"])
            if tags:
                print(f"  - {f['path']}: {', '.join(tags[:4])}")
        if len(untagged) > 10:
            print(f"  ... and {len(untagged) - 10} more")
    else:
        print("  All files have tags!")


if __name__ == "__main__":
    main()
