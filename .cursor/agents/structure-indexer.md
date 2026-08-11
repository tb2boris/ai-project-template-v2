---
name: structure-indexer
description: Maintain file registry and per-directory file-list.md tables; paths from project.manifest.yaml
is_background: false
---

# Structure Indexer

Refresh file and directory registry for the **current workspace**. Read scan roots from `project.manifest.yaml` → `paths`.

## Actions

1. **Scan** (defaults from manifest):
   - `paths.knowledge_base`, `paths.intake`, `paths.domains`, `paths.deliverables`
   - `paths.registry`, `paths.communications`, `paths.quality`
   - `paths.engineering`, `paths.integrations` (if present)

2. **Central registry:** Create or update **`paths.file_registry`** with folder/file tree (paths relative to workspace root). Header: last update timestamp.

3. **Per-directory file-list.md:** For each scanned docs subdirectory:
   - Scan **current** files only (do not copy stale rows from old file-list).
   - Table: filename (relative) | brief description or title
   - Header: last update timestamp
   - No duplicate list files (`opisanie_*.md`) — pointer to file-list only

## When to invoke

- User request: "update file lists", "refresh registry"
- After bulk intake upload
- Before compliance pipelines on new tree

## Output

Short summary: which directories updated, paths to registry and file-lists.
