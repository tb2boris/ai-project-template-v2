# Инструкция: обработка записи совещания / демонстрации

Краткий справочник: **отдельные шаги** и **полный пайплайн**. Пути — по `project.manifest.yaml` (по умолчанию `docs/05-communications/`, `docs/04-registry/meetings/`).

Субагенты: [.cursor/agents/AGENTS_CATALOG.md](agents/AGENTS_CATALOG.md) — `@meeting-terminology-normalizer`, `@meeting-demo-task-report-builder`.  
Навык-оркестратор: **`meeting-transcript-pipeline`** — [SKILL.md](skills/meeting-transcript-pipeline/SKILL.md).

---

## Когда что использовать

| Задача | Как запускать |
|--------|----------------|
| Встреча ещё в mymeet.ai | **`/mymeet-meeting-pipeline`** — см. [STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md](STARTER_PROMPT_MYMEET_MEETING_PIPELINE.md) |
| Только импорт из mymeet | `/mymeet-meeting-import` |
| Только термины в протоколе | `@meeting-terminology-normalizer` + файл |
| Только Excel по задачам | `@meeting-demo-task-report-builder` + файл |
| Объединить ч.1 + ч.2 | Скрипт merge или пайплайн с `части_встречи` |
| Файл уже в transcripts/ → термины → Excel | **`meeting-transcript-pipeline`** |

**Не использовать VKS** для новых проектов (deprecated). Primary ingest = MyMeet MCP.

**Источник задач для Excel:** только блок **`Транскрипт:`**. Блоки «Супер краткое содержание», «Саммари по темам», «Задачи:» — справочно.

**Колонка «Выполнение.»:** по умолчанию «Открыт» / «Новая», если на совещании не назван иной статус.

---

## A. Отдельный шаг — нормализация терминов

```
@meeting-terminology-normalizer

Файл: @docs/05-communications/transcripts/<файл>.md

Правки в файле (не report-only).
Эталон: terminology.canonical_file и terminology.asr_mappings_file из project.manifest.yaml
```

---

## B. Отдельный шаг — объединение частей

```powershell
python tools/merge_meeting_transcript_parts.py `
  --parts "docs/05-communications/transcripts/meeting-ч1.md" `
          "docs/05-communications/transcripts/meeting-ч2.md" `
  --out "docs/05-communications/transcripts/meeting-merged.md" `
  --title "**2026-05-28. Тема совещания**"
```

Или в чате:

```
Объедини части встречи:
@meeting-ч1.md @meeting-ч2.md
→ один файл с блоками Супер краткое / Саммари / Задачи / Транскрипт
(скрипт tools/merge_meeting_transcript_parts.py)
```

---

## C. Отдельный шаг — отчёт Excel (7 колонок)

```
@meeting-demo-task-report-builder

Файл: @docs/05-communications/transcripts/<файл>.md
Папка скриншотов: <явный путь>   # если есть

Источник — только Транскрипт.
JSON → docs/04-registry/meetings/<имя>.tasks.json
Excel → docs/04-registry/meetings/<имя>-tasks.xlsx

Сборка:
python tools/build_meeting_task_report_xlsx.py `
  --json docs/04-registry/meetings/<имя>.tasks.json `
  --out docs/04-registry/meetings/<имя>-tasks.xlsx
```

Схема колонок: [platform/templates/meeting-tasks.columns.yaml](../platform/templates/meeting-tasks.columns.yaml).

---

## D. Полный пайплайн (оркестратор)

Шаблон параметров: [prompt-template.md](skills/meeting-transcript-pipeline/prompt-template.md).

```
## Параметры пайплайна

файл_встречи: docs/05-communications/transcripts/2026-05-28-status.md

# Или части:
# части_встречи:
#   - docs/05-communications/transcripts/status-ч1.md
#   - docs/05-communications/transcripts/status-ч2.md
# заголовок_объединения: "**2026-05-28. Статусное совещание**"

нормализация_терминов: да
отчет_excel: да
папка_скриншотов: docs/05-communications/media/2026-05-28/screenshots/

Запусти meeting-transcript-pipeline по SKILL.md.
Без подтверждений между шагами.
```

**Порядок шагов:**

1. VKS export (если `vks_meeting_id` и API настроен)
2. Объединение частей — `merge_meeting_transcript_parts.py`
3. `@meeting-terminology-normalizer` (если `нормализация_терминов: да`)
4. `@meeting-demo-task-report-builder` + `build_meeting_task_report_xlsx.py`

---

## Скриншоты: время из имени файла

| Файл | Цифры | Расшифровка | Время |
|------|-------|-------------|-------|
| `0945.png` | 4 | 09 мин, 45 сек | `0:09:45` |
| `12450.png` | 5 | 1 ч, 24 мин, 50 сек | `1:24:50` |

```powershell
python tools/parse_screenshot_timecode.py --dir "docs/05-communications/media/<meeting>/screenshots"
```

---

## Результаты пайплайна

| Артефакт | Путь |
|----------|------|
| Объединённый протокол | `--out` или `файл_встречи` |
| JSON задач (аудит) | `docs/04-registry/meetings/<имя>.tasks.json` |
| Excel | `docs/04-registry/meetings/<имя>-tasks.xlsx` |

Утверждающий: PM / BA.
