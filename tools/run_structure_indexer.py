#!/usr/bin/env python3
"""Scan docs tree and update file-registry.md. Paths from project.manifest.yaml."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

DEFAULT_REGISTRY = "docs/04-registry/file-registry.md"
DEFAULT_SCAN = [
    "docs/00-knowledge",
    "docs/01-intake",
    "docs/02-domains",
    "docs/03-deliverables",
    "docs/04-registry",
    "docs/05-communications",
    "docs/06-quality",
    "engineering",
]


def load_manifest(root: Path) -> dict:
    manifest_path = root / "project.manifest.yaml"
    if yaml and manifest_path.exists():
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        paths = data.get("paths", {})
        registry = paths.get("file_registry", DEFAULT_REGISTRY)
        scan = [
            paths.get("knowledge_base"),
            paths.get("intake"),
            paths.get("domains"),
            paths.get("deliverables"),
            paths.get("registry"),
            paths.get("communications"),
            paths.get("quality"),
            paths.get("engineering"),
        ]
        scan = [p for p in scan if p]
        return {"registry": registry, "scan": scan or DEFAULT_SCAN}
    return {"registry": DEFAULT_REGISTRY, "scan": DEFAULT_SCAN}


def collect_files(root: Path, scan_dirs: list[str]) -> list[Path]:
    files: list[Path] = []
    for rel in scan_dirs:
        base = root / rel
        if not base.exists():
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file() and not p.name.startswith("."):
                files.append(p.relative_to(root))
    return files


def write_registry(root: Path, registry_rel: str, files: list[Path]) -> Path:
    out = root / registry_rel
    out.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"# File registry\n\nUpdated: {ts}\n\n"]
    by_dir: dict[str, list[Path]] = {}
    for f in files:
        by_dir.setdefault(str(f.parent), []).append(f)
    for dir_name in sorted(by_dir):
        lines.append(f"## `{dir_name}`\n\n")
        for f in sorted(by_dir[dir_name]):
            lines.append(f"- `{f}`\n")
        lines.append("\n")
    out.write_text("".join(lines), encoding="utf-8")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Update file-registry.md from manifest paths")
    parser.add_argument("--root", type=Path, default=Path("."), help="Repository root")
    args = parser.parse_args()
    root = args.root.resolve()
    cfg = load_manifest(root)
    files = collect_files(root, cfg["scan"])
    out = write_registry(root, cfg["registry"], files)
    print(f"Wrote {len(files)} entries to {out}")


if __name__ == "__main__":
    main()
