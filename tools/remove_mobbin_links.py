#!/usr/bin/env python3
"""Remove inaccessible Mobbin URLs while preserving local visual evidence."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MOBBIN_URL = re.compile(r"https?://(?:www\.)?mobbin\.com[^\s\"'<>),\]]*", re.I)


def clean_text(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    if not MOBBIN_URL.search(original):
        return False
    lines = []
    for line in original.splitlines(keepends=True):
        if re.fullmatch(r"\s*[-*]?\s*" + MOBBIN_URL.pattern + r"\s*", line.rstrip("\r\n"), re.I):
            continue
        cleaned_line = MOBBIN_URL.sub("", line)
        ending = "\n" if cleaned_line.endswith("\n") else ""
        lines.append(cleaned_line.rstrip("\r\n").rstrip() + ending)
    cleaned = "".join(lines)
    if cleaned == original:
        return False
    path.write_text(cleaned, encoding="utf-8")
    return True


def main() -> int:
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT
    ).decode().split("\0")
    changed = []
    for relative in tracked:
        if not relative:
            continue
        path = ROOT / relative
        if path.suffix.lower() == ".py" or not path.is_file():
            continue
        try:
            did_change = clean_text(path)
        except UnicodeDecodeError:
            continue
        if did_change:
            changed.append(relative)
    print(f"Removed Mobbin URLs from {len(changed)} tracked files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
