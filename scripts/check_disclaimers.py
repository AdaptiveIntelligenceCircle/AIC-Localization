#!/usr/bin/env python3
"""
Lightweight check: priority locale files should contain caution markers.

NOT a full QA system. Orientation helper only.
Exits 0 if markers found in scanned files; 1 if any file missing markers.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "locales"

# Substrings we expect to see in orientation pages (any language variant).
MARKERS = [
    "pre-Covenant",
    "under-claim",
    "not legal advice",
    "không phải tư vấn pháp lý",
    "Pre-Covenant",
    "entity ≠ immunity",
    "thực thể ≠ miễn trừ",
    "Entity ≠ immunity",
]


def main() -> int:
    if not LOCALES.is_dir():
        print("No locales/ directory")
        return 1

    missing = []
    scanned = 0
    for path in sorted(LOCALES.rglob("*.md")):
        # Skip pure index files that only point elsewhere if desired;
        # still scan everything for simplicity.
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        scanned += 1
        if not any(m.lower() in text for m in MARKERS):
            missing.append(path)

    print(f"Scanned {scanned} markdown files under locales/")
    if missing:
        print("Files with no recognized caution marker:")
        for p in missing:
            print(f"  - {p}")
        print("Add appropriate under-claim / pre-Covenant / not-legal-advice notice.")
        return 1

    print("OK: each file contains at least one recognized caution marker.")
    return 0

if __name__ == "__main__": 
    sys.exit(main())