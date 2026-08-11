# roadmap — материалы вне рабочего контура

Папка для roadmap / архитектурных черновиков **вне** `docs/` и пайплайнов.

## Политика (как у `.archive/`)

- **Не** сканируется `@structure-indexer` / `tools/run_structure_indexer.py` (нет в `paths.*` манифеста).
- **Не** входит в `scope_matrix` и не является deliverable / intake.
- Исключена из индексации Cursor: `.cursorignore` → `roadmap/`.
- В `project.manifest.yaml` → `boundary.forbidden_paths` (агенты не читают без явного запроса человека).

Содержимое **хранится в git** (в отличие от локальных дампов `.archive/**`), чтобы материалы были доступны на GitHub, но не участвовали в обработке документации.
