---
name: meeting-transcript-pipeline
description: Экспорт VKS → нормализатор терминов → Excel с задачами совещания
disable-model-invocation: true
---

# Meeting transcript pipeline (пайплайн транскрипта совещания)

Downstream-оркестратор после **VKS Processing Service** (когда `integrations.vks.enabled: true`).

## Когда использовать

- Полная обработка совещания: транскрипт → нормализация → Excel с задачами
- Явный вызов: `/meeting-transcript-pipeline`

## Обязательный вход

| Поле | Обязательно |
|------|-------------|
| `meeting_file` ИЛИ `vks_meeting_id` | Да |
| `normalize_terminology` | По умолчанию: да |
| `excel_report` | По умолчанию: да |
| `screenshot_folder` | Опционально |

## Шаги

```
- [ ] 0. Проверить вход; если vks_meeting_id → tools/vks_export_to_repo.py
- [ ] 1. Опциональная склейка: tools/merge_meeting_transcript_parts.py
- [ ] 2. @meeting-terminology-normalizer (если включено)
- [ ] 3. @meeting-demo-task-report-builder → `tools/build_meeting_task_report_xlsx.py` (если включено)
- [ ] 4. Сводка для пользователя (пути, количество строк)
```

## Связанные файлы

- [prompt-template.md](prompt-template.md) — параметры для copy-paste
- [artifact-paths.md](artifact-paths.md) — пути выходных артефактов по умолчанию
- [.cursor/STARTER_PROMPT_MEETING_PIPELINE.md](../../STARTER_PROMPT_MEETING_PIPELINE.md) — руководство пользователя (RU)

## Пути (из манифеста)

- Транскрипты: `paths.communications` / `integrations.vks.export_paths.transcripts`
- JSON/Excel задач: `paths.meetings_registry`
- Builder: `meeting_tasks.builder_script` или `tools/build_meeting_task_report_xlsx.py`

## Команда merge (когда `части_встречи`)

```bash
python tools/merge_meeting_transcript_parts.py \
  --parts <part1> <part2> ... \
  --out <merged.md> \
  --title "<title>"
```

Human approver: PM / BA.

*Зеркало: `.cursor/skills/meeting-transcript-pipeline/SKILL.md`*
