# -*- coding: utf-8
"""Merge two or more meeting transcript parts into one .md file.

Sections merged:
  - Супер краткое содержание (bullets concatenated)
  - Саммари по темам (appended)
  - Задачи (bullets concatenated)
  - Транскрипт (appended)

Run from repo root:
  python tools/merge_meeting_transcript_parts.py \\
    --parts docs/05-communications/transcripts/meeting-ч1.md \\
           docs/05-communications/transcripts/meeting-ч2.md \\
    --out docs/05-communications/transcripts/meeting-merged.md \\
    --title "**2026-05-28. Meeting title**"

Paths default per project.manifest.yaml → paths.communications / transcripts.
"""
from __future__ import annotations

import argparse
from pathlib import Path

MARKERS = [
    "**Супер краткое содержание**:",
    "**Саммари по темам**:",
    "**Задачи:**",
    "**Транскрипт:**",
]


def split_sections(text: str) -> dict[str, str]:
    parts: dict[str, str] = {"header": ""}
    current = "header"
    buf: list[str] = []
    for line in text.splitlines():
        hit = next((m for m in MARKERS if line.strip() == m), None)
        if hit:
            parts[current] = "\n".join(buf).strip("\n")
            buf = []
            current = hit
        else:
            buf.append(line)
    parts[current] = "\n".join(buf).strip("\n")
    return parts


def merge_bullets(blocks: list[str]) -> str:
    lines: list[str] = []
    for block in blocks:
        for ln in block.splitlines():
            if ln.strip().startswith("- "):
                lines.append(ln)
    return "\n".join(lines)


def merge_text(blocks: list[str]) -> str:
    return "\n\n".join(b.strip() for b in blocks if b.strip()).strip()


def build_doc(title: str, sources: list[Path], sections: dict[str, str]) -> str:
    src_line = ", ".join(f"`{p.name}`" for p in sources)
    header = f"{title}\n\n*Объединённая запись. Источники: {src_line}.*"
    chunks = [
        header,
        MARKERS[0],
        sections[MARKERS[0]],
        MARKERS[1],
        sections[MARKERS[1]],
        MARKERS[2],
        sections[MARKERS[2]],
        MARKERS[3],
        sections[MARKERS[3]],
        "",
    ]
    return "\n\n".join(chunks)


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge meeting transcript part files")
    parser.add_argument("--parts", nargs="+", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--title", required=True, help="Markdown title line(s) for merged file")
    args = parser.parse_args()

    all_sections: dict[str, list[str]] = {m: [] for m in MARKERS}
    for part in args.parts:
        if not part.exists():
            raise FileNotFoundError(part)
        text = part.read_text(encoding="utf-8")
        sec = split_sections(text)
        for m in MARKERS:
            all_sections[m].append(sec.get(m, ""))

    merged = {
        MARKERS[0]: merge_bullets(all_sections[MARKERS[0]]),
        MARKERS[1]: merge_text(all_sections[MARKERS[1]]),
        MARKERS[2]: merge_bullets(all_sections[MARKERS[2]]),
        MARKERS[3]: merge_text(all_sections[MARKERS[3]]),
    }
    doc = build_doc(args.title.strip(), args.parts, merged)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(doc, encoding="utf-8")
    print(f"Merged {len(args.parts)} parts -> {args.out} ({len(doc.splitlines())} lines)")


if __name__ == "__main__":
    main()
