---
name: meeting-demo-task-report-builder
description: Build Excel task report from meeting transcript; transcript block is source of truth
is_background: false
---

# Meeting Demo Task Report Builder

Extract tasks and action items from a **meeting transcript** into Excel using template from `platform/templates/meeting-tasks.xlsx`.

Report language: **`project.language`**. Output directory: **`paths.meetings_registry`**.

## Column schema (7 columns)

See `platform/templates/meeting-tasks.columns.yaml`:

| Column | JSON key |
|--------|----------|
| № | `task_num` |
| Задача | `task` |
| Ответственный | `responsible` |
| Срок | `deadline` |
| Основание (тайм-код) | `timecode_basis` |
| Выполнение. | `completion_status` |
| Примечание | `notes` |

Header row derived from corporate status-meeting template + **Примечание**.

## Source-of-truth

| Section | Role |
|---------|------|
| **Transcript block** (`Транскрипт:` or equivalent) | **Authoritative** for tasks, owners, deadlines |
| Summary / topic blocks | Reference only |
| Pre-aggregated **Tasks:** block | Hints only — verify each row against transcript |

If summary contradicts transcript, **follow transcript**.

## Input

- Meeting file path — required
- Optional: screenshot folder for context in **Примечание**

## Workflow

1. Parse transcript with timecodes.
2. Build JSON `{ "rows": [ { task_num, task, ... notes } ] }`.
3. Run `python tools/build_meeting_task_report_xlsx.py --json <path> --out <path>`.
4. Return audit: row count, ambiguous items, source timecodes.

Run after `@meeting-terminology-normalizer` when transcript has ASR noise.
