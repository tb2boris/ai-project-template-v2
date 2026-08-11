# -*- coding: utf-8
"""Parse meeting screenshot filename timecode (4–5 digits before extension).

Rules (from the right):
  - last 2 digits → seconds
  - previous 2 digits → minutes
  - optional 5th digit (leftmost) → hours

Examples:
  0945.png   → 0:09:45
  12450.png  → 1:24:50

Usage:
  python tools/parse_screenshot_timecode.py 0945.png 12450.png
  python tools/parse_screenshot_timecode.py --dir docs/05-communications/media/screenshots
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


def extract_digit_run(stem: str) -> str | None:
    """Prefer longest contiguous digit run of length 4 or 5 in the stem."""
    runs = re.findall(r"\d{4,5}", stem)
    if not runs:
        digits = re.sub(r"\D", "", stem)
        return digits if len(digits) in (4, 5) else None
    for run in sorted(runs, key=len, reverse=True):
        if len(run) in (4, 5):
            return run
    return None


def parse_timecode_from_name(name: str) -> str | None:
    stem = Path(name).stem
    digits = extract_digit_run(stem)
    if not digits or len(digits) not in (4, 5):
        return None
    ss = int(digits[-2:])
    mm = int(digits[-4:-2])
    hh = int(digits[:-4]) if len(digits) == 5 else 0
    if mm > 59 or ss > 59:
        return None
    return f"{hh}:{mm:02d}:{ss:02d}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse screenshot timecodes from filenames")
    parser.add_argument("names", nargs="*", help="Filenames or paths")
    parser.add_argument("--dir", type=Path, help="Directory of screenshots")
    args = parser.parse_args()

    paths: list[Path] = []
    if args.dir:
        paths.extend(sorted(args.dir.glob("*.png")))
        paths.extend(sorted(args.dir.glob("*.PNG")))
    for n in args.names:
        paths.append(Path(n))

    for p in paths:
        tc = parse_timecode_from_name(p.name)
        print(f"{p.name}\t{tc or '?'}")


if __name__ == "__main__":
    main()
