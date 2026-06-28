#!/usr/bin/env python3
"""
Knowledge Base Audit - Vault health checker.
Usage:
  python kb_audit.py         # Full audit
  python kb_audit.py --quick  # Quick (skip orphan check)
"""

import os, re, sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

VAULT = Path(r"H:\转录")
IGNORE_DIRS = {".git", ".obsidian", "__pycache__"}
REPORT_FILE = VAULT / "99-Archive" / "_kb_audit_report.md"


def scan():
    all_files, all_dirs = [], []
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        rel = Path(root).relative_to(VAULT)
        if rel != Path("."):
            all_dirs.append(rel)
        for f in files:
            fp = Path(root) / f
            relp = fp.relative_to(VAULT)
            all_files.append({
                "path": relp, "name": f, "stem": fp.stem,
                "ext": fp.suffix.lower(), "size": fp.stat().st_size,
                "parent": str(relp.parent) if relp.parent != Path(".") else "",
            })
    return all_files, all_dirs


def find_duplicates(files):
    issues = []
    by_stem = defaultdict(list)
    for f in files:
        if f["ext"] == ".md":
            by_stem[f["stem"].lower()].append(f)
    for stem, matches in by_stem.items():
        if len(matches) > 1:
            issues.append({"type": "duplicate", "severity": "warning",
                           "desc": f"Potential duplicates ({len(matches)})",
                           "files": [str(m["path"]) for m in matches]})
    return issues


def find_empty_dirs(dirs, files):
    issues = []
    with_content = set()
    for f in files:
        if f["parent"]:
            with_content.add(f["parent"])
    for d in dirs:
        ds = str(d)
        if ds not in with_content:
            has_sub = any(p.startswith(ds + "\\") for p in with_content)
            if not has_sub:
                issues.append({"type": "empty_dir", "severity": "info",
                               "desc": "Empty directory", "files": [ds]})
    return issues


def find_orphans(files, quick=False):
    if quick:
        return []
    issues = []
    mds = [f for f in files if f["ext"] == ".md" and not f["name"].startswith("_")]
    linked = set()
    for f in mds:
        try:
            with open(f["path"], "r", encoding="utf-8", errors="replace") as fp:
                c = fp.read()
            for link in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", c):
                linked.add(link.strip().lower())
        except:
            pass
    for f in mds:
        if f["stem"].lower() not in linked:
            if any(f["parent"].startswith(p) for p in ["90-", "89-", "99-", "97-", "98-"]):
                continue
            if "index" in f["stem"].lower() or "template" in f["stem"].lower():
                continue
            issues.append({"type": "orphan", "severity": "info",
                           "desc": "No internal links point here", "files": [str(f["path"])]})
    return issues


def generate_report(issues, total_files, total_dirs):
    lines = [
        "---",
        f"title: 'Knowledge Base Audit Report'",
        f"date: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "tags: [type/report, system/audit]",
        "---\n",
        "# Knowledge Base Audit Report\n",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "## Overview\n",
        f"- Total files: {total_files}",
        f"- Total dirs: {total_dirs}",
        f"- Issues found: {len(issues)}\n",
    ]
    sev_map = {"error": "Error", "warning": "Warning", "info": "Info"}
    by_sev = defaultdict(list)
    for i in issues:
        by_sev[i["severity"]].append(i)
    for sev, label in sev_map.items():
        items = by_sev.get(sev, [])
        if items:
            lines.append(f"### {label} ({len(items)})")
            for i in items:
                lines.append(f"- **{i['type']}**: {i['desc']}")
                for pf in i["files"]:
                    lines.append(f"  - `{pf}`")
            lines.append("")
    return "\n".join(lines)


def main():
    quick = "--quick" in sys.argv
    print("\nRunning knowledge base audit...")
    files, dirs = scan()
    print(f"  Files: {len(files)}, Dirs: {len(dirs)}")

    issues = []
    issues.extend(find_duplicates(files))
    issues.extend(find_empty_dirs(dirs, files))
    issues.extend(find_orphans(files, quick))

    report = generate_report(issues, len(files), len(dirs))
    os.makedirs(REPORT_FILE.parent, exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport saved to: {REPORT_FILE}")
    print(f"Issues found: {len(issues)}")


if __name__ == "__main__":
    main()
